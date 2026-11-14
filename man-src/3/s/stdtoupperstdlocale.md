---
title: "stdtoupperstdlocale(3)"
name: "stdtoupperstdlocale"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdtoupperstdlocale/"
---

std::toupper(std::locale) - std::toupper(std::locale)

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;locale&gt;

    template &lt;class charT&gt;

    charT toupper(charT ch, const locale &amp;loc);</code></pre> 
Converts the character ch to uppercase if possible, using the conversion rules specified by the given locale's std::ctype facet. 

<h2>Parameters</h2>

ch - character 
loc - locale

<h2>Return value</h2>

Returns the uppercase form of ch if one is listed in the locale, otherwise returns ch unchanged. 

<h2>Notes</h2>

Only 1:1 character mapping can be performed by this function, e.g. the uppercase form of 'ß' is (with some exceptions) the two-character string &quot;SS&quot;, which cannot be obtained by std::toupper. 

<h2>Possible implementation</h2>

&nbsp;<wbr>&nbsp;template&lt; class charT &gt; 
&nbsp;<wbr>&nbsp;charT toupper( charT ch, const std::locale&amp; loc ) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return std::use_facet&lt;std::ctype&lt;charT&gt;&gt;(loc).toupper(ch); 
&nbsp;<wbr>&nbsp;}

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;cwctype&gt;

#include &lt;locale&gt;
int main()

{
    wchar_t c = L'\u017f'; // Latin small letter Long S ('ſ')
    std::cout &lt;&lt; std::hex &lt;&lt; std::showbase;
    std::cout &lt;&lt; &quot;in the default locale, toupper(&quot; &lt;&lt; (std::wint_t)c &lt;&lt; &quot;) = &quot;
              &lt;&lt; std::toupper(c, std::locale()) &lt;&lt; '\n';
    std::cout &lt;&lt; &quot;in Unicode locale, toupper(&quot; &lt;&lt; (std::wint_t)c &lt;&lt; &quot;) = &quot;
              &lt;&lt; std::toupper(c, std::locale(&quot;en_US.utf8&quot;)) &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;in the default locale, toupper(0x17f) = 0x17f 
&nbsp;<wbr>&nbsp;in Unicode locale, toupper(0x17f) = 0x53

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;converts a character to lowercase using the ctype facet of a locale 
tolower(std::locale) <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;converts a character to uppercase 
toupper <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;converts a wide character to uppercase 
towupper <i>(function)</i> 
