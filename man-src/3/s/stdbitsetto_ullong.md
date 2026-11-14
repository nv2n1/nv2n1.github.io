---
title: "stdbitsetto_ullong(3)"
name: "stdbitsetto_ullong"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdbitsetto_ullong/"
---

std::bitset&lt;N&gt;::to_ullong - std::bitset&lt;N&gt;::to_ullong

<h2>Synopsis</h2>

<pre><code>unsigned long long to_ullong() const  (since C++11)</code></pre> 
Converts the contents of the bitset to an unsigned long long integer. 
The first bit of the bitset corresponds to the least significant digit of the number and the last bit corresponds to the most significant digit. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

the converted integer 

<h2>Exceptions</h2>

std::overflow_error if the value can not be represented in unsigned long long.

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;bitset&gt;

#include &lt;limits&gt;
int main()

{
    std::bitset&lt;std::numeric_limits&lt;unsigned long long&gt;::digits&gt; b(
        0x123456789abcdef0LL);
    std::cout &lt;&lt; b &lt;&lt; &quot;  &quot; &lt;&lt; std::hex &lt;&lt; b.to_ullong() &lt;&lt; '\n';
    b.flip();
    std::cout &lt;&lt; b &lt;&lt; &quot;  &quot; &lt;&lt; b.to_ullong() &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;0001001000110100010101100111100010011010101111001101111011110000 123456789abcdef0 
&nbsp;<wbr>&nbsp;1110110111001011101010011000011101100101010000110010000100001111 edcba9876543210f

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns a string representation of the data 
to_string <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns an unsigned long integer representation of the data 
to_ulong <i>(public member function)</i> 
