---
title: "stdmbrtoc16(3)"
name: "stdmbrtoc16"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdmbrtoc16/"
description: "std::mbrtoc16 – std::mbrtoc16"
---

<p>std::mbrtoc16 &#8211; std::mbrtoc16</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;cuchar&gt;

    std::size_t mbrtoc16(char16_t *pc16,

                         const char *s, (since C++ 11)

                                            std::size_t n,

                         std::mbstate_t *ps);</code></pre>
<p>Converts a narrow multibyte character to UTF-16 character representation.<br />
If s is not a null pointer, inspects at most n bytes of the multibyte character string, beginning with the byte pointed to by s to determine the number of bytes necessary to complete the next multibyte character (including any shift sequences). If the function determines that the next multibyte character in s is complete and valid, converts it to the corresponding 16-bit character and stores it in *pc16 (if pc16 is not null).<br />
If the multibyte character in *s corresponds to a multi-char16_t sequence (e.g. a surrogate pair in UTF-16), then after the first call to this function, *ps is updated in such a way that the next call to mbrtoc16 will write out the additional char16_t, without considering *s.<br />
If s is a null pointer, the values of n and pc16 are ignored and the call is equivalent to std::mbrtoc16(NULL, &quot;&quot;, 1, ps).<br />
If the wide character produced is the null character, the conversion state *ps represents the initial shift state.<br />
The multibyte encoding used by this function is specified by the currently active C locale. </p>
<h2>Parameters</h2>
<p>pc16 &#8211; pointer to the location where the resulting 16-bit character will be written<br />
s &#8211; pointer to the multibyte character string used as input<br />
n &#8211; limit on the number of bytes in s that can be examined<br />
ps &#8211; pointer to the conversion state object used when interpreting the multibyte string</p>
<h2>Return value</h2>
<p>The first of the following that applies:<br />
* 0 if the character converted from s (and stored in *pc16 if non-null) was the null character<br />
* the number of bytes [1&#8230;n] of the multibyte character successfully converted from s<br />
* -3 if the next char16_t from a multi-char16_t character (e.g. a surrogate pair) has now been written to *pc16. No bytes are processed from the input in this case.<br />
* -2 if the next n bytes constitute an incomplete, but so far valid, multibyte character. Nothing is written to *pc16.<br />
* -1 if encoding error occurs. Nothing is written to *pc16, the value EILSEQ is stored in errno and the value of *ps is unspecified. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;iomanip&gt;

#include &lt;clocale&gt;

#include &lt;cstring&gt;

#include &lt;cwchar&gt;

#include &lt;cuchar&gt;
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
    char16_t c16;
    const char *ptr = &amp;str[0], *end = &amp;str[0] + str.size();
    while (std::size_t rc = std::mbrtoc16(&amp;c16, ptr, end - ptr + 1, &amp;state)) {
        std::cout &lt;&lt; &quot;Next UTF-16 char: &quot; &lt;&lt; std::hex &lt;&lt; c16 &lt;&lt; &quot; obtained from &quot;;
        if (rc == (std::size_t)-3)
            std::cout &lt;&lt; &quot;earlier surrogate pair
&quot;;
        else if (rc == (std::size_t)-2)
            break;
        else if (rc == (std::size_t)-1)
            break;
        else {
            std::cout &lt;&lt; std::dec &lt;&lt; rc &lt;&lt; &quot; bytes [ &quot;;
            for (std::size_t n = 0; n &lt; rc; ++n)
                std::cout &lt;&lt; std::hex &lt;&lt; +(unsigned char)ptr[n] &lt;&lt; ' ';
            std::cout &lt;&lt; &quot;]
&quot;;
            ptr += rc;
        }
    }
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;Processing 10 bytes: [ 0x7a 0xc3 0x9f 0xe6 0xb0 0xb4 0xf0 0x9f 0x8d 0x8c ]<br />
&nbsp;<wbr>&nbsp;Next UTF-16 char: 0x7a obtained from 1 bytes [ 0x7a ]<br />
&nbsp;<wbr>&nbsp;Next UTF-16 char: 0xdf obtained from 2 bytes [ 0xc3 0x9f ]<br />
&nbsp;<wbr>&nbsp;Next UTF-16 char: 0x6c34 obtained from 3 bytes [ 0xe6 0xb0 0xb4 ]<br />
&nbsp;<wbr>&nbsp;Next UTF-16 char: 0xd83c obtained from 4 bytes [ 0xf0 0x9f 0x8d 0x8c ]<br />
&nbsp;<wbr>&nbsp;Next UTF-16 char: 0xdf4c obtained from earlier surrogate pair</p>
<h2>See also</h2>
<p>c16rtomb convert a 16-bit wide character to narrow multibyte string<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
do_in converts a string from externT to internT, such as when reading from file<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::codecvt&lt;InternT,ExternT,State&gt;)</i><br />
<code>[virtual]</code> </p>
