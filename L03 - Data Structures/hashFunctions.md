# Hash Functions Exercises

## 1

Suppose we wish to search a linked list of length $n$, where each element contains a key $k$ along with a hash value $h(k)$. Each key is a long character string. How might we take advantage of the hash values when searching the list for an element with a given key?

### Solution

We will only search for elements with the same hash value as our key.

## 2

Consider a hash table of size $m=1000$ and a corresponding hash function $h(k)=\lfloor m(kA\%1)\rfloor$ for $A=(\sqrt{5}-1)/2$. Compute the locations to which the keys 61, 62, 63, 64 and 65 are mapped.

### Solution

$$
h(61) = \lfloor 1000(61 * ((\sqrt{5}-1)/2)\%1)\rfloor = 1000 * 0.7 = 700
$$
$$
h(62) = 318
$$
$$
h(63) = 936
$$
$$
h(64) = 554
$$
$$
h(65) = 172
$$