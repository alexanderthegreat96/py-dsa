// merge sort implementation for rust
mod algos;
use crate::algos::merge_sort;

fn main() {
    let mut numbers = vec![38, 27, 43, 3, 9, 82, 10];
    println!("Unsorted Numbers: {:?}", numbers);
    merge_sort(&mut numbers);
    println!("Sorted Numbers: {:?}", numbers);

    let mut words = vec!["zebra", "apple", "mango"];
    println!("Unsorted Strings: {:?}", words);
    merge_sort(&mut words);
    println!("Sorted Strings: {:?}", words);
}
