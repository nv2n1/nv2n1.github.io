---
title: "stdctypewidendo_widen(3)"
name: "stdctypewidendo_widen"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdctypewidendo_widen/"
---

std::ctype&lt;CharT&gt;::widen,do_widen - std::ctype&lt;CharT&gt;::widen,do_widen

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;locale&gt;

    public : (1)

                 CharT widen(char c) const;

public:
(2)

    const char *widen(const char *beg, const char *end, CharT *dst) const;

protected:
(3)

    virtual CharT do_widen(char c) const;

protected:
(4)

    virtual const char *do_widen(const char *beg, const char *end, CharT *dst) const;</code></pre> 
1,2) public member function, calls the protected virtual member function do_widen of the most derived class. 
3) Converts the single-byte character c to the corresponding wide character representation using the simplest reasonable transformation. Typically, this applies only to the characters whose multibyte encoding is a single byte (e.g. U+0000-U+007F in UTF-8). 
4) For every character in the character array [beg, end), writes the corresponding widened character to the successive locations in the character array pointed to by dst. 
Widening always returns a wide character, but only the characters from the basic source character set (latin letters, digits, and punctuations required to write a C++ program) are guaranteed to have a unique, well-defined, widening transformation, which is also guaranteed to be reversible (by narrow()). In practice, all characters whose multibyte representation is a single byte are usually widened to their wide character counterparts, and the rest of the possible single-byte values are usually mapped into the same placeholder value, typically CharT(-1). 
Widening, if successful, preserves all character classification categories known to is(). 

<h2>Parameters</h2>

c - character to convert 
dflt - default value to produce if the conversion fails 
beg - pointer to the first character in an array of characters to convert 
end - one past the end pointer for the array of characters to convert 
dst - pointer to the first element of the array of char to fill

<h2>Return value</h2>

1,3) widened character 
2,4) end 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;locale&gt;

#include &lt;iostream&gt;
void try_widen(const std::ctype&lt;wchar_t&gt; &amp;f, char c)

{
    wchar_t w = f.widen(c);
    std::cout &lt;&lt; &quot;The single-byte character &quot; &lt;&lt; +(unsigned char)c
              &lt;&lt; &quot; widens to &quot; &lt;&lt; +w &lt;&lt; '\n';
}
int main()

{
    std::locale::global(std::locale(&quot;cs_CZ.iso88592&quot;));
    auto &amp;f = std::use_facet&lt;std::ctype&lt;wchar_t&gt;&gt;(std::locale());
    std::cout &lt;&lt; std::hex &lt;&lt; std::showbase &lt;&lt; &quot;In Czech ISO-8859-2 locale:\n&quot;;
    try_widen(f, 'a');
    try_widen(f, '\xdf'); // German letter ß (U+00df) in ISO-8859-2
    try_widen(f, '\xec'); // Czech letter ě (U+011b) in ISO-8859-2
    std::locale::global(std::locale(&quot;cs_CZ.utf8&quot;));
    auto &amp;f2 = std::use_facet&lt;std::ctype&lt;wchar_t&gt;&gt;(std::locale());
    std::cout &lt;&lt; &quot;In Czech UTF-8 locale:\n&quot;;
    try_widen(f2, 'a');
    try_widen(f2, '\xdf');
    try_widen(f2, '\xec');
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;In Czech ISO-8859-2 locale: 
&nbsp;<wbr>&nbsp;The single-byte character 0x61 widens to 0x61 
&nbsp;<wbr>&nbsp;The single-byte character 0xdf widens to 0xdf 
&nbsp;<wbr>&nbsp;The single-byte character 0xec widens to 0x11b 
&nbsp;<wbr>&nbsp;In Czech UTF-8 locale: 
&nbsp;<wbr>&nbsp;The single-byte character 0x61 widens to 0x61 
&nbsp;<wbr>&nbsp;The single-byte character 0xdf widens to 0xffffffff 
&nbsp;<wbr>&nbsp;The single-byte character 0xec widens to 0xffffffff

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;invokes do_narrow 
narrow <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;widens characters 
widen <i>(public member function of std::basic_ios&lt;CharT,Traits&gt;)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;widens a single-byte narrow character to wide character, if possible 
btowc <i>(function)</i> 
