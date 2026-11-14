---
title: "operatorstdbitset(3)"
name: "operatorstdbitset"
section: "3"
letter: "o"
url: "/docs/linux/man/3-operatorstdbitset/"
---

operator&amp;,|,^(std::bitset) - operator&amp;,|,^(std::bitset)

<h2>Synopsis</h2>

<pre><code>template &lt;std::size_t N&gt;
(1)

    bitset&lt;N&gt;
    operator&amp;(const bitset&lt;N&gt; &amp;lhs, const bitset&lt;N&gt; &amp;rhs);

template &lt;std::size_t N&gt;
(2)

    bitset&lt;N&gt;
    operator|(const bitset&lt;N&gt; &amp;lhs, const bitset&lt;N&gt; &amp;rhs);

template &lt;std::size_t N&gt;
(3)

    bitset&lt;N&gt;
    operator^(const bitset&lt;N&gt; &amp;lhs, const bitset&lt;N&gt; &amp;rhs);</code></pre> 
Performs binary AND, OR, and XOR between two bitsets, lhs and rhs. 
1) Returns a bitset&lt;N&gt; containing the result of binary AND on corresponding pairs of bits of lhs and rhs. 
2) Returns a bitset&lt;N&gt; containing the result of binary OR on corresponding pairs of bits of lhs and rhs. 
3) Returns a bitset&lt;N&gt; containing the result of binary XOR on corresponding pairs of bits of lhs and rhs. 

<h2>Parameters</h2>

lhs - the bitset on the left-hand side of the operator 
rhs - the bitset on the right-hand side of the operator

<h2>Return value</h2>

1) bitset&lt;N&gt;(lhs) &amp;= rhs

2) bitset&lt;N&gt;(lhs) |= rhs

3) bitset&lt;N&gt;(lhs) ^= rhs


<h2>Exceptions</h2>

<i>(none)</i> <i>(until C++11)</i> 
noexcept specification: <i>(since C++11)</i> 
noexcept

<h2>Example</h2>

// Run this code #include &lt;bitset&gt;

#include &lt;iostream&gt;
int main()

{
    std::bitset&lt;4&gt; b1(&quot;0110&quot;);
    std::bitset&lt;4&gt; b2(&quot;0011&quot;);
    std::cout &lt;&lt; &quot;b1 &amp; b2: &quot; &lt;&lt; (b1 &amp; b2) &lt;&lt; '\n';
    std::cout &lt;&lt; &quot;b1 | b2: &quot; &lt;&lt; (b1 | b2) &lt;&lt; '\n';
    std::cout &lt;&lt; &quot;b1 ^ b2: &quot; &lt;&lt; (b1 ^ b2) &lt;&lt; '\n';
}


<h2>Output:</h2>

&nbsp;<wbr>&nbsp;b1 &amp; b2: 0010 
&nbsp;<wbr>&nbsp;b1 | b2: 0111 
&nbsp;<wbr>&nbsp;b1 ^ b2: 0101

<h2>See also</h2>

<pre><code>operator&amp;= performs binary AND, OR, XOR and NOT

operator|= (public member function)

operator^=

operator~




</code></pre>
