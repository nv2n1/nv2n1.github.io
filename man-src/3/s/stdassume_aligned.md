---
title: "stdassume_aligned(3)"
name: "stdassume_aligned"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdassume_aligned/"
---

std::assume_aligned - std::assume_aligned

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;memory&gt;

    template &lt;std::size_t N, class T&gt;
    (since C++ 20)

        [[nodiscard]] constexpr T *assume_aligned(T *ptr);
Informs the implementation that the object ptr points to is aligned to at least N.The implementation may use this information to generate more efficient code, but it might only make this assumption if the object is accessed via the return value of assume_aligned.

                                                                                                                                                                   The program is ill -
                                                                                                                                                                   formed if N is not a power of 2. The behavior is undefined if ptr does not point to an object of type T(ignoring cv - qualification at every level),
    or if the object's alignment is not at least N.
</code></pre>

<h2>Return value</h2>

ptr. 

<h2>Exceptions</h2>

Throws nothing.

<h2>Notes</h2>

To ensure that the program benefits from the optimizations enabled by assume_aligned, it is important to access the object via its return value: <pre><code>void f(int *p)
{
    int *p1 = std::assume_aligned&lt;256&gt;(p);
    // Use p1, not p, to ensure benefit from the alignment assumption.
    // However, the program has undefined behavior if p is not aligned
    // regardless of whether p1 is used.
}</code></pre> 
It is up to the program to ensure that the alignment assumption actually holds. A call to assume_aligned does not cause the compiler to verify or enforce this. 
