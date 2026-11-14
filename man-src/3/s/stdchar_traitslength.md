---
title: "stdchar_traitslength(3)"
name: "stdchar_traitslength"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchar_traitslength/"
---

std::char_traits&lt;CharT&gt;::length - std::char_traits&lt;CharT&gt;::length

<h2>Synopsis</h2>

<pre><code>static std::size_t length(const char_type *s);
(until C++ 17)

    static constexpr std::size_t length(const char_type *s);
(since C++ 17)</code></pre> 
Returns the length of the character sequence pointed to by s, that is, the position of the terminating null character (CharT()). 

<h2>Parameters</h2>

s - pointer to a character sequence to return length of

<h2>Return value</h2>

The length of character sequence pointed to by s. 

<h2>Exceptions</h2>

<i>(none)</i>

<h2>Complexity</h2>

Linear.

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;
void print(const char *str)

{
    std::cout &lt;&lt; &quot;string '&quot; &lt;&lt; str &lt;&lt; &quot;' &quot;;
    std::cout &lt;&lt; &quot;length = &quot; &lt;&lt; std::char_traits&lt;char&gt;::length(str) &lt;&lt; '\n';
}
int main()

{
    print(&quot;foo&quot;);
    std::string s(&quot;booo&quot;);
    print(s.c_str());
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;string 'foo' length = 3 
&nbsp;<wbr>&nbsp;string 'booo' length = 4
