# Exercises for Lecture 1: Growth of Functions

Following taken from page 50 of Cormen et al. (2001)

## Exercises

### 3.1-1

Let $f(n)$ and $g(n)$ be asymptotically nonnegative functions. Using the basic definition of $\Theta$-notation, prove that $\max(f(n),g(n)) = \Theta(f(n)+g(n))$.

#### Answer

To prove this we have to show the existence of the constants $c_1$, $c_2$, $n_0<0$, such that $n\ge n_0$.

$$
0\le c_1(f(n)+g(n))\le\max(f(n),g(n))\le c_2(f(n)+g(n))
$$

As the functions are asymptotically non-negative, we can assume that for some $n_0 > 0$, $f(n)\ge 0$ and $g(n) \ge 0$. We therefore have $n\ge n_0$

$$
f(n)+g(n)\ge\max(f(n),g(n))
$$

We note that $f(n)\le\max(f(n),g(n))$ and $g(n)\le\max(f(n),g(n))$:

$$
f(n)+g(n)\le2\max(f(n),g(n))
$$

$$
\frac{f(n)}{2}+\frac{g(n)}{2}\le\frac{2\max(f(n),g(n))}{2}
$$

$$
\frac{1}{2}(f(n)+g(n))\le\max(f(n),g(n))
$$

Then we combine the two inequalities:

$$
0\le\frac{1}{2}(f(n)+g(n))\le\max(f(n),g(n))\le(f(n)+g(n))
$$

Meaning that $\max(f(n),g(n))=\Theta(f(n)+g(n))$, because there exists $c_1=0.5$ and $c_2=1$

### 3.1-2

Show that for any real constants $a$ and $b$, where $b>0$,
$$
(n+a)^b=\Theta(n^b)
$$

#### Answer

Here, $a$ is just a constant, so it can be ignored, and the result is an asymptotically tight upper and lower bound of $n$ to the $b$-th order.

### 3.1-3

Explain why the statement, "The running time of an algorithm $A$ is at least $O(n^2)$," is meaningless

#### Answer

This statement only concludes an upper bound of the algorithm, but it is not necesarrily tight, so any upper bound more rapid than $n^2$ would be valid as well. For the lower bound, if the running time were $O(n^2)$, anything below is still available. Therefore, all options are still on the table, and the sentence is meaningless.

### 3.1-4

* Is $2^{n+1} = O(2^n)$?
* Is $2^{2n} = O(2^n)$?

#### Answer

* Yes, the $1$ has such a small effect for larger $n$, that it can be neglected
* No, the $2$ means that $n$ will always be doubled, so that will have a big enough effect that it should be accounted for

### 3.1-5

Prove Theorem 3.1.

>Theorem 3.1
>For any two functions $f(n)$ and $g(n)$, we have $f(n) = \Theta(g(n))$ if and only if $f(n)=O(g(n))$ and $f(n)=\Omega(g(n))$

#### Answer

To prove this theorem, we need to show that the logic holds both ways, i.e.

$$
f(n)=\Theta(g(n)) \Rightarrow f(n)=O(g(n)) \text{ and } f(n)=\Omega(g(n))
$$

<center>and</center>

$$
f(n)=O(g(n)) \text{ and } f(n)=\Omega(g(n))\Rightarrow f(n)=\Theta(g(n))
$$

##### Part 1

If $f(n)=\Theta(g(n))$, then for $n\ge n_0$,

$$
0\le c_1g(n)\le f(n)\le c_2g(n)
$$

As $0\le f(n)\le c_2g(n)$ for $n\ge n_0$, $f(n)=O(g(n))$
As $0\le c_1g(n)\le f(n)$ for $n\ge n_0$, $f(n)=\Omega(g(n))$

##### Part 2

If $f(n) = \Omega(g(n))$, then for $n\ge n_1$,

$$
0\le c_1g(n)\le f(n)
$$

If $f(n)=O(g(n))$, then for $n\ge n_2$,

$$
0\le f(n)\le c_2g(n)
$$

Combining the above two inequalities, we can say for $n\ge \max(n_1,n_2)$,

$$
0\le c_1g(n)\le f(n)\le c_2g(n)
$$

In other words, $f(n) = \Theta(g(n))$

### 3.1-6

Prove that the running time of an algorithm is $\Theta(g(n))$ if and only if its worst-case running time is $O(g(n))$ and its best-case running time is $\Omega(g(n))$.

#### Answer

Since $\Theta$ represents both upper and lower bounds, it is necessary for $O$ and $\Omega$ to be the same, asymptotically tight bounds on $g(n)$

### 3.1-7

Prove that $o(g(n)) \cap \omega(g(n))$ is the empty set.

#### Answer

$o$ and $\omega$ are both strictly loose bounds on $g(n)$, so by definition, there is no intersection between the two.

### 3.1-8

We can extend our notation to the case of two parameters $n$ and $m$ that can go to infinity independently at different rates. For a given function $g(n,m)$, we denote by $O(g(n,m))$ the set of functions

$$
\begin{matrix}
O(g(n,m))=\{f(n,m):& \text{there exists positive constants } c, n_0, \text{ and } m_0\\ & \text{such that } 0\le f(n,m)\le cg(n,m) \text{ for all}\\ &n\ge n_0\text{ or }m\ge m_0\}
\end{matrix}
$$

Give corresponding definitions for $\Omega(g(n,m))$ and $\Theta(g(n,m))$

#### Answer

