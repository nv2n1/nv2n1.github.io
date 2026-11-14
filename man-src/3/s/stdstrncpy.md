---
title: "stdstrncpy(3)"
name: "stdstrncpy"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdstrncpy/"
---

std::strncpy - std::strncpy

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cstring&gt;

    char *strncpy(char *dest, const char *src, std::size_t count);</code></pre> 
Copies at most count characters of the byte string pointed to by src (including the terminating null character) to character array pointed to by dest. 
If count is reached before the entire string src was copied, the resulting character array is not null-terminated. 
If, after copying the terminating null character from src, count is not reached, additional null characters are written to dest until the total of count characters have been written. 
If the strings overlap, the behavior is undefined. 

<h2>Parameters</h2>

dest - pointer to the character array to copy to 
src - pointer to the byte string to copy from 
count - maximum number of characters to copy

<h2>Return value</h2>

dest 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;cstring&gt;
int main()

{
    const char *src = &quot;hi&quot;;
    char dest[6] = {'a', 'b', 'c', 'd', 'e', 'f'};
    std::strncpy(dest, src, 5);
    std::cout &lt;&lt; &quot;The contents of dest are: &quot;;
    for (char c : dest) {
        if (c) {
            std::cout &lt;&lt; c &lt;&lt; ' ';
        } else {
            std::cout &lt;&lt; &quot;\\0&quot; &lt;&lt; ' ';
        }
    }
    std::cout &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;The contents of dest are: h i \0 \0 \0 f

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;copies one string to another 
strcpy <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;copies one buffer to another 
memcpy <i>(function)</i> 
