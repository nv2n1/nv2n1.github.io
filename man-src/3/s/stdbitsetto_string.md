---
title: "stdbitsetto_string(3)"
name: "stdbitsetto_string"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdbitsetto_string/"
---

std::bitset&lt;N&gt;::to_string - std::bitset&lt;N&gt;::to_string

<h2>Synopsis</h2>

<pre><code>template &lt;

    class CharT,

    class Traits, (until C++ 11)

                      class Alloc

    &gt;
std::basic_string&lt;CharT, Traits, Allocator&gt; to_string() const;

template &lt;

    class CharT = char,

    class Traits = std::char_traits&lt;CharT&gt;, (since C++ 11)

                                                class Allocator = std::allocator&lt;CharT&gt;

    &gt;
std::basic_string&lt;CharT, Traits, Allocator&gt;

to_string(CharT zero = CharT('0'), CharT one = CharT('1')) const;</code></pre> 
Converts the contents of the bitset to a string. Uses zero to represent bits with value of false and one to represent bits with value of true. 
The resulting string contains N characters with the first character corresponds to the last (N-1th) bit and the last character corresponding to the first bit. 

<h2>Parameters</h2>

zero - character to use to represent false 
one - character to use to represent true

<h2>Return value</h2>

the converted string 

<h2>Exceptions</h2>

May throw std::bad_alloc from the the std::string constructor.

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;bitset&gt;

int main()

{
    std::bitset&lt;8&gt; b(42);
    std::cout &lt;&lt; b.to_string() &lt;&lt; '\n'
              &lt;&lt; b.to_string('*') &lt;&lt; '\n'
              &lt;&lt; b.to_string('O', 'X') &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;00101010 
&nbsp;<wbr>&nbsp;**1*1*1* 
&nbsp;<wbr>&nbsp;OOXOXOXO

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns an unsigned long integer representation of the data 
to_ulong <i>(public member function)</i> 
to_ullong returns an unsigned long long integer representation of the data 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public member function)</i> 
<i>(C++11)</i> 
