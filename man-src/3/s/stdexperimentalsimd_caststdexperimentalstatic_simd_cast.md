---
title: "stdexperimentalsimd_caststdexperimentalstatic_simd_cast(3)"
name: "stdexperimentalsimd_caststdexperimentalstatic_simd_cast"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalsimd_caststdexperimentalstatic_simd_cast/"
---

std::experimental::simd_cast,std::experimental::static_simd_cast - std::experimental::simd_cast,std::experimental::static_simd_cast

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;experimental / simd&gt;

    template &lt;class V, class T, class Abi&gt;
    (1)

    /*see below*/ simd_cast(const simd&lt;T, Abi&gt; &amp;v);

template &lt;class V, class T, class Abi&gt;
(2)

    /*see below*/ static_simd_cast(const simd&lt;T, Abi&gt; &amp;v);</code></pre> 
Cast a simd object to another simd object. If V is T, returns simd&lt;T, Abi&gt;; otherwise, if V is a scalar type, returns simd&lt;V, simd_abi::fixed_size&lt;simd&lt;T, Abi&gt;::size()&gt;&gt;. Otherwise, V must be a simd type, and the function returns V. 
1) This function does not participate in overloading resolution unless 
* every possible value of the input element can be represented with the output element 
* either is_simd_v&lt;V&gt; is false, or V::size() is simd&lt;T, Abi&gt;::size() 
2) This function does not participate in overloading resolution unless either is_simd_v&lt;V&gt; is false, or V::size() is simd&lt;T, Abi&gt;::size(). 

<h2>Parameters</h2>

v - the input simd object

<h2>Return value</h2>

A simd object with the i-th element initialized to static_cast&lt;To&gt;(v[i]), where To is the output element type as specified. 

<h2>Example</h2>


