package main

import "fmt"

func someFunction() {
	fmt.Println("Im just printing text")
}

func funChallenge(input []int) int {
	var a int = 10 // O(1)
	a = 50 + 3     // O(1)

	// O(n) + O(n) + O(n) + O(n) = O(4n) = O(n)
	for i := 0; i < len(input); i++ { // O(n)
		someFunction()                                           // O(n)
		stranger := true                                         // O(n)
		fmt.Printf("Iteration: %d is stranger: %t", i, stranger) // O(n)
		a++
	}

	return a
}

func main() {
	var testData []int = []int{1, 2, 3, 4, 5}
	funChallenge(testData)
}
