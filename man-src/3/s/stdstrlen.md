---
title: "stdstrlen(3)"
name: "stdstrlen"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdstrlen/"
---

std::strlen - std::strlen

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cstring&gt;

    std::size_t strlen(const char *str);</code></pre> 
Returns the length of the given byte string, that is, the number of characters in a character array whose first element is pointed to by str up to and not including the first null character. The behavior is undefined if there is no null character in the character array pointed to by str. 

<h2>Parameters</h2>

str - pointer to the null-terminated byte string to be examined

<h2>Return value</h2>

The length of the null-terminated string str. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;cstring&gt;

#include &lt;iostream&gt;
int main()

{
    const char str[] = &quot;How many characters does this string contain?&quot;;
    std::cout &lt;&lt; &quot;without null character: &quot; &lt;&lt; std::strlen(str) &lt;&lt; '\n'
              &lt;&lt; &quot;with null character: &quot; &lt;&lt; sizeof str &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;without null character: 45 
&nbsp;<wbr>&nbsp;with null character: 46

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the length of a wide string 
wcslen <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the number of bytes in the next multibyte character 
mblen <i>(function)</i> 
