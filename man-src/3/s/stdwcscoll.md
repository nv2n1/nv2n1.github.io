---
title: "stdwcscoll(3)"
name: "stdwcscoll"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdwcscoll/"
description: "std::wcscoll – std::wcscoll"
---

<p>std::wcscoll &#8211; std::wcscoll</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;cwchar&gt;

    int wcscoll(const wchar_t *lhs, const wchar_t *rhs);</code></pre>
<p>Compares two null-terminated wide strings according to the locale most recently installed by std::setlocale, as defined by the LC_COLLATE category. </p>
<h2>Parameters</h2>
<p>lhs, rhs &#8211; pointers to the null-terminated wide strings to compare</p>
<h2>Return value</h2>
<p>Negative value if lhs is less than (precedes) rhs.<br />
0 if lhs is equal to rhs.<br />
Positive value if lhs is greater than (follows) rhs. </p>
<h2>Notes</h2>
<p>Collation order is the dictionary order: the position of the letter in the national alphabet (its equivalence class) has higher priority than its case or variant. Within an equivalence class, lowercase characters collate before their uppercase equivalents and locale-specific order may apply to the characters with diacritics. In some locales, groups of characters compare as single collation units. For example, &quot;ch&quot; in Czech follows &quot;h&quot; and precedes &quot;i&quot;, and &quot;dzs&quot; in Hungarian follows &quot;dz&quot; and precedes &quot;g&quot;. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;clocale&gt;
void try_compare(const wchar_t *p1, const wchar_t *p2)

{
    if (std::wcscoll(p1, p2) &lt; 0)
        std::wcout &lt;&lt; p1 &lt;&lt; &quot; before &quot; &lt;&lt; p2 &lt;&lt; '
';
    else
        std::wcout &lt;&lt; p2 &lt;&lt; &quot; before &quot; &lt;&lt; p1 &lt;&lt; '
';
}
int main()

{
    std::setlocale(LC_ALL, &quot;en_US.utf8&quot;);
    std::wcout &lt;&lt; &quot;In the American locale: &quot;;
    try_compare(L&quot;hrnec&quot;, L&quot;chrt&quot;);
    std::setlocale(LC_COLLATE, &quot;cs_CZ.utf8&quot;);
    std::wcout &lt;&lt; &quot;In the Czech locale: &quot;;
    try_compare(L&quot;hrnec&quot;, L&quot;chrt&quot;);
    std::setlocale(LC_COLLATE, &quot;en_US.utf8&quot;);
    std::wcout &lt;&lt; &quot;In the American locale: &quot;;
    try_compare(L&quot;år&quot;, L&quot;ängel&quot;);
    std::setlocale(LC_COLLATE, &quot;sv_SE.utf8&quot;);
    std::wcout &lt;&lt; &quot;In the Swedish locale: &quot;;
    try_compare(L&quot;år&quot;, L&quot;ängel&quot;);
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;In the American locale: chrt before hrnec<br />
&nbsp;<wbr>&nbsp;In the Czech locale: hrnec before chrt<br />
&nbsp;<wbr>&nbsp;In the American locale: ängel before år<br />
&nbsp;<wbr>&nbsp;In the Swedish locale: år before ängel</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;compares two strings in accordance to the current locale<br />
strcoll <i>(function)</i><br />
do_compare compares two strings using this facet&#8217;s collation rules<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::collate&lt;CharT&gt;)</i><br />
<code>[virtual]</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;transform a wide string so that wcscmp would produce the same result as wcscoll<br />
wcsxfrm <i>(function)</i> </p>
