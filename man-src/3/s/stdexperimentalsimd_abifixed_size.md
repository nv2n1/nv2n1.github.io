---
title: "stdexperimentalsimd_abifixed_size(3)"
name: "stdexperimentalsimd_abifixed_size"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalsimd_abifixed_size/"
---

std::experimental::simd_abi::fixed_size - std::experimental::simd_abi::fixed_size

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;experimental / simd&gt;

    namespace simd_abi
{

    template &lt;int N&gt;

    struct fixed_size {
    };
}</code></pre> 
The simd_abi::fixed_size&lt;N&gt; tag type ensures data-parallel types to store and manipulate N elements (i.e. simd&lt;T, simd_abi::fixed_size&lt;N&gt;&gt;::size() returns N). An implementation shall support at least all N ∈ [1 … 32]. Additionally, for every supported simd&lt;T, Abi&gt;, where Abi is an implementation-defined ABI tag, N = simd&lt;T, Abi&gt;::size() shall be supported. 

<h2>Notes</h2>

An implementation may choose to forego ABI compatibility between differently compiled translation units for simd and simd_mask instantiations using the same simd_abi::fixed_size&lt;N&gt; tag. Otherwise, the efficiency of simd&lt;T, Abi&gt; is likely to be better than simd&lt;T, fixed_size&lt;simd_size_v&lt;T, Abi&gt;&gt;&gt; (with Abi not an instance of simd_abi::fixed_size). 

<h2>See also</h2>


