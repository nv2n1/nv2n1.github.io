---
title: "stdtowlower(3)"
name: "stdtowlower"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdtowlower/"
---

std::towlower - std::towlower

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;cwctype&gt;

std::wint_t towlower( std::wint_t ch );</code></pre> 
Converts the given wide character to lowercase, if possible. 
If the value of ch is neither representable as a wchar_t nor equal to the value of the macro WEOF, the behavior is undefined. 

<h2>Parameters</h2>

ch - wide character to be converted

<h2>Return value</h2>

Lowercase version of ch or unmodified ch if no lowercase version is listed in the current C locale. 

<h2>Notes</h2>

Only 1:1 character mapping can be performed by this function, e.g. the Greek uppercase letter 'Σ' has two lowercase forms, depending on the position in a word: 'σ' and 'ς'. A call to std::towlower cannot be used to obtain the correct lowercase form in this case. 
ISO_30112 specifies which pairs of Unicode characters are included in this mapping. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;cwctype&gt;

#include &lt;clocale&gt;
int main()

{
    wchar_t c = L'\u0190'; // Latin capital open E ('Ɛ')
    std::cout &lt;&lt; std::hex &lt;&lt; std::showbase;
    std::cout &lt;&lt; &quot;in the default locale, towlower(&quot; &lt;&lt; (std::wint_t)c &lt;&lt; &quot;) = &quot;
              &lt;&lt; std::towlower(c) &lt;&lt; '\n';
    std::setlocale(LC_ALL, &quot;en_US.utf8&quot;);
    std::cout &lt;&lt; &quot;in Unicode locale, towlower(&quot; &lt;&lt; (std::wint_t)c &lt;&lt; &quot;) = &quot;
              &lt;&lt; std::towlower(c) &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;in the default locale, towlower(0x190) = 0x190 
&nbsp;<wbr>&nbsp;in Unicode locale, towlower(0x190) = 0x25b

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;converts a wide character to uppercase 
towupper <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;converts a character to lowercase using the ctype facet of a locale 
tolower(std::locale) <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;converts a character to lowercase 
tolower <i>(function)</i> 
