---
title: "stdbitsetflip(3)"
name: "stdbitsetflip"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdbitsetflip/"
description: "std::bitset<N>::flip – std::bitset<N>::flip"
---

<p>std::bitset&lt;N&gt;::flip &#8211; std::bitset&lt;N&gt;::flip</p>
<h2>Synopsis</h2>
<p>bitset&lt;N&gt;&amp; flip(); <i>(until C++11)</i><br />
bitset&lt;N&gt;&amp; flip() noexcept; <code>(1)</code> <i>(since C++11)</i><br />
bitset&lt;N&gt;&amp; flip( std::size_t pos ); <code>(2)</code><br />
Flips bits, i.e. changes true values to false and false values to true. Equivalent to a logical NOT operation on part or all of the bitset.<br />
1) Flips all bits (like operator~, but in-place)<br />
2) Flips the bit at the position pos. </p>
<h2>Parameters</h2>
<p>pos &#8211; the position of the bit to flip</p>
<h2>Return value</h2>
<p>*this </p>
<h2>Exceptions</h2>
<p>2) throws std::out_of_range if pos does not correspond to a valid position within the bitset.</p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;bitset&gt;
int main()

{
    std::bitset&lt;4&gt; b;
    std::cout &lt;&lt; b &lt;&lt; &quot;
&quot;;
    std::cout &lt;&lt; b.flip(0) &lt;&lt; '
';
    std::cout &lt;&lt; b.flip(2) &lt;&lt; '
';
    std::cout &lt;&lt; b.flip() &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;0000<br />
&nbsp;<wbr>&nbsp;0001<br />
&nbsp;<wbr>&nbsp;0101<br />
&nbsp;<wbr>&nbsp;1010</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sets bits to true or given value<br />
set <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sets bits to false<br />
reset <i>(public member function)</i> </p>
<pre><code>operator&amp;= performs binary AND, OR, XOR and NOT

operator|= (public member function)

operator^=

operator~




</code></pre>
