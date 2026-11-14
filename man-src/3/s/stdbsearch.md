---
title: "stdbsearch(3)"
name: "stdbsearch"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdbsearch/"
---

std::bsearch - std::bsearch

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cstdlib&gt;

    void *bsearch(const void *key, const void *ptr, std::size_t count,

                  std::size_t size, /*compare-pred*/ *comp);
(1)

    void *bsearch(const void *key, const void *ptr, std::size_t count,

                  std::size_t size, /*c-compare-pred*/ *comp);

extern &quot;C++&quot; using /*compare-pred*/ = int(const void *, const void *); // exposition-only (2)

extern &quot;C&quot; using /*c-compare-pred*/ = int(const void *, const void *); // exposition-only</code></pre> 
Finds an element equal to element pointed to by key in an array pointed to by ptr. The array contains count elements of size bytes each and must be partitioned with respect to the object pointed to by key, that is, all the elements that compare less than must appear before all the elements that compare equal to, and those must appear before all the elements that compare greater than the key object. A fully sorted array satisfies these requirements. The elements are compared using function pointed to by comp. 
The behavior is undefined if the array is not already partitioned in ascending order with respect to key, according to the same criterion that comp uses. 
If the array contains several elements that comp would indicate as equal to the element searched for, then it is unspecified which element the function will return as the result. 

<h2>Parameters</h2>

key - pointer to the element to search for 
ptr - pointer to the array to examine 
count - number of element in the array 
size - size of each element in the array in bytes 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;comparison function which returns a negative integer value if the first argument is less than the second, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;a positive integer value if the first argument is greater than the second and zero if the arguments are equal. key is passed as the first argument, an element from the array as the second. 
comp - The signature of the comparison function should be equivalent to the following: 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int cmp(const void *a, const void *b); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The function must not modify the objects passed to it and must return consistent results when called for the same objects, regardless of their positions in the array. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;

<h2>Return value</h2>

Pointer to the found element or null pointer if the element has not been found. 

<h2>Notes</h2>

Despite the name, neither C nor POSIX standards require this function to be implemented using binary search or make any complexity guarantees. 
The two overloads provided by the C++ standard library are distinct because the types of the parameter comp are distinct (language_linkage is part of its type) 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;cstdlib&gt;

#include &lt;iostream&gt;
int compare(const void *ap, const void *bp)

{
    const int *a = (int *)ap;
    const int *b = (int *)bp;
    if (*a &lt; *b)
        return -1;
    else if (*a &gt; *b)
        return 1;
    else
        return 0;
}
int main(int argc, char **argv)

{
    const int ARR_SIZE = 8;
    int arr[ARR_SIZE] = {1, 2, 3, 4, 5, 6, 7, 8};
    int key1 = 4;
    int *p1 = (int *)std::bsearch(&amp;key1, arr, ARR_SIZE, sizeof(arr[0]), compare);
    if (p1)
        std::cout &lt;&lt; &quot;value &quot; &lt;&lt; key1 &lt;&lt; &quot; found at position &quot; &lt;&lt; (p1 - arr) &lt;&lt; '\n';
    else
        std::cout &lt;&lt; &quot;value &quot; &lt;&lt; key1 &lt;&lt; &quot; not found\n&quot;;
    int key2 = 9;
    int *p2 = (int *)std::bsearch(&amp;key2, arr, ARR_SIZE, sizeof(arr[0]), compare);
    if (p2)
        std::cout &lt;&lt; &quot;value &quot; &lt;&lt; key2 &lt;&lt; &quot; found at position &quot; &lt;&lt; (p2 - arr) &lt;&lt; '\n';
    else
        std::cout &lt;&lt; &quot;value &quot; &lt;&lt; key2 &lt;&lt; &quot; not found\n&quot;;
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;value 4 found at position 3 
&nbsp;<wbr>&nbsp;value 9 not found

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sorts a range of elements with unspecified type 
qsort <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns range of elements matching a specific key 
equal_range <i>(function template)</i> 
