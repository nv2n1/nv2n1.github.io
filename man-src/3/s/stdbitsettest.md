---
title: "stdbitsettest(3)"
name: "stdbitsettest"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdbitsettest/"
---

std::bitset&lt;N&gt;::test - std::bitset&lt;N&gt;::test

<h2>Synopsis</h2>

<pre><code>bool test(size_t pos) const;</code></pre> 
Returns the value of the bit at the position pos. 
Unlike operator[], performs a bounds check and throws std::out_of_range if pos does not correspond to a valid position in the bitset. 

<h2>Parameters</h2>

pos - position of the bit to return

<h2>Return value</h2>

true if the requested bit is set, false otherwise. 

<h2>Exceptions</h2>

std::out_of_range if pos does not correspond to a valid position within the bitset.

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;bitset&gt;
int main()

{
    std::bitset&lt;10&gt; b1(&quot;1111010000&quot;);
    size_t idx = 0;
    while (idx &lt; b1.size() &amp;&amp; !b1.test(idx)) {
        ++idx;
    }
    if (idx &lt; b1.size()) {
        std::cout &lt;&lt; &quot;first set bit at index &quot; &lt;&lt; idx &lt;&lt; '\n';
    } else {
        std::cout &lt;&lt; &quot;no set bits\n&quot;;
    }
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;first set bit at index 4

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;accesses specific bit 
operator[] <i>(public member function)</i> 
