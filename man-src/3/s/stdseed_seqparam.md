---
title: "stdseed_seqparam(3)"
name: "stdseed_seqparam"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdseed_seqparam/"
---

std::seed_seq::param - std::seed_seq::param

<h2>Synopsis</h2>

<pre><code>template &lt;class OutputIt&gt;
(since C++ 11)

    void param(OutputIt dest) const;</code></pre> 
Outputs the initial seed sequence that's stored in the std::seed_seq object. 

<h2>Parameters</h2>

dest - output iterator such that the expression *dest=rt is valid for a value rt of result_type

<h2>Type requirements</h2>

- 
OutputIt must meet the requirements of LegacyOutputIterator.

<h2>Return value</h2>

<i>(none)</i> 

<h2>Exceptions</h2>

Throws only if an operation on dest throws.

<h2>Example</h2>

// Run this code <pre><code>#include &lt;random&gt;

#include &lt;iostream&gt;

#include &lt;iterator&gt;

int main()

{
    std::seed_seq s1 = {-1, 0, 1};
    s1.param(std::ostream_iterator&lt;int&gt;(std::cout, &quot; &quot;));
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;-1 0 1
