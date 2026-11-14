---
title: "stdcollatecomparestdcollatedo_compare(3)"
name: "stdcollatecomparestdcollatedo_compare"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdcollatecomparestdcollatedo_compare/"
---

std::collate&lt;CharT&gt;::compare,std::collate&lt;CharT&gt;::do_compare - std::collate&lt;CharT&gt;::compare,std::collate&lt;CharT&gt;::do_compare

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;locale&gt;

    public :

    int
    compare(const CharT *low1, const CharT *high1, (1)

                                                       const CharT *low2,
            const CharT *high2) const;

protected:
virtual int do_compare(const CharT *low1, const CharT *high1, (2)

                                                                  const CharT *low2,
                       const CharT *high2) const;</code></pre> 
1) Public member function, calls the protected virtual member function do_compare of the most derived class. 
2) Compares the character sequence [low1, high1) to the character sequence [low2, high2), using this locale's collation rules, and returns 1 if the first string follows the second, -1 if the first string precedes the second, zero if the two strings are equivalent. 

<h2>Parameters</h2>

low1 - pointer to the first character of the first string 
high1 - one past the end pointer for the first string 
low2 - pointer to the first character of the second string 
high2 - one past the end pointer for the second string

<h2>Return value</h2>

1 if the first string is greater than the second (that is, follows the second in the collation order), -1 if the first string is less than the second (precedes the second in the collation order), zero if the two strings are equivalent. 

<h2>Notes</h2>

When three-way comparison is not required (such as when providing a Compare argument to standard algorithms such as std::sort), std::locale::operator() may be more appropriate. 
Collation order is the dictionary order: the position of the letter in the national alphabet (its equivalence class) has higher priority than its case or variant. Within an equivalence class, lowercase characters collate before their uppercase equivalents and locale-specific order may apply to the characters with diacritics. In some locales, groups of characters compare as single collation units. For example, &quot;ch&quot; in Czech follows &quot;h&quot; and precedes &quot;i&quot;, and &quot;dzs&quot; in Hungarian follows &quot;dz&quot; and precedes &quot;g&quot;. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;string&gt;

#include &lt;locale&gt;
template &lt;typename CharT&gt;

void try_compare(const std::locale &amp;l, const CharT *p1, const CharT *p2)

{
    auto &amp;f = std::use_facet&lt;std::collate&lt;CharT&gt;&gt;(l);
    std::basic_string&lt;CharT&gt; s1(p1), s2(p2);
    if (f.compare(&amp;s1[0], &amp;s1[0] + s1.size(),
                  &amp;s2[0], &amp;s2[0] + s2.size()) &lt; 0)
        std::wcout &lt;&lt; p1 &lt;&lt; &quot; before &quot; &lt;&lt; p2 &lt;&lt; '\n';
    else
        std::wcout &lt;&lt; p2 &lt;&lt; &quot; before &quot; &lt;&lt; p1 &lt;&lt; '\n';
}
int main()

{
    std::locale::global(std::locale(&quot;en_US.utf8&quot;));
    std::wcout.imbue(std::locale());
    std::wcout &lt;&lt; &quot;In the American locale: &quot;;
    try_compare(std::locale(), &quot;hrnec&quot;, &quot;chrt&quot;);
    std::wcout &lt;&lt; &quot;In the Czech locale: &quot;;
    try_compare(std::locale(&quot;cs_CZ.utf8&quot;), &quot;hrnec&quot;, &quot;chrt&quot;);
    std::wcout &lt;&lt; &quot;In the American locale: &quot;;
    try_compare(std::locale(), L&quot;år&quot;, L&quot;ängel&quot;);
    std::wcout &lt;&lt; &quot;In the Swedish locale: &quot;;
    try_compare(std::locale(&quot;sv_SE.utf8&quot;), L&quot;år&quot;, L&quot;ängel&quot;);
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;In the American locale: chrt before hrnec 
&nbsp;<wbr>&nbsp;In the Czech locale: hrnec before chrt 
&nbsp;<wbr>&nbsp;In the American locale: ängel before år 
&nbsp;<wbr>&nbsp;In the Swedish locale: år before ängel

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;compares two strings in accordance to the current locale 
strcoll <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;compares two wide strings in accordance to the current locale 
wcscoll <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;lexicographically compares two strings using this locale's collate facet 
operator() <i>(public member function of std::locale)</i> 
