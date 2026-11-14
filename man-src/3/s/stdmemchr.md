---
title: "stdmemchr(3)"
name: "stdmemchr"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdmemchr/"
---

std::memchr - std::memchr

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cstring&gt;

    const void *memchr(const void *ptr, int ch, std::size_t count);

void *memchr(void *ptr, int ch, std::size_t count);</code></pre> 
Converts ch to unsigned char and locates the first occurrence of that value in the initial count characters (each interpreted as unsigned char) of the object pointed to by ptr. 
This function behaves as if it reads the characters sequentially and stops as soon as a matching character is found: if the array pointed to by ptr is smaller than count, but the match is found within the array, the behavior is well-defined <i>(since C++17)</i> 

<h2>Parameters</h2>

ptr - pointer to the object to be examined 
ch - character to search for 
count - max number of characters to examine

<h2>Return value</h2>

Pointer to the location of the character, or NULL if no such character is found. 

<h2>Example</h2>

Search an array of characters. 
 // Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;cstring&gt;
int main()

{
    char arr[] = {'a', '\0', 'a', 'A', 'a', 'a', 'A', 'a'};
    char *pc = (char *)std::memchr(arr, 'A', sizeof arr);
    if (pc != NULL)
        std::cout &lt;&lt; &quot;search character found\n&quot;;
    else
        std::cout &lt;&lt; &quot;search character not found\n&quot;;
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;search character found

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;finds the first occurrence of a character 
strchr <i>(function)</i> 
find 
find_if 
find_if_not finds the first element satisfying specific criteria 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
