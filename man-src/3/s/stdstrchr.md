---
title: "stdstrchr(3)"
name: "stdstrchr"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdstrchr/"
---

std::strchr - std::strchr

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cstring&gt;

    const char *strchr(const char *str, int ch);

char *strchr(char *str, int ch);</code></pre> 
Finds the first occurrence of the character static_cast&lt;char&gt;(ch) in the byte string pointed to by str. 
The terminating null character is considered to be a part of the string and can be found if searching for '\0'. 

<h2>Parameters</h2>

str - pointer to the null-terminated byte string to be analyzed 
ch - character to search for

<h2>Return value</h2>

Pointer to the found character in str, or a null pointer if no such character is found. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;cstring&gt;
int main()

{
    const char *str = &quot;Try not. Do, or do not. There is no try.&quot;;
    char target = 'T';
    const char *result = str;
    while ((result = std::strchr(result, target)) != NULL) {
        std::cout &lt;&lt; &quot;Found '&quot; &lt;&lt; target
                  &lt;&lt; &quot;' starting at '&quot; &lt;&lt; result &lt;&lt; &quot;'\n&quot;;
        // Increment result, otherwise we'll find target at the same location
        ++result;
    }
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;Found 'T' starting at 'Try not. Do, or do not. There is no try.' 
&nbsp;<wbr>&nbsp;Found 'T' starting at 'There is no try.'

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;searches an array for the first occurrence of a character 
memchr <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;find characters in the string 
find <i>(public member function of std::basic_string&lt;CharT,Traits,Allocator&gt;)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;finds the first occurrence of a wide character in a wide string 
wcschr <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;finds the last occurrence of a character 
strrchr <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;finds the first location of any character from a set of separators 
strpbrk <i>(function)</i> 
