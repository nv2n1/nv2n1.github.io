---
title: "stdqsort(3)"
name: "stdqsort"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdqsort/"
---

std::qsort - std::qsort

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cstdlib&gt;

    void qsort(void *ptr, std::size_t count, std::size_t size, /*compare-pred*/ *comp);
(1)

    void qsort(void *ptr, std::size_t count, std::size_t size, /*c-compare-pred*/ *comp);

extern &quot;C++&quot; using /*compare-pred*/ = int(const void *, const void *); // exposition-only (2)

extern &quot;C&quot; using /*c-compare-pred*/ = int(const void *, const void *); // exposition-only</code></pre> 
Sorts the given array pointed to by ptr in ascending order. The array contains count elements of size bytes. Function pointed to by comp is used for object comparison. 
If comp indicates two elements as equivalent, their order is unspecified. 

<h2>Parameters</h2>

ptr - pointer to the array to sort 
count - number of elements in the array 
size - size of each element in the array in bytes 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;comparison function which returns a negative integer value if the first argument is less than the second, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;a positive integer value if the first argument is greater than the second and zero if the arguments are equal. 
comp - The signature of the comparison function should be equivalent to the following: 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int cmp(const void *a, const void *b); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The function must not modify the objects passed to it and must return consistent results when called for the same objects, regardless of their positions in the array. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;

<h2>Return value</h2>

<i>(none)</i> 

<h2>Notes</h2>

Despite the name, C++, C, and POSIX standards do not require this function to be implemented using quicksort or make any complexity or stability guarantees. 
The type of the elements of the array must be a TrivialType, otherwise the behavior is undefined. 
The two overloads provided by the C++ standard library are distinct because the types of the parameter comp are distinct (language_linkage is part of its type) 

<h2>Example</h2>

The following code sorts an array of integers using qsort(). 
 // Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;cstdlib&gt;

#include &lt;climits&gt;
int main()

{
    int a[] = {-2, 99, 0, -743, 2, INT_MIN, 4};
    constexpr std::size_t size = sizeof a / sizeof *a;
    std::qsort(a, size, sizeof *a, [](const void *a, const void *b) {
        int arg1 = *static_cast&lt;const int *&gt;(a);
        int arg2 = *static_cast&lt;const int *&gt;(b);
        if (arg1 &lt; arg2)
            return -1;
        if (arg1 &gt; arg2)
            return 1;
        return 0;
        //  return (arg1 &gt; arg2) - (arg1 &lt; arg2); // possible shortcut
        //  return arg1 - arg2; // erroneous shortcut (fails if INT_MIN is present)
    });
    for (int ai : a)
        std::cout &lt;&lt; ai &lt;&lt; ' ';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;-2147483648 -743 -2 0 2 4 99

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;searches an array for an element of unspecified type 
bsearch <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sorts a range into ascending order 
sort <i>(function template)</i> 
is_trivial checks if a type is trivial 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
