---
title: "stdisspacestdlocale(3)"
name: "stdisspacestdlocale"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdisspacestdlocale/"
---

std::isspace(std::locale) - std::isspace(std::locale)

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;locale&gt;

    template &lt;class charT&gt;

    bool isspace(charT ch, const locale &amp;loc);</code></pre> 
Checks if the given character is classified as a whitespace character by the given locale's ctype facet. 

<h2>Parameters</h2>

ch - character 
loc - locale

<h2>Return value</h2>

Returns true if the character is classified as a whitespace character, false otherwise. 

<h2>Possible implementation</h2>

&nbsp;<wbr>&nbsp;template&lt; class charT &gt; 
&nbsp;<wbr>&nbsp;bool isspace( charT ch, const std::locale&amp; loc ) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return std::use_facet&lt;std::ctype&lt;charT&gt;&gt;(loc).is(std::ctype_base::space, ch); 
&nbsp;<wbr>&nbsp;}

<h2>Example</h2>

Demonstrates the use of isspace() with different locales (OS-specific). 
 // Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;locale&gt;
void try_with(wchar_t c, const char *loc)

{
    std::wcout &lt;&lt; &quot;isspace('&quot; &lt;&lt; c &lt;&lt; &quot;', locale(\&quot;&quot; &lt;&lt; loc &lt;&lt; &quot;\&quot;)) returned &quot;
               &lt;&lt; std::boolalpha &lt;&lt; std::isspace(c, std::locale(loc)) &lt;&lt; '\n';
}
int main()

{
    const wchar_t EM_SPACE = L'\u2003'; // Unicode character 'EM SPACE'
    try_with(EM_SPACE, &quot;C&quot;);
    try_with(EM_SPACE, &quot;en_US.UTF8&quot;);
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;isspace(' ', locale(&quot;C&quot;)) returned false 
&nbsp;<wbr>&nbsp;isspace(' ', locale(&quot;en_US.UTF8&quot;)) returned true

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks if a character is a space character 
isspace <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks if a wide character is a space character 
iswspace <i>(function)</i> 
