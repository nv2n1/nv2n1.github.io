---
title: "stdbitsetcount(3)"
name: "stdbitsetcount"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdbitsetcount/"
---

std::bitset&lt;N&gt;::count - std::bitset&lt;N&gt;::count

<h2>Synopsis</h2>

std::size_t count() const; <i>(until C++11)</i> 
std::size_t count() const noexcept; <i>(since C++11)</i> 
Returns the number of bits that are set to true. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

number of bits that are set to true. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;bitset&gt;
int main()

{
    std::bitset&lt;8&gt; b(&quot;00010010&quot;);
    std::cout &lt;&lt; &quot;initial value: &quot; &lt;&lt; b &lt;&lt; '\n';
    // find the first unset bit
    std::size_t idx = 0;
    while (idx &lt; b.size() &amp;&amp; b.test(idx))
        ++idx;
    // continue setting bits until half the bitset is filled
    while (idx &lt; b.size() &amp;&amp; b.count() &lt; b.size() / 2) {
        b.set(idx);
        std::cout &lt;&lt; &quot;setting bit &quot; &lt;&lt; idx &lt;&lt; &quot;: &quot; &lt;&lt; b &lt;&lt; '\n';
        while (idx &lt; b.size() &amp;&amp; b.test(idx))
            ++idx;
    }
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;initial value: 00010010 
&nbsp;<wbr>&nbsp;setting bit 0: 00010011 
&nbsp;<wbr>&nbsp;setting bit 2: 00010111

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the size number of bits that the bitset can hold 
size <i>(public member function)</i> 
