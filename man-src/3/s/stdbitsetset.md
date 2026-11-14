---
title: "stdbitsetset(3)"
name: "stdbitsetset"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdbitsetset/"
---

std::bitset&lt;N&gt;::set - std::bitset&lt;N&gt;::set

<h2>Synopsis</h2>

<pre><code>bitset&lt;N&gt;&amp; set();                                             (until C++11)

bitset&lt;N&gt;&amp; set() noexcept;                            (1)     (since C++11)

bitset&lt;N&gt;&amp; set( std::size_t pos, bool value = true );     (2)</code></pre> 
Sets all bits to true or to specified value. 
1) Sets all bits to true. 
2) Sets the bit at position pos to the value value. 

<h2>Parameters</h2>

pos - the position of the bit to set (least significant to most significant) 
value - the value to set the bit to

<h2>Return value</h2>

*this 

<h2>Exceptions</h2>

2) Throws std::out_of_range if pos does not correspond to a valid position within the bitset.

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;bitset&gt;
int main()

{
    std::bitset&lt;8&gt; b;
    for (size_t i = 1; i &lt; b.size(); i += 2) {
        b.set(i);
    }
    std::cout &lt;&lt; b &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;10101010

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sets bits to false 
reset <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;toggles the values of bits 
flip <i>(public member function)</i> 
