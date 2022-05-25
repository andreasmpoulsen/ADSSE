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
