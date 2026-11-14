---
title: "stdmbrtoc32(3)"
name: "stdmbrtoc32"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdmbrtoc32/"
description: "std::mbrtoc32 – std::mbrtoc32"
---

<p>std::mbrtoc32 &#8211; std::mbrtoc32</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;cuchar&gt;

    std::size_t mbrtoc32(char32_t *pc32,

                         const char *s, (since C++ 11)

                                            std::size_t n,

                         std::mbstate_t *ps);</code></pre>
<p>Converts a narrow multibyte character to its UTF-32 character representation.<br />
If s is not a null pointer, inspects at most n bytes of the multibyte character string, beginning with the byte pointed to by s to determine the number of bytes necessary to complete the next multibyte character (including any shift sequences). If the function determines that the next multibyte character in s is complete and valid, converts it to the corresponding 32-bit character and stores it in *pc32 (if pc32 is not null).<br />
If the multibyte character in *s corresponds to a multi-char32_t sequence (not possible with UTF-32), then after the first call to this function, *ps is updated in such a way that the next calls to mbrtoc32 will write out the additional char32_t, without considering *s.<br />
If s is a null pointer, the values of n and pc32 are ignored and the call is equivalent to std::mbrtoc32(NULL, &quot;&quot;, 1, ps).<br />
If the wide character produced is the null character, the conversion state *ps represents the initial shift state.<br />
The multibyte encoding used by this function is specified by the currently active C locale. </p>
<h2>Parameters</h2>
<p>pc32 &#8211; pointer to the location where the resulting 32-bit character will be written<br />
s &#8211; pointer to the multibyte character string used as input<br />
n &#8211; limit on the number of bytes in s that can be examined<br />
ps &#8211; pointer to the conversion state object used when interpreting the multibyte string</p>
<h2>Return value</h2>
<p>The first of the following that applies:<br />
* 0 if the character converted from s (and stored in *pc32 if non-null) was the null character<br />
* the number of bytes [1&#8230;n] of the multibyte character successfully converted from s<br />
* -3 if the next char32_t from a multi-char32_t character has now been written to *pc32. No bytes are processed from the input in this case.<br />
* -2 if the next n bytes constitute an incomplete, but so far valid, multibyte character. Nothing is written to *pc32.<br />
* -1 if encoding error occurs. Nothing is written to *pc32, the value EILSEQ is stored in errno and the value of *ps is unspecified. </p>
<h2>Examples</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;iomanip&gt;

#include &lt;clocale&gt;

#include &lt;cstring&gt;

#include &lt;cwchar&gt;

#include &lt;cuchar&gt;

#include &lt;cassert&gt;
int main()

{
    std::setlocale(LC_ALL, &quot;en_US.utf8&quot;);
    std::string str = u8&quot;zß水&#x1f34c;&quot;; // or u8&quot;zß水&#x1f34c;&quot;
    std::cout &lt;&lt; &quot;Processing &quot; &lt;&lt; str.size() &lt;&lt; &quot; bytes: [ &quot; &lt;&lt; std::showbase;
    for (unsigned char c : str)
        std::cout &lt;&lt; std::hex &lt;&lt; +c &lt;&lt; ' ';
    std::cout &lt;&lt; &quot;]
&quot;;
    std::mbstate_t state{}; // zero-initialized to initial state
    char32_t c32;
    const char *ptr = str.c_str(), *end = str.c_str() + str.size() + 1;
    while (std::size_t rc = std::mbrtoc32(&amp;c32, ptr, end - ptr, &amp;state)) {
        std::cout &lt;&lt; &quot;Next UTF-32 char: &quot; &lt;&lt; std::hex &lt;&lt; c32 &lt;&lt; &quot; obtained from &quot;;
        assert(rc != (std::size_t)-3); // no surrogates in UTF-32
        if (rc == (std::size_t)-1)
            break;
        if (rc == (std::size_t)-2)
            break;
        std::cout &lt;&lt; std::dec &lt;&lt; rc &lt;&lt; &quot; bytes [ &quot;;
        for (std::size_t n = 0; n &lt; rc; ++n)
            std::cout &lt;&lt; std::hex &lt;&lt; +(unsigned char)ptr[n] &lt;&lt; ' ';
        std::cout &lt;&lt; &quot;]
&quot;;
        ptr += rc;
    }
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;Processing 10 bytes: [ 0x7a 0xc3 0x9f 0xe6 0xb0 0xb4 0xf0 0x9f 0x8d 0x8c ]<br />
&nbsp;<wbr>&nbsp;Next UTF-32 char: 0x7a obtained from 1 bytes [ 0x7a ]<br />
&nbsp;<wbr>&nbsp;Next UTF-32 char: 0xdf obtained from 2 bytes [ 0xc3 0x9f ]<br />
&nbsp;<wbr>&nbsp;Next UTF-32 char: 0x6c34 obtained from 3 bytes [ 0xe6 0xb0 0xb4 ]<br />
&nbsp;<wbr>&nbsp;Next UTF-32 char: 0x1f34c obtained from 4 bytes [ 0xf0 0x9f 0x8d 0x8c ]</p>
<h2>See also</h2>
<p>c32rtomb convert a 32-bit wide character to narrow multibyte string<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
do_in converts a string from externT to internT, such as when reading from file<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::codecvt&lt;InternT,ExternT,State&gt;)</i><br />
<code>[virtual]</code> </p>
