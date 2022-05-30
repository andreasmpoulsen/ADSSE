# Hash Tables Exercises

## 1

Suppose we have a dynamic set, S, stored in a direct‐address table, T, of length m. Write a procedure for finding the maximum element in S. What is the worst-­case running time of this procedure?

### Solution

Suppose that we maintain a variable "max" with the lowest possible value. Now we iterate through each element in the set and check if the current value is greater than the max variable. If it is, then the current value becomes max element else we move to the next element. We keep iterating over all the elements in the set. The worst case running time would be $O(n)$

## 2

A **bit vector** is simply an array of bits. A bit vector of length m takes much
less space than an array of m pointers. How could you use a bit vector to
represent a dynamic set of distinct elements with no satellite data? Write
dictionary operations for this implementation and confirm that their
running times are all $O(1)$.

### Solution

If no satellite data needs to be store, we can create a bit vector of size $m$, where $m$ is the largest element we can store. Each index in the bit array is analogous to an element. If an element is present, the value at that specific index is 1, else it is 0. That way all the dictionary operations (Search, Insert and Delete) will run in $O(1)$ time.

```text
SEARCH(B, k)
    return B[k]
```

```text
INSERT(B, k)
    if not B[k]
        B[k] = 1
```

```text
DELETE(B, k)
    if B[k]
        B[k] = 0
```


## 3

Suppose a hash function, h, hashes n distinct keys to an array T of length
m. Assuming simple uniform hashing, what is the expected number of
collisions? More precisely, what is the expected cardinality of $\{\{k,l\}: k≠l
\text{ and } h(k) = h(l)\}$

### Solution

Here we need to calculate the load factor:
$$
\alpha = \frac{n}{m}
$$

## 4

Show what happens when we insert the keys 5, 28, 19, 15, 20, 33, 12, 17
and 10 into a hash table where collisions are resolved by chaining.
Suppose the table has 9 slots and let the hash function, $h(k) = k \% 9$.

### Solution

$$
h(5) = 5 \% 9 = 5
$$
$$
h(28) = 28 \% 9 = 1
$$
$$
h(19) = 19 \% 9 = 1
$$
$$
h(15) = 15 \% 9 = 6
$$
$$
h(20) = 20 \% 9 = 2
$$
$$
h(33) = 33 \% 9 = 6
$$
$$
h(12) = 12 \% = 3
$$
$$
h(17) = 17 \% 9 = 8
$$
$$
h(10) = 10 \% 9 = 1
$$
| 1  |  2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|
|10 -> 19 -> 28|20|12||5|15 -> 35||17||
