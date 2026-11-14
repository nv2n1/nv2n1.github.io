---
title: "stdexperimentalsimd_abicompatible(3)"
name: "stdexperimentalsimd_abicompatible"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalsimd_abicompatible/"
---

std::experimental::simd_abi::compatible - std::experimental::simd_abi::compatible

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;experimental/simd&gt;

namespace simd_abi {

    template &lt; class T &gt;

    using compatible = /*implementation-defined*/;

}</code></pre> 
compatible&lt;T&gt; is an implementation-defined alias for an ABI tag. 

<h2>Notes</h2>

The intent is to use the ABI tag producing the most efficient data-parallel execution for the element type T that ensures ABI compatibility between translation units on the target architecture. 

<h2>See also</h2>


