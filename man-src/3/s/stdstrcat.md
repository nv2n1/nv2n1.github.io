---
title: "stdstrcat(3)"
name: "stdstrcat"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdstrcat/"
---

std::strcat - std::strcat

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cstring&gt;

    char *strcat(char *dest, const char *src);</code></pre> 
Appends a copy of the character string pointed to by src to the end of the character string pointed to by dest. The character src[0] replaces the null terminator at the end of dest. The resulting byte string is null-terminated. 
The behavior is undefined if the destination array is not large enough for the contents of both src and dest and the terminating null character. 
The behavior is undefined if the strings overlap. 

<h2>Parameters</h2>

dest - pointer to the null-terminated byte string to append to 
src - pointer to the null-terminated byte string to copy from

<h2>Return value</h2>

dest 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;cstring&gt;

#include &lt;cstdio&gt;
int main()

{
    char str[50] = &quot;Hello &quot;;
    char str2[50] = &quot;World!&quot;;
    std::strcat(str, str2);
    std::strcat(str, &quot; Goodbye World!&quot;);
    std::puts(str);
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;Hello World! Goodbye World!

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;concatenates a certain amount of characters of two strings 
strncat <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;copies one string to another 
strcpy <i>(function)</i> 
