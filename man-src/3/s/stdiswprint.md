---
title: "stdiswprint(3)"
name: "stdiswprint"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdiswprint/"
---

std::iswprint - std::iswprint

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cwctype&gt;

    int iswprint(std::wint_t ch);</code></pre> 
Checks if the given wide character can be printed, i.e. it is either a number (0123456789), an uppercase letter (ABCDEFGHIJKLMNOPQRSTUVWXYZ), a lowercase letter (abcdefghijklmnopqrstuvwxyz), a punctuation character(!&quot;#$%&amp;'()*+,-./:;&lt;=&gt;?@[\]^_`{|}~), space or any printable character specific to the current C locale. 
If the value of ch is neither representable as a wchar_t nor equal to the value of the macro WEOF, the behavior is undefined. 

<h2>Parameters</h2>

ch - wide character

<h2>Return value</h2>

Non-zero value if the wide character can be printed, zero otherwise. 

<h2>Notes</h2>

ISO_30112 specifies which Unicode characters are include in POSIX print category. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;cwctype&gt;

#include &lt;clocale&gt;
int main()

{
    wchar_t c = L'\u2002'; // en-space
    std::setlocale(LC_ALL, &quot;en_US.utf8&quot;);
    std::cout &lt;&lt; std::boolalpha &lt;&lt; std::hex &lt;&lt; std::showbase
              &lt;&lt; &quot;in Unicode locale,\n&quot;
              &lt;&lt; &quot;iswprint('&quot; &lt;&lt; c &lt;&lt; &quot;') = &quot;
              &lt;&lt; (bool)std::iswprint(c) &lt;&lt; '\n';
    c = L'\u0082'; // break permitted
    std::cout &lt;&lt; &quot;iswprint('&quot; &lt;&lt; c &lt;&lt; &quot;') = &quot;
              &lt;&lt; (bool)std::iswprint(c) &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;in Unicode locale, 
&nbsp;<wbr>&nbsp;iswprint('0x2002') = true 
&nbsp;<wbr>&nbsp;iswprint('0x82') = false

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks if a character is classified as printable by a locale 
isprint(std::locale) <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks if a character is a printing character 
isprint <i>(function)</i> 
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
