---
title: "stdstrcpy(3)"
name: "stdstrcpy"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdstrcpy/"
---

std::strcpy - std::strcpy

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cstring&gt;

    char *strcpy(char *dest, const char *src);</code></pre> 
Copies the character string pointed to by src, including the null terminator, to the character array whose first element is pointed to by dest. 
The behavior is undefined if the dest array is not large enough. The behavior is undefined if the strings overlap. 

<h2>Parameters</h2>

dest - pointer to the character array to write to 
src - pointer to the null-terminated byte string to copy from

<h2>Return value</h2>

dest 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;cstring&gt;

#include &lt;memory&gt;
int main()

{
    const char *src = &quot;Take the test.&quot;;

    //  src[0] = 'M'; // can't modify string literal
    auto dst = std::make_unique&lt;char[]&gt;(std::strlen(src) + 1); // +1 for the null terminator
    std::strcpy(dst.get(), src);
    dst[0] = 'M';
    std::cout &lt;&lt; src &lt;&lt; '\n'
              &lt;&lt; dst.get() &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;Take the test. 
&nbsp;<wbr>&nbsp;Make the test.

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;copies a certain amount of characters from one string to another 
strncpy <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;copies one buffer to another 
memcpy <i>(function)</i> 
