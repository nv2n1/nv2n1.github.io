---
title: "stdstrcoll(3)"
name: "stdstrcoll"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdstrcoll/"
description: "std::strcoll – std::strcoll"
---

<p>std::strcoll &#8211; std::strcoll</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;cstring&gt;

    int strcoll(const char *lhs, const char *rhs);</code></pre>
<p>Compares two null-terminated byte strings according to the current locale as defined by the LC_COLLATE category. </p>
<h2>Parameters</h2>
<p>lhs, rhs &#8211; pointers to the null-terminated byte strings to compare</p>
<h2>Return value</h2>
<p>Negative value if lhs is less than (precedes) rhs.<br />
0 if lhs is equal to rhs.<br />
Positive value if lhs is greater than (follows) rhs. </p>
<h2>Notes</h2>
<p>Collation order is the dictionary order: the position of the letter in the national alphabet (its equivalence class) has higher priority than its case or variant. Within an equivalence class, lowercase characters collate before their uppercase equivalents and locale-specific order may apply to the characters with diacritics. In some locales, groups of characters compare as single collation units. For example, &quot;ch&quot; in Czech follows &quot;h&quot; and precedes &quot;i&quot;, and &quot;dzs&quot; in Hungarian follows &quot;dz&quot; and precedes &quot;g&quot;. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;cstring&gt;

#include &lt;clocale&gt;
int main()

{
    std::setlocale(LC_COLLATE, &quot;cs_CZ.iso88592&quot;);
    const char *s1 = &quot;hrnec&quot;;
    const char *s2 = &quot;chrt&quot;;
    std::cout &lt;&lt; &quot;In the Czech locale: &quot;;
    if (std::strcoll(s1, s2) &lt; 0)
        std::cout &lt;&lt; s1 &lt;&lt; &quot; before &quot; &lt;&lt; s2 &lt;&lt; '
';
    else
        std::cout &lt;&lt; s2 &lt;&lt; &quot; before &quot; &lt;&lt; s1 &lt;&lt; '
';
    std::cout &lt;&lt; &quot;In lexicographical comparison: &quot;;
    if (std::strcmp(s1, s2) &lt; 0)
        std::cout &lt;&lt; s1 &lt;&lt; &quot; before &quot; &lt;&lt; s2 &lt;&lt; '
';
    else
        std::cout &lt;&lt; s2 &lt;&lt; &quot; before &quot; &lt;&lt; s1 &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;In the Czech locale: hrnec before chrt<br />
&nbsp;<wbr>&nbsp;In lexicographical comparison: chrt before hrnec</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;compares two wide strings in accordance to the current locale<br />
wcscoll <i>(function)</i><br />
do_compare compares two strings using this facet&#8217;s collation rules<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::collate&lt;CharT&gt;)</i><br />
<code>[virtual]</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;transform a string so that strcmp would produce the same result as strcoll<br />
strxfrm <i>(function)</i> </p>
