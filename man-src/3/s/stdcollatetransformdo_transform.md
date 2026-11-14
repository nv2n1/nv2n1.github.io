---
title: "stdcollatetransformdo_transform(3)"
name: "stdcollatetransformdo_transform"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdcollatetransformdo_transform/"
---

std::collate&lt;CharT&gt;::transform,do_transform - std::collate&lt;CharT&gt;::transform,do_transform

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;locale&gt;

    public : (1)

                 string_type transform(const CharT *low, const CharT *high) const;

protected:
(2)

    virtual string_type do_transform(const CharT *low, const CharT *high) const;</code></pre> 
1) Public member function, calls the protected virtual member function do_transform of the most derived class. 
2) Converts the character sequence [low, high) to a string that, compared lexicographically (e.g. with operator&lt; for strings) with the result of calling transform() on another string, produces the same result as calling do_compare() on the same two strings. 

<h2>Parameters</h2>

low - pointer to the first character in the sequence to transform 
high - one past the end pointer for the sequence to transform

<h2>Return value</h2>

The string transformed so that lexicographic comparison of the transformed strings may be used instead of collating of the originals. In the &quot;C&quot; locale, the returned string is the exact copy of [low, high). In other locales, the contents of the returned string are implementation-defined, and the size may be considerably longer. 

<h2>Notes</h2>

In addition to the use in collation, the implementation-specific format of the transformed string is known to std::regex_traits&lt;&gt;::transform_primary, which is able to extract the equivalence class information. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;iomanip&gt;

#include &lt;locale&gt;
int main()

{
    std::locale::global(std::locale(&quot;sv_SE.utf8&quot;));
    auto &amp;f = std::use_facet&lt;std::collate&lt;wchar_t&gt;&gt;(std::locale());
    std::wstring in1 = L&quot;\u00e4ngel&quot;;
    std::wstring in2 = L&quot;\u00e5r&quot;;
    std::wstring out1 = f.transform(&amp;in1[0], &amp;in1[0] + in1.size());
    std::wstring out2 = f.transform(&amp;in2[0], &amp;in2[0] + in2.size());
    std::wcout &lt;&lt; &quot;In the Swedish locale: &quot;;
    if (out1 &lt; out2)
        std::wcout &lt;&lt; in1 &lt;&lt; &quot; before &quot; &lt;&lt; in2 &lt;&lt; '\n';
    else
        std::wcout &lt;&lt; in2 &lt;&lt; &quot; before &quot; &lt;&lt; in1 &lt;&lt; '\n';
    std::wcout &lt;&lt; &quot;In lexicographic comparison: &quot;;
    if (in1 &lt; in2)
        std::wcout &lt;&lt; in1 &lt;&lt; &quot; before &quot; &lt;&lt; in2 &lt;&lt; '\n';
    else
        std::wcout &lt;&lt; in2 &lt;&lt; &quot; before &quot; &lt;&lt; in1 &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;In the Swedish locale: år before ängel 
&nbsp;<wbr>&nbsp;In lexicographic comparison: ängel before år

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;transform a string so that strcmp would produce the same result as strcoll 
strxfrm <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;transform a wide string so that wcscmp would produce the same result as wcscoll 
wcsxfrm <i>(function)</i> 
