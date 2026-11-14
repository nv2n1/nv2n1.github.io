---
title: "stdwcsxfrm(3)"
name: "stdwcsxfrm"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdwcsxfrm/"
description: "std::wcsxfrm – std::wcsxfrm"
---

<p>std::wcsxfrm &#8211; std::wcsxfrm</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;cwchar&gt;

    std::size_t strxfrm(wchar_t *dest, const wchar_t *src, std::size_t count);</code></pre>
<p>Transforms the null-terminated wide string pointed to by src into the implementation-defined form such that comparing two transformed strings with std::wcscmp gives the same result as comparing the original strings with std::wcscoll, in the current C locale.<br />
The first count characters of the transformed string are written to destination, including the terminating null character, and the length of the full transformed string is returned, excluding the terminating null character.<br />
If count is 0, then dest is allowed to be a null pointer. </p>
<h2>Notes</h2>
<p>The correct length of the buffer that can receive the entire transformed string is 1+std::wcsxfrm(NULL, src, 0)<br />
This function is used when making multiple locale-dependent comparisons using the same wide string or set of wide strings, because it is more efficient to use std::wcsxfrm to transform all the strings just once, and subsequently compare the transformed wide strings with std::wcscmp. </p>
<h2>Parameters</h2>
<p>dest &#8211; pointer to the first element of a wide null-terminated string to write the transformed string to<br />
src &#8211; pointer to the null-terminated wide character string to transform<br />
count &#8211; maximum number of characters to output</p>
<h2>Return value</h2>
<p>The length of the transformed wide string, not including the terminating null-character. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;cwchar&gt;
int main()

{
    std::setlocale(LC_ALL, &quot;sv_SE.utf8&quot;);
    std::wstring in1 = L&quot;år&quot;;
    std::wstring out1(1 + std::wcsxfrm(nullptr, in1.c_str(), 0), L' ');
    std::wstring in2 = L&quot;ängel&quot;;
    std::wstring out2(1 + std::wcsxfrm(nullptr, in2.c_str(), 0), L' ');
    std::wcsxfrm(&amp;out1[0], in1.c_str(), out1.size());
    std::wcsxfrm(&amp;out2[0], in2.c_str(), out2.size());
    std::wcout &lt;&lt; &quot;In the Swedish locale: &quot;;
    if (out1 &lt; out2)
        std::wcout &lt;&lt; in1 &lt;&lt; &quot; before &quot; &lt;&lt; in2 &lt;&lt; '
';
    else
        std::wcout &lt;&lt; in2 &lt;&lt; &quot; before &quot; &lt;&lt; in1 &lt;&lt; '
';
    std::wcout &lt;&lt; &quot;In lexicographical comparison: &quot;;
    if (in1 &lt; in2)
        std::wcout &lt;&lt; in1 &lt;&lt; &quot; before &quot; &lt;&lt; in2 &lt;&lt; '
';
    else
        std::wcout &lt;&lt; in2 &lt;&lt; &quot; before &quot; &lt;&lt; in1 &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;In the Swedish locale: år before ängel<br />
&nbsp;<wbr>&nbsp;In lexicographical comparison: ängel before år</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;transform a string so that strcmp would produce the same result as strcoll<br />
strxfrm <i>(function)</i><br />
do_transform transforms a string so that collation can be replaced by comparison<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::collate&lt;CharT&gt;)</i><br />
<code>[virtual]</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;compares two wide strings in accordance to the current locale<br />
wcscoll <i>(function)</i> </p>
