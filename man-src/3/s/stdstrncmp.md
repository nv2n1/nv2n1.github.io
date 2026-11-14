---
title: "stdstrncmp(3)"
name: "stdstrncmp"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdstrncmp/"
---

std::strncmp - std::strncmp

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cstring&gt;

    int strncmp(const char *lhs, const char *rhs, size_t count);</code></pre> 
Compares at most count characters of two null-terminated byte strings. The comparison is done lexicographically. 
The sign of the result is the sign of the difference between the values of the first pair of characters (both interpreted as unsigned char) that differ in the strings being compared. 
The behavior is undefined if lhs or rhs are not pointers to null-terminated strings. 
Characters following the null character are not compared. 

<h2>Parameters</h2>

lhs, rhs - pointers to the null-terminated byte strings to compare 
count - maximum number of characters to compare

<h2>Return value</h2>

Negative value if lhs appears before rhs in lexicographical order. 
Zero if lhs and rhs compare equal. 
Positive value if lhs appears after rhs in lexicographical order. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;cstring&gt;

#include &lt;iostream&gt;
void demo(const char *lhs, const char *rhs, int sz)

{
    int rc = std::strncmp(lhs, rhs, sz);
    if (rc == 0)
        std::cout &lt;&lt; &quot;First &quot; &lt;&lt; sz &lt;&lt; &quot; chars of [&quot;
                  &lt;&lt; lhs &lt;&lt; &quot;] equal [&quot; &lt;&lt; rhs &lt;&lt; &quot;]\n&quot;;
    else if (rc &lt; 0)
        std::cout &lt;&lt; &quot;First &quot; &lt;&lt; sz &lt;&lt; &quot; chars of [&quot;
                  &lt;&lt; lhs &lt;&lt; &quot;] precede [&quot; &lt;&lt; rhs &lt;&lt; &quot;]\n&quot;;
    else if (rc &gt; 0)
        std::cout &lt;&lt; &quot;First &quot; &lt;&lt; sz &lt;&lt; &quot; chars of [&quot;
                  &lt;&lt; lhs &lt;&lt; &quot;] follow [&quot; &lt;&lt; rhs &lt;&lt; &quot;]\n&quot;;
}

int main()

{
    demo(&quot;Hello, world!&quot;, &quot;Hello, everybody!&quot;, 13);
    demo(&quot;Hello, everybody!&quot;, &quot;Hello, world!&quot;, 13);
    demo(&quot;Hello, everybody!&quot;, &quot;Hello, world!&quot;, 7);
    demo(&quot;Hello, everybody!&quot; + 12, &quot;Hello, somebody!&quot; + 11, 5);
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;First 13 chars of [Hello, world!] follow [Hello, everybody!] 
&nbsp;<wbr>&nbsp;First 13 chars of [Hello, everybody!] precede [Hello, world!] 
&nbsp;<wbr>&nbsp;First 7 chars of [Hello, everybody!] equal [Hello, world!] 
&nbsp;<wbr>&nbsp;First 5 chars of [body!] equal [body!]

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;compares two strings 
strcmp <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;compares a certain amount of characters from two wide strings 
wcsncmp <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;compares two buffers 
memcmp <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;compares two strings in accordance to the current locale 
strcoll <i>(function)</i> 
