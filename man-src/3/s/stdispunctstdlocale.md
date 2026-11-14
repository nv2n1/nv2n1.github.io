---
title: "stdispunctstdlocale(3)"
name: "stdispunctstdlocale"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdispunctstdlocale/"
---

std::ispunct(std::locale) - std::ispunct(std::locale)

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;locale&gt;

    template &lt;class charT&gt;

    bool ispunct(charT ch, const locale &amp;loc);</code></pre> 
Checks if the given character is classified as an punctuation character by the given locale's std::ctype facet. 

<h2>Parameters</h2>

ch - character 
loc - locale

<h2>Return value</h2>

Returns true if the character is classified as punctuation, false otherwise. 

<h2>Possible implementation</h2>

&nbsp;<wbr>&nbsp;template&lt; class charT &gt; 
&nbsp;<wbr>&nbsp;bool ispunct( charT ch, const std::locale&amp; loc ) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return std::use_facet&lt;std::ctype&lt;charT&gt;&gt;(loc).is(std::ctype_base::punct, ch); 
&nbsp;<wbr>&nbsp;}

<h2>Example</h2>

Demonstrates the use of ispunct() with different locales (OS-specific). 
 // Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;locale&gt;

int main()

{
    const wchar_t c = L'\u214b'; // upside-down ampersand
    std::locale loc1(&quot;C&quot;);
    std::cout &lt;&lt; &quot;ispunct('⅋', C locale) returned &quot;
              &lt;&lt; std::boolalpha &lt;&lt; std::ispunct(c, loc1) &lt;&lt; '\n';
    std::locale loc2(&quot;en_US.UTF-8&quot;);
    std::cout &lt;&lt; &quot;ispunct('⅋', Unicode locale) returned &quot;
              &lt;&lt; std::boolalpha &lt;&lt; std::ispunct(c, loc2) &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;isalpha('⅋', C locale) returned false 
&nbsp;<wbr>&nbsp;isalpha('⅋', Unicode locale) returned true

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks if a character is a punctuation character 
ispunct <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks if a wide character is a punctuation character 
iswpunct <i>(function)</i> 
