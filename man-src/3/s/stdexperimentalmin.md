---
title: "stdexperimentalmin(3)"
name: "stdexperimentalmin"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalmin/"
---

std::experimental::min - std::experimental::min

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;experimental / simd&gt;

    template &lt;class T, class Abi&gt;

    simd&lt;T, Abi&gt; min(const simd&lt;T, Abi&gt; &amp;a, const simd&lt;T, Abi&gt; &amp;b) noexcept;
</code></pre>

<h2>Parameters</h2>

a - the first vector of elements for min 
b - the second vector of elements for min

<h2>Return value</h2>

The result of binary element-wise application of std::min(a[i], b[i]) for all i ∈ [0, size()). 

<h2>Example</h2>



<h2>See also</h2>


