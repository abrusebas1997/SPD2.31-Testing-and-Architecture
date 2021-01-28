# Solutions
## Merge Sort
### Bug 1: `IndexError: list index out of range`
- Change from `i` to `j` -> `right_side[j]`
    ```
    line 37, in merge_sort
        arr[k] = right_side[i]
    ```

### Bug 2: List sorted in descending order
- Change line 23 `>` to `<` :   
```python
    if left_side[i] < right_side[j]:
```

### Bug 3: `2` appears three times, missing `6` and `7`
- Increment `k +=1 ` in the `while` `i`/`j` < `len(left_side)`/`len(right_side)` checks
```python
    while i < len(left_side):
        arr[k] = left_side[i]
        i += 1
        k += 1

    while j < len(right_side):
        arr[k] = right_side[j]
        j += 1
        k += 1
```

## Binary Search

### Bug 1: `TypeError: list indices must be integers or slices, not float`
- For line, 51, use floor int division (`//`) for mid  
```python
    mid = (high + low) // 2
```

### Bug 2: Comments/pseudocode is mismatched to code, 
- Rearranged pseudocode to line up with correct code

### Bug 3: Index of 5 is: -1, but should be 4
- Change line 49 to include condition when `low == high` so that it can complete and utilize the `else` condition to return `mid`  
```python
    while low <= high:
```
