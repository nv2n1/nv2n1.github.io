---
title: "stdbtowc(3)"
name: "stdbtowc"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdbtowc/"
description: "std::btowc – std::btowc"
---

<p>std::btowc &#8211; std::btowc</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;cwchar&gt;

    std::wint_t btowc(int c);</code></pre>
<p>Widens a single-byte character c to its wide character equivalent.<br />
Most multibyte character encodings use single-byte codes to represent the characters from the ASCII character set. This function may be used to convert such characters to wchar_t. </p>
<h2>Parameters</h2>
<p>c &#8211; single-byte character to widen</p>
<h2>Return value</h2>
<p>WEOF if c is EOF.<br />
Wide character representation of c if (unsigned char)c is a valid single-byte character in the initial shift state, WEOF otherwise. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;cwchar&gt;

#include &lt;clocale&gt;
void try_widen(char c)

{
    std::wint_t w = std::btowc(c);
    if (w != WEOF)
        std::cout &lt;&lt; &quot;The single-byte character &quot; &lt;&lt; +(unsigned char)c
                  &lt;&lt; &quot; widens to &quot; &lt;&lt; +w &lt;&lt; '
';
    else
        std::cout &lt;&lt; &quot;The single-byte character &quot; &lt;&lt; +(unsigned char)c
                  &lt;&lt; &quot; failed to widen
&quot;;
}
int main()

{
    std::setlocale(LC_ALL, &quot;lt_LT.iso88594&quot;);
    std::cout &lt;&lt; std::hex &lt;&lt; std::showbase &lt;&lt; &quot;In Lithuanian ISO-8859-4 locale:
&quot;;
    try_widen('A');
    try_widen('�'); // German letter ß (U+00df) in ISO-8859-4
    try_widen('�'); // Lithuanian letter ų (U+0173) in ISO-8859-4
    std::setlocale(LC_ALL, &quot;lt_LT.utf8&quot;);
    std::cout &lt;&lt; &quot;In Lithuanian UTF-8 locale:
&quot;;
    try_widen('A');
    try_widen('�');
    try_widen('�');
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;In Lithuanian ISO-8859-4 locale:<br />
&nbsp;<wbr>&nbsp;The single-byte character 0x41 widens to 0x41<br />
&nbsp;<wbr>&nbsp;The single-byte character 0xdf widens to 0xdf<br />
&nbsp;<wbr>&nbsp;The single-byte character 0xf9 widens to 0x173<br />
&nbsp;<wbr>&nbsp;In Lithuanian UTF-8 locale:<br />
&nbsp;<wbr>&nbsp;The single-byte character 0x41 widens to 0x41<br />
&nbsp;<wbr>&nbsp;The single-byte character 0xdf failed to widen<br />
&nbsp;<wbr>&nbsp;The single-byte character 0xf9 failed to widen</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;narrows a wide character to a single-byte narrow character, if possible<br />
wctob <i>(function)</i><br />
do_widen converts a character or characters from char to charT<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::ctype&lt;CharT&gt;)</i><br />
<code>[virtual]</code> </p>
