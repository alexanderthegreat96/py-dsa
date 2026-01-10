package main

import (
	"cmp"
	"reflect"
	"testing"
)

func TestMergeSort(t *testing.T) {
	type testCase[T cmp.Ordered] struct {
		name     string
		input    []T
		expected []T
	}

	intTests := []testCase[int]{
		{
			name:     "Random Integers",
			input:    []int{54, 26, 93, 17, 77, 31, 44, 55, 20},
			expected: []int{17, 20, 26, 31, 44, 54, 55, 77, 93},
		},
		{
			name:     "Already Sorted",
			input:    []int{1, 2, 3, 4, 5},
			expected: []int{1, 2, 3, 4, 5},
		},
		{
			name:     "Reverse Sorted",
			input:    []int{5, 4, 3, 2, 1},
			expected: []int{1, 2, 3, 4, 5},
		},
		{
			name:     "Empty Slice",
			input:    []int{},
			expected: []int{},
		},
		{
			name:     "Single Element",
			input:    []int{10},
			expected: []int{10},
		},
	}

	stringTests := []testCase[string]{
		{
			name:     "Unsorted Strings",
			input:    []string{"peach", "apple", "banana", "cherry"},
			expected: []string{"apple", "banana", "cherry", "peach"},
		},
		{
			name:     "Capitalized Strings",
			input:    []string{"zebra", "Apple", "mango"},
			expected: []string{"Apple", "mango", "zebra"},
		},
	}

	for _, tt := range intTests {
		t.Run(tt.name, func(t *testing.T) {
			data := make([]int, len(tt.input))
			copy(data, tt.input)
			mergeSort(data, 0, len(data))
			if !reflect.DeepEqual(data, tt.expected) {
				t.Errorf("failed %s: expected %v, got %v", tt.name, tt.expected, data)
			}
		})
	}

	for _, tt := range stringTests {
		t.Run(tt.name, func(t *testing.T) {
			data := make([]string, len(tt.input))
			copy(data, tt.input)
			mergeSort(data, 0, len(data))
			if !reflect.DeepEqual(data, tt.expected) {
				t.Errorf("failed %s: expected %v, got %v", tt.name, tt.expected, data)
			}
		})
	}
}

func BenchmarkMergeSortLarge(b *testing.B) {
	size := 10000
	data := make([]int, size)
	for i := 0; i < size; i++ {
		data[i] = size - i
	}

	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		temp := make([]int, size)
		copy(temp, data)
		mergeSort(temp, 0, len(temp))
	}
}
