---
title: "stdexperimentalminmax(3)"
name: "stdexperimentalminmax"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalminmax/"
---

std::experimental::minmax - std::experimental::minmax

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;experimental / simd&gt;

    template &lt;class T, class Abi&gt;

    std::pair&lt;simd&lt;T, Abi&gt;, simd&lt;T, Abi&gt;&gt;

    minmax(const simd&lt;T, Abi&gt; &amp;a, const simd&lt;T, Abi&gt; &amp;b) noexcept;</code></pre> 
Returns both the element-wise min result and element-wise max result. 

<h2>Parameters</h2>

a - the first vector of elements for minmax 
b - the second vector of elements for minmax

<h2>Return value</h2>

An object r, where the i-th element of r.first is std::min(a[i], b[i]), and the i-th element of r.second is std::max(a[i], b[i]). 

<h2>Example</h2>



<h2>See also</h2>


