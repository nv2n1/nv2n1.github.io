---
title: "stdmemcmp(3)"
name: "stdmemcmp"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdmemcmp/"
---

std::memcmp - std::memcmp

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cstring&gt;

    int memcmp(const void *lhs, const void *rhs, std::size_t count);</code></pre> 
Reinterprets the objects pointed to by lhs and rhs as arrays of unsigned char and compares the first count characters of these arrays. The comparison is done lexicographically. 
The sign of the result is the sign of the difference between the values of the first pair of bytes (both interpreted as unsigned char) that differ in the objects being compared. 

<h2>Parameters</h2>

lhs, rhs - pointers to the memory buffers to compare 
count - number of bytes to examine

<h2>Return value</h2>

Negative value if the first differing byte (reinterpreted as unsigned char) in lhs is less than the corresponding byte in rhs. 
0 if all count bytes of lhs and rhs are equal. 
Positive value if the first differing byte in lhs is greater than the corresponding byte in rhs. 

<h2>Notes</h2>

This function reads object_representations, not the object values, and is typically only meaningful for trivially-copyable objects with no padding. For example, memcmp() between two objects of type std::string or std::vector will not compare their contents, and memcmp() between two objects of type struct{char c; int n;} will compare the padding bytes whose values may differ when the values of c and n are the same. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;cstring&gt;
void demo(const char *lhs, const char *rhs, std::size_t sz)

{
    std::cout &lt;&lt; std::string(lhs, sz);
    int rc = std::memcmp(lhs, rhs, sz);
    if (rc == 0)
        std::cout &lt;&lt; &quot; compares equal to &quot;;
    else if (rc &lt; 0)
        std::cout &lt;&lt; &quot; precedes &quot;;
    else if (rc &gt; 0)
        std::cout &lt;&lt; &quot; follows &quot;;
    std::cout &lt;&lt; std::string(rhs, sz) &lt;&lt; &quot; in lexicographical order\n&quot;;
}
int main()

{
    char a1[] = {'a', 'b', 'c'};
    char a2[sizeof a1] = {'a', 'b', 'd'};
    demo(a1, a2, sizeof a1);
    demo(a2, a1, sizeof a1);
    demo(a1, a1, sizeof a1);
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;abc precedes abd in lexicographical order 
&nbsp;<wbr>&nbsp;abd follows abc in lexicographical order 
&nbsp;<wbr>&nbsp;abc compares equal to abc in lexicographical order

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;compares two strings 
strcmp <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;compares a certain number of characters from two strings 
strncmp <i>(function)</i> 
