---
title: "stdbitsetoperator(3)"
name: "stdbitsetoperator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdbitsetoperator/"
description: "std::bitset<N>::operator[] – std::bitset<N>::operator[]"
---

<p>std::bitset&lt;N&gt;::operator[] &#8211; std::bitset&lt;N&gt;::operator[]</p>
<h2>Synopsis</h2>
<p>bool operator[]( std::size_t pos ) const; <i>(until C++11)</i><br />
constexpr bool operator[]( std::size_t pos ) const; <code>(1)</code> <i>(since C++11)</i><br />
reference operator[]( std::size_t pos ); <code>(2)</code><br />
Accesses the bit at position pos. The first version returns the value of the bit, the second version returns an object of type std::bitset::reference that allows modification of the value.<br />
Unlike test(), does not throw exceptions: the behavior is undefined if pos is out of bounds. </p>
<h2>Parameters</h2>
<p>pos &#8211; position of the bit to return</p>
<h2>Return value</h2>
<p>1) the value of the requested bit<br />
2) an object of type std::bitset::reference, which allows writing to the requested bit. </p>
<h2>Exceptions</h2>
<p>None</p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;bitset&gt;
int main()

{
    std::bitset&lt;8&gt; b1(42);
    for (std::size_t i = 0; i &lt; b1.size(); ++i) {
        std::cout &lt;&lt; &quot;b1[&quot; &lt;&lt; i &lt;&lt; &quot;]: &quot; &lt;&lt; b1[i] &lt;&lt; '
';
    }
    b1[0] = true; // modifies the first bit through bitset::reference
    std::cout &lt;&lt; &quot;After setting bit 0, the bitset holds &quot; &lt;&lt; b1 &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;b1[0]: 0<br />
&nbsp;<wbr>&nbsp;b1[1]: 1<br />
&nbsp;<wbr>&nbsp;b1[2]: 0<br />
&nbsp;<wbr>&nbsp;b1[3]: 1<br />
&nbsp;<wbr>&nbsp;b1[4]: 0<br />
&nbsp;<wbr>&nbsp;b1[5]: 1<br />
&nbsp;<wbr>&nbsp;b1[6]: 0<br />
&nbsp;<wbr>&nbsp;b1[7]: 0<br />
&nbsp;<wbr>&nbsp;After setting bit 0, the bitset holds 00101011</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;accesses specific bit<br />
test <i>(public member function)</i> </p>
