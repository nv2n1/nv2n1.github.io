---
title: "stdispunct(3)"
name: "stdispunct"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdispunct/"
---

std::ispunct - std::ispunct

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cctype&gt;

    int ispunct(int ch);</code></pre> 
Checks if the given character is a punctuation character as classified by the current C locale. The default C locale classifies the characters !&quot;#$%&amp;'()*+,-./:;&lt;=&gt;?@[\]^_`{|}~ as punctuation. 
The behavior is undefined if the value of ch is not representable as unsigned char and is not equal to EOF. 

<h2>Parameters</h2>

ch - character to classify

<h2>Return value</h2>

Non-zero value if the character is a punctuation character, zero otherwise. 

<h2>Notes</h2>

Like all other functions from &lt;cctype&gt;, the behavior of std::ispunct is undefined if the argument's value is neither representable as unsigned char nor equal to EOF. To use these functions safely with plain chars (or signed chars), the argument should first be converted to unsigned char: bool my_ispunct(char ch)

{
    return std::ispunct(static_cast&lt;unsigned char&gt;(ch));
} 
Similarly, they should not be directly used with standard algorithms when the iterator's value type is char or signed char. Instead, convert the value to unsigned char first: int count_puncts(const std::string &amp;s)

{
    return std::count_if(s.begin(), s.end(),
                         // static_cast&lt;int(*)(int)&gt;(std::ispunct)         // wrong
                         // [](int c){ return std::ispunct(c); }           // wrong
                         // [](char c){ return std::ispunct(c); }          // wrong
                         [](unsigned char c) { return std::ispunct(c); } // correct
    );
}


<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;cctype&gt;

#include &lt;clocale&gt;
int main()

{
    unsigned char c = '\xd7'; // the character × (multiplication sign) in ISO-8859-1
    std::cout &lt;&lt; &quot;ispunct(\'\\xd7\', default C locale) returned &quot;
              &lt;&lt; std::boolalpha &lt;&lt; (bool)std::ispunct(c) &lt;&lt; '\n';
    std::setlocale(LC_ALL, &quot;en_GB.iso88591&quot;);
    std::cout &lt;&lt; &quot;ispunct(\'\\xd7\', ISO-8859-1 locale) returned &quot;
              &lt;&lt; std::boolalpha &lt;&lt; (bool)std::ispunct(c) &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;ispunct('\xd7', default C locale) returned false 
&nbsp;<wbr>&nbsp;ispunct('\xd7', ISO-8859-1 locale) returned true

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks if a character is classified as punctuation by a locale 
ispunct(std::locale) <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks if a wide character is a punctuation character 
iswpunct <i>(function)</i> 
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
