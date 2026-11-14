---
title: "stdisalphastdlocale(3)"
name: "stdisalphastdlocale"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdisalphastdlocale/"
---

std::isalpha(std::locale) - std::isalpha(std::locale)

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;locale&gt;

    template &lt;class charT&gt;

    bool isalpha(charT ch, const locale &amp;loc);</code></pre> 
Checks if the given character is classified as an alphabetic character by the given locale's std::ctype facet. 

<h2>Parameters</h2>

ch - character 
loc - locale

<h2>Return value</h2>

Returns true if the character is classified as alphabetic, false otherwise. 

<h2>Possible implementation</h2>

&nbsp;<wbr>&nbsp;template&lt; class charT &gt; 
&nbsp;<wbr>&nbsp;bool isalpha( charT ch, const std::locale&amp; loc ) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return std::use_facet&lt;std::ctype&lt;charT&gt;&gt;(loc).is(std::ctype_base::alpha, ch); 
&nbsp;<wbr>&nbsp;}

<h2>Example</h2>

Demonstrates the use of isalpha() with different locales (OS-specific). 
 // Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;locale&gt;

int main()

{
    const wchar_t c = L'\u042f'; // cyrillic capital letter ya
    std::locale loc1(&quot;C&quot;);
    std::cout &lt;&lt; &quot;isalpha('Я', C locale) returned &quot;
              &lt;&lt; std::boolalpha &lt;&lt; std::isalpha(c, loc1) &lt;&lt; '\n';
    std::locale loc2(&quot;en_US.UTF8&quot;);
    std::cout &lt;&lt; &quot;isalpha('Я', Unicode locale) returned &quot;
              &lt;&lt; std::boolalpha &lt;&lt; std::isalpha(c, loc2) &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;isalpha('Я', C locale) returned false 
&nbsp;<wbr>&nbsp;isalpha('Я', Unicode locale) returned true

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks if a character is alphabetic 
isalpha <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks if a wide character is alphabetic 
iswalpha <i>(function)</i> 
