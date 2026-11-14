---
title: "stdexperimentalclamp(3)"
name: "stdexperimentalclamp"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalclamp/"
---

std::experimental::clamp - std::experimental::clamp

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;experimental / simd&gt;

    template &lt;class T, class Abi&gt;

    simd&lt;T, Abi&gt;

    clamp(const simd&lt;T, Abi&gt; &amp;v, const simd&lt;T, Abi&gt; &amp;lo, const simd&lt;T, Abi&gt; &amp;hi);
</code></pre>

<h2>Parameters</h2>

v - the elements to clamp 
lo, hi - the boundaries to clamp v to

<h2>Return value</h2>

The result of element-wise application of std::clamp(v[i], lo[i], hi[i]) for all i ∈ [0, size()). 

<h2>Example</h2>



<h2>See also</h2>


