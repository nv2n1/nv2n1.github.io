---
title: "stdstrncat(3)"
name: "stdstrncat"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdstrncat/"
---

std::strncat - std::strncat

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cstring&gt;

    char *strncat(char *dest, const char *src, std::size_t count);</code></pre> 
Appends a byte string pointed to by src to a byte string pointed to by dest. At most count characters are copied. The resulting byte string is null-terminated. 
The destination byte string must have enough space for the contents of both dest and src plus the terminating null character, except that the size of src is limited to count. 
The behavior is undefined if the strings overlap. 

<h2>Parameters</h2>

dest - pointer to the null-terminated byte string to append to 
src - pointer to the null-terminated byte string to copy from 
count - maximum number of characters to copy

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
    std::strncat(str, &quot; Goodbye World!&quot;, 3);
    std::puts(str);
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;Hello World! Go

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;concatenates two strings 
strcat <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;copies one string to another 
strcpy <i>(function)</i> 
