---
title: "stdiswctype(3)"
name: "stdiswctype"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdiswctype/"
---

std::iswctype - std::iswctype

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cwctype&gt;

    int iswctype(std::wint_t wc, std::wctype_t desc);</code></pre> 
Classifies the wide character wc using the current C locale's LC_CTYPE category identified by desc. 
If the value of wc is neither representable as a wchar_t nor equal to the value of the macro WEOF, the behavior is undefined. 

<h2>Parameters</h2>

wc - the wide character to classify 
desc - the LC_CTYPE category, obtained from a call to std::wctype

<h2>Return value</h2>

Non-zero if the character ch has the property identified by desc in LC_CTYPE facet of the current C locale, zero otherwise. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;clocale&gt;

#include &lt;cwctype&gt;

#include &lt;iostream&gt;

bool classify(wchar_t wc, const std::string &amp;cat)

{
    return std::iswctype(wc, std::wctype(cat.c_str()));
}

int main()

{
    std::setlocale(LC_ALL, &quot;ja_JP.UTF-8&quot;);
    std::cout &lt;&lt; &quot;The character \u6c34 is...\n&quot;;
    for (std::string s : {&quot;digit&quot;, &quot;alpha&quot;, &quot;space&quot;, &quot;cntrl&quot;, &quot;jkanji&quot;})
        std::cout &lt;&lt; s &lt;&lt; &quot;? &quot; &lt;&lt; std::boolalpha &lt;&lt; classify(L'\u6c34', s) &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;The character 水 is... 
&nbsp;<wbr>&nbsp;digit? false 
&nbsp;<wbr>&nbsp;alpha? true 
&nbsp;<wbr>&nbsp;space? false 
&nbsp;<wbr>&nbsp;cntrl? false 
&nbsp;<wbr>&nbsp;jkanji? true

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;looks up a character classification category in the current C locale 
wctype <i>(function)</i> 
