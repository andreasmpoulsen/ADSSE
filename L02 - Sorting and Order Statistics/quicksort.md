# Quicksort Exercises

## 1

Show that the running time of QUICKSORT is $\Theta(n^2)$ when the array _A_ contains distinct elements and is sorted in decreasing order.

### Solution

In this case, partioning will make one partition with $n-1$ elements, and one partition with $0$ elements.

This gives the following reccurrence:
$$
T(n)=T(n-1)+T(0)+\Theta(n)=T(n-1)+\Theta(n)
$$

Now, if we sum the cost on each level, we get:
$$
\sum^n_{i=1}i=n(n-1)/2=\Theta(n^2)
$$

Which is the running time of QUICKSORT in the worst case.

## 2

Suppose that the splits at every level of QUICKSORT are in the proportion $1-\alpha$ to $\alpha$, where $0<\alpha\le 1/2$ is a constant. Show that the minimum depth of a leaf in the recursion tree is approximately $-\lg n/\lg\alpha$ and that the maximum depth is approximately $-\lg n/\lg(1-\alpha)$. (Don't worry about integer round-off.)

### Solution
The minimum depth follows a path that always takes the smaller part of the partition - i.e., that multiplies the number of elements by $\alpha$. One iteration reduces the number of elements from $n$ to $\alpha n$, and $i$ iterations reduce the number of elements to $\alpha^in$. At a leaf, there is just one remaining element and so at a minimum-depth leaf of depth m, we have $\alpha^mn=1$. Thus $\alpha^m=\frac{1}{n}$. Taking logs we get $m=-\lg n/ \lg \alpha$.

The maximum depth follows a path that always takes the larger part of the partition - i.e., that multiplies the number of elements by $\alpha - 1$. One iteration reduces the number of elements from $n$ to $(\alpha - 1)n$, and $i$ iterations reduce the number of elements to $(\alpha - 1)^in$. At a leaf, there is just one remaining element and so at a maximum-depth leaf of depth $m$, we have $(\alpha-1)^mn=1$. Thus $(\alpha - 1)^m=\frac{1}{n}$. Taking logs we get $m=-\lg n/\lg(\alpha -1)$.

## 3

The original partition algorithm is:

```text
HOARE-PARTITION(A,p,r)
    x = A[p]
    i = p - 1
    j = r + 1
    while TRUE
        repeat
        j = j - 1
        until A[j] <= x
        repeat
            i = i + 1
        until A[i] >= x
        if i < j
            exchange A[i] with A[j]
        else return j
```

### a

Demonstrate the operation of HOARE-PARTITION on the array $A=\langle 13,19,9,5,12,8,7,4,11,2,6,21\rangle$, showing the values of the array and auxiliary values after each iteration of the while loop.

#### Solution

$A=\langle 13,19,9,5,12,8,7,4,11,2,6,21\rangle, p = 1, r = 12$
$$
x = A[p] = A[1] = 13
$$
$$
i = p - 1 = 1 - 1 = 0
$$
$$
j = r + 1 = 12 + 1 = 13
$$

##### 1st loop

REPEAT $j = j - 1$ UNTIL $A[j] \le x$
    - After 2 decrements, $j = 13 - 2 = 11$ and $A[11] = 6$
  
REPEAT $i = i + 1$ UNTIL $A[j] \ge x$
    - After 1 increment, $i = 0 + 1 = 1$ and $A[1] = 13$

IF $i < j$ EXCHANGE $A[i]$ WITH $A[j]$
    - $A=\langle 6, 19, 9, 5, 12, 8, 7, 4, 11, 2, 13, 21 \rangle$

##### 2nd loop

REPEAT $j = j - 1$ UNTIL $A[j] \le x$
    - After 1 decrement, $j = 11 - 1 = 10$ and $A[10] = 2$
  
REPEAT $i = i + 1$ UNTIL $A[j] \ge x$
    - After 1 increment, $i = 1 + 1 = 2$ and $A[2] = 19$

IF $i < j$ EXCHANGE $A[i]$ WITH $A[j]$
    - $A=\langle 6, 2, 9, 5, 12, 8, 7, 4, 11, 19, 13, 21 \rangle$

##### 3rd loop

REPEAT $j = j - 1$ UNTIL $A[j] \le x$
    - After 1 decrement, $j = 10 - 1 = 9$ and $A[9] = 11$
  
REPEAT $i = i + 1$ UNTIL $A[j] \ge x$
    - After 8 increments, $i = 2 + 8 = 10$ and $A[19] = 19$

IF $i < j$ EXCHANGE $A[i]$ WITH $A[j]$
    - ELSE RETURN j

### b

Assuming that the subarray $A[p..r]$ contains at least two elements, prove the following:

The indices _i_ and _j_ are such that we never access an element of _A_ outside the subarray $A[p..r]$

#### Solution

Because when HOARE-PARTITION is running, $p \le i < j \le r$ will always hold, $i$, $j$ won't access any element of A outside the subarray $A[p..r]$.

### c

When HOARE-PARTITION terminates, it returns a value _j_ such that $p\le j<r$

#### Solution

HOARE-PARTITION terminates when $j\ge i$, so therefore $p\le j < r$.

### d

Every element of $A[p..j]$ is less than or equal to every element of $A[j+1..r]$ when HOARE-PARTITION terminates

#### Solution

At the time of termination, all elements in $A[p..j]$ are less than or equal to x, and all elements in $A[j+1..r]$ are greater than or equal to x.

### e

Rewrite the QUICKSORT procedure to use HOARE-PARTITION.

```text
QUICKSORT(A, p, r)
    if p < r
        q = HOARE-PARTITION(A, p, r)
        QUICKSORT(A, p, q)
        QUICKSORT(A, q + 1, r)
```
