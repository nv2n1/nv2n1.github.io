---
title: "stdexperimentalsimd_abimax_fixed_size(3)"
name: "stdexperimentalsimd_abimax_fixed_size"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalsimd_abimax_fixed_size/"
---

std::experimental::simd_abi::max_fixed_size - std::experimental::simd_abi::max_fixed_size

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;experimental / simd&gt;

    namespace simd_abi
{

    template &lt;class T&gt;

    inline constexpr int max_fixed_size = /*implementation-defined*/;
}</code></pre> 
The value of max_fixed_size&lt;T&gt; declares that an instance of simd&lt;T, fixed_size&lt;N&gt;&gt; with N &lt;= max_fixed_size&lt;T&gt; is supported by the implementation. 

<h2>Notes</h2>

It is unspecified whether an implementation supports simd&lt;T, fixed_size&lt;N&gt;&gt; with N &gt; max_fixed_size&lt;T&gt;. The value of max_fixed_size&lt;T&gt; may depend on compiler flags and may change between different compiler versions. 
