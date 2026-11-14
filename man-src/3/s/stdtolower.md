---
title: "stdtolower(3)"
name: "stdtolower"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdtolower/"
---

std::tolower - std::tolower

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cctype&gt;

    int tolower(int ch);</code></pre> 
Converts the given character to lowercase according to the character conversion rules defined by the currently installed C locale. 
In the default &quot;C&quot; locale, the following uppercase letters ABCDEFGHIJKLMNOPQRSTUVWXYZ are replaced with respective lowercase letters abcdefghijklmnopqrstuvwxyz. 

<h2>Parameters</h2>

ch - character to be converted. If the value of ch is not representable as unsigned char and does not equal EOF, the behavior is undefined

<h2>Return value</h2>

Lowercase version of ch or unmodified ch if no lowercase version is listed in the current C locale. 

<h2>Notes</h2>

Like all other functions from &lt;cctype&gt;, the behavior of std::tolower is undefined if the argument's value is neither representable as unsigned char nor equal to EOF. To use these functions safely with plain chars (or signed chars), the argument should first be converted to unsigned char: char my_tolower(char ch)

{
    return static_cast&lt;char&gt;(std::tolower(static_cast&lt;unsigned char&gt;(ch)));
} 
Similarly, they should not be directly used with standard algorithms when the iterator's value type is char or signed char. Instead, convert the value to unsigned char first: std::string str_tolower(std::string s)
{
    std::transform(s.begin(), s.end(), s.begin(),
                   // static_cast&lt;int(*)(int)&gt;(std::tolower)         // wrong
                   // [](int c){ return std::tolower(c); }           // wrong
                   // [](char c){ return std::tolower(c); }          // wrong
                   [](unsigned char c) { return std::tolower(c); } // correct
    );
    return s;
}


<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;cctype&gt;

#include &lt;clocale&gt;
int main()

{
    unsigned char c = '\xb4'; // the character Ž in ISO-8859-15
                              // but ´ (acute accent) in ISO-8859-1
    std::setlocale(LC_ALL, &quot;en_US.iso88591&quot;);
    std::cout &lt;&lt; std::hex &lt;&lt; std::showbase;
    std::cout &lt;&lt; &quot;in iso8859-1, tolower('0xb4') gives &quot;
              &lt;&lt; std::tolower(c) &lt;&lt; '\n';
    std::setlocale(LC_ALL, &quot;en_US.iso885915&quot;);
    std::cout &lt;&lt; &quot;in iso8859-15, tolower('0xb4') gives &quot;
              &lt;&lt; std::tolower(c) &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;in iso8859-1, tolower('0xb4') gives 0xb4 
&nbsp;<wbr>&nbsp;in iso8859-15, tolower('0xb4') gives 0xb8

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;converts a character to uppercase 
toupper <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;converts a character to lowercase using the ctype facet of a locale 
tolower(std::locale) <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;converts a wide character to lowercase 
towlower <i>(function)</i> 
