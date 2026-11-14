---
title: "stdwctob(3)"
name: "stdwctob"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdwctob/"
---

std::wctob - std::wctob

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cwchar&gt;

    int wctob(std::wint_t c);</code></pre> 
Narrows a wide character c if its multibyte character equivalent in the initial shift state is a single byte. 
This is typically possible for the characters from the ASCII character set, since most multibyte encodings (such as UTF-8) use single bytes to encode those characters. 

<h2>Parameters</h2>

c - wide character to narrow

<h2>Return value</h2>

EOF if c does not represent a multibyte character with length 1 in initial shift state. 
Otherwise, the single-byte representation of c as unsigned char converted to int 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;clocale&gt;

#include &lt;cwchar&gt;

#include &lt;iostream&gt;
void try_narrowing(wchar_t c)

{
    int cn = std::wctob(c);
    if (cn != EOF)
        std::cout &lt;&lt; '\'' &lt;&lt; c &lt;&lt; &quot;' narrowed to &quot; &lt;&lt; +cn &lt;&lt; '\n';
    else
        std::cout &lt;&lt; '\'' &lt;&lt; c &lt;&lt; &quot;' could not be narrowed\n&quot;;
}
int main()

{
    std::setlocale(LC_ALL, &quot;th_TH.utf8&quot;);
    std::cout &lt;&lt; std::hex &lt;&lt; std::showbase &lt;&lt; &quot;In Thai UTF-8 locale:\n&quot;;
    try_narrowing(L'a');
    try_narrowing(L'๛');
    std::setlocale(LC_ALL, &quot;th_TH.tis620&quot;);
    std::cout &lt;&lt; &quot;In Thai TIS-620 locale:\n&quot;;
    try_narrowing(L'a');
    try_narrowing(L'๛');
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;In Thai UTF-8 locale: 
&nbsp;<wbr>&nbsp;'0x61' narrowed to 0x61 
&nbsp;<wbr>&nbsp;'0xe5b' could not be narrowed 
&nbsp;<wbr>&nbsp;In Thai TIS-620 locale: 
&nbsp;<wbr>&nbsp;'0x61' narrowed to 0x61 
&nbsp;<wbr>&nbsp;'0xe5b' narrowed to 0xfb

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;widens a single-byte narrow character to wide character, if possible 
btowc <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;narrows characters 
narrow <i>(public member function of std::basic_ios&lt;CharT,Traits&gt;)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;invokes do_narrow 
narrow <i>(public member function of std::ctype&lt;CharT&gt;)</i> 
