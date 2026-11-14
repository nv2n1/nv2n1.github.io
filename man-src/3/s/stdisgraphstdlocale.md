---
title: "stdisgraphstdlocale(3)"
name: "stdisgraphstdlocale"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdisgraphstdlocale/"
---

std::isgraph(std::locale) - std::isgraph(std::locale)

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;locale&gt;

    template &lt;class charT&gt;

    bool isgraph(charT ch, const locale &amp;loc);</code></pre> 
Checks if the given character classified as a graphic character (i.e. printable, excluding space) by the given locale's std::ctype facet. 

<h2>Parameters</h2>

ch - character 
loc - locale

<h2>Return value</h2>

Returns true if the character is classified as graphic, false otherwise. 

<h2>Possible implementation</h2>

&nbsp;<wbr>&nbsp;template&lt; class charT &gt; 
&nbsp;<wbr>&nbsp;bool isgraph( charT ch, const std::locale&amp; loc ) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return std::use_facet&lt;std::ctype&lt;charT&gt;&gt;(loc).is(std::ctype_base::graph, ch); 
&nbsp;<wbr>&nbsp;}

<h2>Example</h2>

Demonstrates the use of isgraph() with different locales (OS-specific). 
 // Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;locale&gt;

int main()

{
    const wchar_t c = L'\u2a0c'; // quadruple integral
    std::locale loc1(&quot;C&quot;);
    std::cout &lt;&lt; &quot;isgraph('⨌', C locale) returned &quot;
              &lt;&lt; std::boolalpha &lt;&lt; std::isgraph(c, loc1) &lt;&lt; '\n';
    std::locale loc2(&quot;en_US.UTF-8&quot;);
    std::cout &lt;&lt; &quot;isgraph('⨌', Unicode locale) returned &quot;
              &lt;&lt; std::boolalpha &lt;&lt; std::isgraph(c, loc2) &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;isgraph('⨌', C locale) returned false 
&nbsp;<wbr>&nbsp;isgraph('⨌', Unicode locale) returned true

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks if a character is a graphical character 
isgraph <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks if a wide character is a graphical character 
iswgraph <i>(function)</i> 
