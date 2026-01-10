package main

import "fmt"

func printFirstItemThenFirstHalfThenSayHi100Times(items []string) {
	if len(items) == 0 {
		return
	}

	// Print the first item
	fmt.Println(items[0]) // O(1)
	halfLength := len(items) / 2

	for i := 0; i < halfLength; i++ { // O(n/2) -> O(n)
		fmt.Println(items[i])
	}

	for i := 0; i < 100; i++ { // O(1)
		fmt.Println("Hi")
	}
}

func main() {
	sampleItems := []string{"apple", "banana", "cherry", "date", "elderberry", "fig", "grape"}
	printFirstItemThenFirstHalfThenSayHi100Times(sampleItems)
}
