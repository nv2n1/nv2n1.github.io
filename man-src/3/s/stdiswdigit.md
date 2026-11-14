---
title: "stdiswdigit(3)"
name: "stdiswdigit"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdiswdigit/"
---

std::iswdigit - std::iswdigit

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cwctype&gt;

    int iswdigit(wint_t ch);</code></pre> 
Checks if the given wide character corresponds (if narrowed) to one of the ten decimal digit characters 0123456789. 
If the value of ch is neither representable as a wchar_t nor equal to the value of the macro WEOF, the behavior is undefined. 

<h2>Parameters</h2>

ch - wide character

<h2>Return value</h2>

Non-zero value if the wide character is an numeric character, zero otherwise. 

<h2>Notes</h2>

std::iswdigit and std::iswxdigit are the only standard wide character classification functions that are not affected by the currently installed C locale. 

<h2>Example</h2>

Some locales offer additional character classes that detect non-ASCII digits 
 // Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;cwctype&gt;

#include &lt;clocale&gt;

void test(wchar_t a3, wchar_t u3, wchar_t j3)

{
    std::wcout &lt;&lt; std::boolalpha
               &lt;&lt; &quot;          '&quot; &lt;&lt; a3 &lt;&lt; &quot;'   '&quot; &lt;&lt; u3 &lt;&lt; &quot;'  '&quot; &lt;&lt; j3 &lt;&lt; &quot;'\n&quot;
               &lt;&lt; &quot;iswdigit &quot;
               &lt;&lt; (bool)std::iswdigit(a3) &lt;&lt; &quot;  &quot;
               &lt;&lt; (bool)std::iswdigit(u3) &lt;&lt; &quot; &quot;
               &lt;&lt; (bool)std::iswdigit(j3) &lt;&lt; '\n'
               &lt;&lt; &quot;jdigit:  &quot;
               &lt;&lt; (bool)std::iswctype(a3, std::wctype(&quot;jdigit&quot;)) &lt;&lt; ' '
               &lt;&lt; (bool)std::iswctype(u3, std::wctype(&quot;jdigit&quot;)) &lt;&lt; ' '
               &lt;&lt; (bool)std::iswctype(j3, std::wctype(&quot;jdigit&quot;)) &lt;&lt; '\n';
}

int main()

{
    wchar_t a3 = L'3';  // the ASCII digit 3
    wchar_t u3 = L'三'; // the CJK numeral 3
    wchar_t j3 = L'３'; // the fullwidth digit 3
    std::setlocale(LC_ALL, &quot;en_US.utf8&quot;);
    std::wcout &lt;&lt; &quot;In american locale:\n&quot;;
    test(a3, u3, j3);
    std::wcout &lt;&lt; &quot;\nIn japanese locale:\n&quot;;
    std::setlocale(LC_ALL, &quot;ja_JP.utf8&quot;);
    test(a3, u3, j3);
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;In american locale: 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;'3' '三' '３' 
&nbsp;<wbr>&nbsp;iswdigit true false false 
&nbsp;<wbr>&nbsp;jdigit: false false false 

 
&nbsp;<wbr>&nbsp;In japanese locale: 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;'3' '三' '３' 
&nbsp;<wbr>&nbsp;iswdigit true false false 
&nbsp;<wbr>&nbsp;jdigit: false false true

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks if a character is classified as a digit by a locale 
isdigit(std::locale) <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks if a character is a digit 
isdigit <i>(function)</i> 
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
