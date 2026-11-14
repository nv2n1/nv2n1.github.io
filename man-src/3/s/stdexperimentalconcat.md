---
title: "stdexperimentalconcat(3)"
name: "stdexperimentalconcat"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalconcat/"
---

std::experimental::concat - std::experimental::concat

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;experimental / simd&gt;

    template &lt;class T, class... Abis&gt;

    simd&lt;T, simd_abi::deduce_t&lt;T, (simd_size_v&lt;T, Abis&gt; + ...)&gt;&gt;(1)

        concat(const simd&lt;T, Abis&gt; &amp;...vs);

template &lt;class T, class... Abis&gt;

simd_mask&lt;T, simd_abi::deduce_t&lt;T, (simd_size_v&lt;T, Abis&gt; + ...)&gt;&gt;(2)

    concat(const simd_mask&lt;T, Abis&gt; &amp;...vs);</code></pre> 
Concatenates the input simd or simd_mask objects. 
Parameter 
vs - the input simd or simd_mask parameter pack 

<h2>Return value</h2>

The concatenated result of a single simd or simd_mask object. 

<h2>Example</h2>


