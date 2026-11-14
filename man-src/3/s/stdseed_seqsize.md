---
title: "stdseed_seqsize(3)"
name: "stdseed_seqsize"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdseed_seqsize/"
---

std::seed_seq::size - std::seed_seq::size

<h2>Synopsis</h2>

std::size_t size() const; <i>(since C++11)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(until C++17)</i> 
std::size_t size() const noexcept; <i>(since C++17)</i> 
Returns the size of the stored initial seed sequence. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

The size of the private container that was populated at construction time. 

<h2>Complexity</h2>

Constant time.

<h2>Example</h2>

// Run this code <pre><code>#include &lt;random&gt;

#include &lt;iostream&gt;

int main()

{
    std::seed_seq s1 = {-1, 0, 1};
    std::cout &lt;&lt; s1.size() &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;3
