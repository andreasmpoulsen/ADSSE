# Sorting in Linear Time Exercises

## 1

Suppose we use Randomize-Select to select the minimum element of the array $A = \langle 3, 2, 9, 0, 7, 5, 4, 8, 6, 1\rangle$. Describe a sequence of partitions that results in a worst-case performance of Randomize-Select.

### Solution

The worst case of RANDOMIZED-SELECT is when we partition around the largest element.

So if the first pivot is 9, the partitions would be:
$l = \langle 3, 2, 1, 0, 7, 5, 4, 8, 6\rangle, r = \langle\rangle$

Then, the next pivot is 8:
$l = \langle 3, 2, 1, 0, 7, 5, 4, 6\rangle, r = \langle\rangle$

Next is 7:
$l = \langle 3, 2, 1, 0, 6, 5, 4\rangle, r = \langle\rangle$

6:
$l = \langle 3, 2, 1, 0, 4, 5\rangle, r = \langle\rangle$

5:
$l = \langle 3, 2, 1, 0, 4\rangle, r = \langle\rangle$

4:
$l = \langle 3, 2, 1, 0\rangle, r = \langle\rangle$

3:
$l = \langle 0, 2, 1\rangle, r = \langle\rangle$

2:
$l = \langle 0, 1\rangle, r = \langle\rangle$

1: $l = \langle 0\rangle, r = \langle\rangle$

## 2

In the algorithm SELECT, the input elements are divided into groups of 5. Will the algorithm work in linear time if they are divided into groups of 7? Argue that Select does not run in linear time if groups of 3 are used.

## 3

Show how QUICKSORT can be made to run in $O(n\lg n)$ time in the worst case, assuming that all elements are distinct

### Solution

The worst case running time of QUICKSORT happens when the array is already sorted, because the partition would be one-sided.

If we were to use the PARTITION algorithm from SELECT, the pivot would be the median, and that would guarantee equally sized partitions for QUICKSORT, and thus always give a best-case running time ($O(n\lg n)$)