---
title: "stdisblankstdlocale(3)"
name: "stdisblankstdlocale"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdisblankstdlocale/"
---

std::isblank(std::locale) - std::isblank(std::locale)

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;locale&gt;

    template &lt;class charT&gt;
    (since C++ 11)

        bool isblank(charT ch, const locale &amp;loc);
</code></pre> 
Checks if the given character is classified as a blank character by the given locale's ctype facet. 

<h2>Parameters</h2>

ch - character 
loc - locale

<h2>Return value</h2>

Returns true if the character is classified as a blank character, false otherwise. 

<h2>Possible implementation</h2>

&nbsp;<wbr>&nbsp;template&lt; class charT &gt; 
&nbsp;<wbr>&nbsp;bool isblank( charT ch, const std::locale&amp; loc ) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return std::use_facet&lt;std::ctype&lt;charT&gt;&gt;(loc).is(std::ctype_base::blank, ch); 
&nbsp;<wbr>&nbsp;}

<h2>Example</h2>

Demonstrates the use of isblank() with different locales (OS-specific). 
 // Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;locale&gt;
void try_with(wchar_t c, const char *loc)

{
    std::wcout &lt;&lt; &quot;isblank('&quot; &lt;&lt; c &lt;&lt; &quot;', locale(\&quot;&quot; &lt;&lt; loc &lt;&lt; &quot;\&quot;)) returned &quot; &lt;&lt; std::boolalpha
               &lt;&lt; std::isblank(c, std::locale(loc)) &lt;&lt; '\n';
}

int main()

{
    const wchar_t IDEO_SPACE = L'\u3000'; // Unicode character 'IDEOGRAPHIC SPACE'
    try_with(IDEO_SPACE, &quot;C&quot;);
    try_with(IDEO_SPACE, &quot;en_US.UTF-8&quot;);
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;isblank(' ', locale(&quot;C&quot;)) returned false 
&nbsp;<wbr>&nbsp;isblank(' ', locale(&quot;en_US.UTF-8&quot;)) returned true

<h2>See also</h2>

isblank checks if a character is a blank character 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 
iswblank checks if a wide character is a blank character 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 
