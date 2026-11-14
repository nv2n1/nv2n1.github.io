---
title: "stdctypenarrowdo_narrow(3)"
name: "stdctypenarrowdo_narrow"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdctypenarrowdo_narrow/"
---

std::ctype&lt;CharT&gt;::narrow,do_narrow - std::ctype&lt;CharT&gt;::narrow,do_narrow

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;locale&gt;

    public : (1)

                 char narrow(CharT c, char dflt) const;

public:
const CharT *narrow(const CharT *beg, const CharT *end, (2)

                                                            char dflt,
                    char *dst) const;

protected:
(3)

    virtual char do_narrow(CharT c, char dflt) const;

protected:
virtual const CharT *do_narrow(const CharT *beg, const CharT *end, (4)

                                                                       char dflt,
                               char *dst) const;</code></pre> 
1,2) Public member function, calls the protected virtual member function do_narrow of the most derived class. 
3) Converts the (possibly wide) character c to multibyte representation if the character can be represented with a single byte (for example, ASCII characters in UTF-8 encoding are single bytes). Returns dflt if such conversion does not exist. 
4) For every character in the character array [beg, end), writes narrowed characters (or dflt whenever narrowing fails) to the successive locations in the character array pointed to by dst. 
Narrowing is always successful and is always reversible (by calling widen()) for all characters from the basic source character set (latin letters, digits, and punctuations required to write a C++ program) 
Narrowing, if successful, preserves all character classification categories known to is(). 
Narrowing of any digit character guarantees that if the result is subtracted from the character literal '0', the difference equals the digit value of the original character. 

<h2>Parameters</h2>

c - character to convert 
dflt - default value to produce if the conversion fails 
beg - pointer to the first character in an array of characters to convert 
end - one past the end pointer for the array of characters to convert 
dst - pointer to the first element of the array of char to fill

<h2>Return value</h2>

1,3) narrowed character or dflt if narrowing fails 
2,4) end 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;locale&gt;

#include &lt;iostream&gt;
void try_narrow(const std::ctype&lt;wchar_t&gt; &amp;f, wchar_t c)

{
    char n = f.narrow(c, 0);
    if (n) {
        std::wcout &lt;&lt; '\'' &lt;&lt; c &lt;&lt; &quot;' narrowed to &quot; &lt;&lt; +(unsigned char)n &lt;&lt; '\n';
    } else {
        std::wcout &lt;&lt; '\'' &lt;&lt; c &lt;&lt; &quot;' could not be narrowed\n&quot;;
    }
}
int main()

{
    std::locale::global(std::locale(&quot;en_US.utf8&quot;));
    std::wcout.imbue(std::locale());
    std::wcout &lt;&lt; std::hex &lt;&lt; std::showbase &lt;&lt; &quot;In US English UTF-8 locale:\n&quot;;
    auto &amp;f = std::use_facet&lt;std::ctype&lt;wchar_t&gt;&gt;(std::locale());
    try_narrow(f, L'A');
    try_narrow(f, L'Ａ');
    try_narrow(f, L'ě');
    std::locale::global(std::locale(&quot;cs_CZ.iso88592&quot;));
    auto &amp;f2 = std::use_facet&lt;std::ctype&lt;wchar_t&gt;&gt;(std::locale());
    std::wcout &lt;&lt; &quot;In Czech ISO-8859-2 locale:\n&quot;;
    try_narrow(f2, L'A');
    try_narrow(f2, L'Ａ');
    try_narrow(f2, L'ě');
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;In US English UTF-8 locale: 
&nbsp;<wbr>&nbsp;'A' narrowed to 0x41 
&nbsp;<wbr>&nbsp;'Ａ' could not be narrowed 
&nbsp;<wbr>&nbsp;'ě' could not be narrowed 
&nbsp;<wbr>&nbsp;In Czech ISO-8859-2 locale: 
&nbsp;<wbr>&nbsp;'A' narrowed to 0x41 
&nbsp;<wbr>&nbsp;'Ａ' could not be narrowed 
&nbsp;<wbr>&nbsp;'ě' narrowed to 0xec

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;invokes do_widen 
widen <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;narrows characters 
narrow <i>(public member function of std::basic_ios&lt;CharT,Traits&gt;)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;narrows a wide character to a single-byte narrow character, if possible 
wctob <i>(function)</i> 
