---
title: "stdtoupper(3)"
name: "stdtoupper"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdtoupper/"
---

std::toupper - std::toupper

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cctype&gt;

    int toupper(int ch);</code></pre> 
Converts the given character to uppercase according to the character conversion rules defined by the currently installed C locale. 
In the default &quot;C&quot; locale, the following lowercase letters abcdefghijklmnopqrstuvwxyz are replaced with respective uppercase letters ABCDEFGHIJKLMNOPQRSTUVWXYZ. 

<h2>Parameters</h2>

ch - character to be converted. If the value of ch is not representable as unsigned char and does not equal EOF, the behavior is undefined.

<h2>Return value</h2>

Converted character or ch if no uppercase version is defined by the current C locale. 

<h2>Notes</h2>

Like all other functions from &lt;cctype&gt;, the behavior of std::toupper is undefined if the argument's value is neither representable as unsigned char nor equal to EOF. To use these functions safely with plain chars (or signed chars), the argument should first be converted to unsigned char: char my_toupper(char ch)

{
    return static_cast&lt;char&gt;(std::toupper(static_cast&lt;unsigned char&gt;(ch)));
} 
Similarly, they should not be directly used with standard algorithms when the iterator's value type is char or signed char. Instead, convert the value to unsigned char first: std::string str_toupper(std::string s)
{
    std::transform(s.begin(), s.end(), s.begin(),
                   // static_cast&lt;int(*)(int)&gt;(std::toupper)         // wrong
                   // [](int c){ return std::toupper(c); }           // wrong
                   // [](char c){ return std::toupper(c); }          // wrong
                   [](unsigned char c) { return std::toupper(c); } // correct
    );
    return s;
}


<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;cctype&gt;

#include &lt;clocale&gt;
int main()

{
    unsigned char c = '\xb8'; // the character ž in ISO-8859-15
                              // but ¸ (cedilla) in ISO-8859-1
    std::setlocale(LC_ALL, &quot;en_US.iso88591&quot;);
    std::cout &lt;&lt; std::hex &lt;&lt; std::showbase;
    std::cout &lt;&lt; &quot;in iso8859-1, toupper('0xb8') gives &quot; &lt;&lt; std::toupper(c) &lt;&lt; '\n';
    std::setlocale(LC_ALL, &quot;en_US.iso885915&quot;);
    std::cout &lt;&lt; &quot;in iso8859-15, toupper('0xb8') gives &quot; &lt;&lt; std::toupper(c) &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;in iso8859-1, toupper('0xb8') gives 0xb8 
&nbsp;<wbr>&nbsp;in iso8859-15, toupper('0xb8') gives 0xb4

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;converts a character to lowercase 
tolower <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;converts a character to uppercase using the ctype facet of a locale 
toupper(std::locale) <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;converts a wide character to uppercase 
towupper <i>(function)</i> 
