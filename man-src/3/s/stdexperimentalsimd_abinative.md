---
title: "stdexperimentalsimd_abinative(3)"
name: "stdexperimentalsimd_abinative"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalsimd_abinative/"
---

std::experimental::simd_abi::native - std::experimental::simd_abi::native

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;experimental/simd&gt;

namespace simd_abi {

    template &lt; class T &gt;

    using native = /*implementation-defined*/;

}</code></pre> 
native&lt;T&gt; is an implementation-defined alias for an ABI tag. 

<h2>Notes</h2>

The intent is to use the ABI tag producing the most efficient data-parallel execution for the element type T that is supported on the currently targeted system. For target architectures without ISA extensions, the native&lt;T&gt; and compatible&lt;T&gt; aliases will likely be the same. For target architectures with ISA extensions, compiler flags may influence the native&lt;T&gt; alias while compatible&lt;T&gt; will be the same independent of such flags. 

<h2>See also</h2>


