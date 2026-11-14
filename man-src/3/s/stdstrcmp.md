---
title: "stdstrcmp(3)"
name: "stdstrcmp"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdstrcmp/"
---

std::strcmp - std::strcmp

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cstring&gt;

    int strcmp(const char *lhs, const char *rhs);</code></pre> 
Compares two null-terminated byte strings lexicographically. 
The sign of the result is the sign of the difference between the values of the first pair of characters (both interpreted as unsigned char) that differ in the strings being compared. 
The behavior is undefined if lhs or rhs are not pointers to null-terminated strings. 

<h2>Parameters</h2>

lhs, rhs - pointers to the null-terminated byte strings to compare

<h2>Return value</h2>

Negative value if lhs appears before rhs in lexicographical order. 
Zero if lhs and rhs compare equal. 
Positive value if lhs appears after rhs in lexicographical order. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;vector&gt;

#include &lt;cstring&gt;

#include &lt;algorithm&gt;

#include &lt;iostream&gt;
int main()

{
    std::vector&lt;const char *&gt; cats{&quot;Heathcliff&quot;, &quot;Snagglepuss&quot;, &quot;Hobbes&quot;, &quot;Garfield&quot;};
    std::sort(cats.begin(), cats.end(), [](const char *strA, const char *strB) {
        return std::strcmp(strA, strB) &lt; 0;
    });
    for (const char *cat : cats) {
        std::cout &lt;&lt; cat &lt;&lt; '\n';
    }
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;Garfield 
&nbsp;<wbr>&nbsp;Heathcliff 
&nbsp;<wbr>&nbsp;Hobbes 
&nbsp;<wbr>&nbsp;Snagglepuss

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;compares a certain number of characters from two strings 
strncmp <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;compares two wide strings 
wcscmp <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;compares two buffers 
memcmp <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;compares two strings in accordance to the current locale 
strcoll <i>(function)</i> 
