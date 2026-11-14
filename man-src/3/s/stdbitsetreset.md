---
title: "stdbitsetreset(3)"
name: "stdbitsetreset"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdbitsetreset/"
description: "std::bitset<N>::reset – std::bitset<N>::reset"
---

<p>std::bitset&lt;N&gt;::reset &#8211; std::bitset&lt;N&gt;::reset</p>
<h2>Synopsis</h2>
<p>bitset&lt;N&gt;&amp; reset(); <i>(until C++11)</i><br />
bitset&lt;N&gt;&amp; reset() noexcept; <code>(1)</code> <i>(since C++11)</i><br />
bitset&lt;N&gt;&amp; reset( std::size_t pos ); <code>(2)</code><br />
Sets bits to false.<br />
1) Sets all bits to false<br />
2) Sets the bit at position pos to false. </p>
<h2>Parameters</h2>
<p>pos &#8211; the position of the bit to set</p>
<h2>Return value</h2>
<p>*this </p>
<h2>Exceptions</h2>
<p>2) Throws std::out_of_range if pos does not correspond to a valid position within the bitset</p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;bitset&gt;
int main()

{
    std::bitset&lt;8&gt; b(42);
    std::cout &lt;&lt; &quot;Bitset is         &quot; &lt;&lt; b &lt;&lt; '
';
    b.reset(1);
    std::cout &lt;&lt; &quot;After b.reset(1): &quot; &lt;&lt; b &lt;&lt; '
';
    b.reset();
    std::cout &lt;&lt; &quot;After b.reset():  &quot; &lt;&lt; b &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;Bitset is 00101010<br />
&nbsp;<wbr>&nbsp;After <a href="/docs/linux/man/1-b-reset/">b.reset</a><code>(1)</code>: 00101000<br />
&nbsp;<wbr>&nbsp;After b.reset(): 00000000</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sets bits to true or given value<br />
set <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;toggles the values of bits<br />
flip <i>(public member function)</i> </p>
