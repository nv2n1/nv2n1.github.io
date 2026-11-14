---
title: "stdtolowerstdlocale(3)"
name: "stdtolowerstdlocale"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdtolowerstdlocale/"
---

std::tolower(std::locale) - std::tolower(std::locale)

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;locale&gt;

    template &lt;class charT&gt;

    charT tolower(charT ch, const locale &amp;loc);</code></pre> 
Converts the character ch to lowercase if possible, using the conversion rules specified by the given locale's std::ctype facet. 

<h2>Parameters</h2>

ch - character 
loc - locale

<h2>Return value</h2>

Returns the lowercase form of ch if one is listed in the locale, otherwise return ch unchanged. 

<h2>Notes</h2>

Only 1:1 character mapping can be performed by this function, e.g. the Greek uppercase letter 'Σ' has two lowercase forms, depending on the position in a word: 'σ' and 'ς'. A call to std::tolower cannot be used to obtain the correct lowercase form in this case. 

<h2>Possible implementation</h2>

&nbsp;<wbr>&nbsp;template&lt; class charT &gt; 
&nbsp;<wbr>&nbsp;charT tolower( charT ch, const std::locale&amp; loc ) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return std::use_facet&lt;std::ctype&lt;charT&gt;&gt;(loc).tolower(ch); 
&nbsp;<wbr>&nbsp;}

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;cwctype&gt;

#include &lt;locale&gt;
int main()

{
    wchar_t c = L'\u0190'; // Latin capital open E ('Ɛ')
    std::cout &lt;&lt; std::hex &lt;&lt; std::showbase;
    std::cout &lt;&lt; &quot;in the default locale, tolower(&quot; &lt;&lt; (std::wint_t)c &lt;&lt; &quot;) = &quot;
              &lt;&lt; std::tolower(c, std::locale()) &lt;&lt; '\n';
    std::cout &lt;&lt; &quot;in Unicode locale, tolower(&quot; &lt;&lt; (std::wint_t)c &lt;&lt; &quot;) = &quot;
              &lt;&lt; std::tolower(c, std::locale(&quot;en_US.utf8&quot;)) &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;in the default locale, tolower(0x190) = 0x190 
&nbsp;<wbr>&nbsp;in Unicode locale, tolower(0x190) = 0x25b

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;converts a character to uppercase using the ctype facet of a locale 
toupper(std::locale) <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;converts a character to lowercase 
tolower <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;converts a wide character to lowercase 
towlower <i>(function)</i> 
