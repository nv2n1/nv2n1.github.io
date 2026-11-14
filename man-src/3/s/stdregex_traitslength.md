---
title: "stdregex_traitslength(3)"
name: "stdregex_traitslength"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdregex_traitslength/"
---

std::regex_traits&lt;CharT&gt;::length - std::regex_traits&lt;CharT&gt;::length

<h2>Synopsis</h2>

<pre><code>static std::size_t length(const char_type *p);
Calculates the length of a null - terminated character sequence, that is, the smallest i such that p[i] == 0.

                                                                              Standard library specializations of std::regex_traits execute std::char_traits&lt;CharT&gt;::length(p);
</code></pre>

<h2>Parameters</h2>

p - pointer to the first element of the null-terminated character sequence

<h2>Return value</h2>

The length of the null-terminated character string. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;regex&gt;

#include &lt;iostream&gt;
int main()

{
    std::cout &lt;&lt; std::regex_traits&lt;char&gt;::length(u8&quot;Кошка&quot;) &lt;&lt; '\n'
              &lt;&lt; std::regex_traits&lt;wchar_t&gt;::length(L&quot;Кошка&quot;) &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;10 
&nbsp;<wbr>&nbsp;5
