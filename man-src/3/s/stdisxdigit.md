---
title: "stdisxdigit(3)"
name: "stdisxdigit"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdisxdigit/"
---

std::isxdigit - std::isxdigit

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cctype&gt;

    int isxdigit(int ch);</code></pre> 
Checks if the given character is a hexadecimal numeric character (0123456789abcdefABCDEF). 
The behavior is undefined if the value of ch is not representable as unsigned char and is not equal to EOF. 

<h2>Parameters</h2>

ch - character to classify

<h2>Return value</h2>

Non-zero value if the character is an hexadecimal numeric character, zero otherwise. 

<h2>Notes</h2>

isdigit and isxdigit are the only standard narrow character classification functions that are not affected by the currently installed C locale. although some implementations (e.g. Microsoft in 1252 codepage) may classify additional single-byte characters as digits. 
Like all other functions from &lt;cctype&gt;, the behavior of std::isxdigit is undefined if the argument's value is neither representable as unsigned char nor equal to EOF. To use these functions safely with plain chars (or signed chars), the argument should first be converted to unsigned char: bool my_isxdigit(char ch)

{
    return std::isxdigit(static_cast&lt;unsigned char&gt;(ch));
} 
Similarly, they should not be directly used with standard algorithms when the iterator's value type is char or signed char. Instead, convert the value to unsigned char first: <pre><code>int count_xdigits(const std::string &amp;s)

{
    return std::count_if(s.begin(), s.end(),
                         // static_cast&lt;int(*)(int)&gt;(std::isxdigit)         // wrong
                         // [](int c){ return std::isxdigit(c); }           // wrong
                         // [](char c){ return std::isxdigit(c); }          // wrong
                         [](unsigned char c) { return std::isxdigit(c); } // correct
    );
}
</code></pre>

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks if a character is classified as a hexadecimal digit by a locale 
isxdigit(std::locale) <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks if a character is a hexadecimal character 
iswxdigit <i>(function)</i> 
ASCII values iscntrl isprint isspace isblank isgraph ispunct isalnum isalpha isupper islower isdigit isxdigit 
decimal hexadecimal octal characters iswcntrl iswprint iswspace iswblank iswgraph iswpunct iswalnum iswalpha iswupper iswlower iswdigit iswxdigit 
0–8 \x0–\x8 \0–\10 control codes (NUL, etc.) ≠0 0 0 0 0 0 0 0 0 0 0 0 
9 \x9 \11 tab (\t) ≠0 0 ≠0 ≠0 0 0 0 0 0 0 0 0 
10–13 \xA–\xD \12–\15 whitespaces (\n, \v, \f, \r) ≠0 0 ≠0 0 0 0 0 0 0 0 0 0 
14–31 \xE–\x1F \16–\37 control codes ≠0 0 0 0 0 0 0 0 0 0 0 0 
32 \x20 \40 space 0 ≠0 ≠0 ≠0 0 0 0 0 0 0 0 0 
33–47 \x21–\x2F \41–\57 !&quot;#$%&amp;'()*+,-./ 0 ≠0 0 0 ≠0 ≠0 0 0 0 0 0 0 
48–57 \x30–\x39 \60–\71 0123456789 0 ≠0 0 0 ≠0 0 ≠0 0 0 0 ≠0 ≠0 
58–64 \x3A–\x40 \72–\100:;&lt;=&gt;?@ 0 ≠0 0 0 ≠0 ≠0 0 0 0 0 0 0 
65–70 \x41–\x46 \101–\10ABCDEF 0 ≠0 0 0 ≠0 0 ≠0 ≠0 ≠0 0 0 ≠0 
71–90 \x47–\x5A \107–\13GHIJKLMNOP 0 ≠0 0 0 ≠0 0 ≠0 ≠0 ≠0 0 0 0 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;QRSTUVWXYZ 
91–96 \x5B–\x60 \133–\14[\]^_` 0 ≠0 0 0 ≠0 ≠0 0 0 0 0 0 0 
97–102\x61–\x66 \141–\14abcdef 0 ≠0 0 0 ≠0 0 ≠0 ≠0 0 ≠0 0 ≠0 
103–12\x67–\x7A \147–\17ghijklmnop 0 ≠0 0 0 ≠0 0 ≠0 ≠0 0 ≠0 0 0 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;qrstuvwxyz 
123–12\x7B–\x7E \172–\17{|}~ 0 ≠0 0 0 ≠0 ≠0 0 0 0 0 0 0 
127 \x7F \177 backspace character (DEL) ≠0 0 0 0 0 0 0 0 0 0 0 0 
