---
title: "stdexperimentalsimd_abiscalar(3)"
name: "stdexperimentalsimd_abiscalar"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalsimd_abiscalar/"
---

std::experimental::simd_abi::scalar - std::experimental::simd_abi::scalar

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;experimental / simd&gt;

    namespace simd_abi
{

    struct scalar {
    };
}</code></pre> 
The scalar tag type ensures data-parallel types to store a single element (i.e., simd&lt;T, simd_abi::scalar&gt;::size() returns 1). 

<h2>Notes</h2>

scalar is not an alias to fixed_size&lt;1&gt;. 

<h2>See also</h2>


