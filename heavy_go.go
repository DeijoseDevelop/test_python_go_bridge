package main

import (
	"C"
	"runtime"
	"sync"
	"time"
)
import "fmt"

//export CalculateHeavyTask
func CalculateHeavyTask(n int) int64 {
	start := time.Now()

	var wg sync.WaitGroup
	numCPU := runtime.NumCPU()
	runtime.GOMAXPROCS(numCPU)

	jobs := make(chan int, numCPU*2)
	results := make(chan int64, numCPU*2)

	for w := 1; w <= numCPU; w++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			for num := range jobs {
				results <- int64(num * num)
			}
		}()
	}

	go func() {
		wg.Wait()
		close(results)
	}()

	go func() {
		for i := 1; i <= n; i++ {
			jobs <- i
		}
		close(jobs)
	}()

	var sum int64 = 0
	for res := range results {
		sum += res
	}

	elapsed := time.Since(start)
	fmt.Println("Tiempo total en Go:", elapsed.Seconds(), "segundos")

	return sum
}

func main() {
	fmt.Println(CalculateHeavyTask(1000000))
}
