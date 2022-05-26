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

$A=\langle 13,19,9,5,12,8,7,4,11,2,6,21\rangle, p = 0, r = 11$
$$
x = A[p] = A[0] = 13
$$
$$
i = p - 1 = 0 - 1 = -1
$$
$$
j = r + 1 = 11 + 1 = 12
$$
REPEAT $j = j - 1$ UNTIL $A[j] \le x$:

After one decrement, $j = 12 - 1 = 11$, and $A[11] = 21$, so the condition is fulfilled

REPEAT $i = i + 1$ UNTIL $A[i]\ge x$:

After one increment, $i = -1 + 1 = 0$, and $A[1] = 13$, so the condition is fulfilled

IF $i < j$ EXCHANGE $A[i]$ with $A[j]$:

$A=\langle 21,19,9,5,12,8,7,4,11,2,6,13\rangle$

REPEAT $j = j - 1$ UNTIL $A[j] \le x$:

After ten decrements, $j = 11 - 10 = 1$, and $A[1] = 19$, so the condition is fulfilled

REPEAT $i = i + 1$ UNTIL $A[i]\ge x$:

After one increment, $i = 0 + 1 = 1$, and $A[1] = 19$, so the condition is fulfilled

IF $i < j$ EXCHANGE $A[i]$ with $A[j]$:

$i = j$, so return $j$

Assuming that the subarray $A[p..r]$ contains at least two elements, prove the following:

### b

The indices _i_ and _j_ are such that we never access an element of _A_ outside the subarray $A[p..r]$

### c

When HOARE-PARTITION terminates, it returns a value _j_ such that $p\le j<r$

### d

Every element of $A[p..j]$ is less than or equal to every element of $A[j+1..r]$ when HOARE-PARTITION terminates
