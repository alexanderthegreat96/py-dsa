package main

import "fmt"

// very basic bubbleSort
// but with a small optimisation flag
// data is passed by refference
// which is not entirely necessary
// given that go does receive a header copy of that slice
// but it will still point to the same place in memory
// this is more explicit
func bubbleSort(inputData *[]int) {
	for range *inputData {
		// the actual optimization flag
		swapped := false
		for i := 0; i < len(*inputData)-1; i++ {
			// inner looping to check
			if (*inputData)[i] > (*inputData)[i+1] {
				// tupple unpacking similar to python's
				(*inputData)[i], (*inputData)[i+1] = (*inputData)[i+1], (*inputData)[i]
				swapped = true
			}
		}

		// breaks the loop if the optimization flag is untrue
		// which means, no swaps are made
		// this results in no further useless iterations
		if !swapped {
			break
		}
	}
}

func main() {
	// implementation of a simple bubble sort algorithm in go
	items := []int{12, 33, 567, 322, 74, 122, 4747, 90, -12, -22, 64}

	fmt.Println(items)
	bubbleSort(&items)
	fmt.Println(items)
}
