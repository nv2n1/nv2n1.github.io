---
title: "stdisalnumstdlocale(3)"
name: "stdisalnumstdlocale"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdisalnumstdlocale/"
---

std::isalnum(std::locale) - std::isalnum(std::locale)

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;locale&gt;

    template &lt;class charT&gt;

    bool isalnum(charT ch, const locale &amp;loc);</code></pre> 
Checks if the given character classified as an alphanumeric character by the given locale's std::ctype facet. 

<h2>Parameters</h2>

ch - character 
loc - locale

<h2>Return value</h2>

Returns true if the character is classified as alphanumeric, false otherwise. 

<h2>Possible implementation</h2>

&nbsp;<wbr>&nbsp;template&lt; class charT &gt; 
&nbsp;<wbr>&nbsp;bool isalnum( charT ch, const std::locale&amp; loc ) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return std::use_facet&lt;std::ctype&lt;charT&gt;&gt;(loc).is(std::ctype_base::alnum, ch); 
&nbsp;<wbr>&nbsp;}

<h2>Example</h2>

Demonstrates the use of isalnum() with different locales (OS-specific). 
 // Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;locale&gt;

int main()

{
    const wchar_t c = L'\u2135'; // mathematical symbol aleph
    std::locale loc1(&quot;C&quot;);
    std::cout &lt;&lt; &quot;isalnum('ℵ', C locale) returned &quot;
              &lt;&lt; std::boolalpha &lt;&lt; std::isalnum(c, loc1) &lt;&lt; '\n';
    std::locale loc2(&quot;en_US.UTF-8&quot;);
    std::cout &lt;&lt; &quot;isalnum('ℵ', Unicode locale) returned &quot;
              &lt;&lt; std::boolalpha &lt;&lt; std::isalnum(c, loc2) &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;isalnum('ℵ', C locale) returned false 
&nbsp;<wbr>&nbsp;isalnum('ℵ', Unicode locale) returned true

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks if a character is alphanumeric 
isalnum <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks if a wide character is alphanumeric 
iswalnum <i>(function)</i> 
