---
title: "stdstrpbrk(3)"
name: "stdstrpbrk"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdstrpbrk/"
---

std::strpbrk - std::strpbrk

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cstring&gt;

    const char *strpbrk(const char *dest, const char *breakset);

char *strpbrk(char *dest, const char *breakset);</code></pre> 
Scans the null-terminated byte string pointed to by dest for any character from the null-terminated byte string pointed to by breakset, and returns a pointer to that character. 

<h2>Parameters</h2>

dest - pointer to the null-terminated byte string to be analyzed 
breakset - pointer to the null-terminated byte string that contains the characters to search for

<h2>Return value</h2>

Pointer to the first character in dest, that is also in breakset, or null pointer if no such character exists. 

<h2>Notes</h2>

The name stands for &quot;string pointer break&quot;, because it returns a pointer to the first of the separator (&quot;break&quot;) characters 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;cstring&gt;

#include &lt;iomanip&gt;
int main()

{
    const char *str = &quot;hello world, friend of mine!&quot;;
    const char *sep = &quot; ,!&quot;;
    unsigned int cnt = 0;
    do {
        str = std::strpbrk(str, sep); // find separator
        std::cout &lt;&lt; std::quoted(str) &lt;&lt; '\n';
        if (str)
            str += std::strspn(str, sep); // skip separator
        ++cnt;                            // increment word count
    } while (str &amp;&amp; *str);
    std::cout &lt;&lt; &quot;There are &quot; &lt;&lt; cnt &lt;&lt; &quot; words\n&quot;;
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;&quot; world, friend of mine!&quot; 
&nbsp;<wbr>&nbsp;&quot;, friend of mine!&quot; 
&nbsp;<wbr>&nbsp;&quot; of mine!&quot; 
&nbsp;<wbr>&nbsp;&quot; mine!&quot; 
&nbsp;<wbr>&nbsp;&quot;!&quot; 
&nbsp;<wbr>&nbsp;There are 5 words

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the length of the maximum initial segment that consists 
strcspn of only the characters not found in another byte string 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;finds the next token in a byte string 
strtok <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;finds the first occurrence of a character 
strchr <i>(function)</i> 
