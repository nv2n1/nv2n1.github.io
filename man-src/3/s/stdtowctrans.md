---
title: "stdtowctrans(3)"
name: "stdtowctrans"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdtowctrans/"
---

std::towctrans - std::towctrans

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;cwctype&gt;

std::wint_t towctrans( std::wint_t wc, std::wctrans_t desc );</code></pre> 
Maps the wide character wc using the current C locale's LC_CTYPE mapping category identified by desc. 
If the value of ch is neither representable as a wchar_t nor equal to the value of the macro WEOF, the behavior is undefined. 

<h2>Parameters</h2>

ch - the wide character to map 
desc - the LC_CTYPE mapping, obtained from a call to std::wctrans

<h2>Return value</h2>

The mapped value of ch using the mapping identified by desc in LC_CTYPE facet of the current C locale. 

<h2>Example</h2>

The following example demonstrates katakana to hiragana character mapping 
 // Run this code <pre><code>#include &lt;clocale&gt;

#include &lt;cwctype&gt;

#include &lt;iostream&gt;

#include &lt;algorithm&gt;
std::wstring tohira(std::wstring str)

{
    std::transform(str.begin(), str.end(), str.begin(), [](wchar_t c) {
        return std::towctrans(c, std::wctrans(&quot;tojhira&quot;));
    });
    return str;
}
int main()

{
    std::setlocale(LC_ALL, &quot;ja_JP.UTF-8&quot;);
    std::wstring kana = L&quot;ヒラガナ&quot;;
    std::wcout &lt;&lt; &quot;katakana characters &quot; &lt;&lt; kana
               &lt;&lt; &quot; are &quot; &lt;&lt; tohira(kana) &lt;&lt; &quot; in hiragana\n&quot;;
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;katakana characters ヒラガナ are ひらがな in hiragana

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;looks up a character mapping category in the current C locale 
wctrans <i>(function)</i> 
