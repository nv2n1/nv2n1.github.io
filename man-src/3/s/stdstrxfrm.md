---
title: "stdstrxfrm(3)"
name: "stdstrxfrm"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdstrxfrm/"
description: "std::strxfrm – std::strxfrm"
---

<p>std::strxfrm &#8211; std::strxfrm</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;cstring&gt;

    std::size_t strxfrm(char *dest, const char *src, std::size_t count);</code></pre>
<p>Transforms the null-terminated byte string pointed to by src into the implementation-defined form such that comparing two transformed strings with std::strcmp gives the same result as comparing the original strings with std::strcoll, in the current C locale.<br />
The first count characters of the transformed string are written to destination, including the terminating null character, and the length of the full transformed string is returned, excluding the terminating null character.<br />
The behavior is undefined if the dest array is not large enough. The behavior is undefined if dest and src overlap.<br />
If count is 0, then dest is allowed to be a null pointer. </p>
<h2>Notes</h2>
<p>The correct length of the buffer that can receive the entire transformed string is 1+std::strxfrm(nullptr, src, 0)<br />
This function is used when making multiple locale-dependent comparisons using the same string or set of strings, because it is more efficient to use std::strxfrm to transform all the strings just once, and subsequently compare the transformed strings with std::strcmp. </p>
<h2>Parameters</h2>
<p>dest &#8211; pointer to the first element of the array where the transformed string will be written<br />
src &#8211; pointer to the first character of a null-terminated byte string to transform<br />
count &#8211; maximum number of characters to be written</p>
<h2>Return value</h2>
<p>The length of the transformed string, not including the terminating null-character. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;iomanip&gt;

#include &lt;cstring&gt;

#include &lt;string&gt;

#include &lt;cassert&gt;
int main()

{
    char *loc = std::setlocale(LC_COLLATE, &quot;cs_CZ.iso88592&quot;);
    assert(loc);
    std::string in1 = &quot;hrnec&quot;;
    std::string out1(1 + std::strxfrm(nullptr, in1.c_str(), 0), ' ');
    std::string in2 = &quot;chrt&quot;;
    std::string out2(1 + std::strxfrm(nullptr, in2.c_str(), 0), ' ');
    std::strxfrm(&amp;out1[0], in1.c_str(), out1.size());
    std::strxfrm(&amp;out2[0], in2.c_str(), out2.size());
    std::cout &lt;&lt; &quot;In the Czech locale: &quot;;
    if (out1 &lt; out2)
        std::cout &lt;&lt; in1 &lt;&lt; &quot; before &quot; &lt;&lt; in2 &lt;&lt; '
';
    else
        std::cout &lt;&lt; in2 &lt;&lt; &quot; before &quot; &lt;&lt; in1 &lt;&lt; '
';
    std::cout &lt;&lt; &quot;In lexicographical comparison: &quot;;
    if (in1 &lt; in2)
        std::cout &lt;&lt; in1 &lt;&lt; &quot; before &quot; &lt;&lt; in2 &lt;&lt; '
';
    else
        std::cout &lt;&lt; in2 &lt;&lt; &quot; before &quot; &lt;&lt; in1 &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;In the Czech locale: hrnec before chrt<br />
&nbsp;<wbr>&nbsp;In lexicographical comparison: chrt before hrnec</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;transform a wide string so that wcscmp would produce the same result as wcscoll<br />
wcsxfrm <i>(function)</i><br />
do_transform transforms a string so that collation can be replaced by comparison<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::collate&lt;CharT&gt;)</i><br />
<code>[virtual]</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;compares two strings in accordance to the current locale<br />
strcoll <i>(function)</i> </p>
