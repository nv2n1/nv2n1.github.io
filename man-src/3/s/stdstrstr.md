---
title: "stdstrstr(3)"
name: "stdstrstr"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdstrstr/"
---

std::strstr - std::strstr

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cstring&gt;

    const char *strstr(const char *str, const char *target);

char *strstr(char *str, const char *target);</code></pre> 
Finds the first occurrence of the byte string target in the byte string pointed to by str. The terminating null characters are not compared. 

<h2>Parameters</h2>

str - pointer to the null-terminated byte string to examine 
target - pointer to the null-terminated byte string to search for

<h2>Return value</h2>

Pointer to the first character of the found substring in str, or NULL if no such character is found. If target points to an empty string, str is returned. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;cstring&gt;
int main()

{
    const char *str = &quot;Try not. Do, or do not. There is no try.&quot;;
    const char *target = &quot;not&quot;;
    const char *result = str;
    while ((result = std::strstr(result, target)) != NULL) {
        std::cout &lt;&lt; &quot;Found '&quot; &lt;&lt; target
                  &lt;&lt; &quot;' starting at '&quot; &lt;&lt; result &lt;&lt; &quot;'\n&quot;;
        // Increment result, otherwise we'll find target at the same location
        ++result;
    }
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;Found 'not' starting at 'not. Do, or do not. There is no try.' 
&nbsp;<wbr>&nbsp;Found 'not' starting at 'not. There is no try.'

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;find characters in the string 
find <i>(public member function of std::basic_string&lt;CharT,Traits,Allocator&gt;)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;finds the first occurrence of a wide string within another wide string 
wcsstr <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;finds the first occurrence of a character 
strchr <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;finds the last occurrence of a character 
strrchr <i>(function)</i> 
