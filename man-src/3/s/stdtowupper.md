---
title: "stdtowupper(3)"
name: "stdtowupper"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdtowupper/"
---

std::towupper - std::towupper

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;cwctype&gt;

std::wint_t towupper( std::wint_t ch );</code></pre> 
Converts the given wide character to uppercase, if possible. 
If the value of ch is neither representable as a wchar_t nor equal to the value of the macro WEOF, the behavior is undefined. 

<h2>Parameters</h2>

ch - wide character to be converted

<h2>Return value</h2>

Uppercase version of ch or unmodified ch if no uppercase version is listed in the current C locale. 

<h2>Notes</h2>

Only 1:1 character mapping can be performed by this function, e.g. the uppercase form of 'ß' is (with some exceptions) the two-character string &quot;SS&quot;, which cannot be obtained by std::towupper. 
ISO_30112 specifies which pairs of Unicode characters are included in this mapping. 

<h2>Example</h2>

The latin letter_'ſ'_(U+017F) is the alternative lowercase form of 'S' (U+0053) 
 // Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;cwctype&gt;

#include &lt;clocale&gt;
int main()

{
    wchar_t c = L'\u017f'; // Latin small letter Long S ('ſ')
    std::cout &lt;&lt; std::hex &lt;&lt; std::showbase;
    std::cout &lt;&lt; &quot;in the default locale, towupper(&quot; &lt;&lt; (std::wint_t)c &lt;&lt; &quot;) = &quot;
              &lt;&lt; std::towupper(c) &lt;&lt; '\n';
    std::setlocale(LC_ALL, &quot;en_US.utf8&quot;);
    std::cout &lt;&lt; &quot;in Unicode locale, towupper(&quot; &lt;&lt; (std::wint_t)c &lt;&lt; &quot;) = &quot;
              &lt;&lt; std::towupper(c) &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;in the default locale, towupper(0x17f) = 0x17f 
&nbsp;<wbr>&nbsp;in Unicode locale, towupper(0x17f) = 0x53

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;converts a wide character to lowercase 
towlower <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;converts a character to uppercase using the ctype facet of a locale 
toupper(std::locale) <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;converts a character to uppercase 
toupper <i>(function)</i> 
