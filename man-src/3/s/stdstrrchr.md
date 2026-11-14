---
title: "stdstrrchr(3)"
name: "stdstrrchr"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdstrrchr/"
---

std::strrchr - std::strrchr

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cstring&gt;

    const char *strrchr(const char *str, int ch);

char *strrchr(char *str, int ch);</code></pre> 
Finds the last occurrence of ch (after conversion to char) in the byte string pointed to by str. The terminating null character is considered to be a part of the string and can be found if searching for '\0'. 

<h2>Parameters</h2>

str - pointer to the null-terminated byte string to be analyzed 
ch - character to search for

<h2>Return value</h2>

Pointer to the found character in str, or null pointer if no such character is found. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;cstring&gt;
int main()

{
    char input[] = &quot;/home/user/hello.c&quot;;
    char *output = std::strrchr(input, '/');
    if (output)
        std::cout &lt;&lt; output + 1 &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;hello.c

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;finds the first occurrence of a character 
strchr <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;finds the last occurrence of a wide character in a wide string 
wcsrchr <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;find the last occurrence of a substring 
rfind <i>(public member function of std::basic_string&lt;CharT,Traits,Allocator&gt;)</i> 
