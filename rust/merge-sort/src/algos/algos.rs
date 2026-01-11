use std::cmp::PartialOrd;

fn merge<T: PartialOrd + Copy>(data: &mut [T], mid: usize) -> () {
    let mut temp = Vec::with_capacity(data.len());
    let (left, right) = data.split_at(mid);

    let mut i = 0; // left ptr
    let mut j = 0; // right ptr

    // first copy into the left most elements
    // ensuring the smallest elements go left
    // and the larger elements go right
    while i < left.len() && j < right.len() {
        if left[i] <= right[j] {
            temp.push(left[i]);
            i += 1;
        } else {
            temp.push(right[j]);
            j += 1;
        }
    }

    // start copying remaining elements from left
    temp.extend_from_slice(&left[i..]);

    // start copying remaining elements from the right
    temp.extend_from_slice(&right[j..]);

    // copy back into data from the temp slice
    data.copy_from_slice(&temp);
}

pub fn merge_sort<T: PartialOrd + Copy>(data: &mut [T]) -> () {
    let len = data.len();
    if len < 2 {
        return;
    }

    let mid = len / 2;
    merge_sort(&mut data[..mid]);
    merge_sort(&mut data[mid..]);

    merge(data, mid);
}
