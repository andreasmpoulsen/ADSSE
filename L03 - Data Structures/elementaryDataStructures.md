# Elementary Data Structures Exercises

## 1

Rewrite ENQUEUE and DEQUEUE to detect underflow and overflow.

```text
ENQUEUE(Q,x)
    Q[Q.tail] = x
    if Q.tail == Q.length
        Q.tail = 1
    else Q.tail = Q.tail + 1
```

```text
DEQUEUE(Q)
    x = Q[Q.head]
    if Q.head == Q.length
        Q.head = 1
    else Q.head = Q.head + 1
    return x
```

### Solution

```text
ENQUEUE(Q,x)
    Q[Q.tail] = x
    if Q.head == (Q.tail + 1) or (Q.tail == Q.length and Q.head == 1)
        error "Overflow"
    if Q.tail == Q.length
        Q.tail = 1
    else Q.tail = Q.tail + 1
```

```text
DEQUEUE(Q)
    x = Q[Q.head]
    if Q.head == Q.tail
        error "Underflow"
    if Q.head == Q.length
        Q.head = 1
    else Q.head = Q.head + 1
    return x
```

## 2

How would you implement a queue using two stacks? Analyse the running time of the queue operations

### Solution

We keep one stack empty and one stack filled with values in head to tail order. DEQUEUE is just POP of the filled stack and ENQUEUE can be done by shifting the values from the filled stack to the empty stack, inserting the ENQUEUEd value, and then shifting all previous elements back again.

Running time would be linear for ENQUEUE as we would traverse through the entire queue every time.

Constant time for DEQUEUE as it is just a POP operation.

## 3

Can you implement the dynamic set operations INSERT and DELETE on a singly-linked list in O(1) time?

### Solution

For INSERT, yes, as LIST-INSERT(L, x) runs in $O(1)$ time, however, for LIST-DELETE(L, x) it depends whether we have to find an element with a particular key first.
If not, we can do it in $O(1)$ time, else it would be in $\Theta(n)$ time.

## 4

Implement a stack using a singly-linked list. What are the running times of PUSH and POP using this implementation?

### Solution

LIST-INSERT and PUSH are the same, so PUSH would have a running time of $O(1)$.
LIST-DELETE and POP are the same, so POP would have a running time of $O(1)$

## 5

Implement a queue by a singly-linked list. What are the running times of ENQUEUE and DEQUEUE using this implementation?

### Solution

LIST-INSERT and ENQUEUE are the same, so ENQUEUE would have a running time of $O(1)$
For DEQUEUE we need two lists. One with values and one empty list.
We would then have to LIST-DELETE n - 1 elements, and LIST-INSERT them into the other list.
Then, we can delete the last element.
All elements in the other array are then LIST-DELETEd and LIST-INSERTed back into the initial list.

## 6

As written in the lecture, each loop iteration in the LIST-SEARCH procedure requires two tests: one for $x \neq \text{L.nil}$ and one for $\text{x.key} \neq k$. How could you eliminate the test for $x \neq \text{L.nil}$ in each iteration?

### Solution

```text
LIST-SEARCH(L, k)
    x = L.NIL.next
    L.nil.key = k
    while x.key != k
        x = x.next
    return x
```
