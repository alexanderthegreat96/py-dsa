package main

import (
	"cmp"
	"fmt"
)

// using cmp.Ordered
// to tell the compiler this works with any data type
func mergeSort[T cmp.Ordered](data []T, start int, end int) {
	if (end - start) < 2 {
		return
	}

	mid := (start + end) / 2

	mergeSort(data, start, mid)
	mergeSort(data, mid, end)

	merge(data, start, mid, end)
}

func merge[T cmp.Ordered](data []T, start, mid, end int) {
	// 2 halves are already in order so skip this
	if data[mid-1] <= data[mid] {
		return
	}

	leftPos := start
	rightPos := mid
	tempIndex := 0

	// alocating enough memory for the slice
	temp := make([]T, end-start)

	for leftPos < mid && rightPos < end {
		if data[leftPos] <= data[rightPos] {
			temp[tempIndex] = data[leftPos]
			leftPos++
		} else {
			temp[tempIndex] = data[rightPos]
			rightPos++
		}
		tempIndex++
	}

	// copy whatever remains in either halves
	// only one loop runs anyways
	for leftPos < mid {
		temp[tempIndex] = data[leftPos]
		leftPos++
		tempIndex++
	}

	for rightPos < end {
		temp[tempIndex] = data[rightPos]
		rightPos++
		tempIndex++
	}

	// copy the entire sorted slice into the original one
	for i := range temp {
		data[start+i] = temp[i]
	}
}

func main() {
	// long integer slices
	longInts := []int{98, 23, 45, 14, 6, 67, 33, 42, 10, 88, 54, 2, 19, 76, 50, 31, 4, 99, 25, 8}
	fmt.Println("Original Ints (Length 20):", longInts)
	mergeSort(longInts, 0, len(longInts))
	fmt.Println("Sorted Ints:              ", longInts)
	fmt.Println("--------------------------------------------------")

	// strings
	longStrings := []string{
		"Zebra", "Apple", "Mango", "Peach", "Banana",
		"Cherry", "Elderberry", "Fig", "Grape", "Date",
	}
	fmt.Println("Original Strings:", longStrings)
	mergeSort(longStrings, 0, len(longStrings))
	fmt.Println("Sorted Strings:  ", longStrings)
	fmt.Println("--------------------------------------------------")

	// precision floating point numbers
	longFloats := []float64{10.5, 2.3, 10.55, 0.42, 1.1, 9.9, 5.67, 4.32, 0.01, 100.2}
	fmt.Println("Original Floats:", longFloats)
	mergeSort(longFloats, 0, len(longFloats))
	fmt.Println("Sorted Floats:  ", longFloats)
	fmt.Println("--------------------------------------------------")

	// already sorted data
	sortedSlice := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
	fmt.Println("Testing already sorted slice...")
	mergeSort(sortedSlice, 0, len(sortedSlice))
	fmt.Println("Result:", sortedSlice)
}
