---
title: "stdexperimentalwhere(3)"
name: "stdexperimentalwhere"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalwhere/"
---

std::experimental::where - std::experimental::where

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;experimental / simd&gt;

    template &lt;class T, class Abi&gt;

    where_expression&lt;simd_mask&lt;T, Abi&gt;, simd&lt;T, Abi&gt;&gt;(1)

        where(const typename simd&lt;T, Abi&gt;::mask_type &amp;mask,

              simd&lt;T, Abi&gt; &amp;value) noexcept;

template &lt;class T, class Abi&gt;

const_where_expression&lt;simd_mask&lt;T, Abi&gt;, const simd&lt;T, Abi&gt;&gt;(2)

    where(const typename simd&lt;T, Abi&gt;::mask_type &amp;mask,

          const simd&lt;T, Abi&gt; &amp;value) noexcept;

template &lt;class T, class Abi&gt;

where_expression&lt;simd_mask&lt;T, Abi&gt;, simd_mask&lt;T, Abi&gt;&gt;(3)

    where(const nodeduce_t&lt;simd_mask&lt;T, Abi&gt;&gt; &amp;mask,

          simd_mask&lt;T, Abi&gt; &amp;value) noexcept;

template &lt;class T, class Abi&gt;

const_where_expression&lt;simd_mask&lt;T, Abi&gt;, const simd_mask&lt;T, Abi&gt;&gt;(4)

    where(const nodeduce_t&lt;simd_mask&lt;T, Abi&gt;&gt; &amp;mask,

          const simd_mask&lt;T, Abi&gt; &amp;value) noexcept;

template &lt;class T&gt;

where_expression&lt;bool, T&gt;(5)

    where(/*see below*/ mask, T &amp;value) noexcept;

template &lt;class T&gt;

const_where_expression&lt;bool, const T&gt;(6)

    where(/*see below*/ mask, const T &amp;value) noexcept;</code></pre> 
Constructs a new const_where_expression or where_expression. 
1-6) constructs a where_expression from given mask and value parameters. 

<h2>Parameters</h2>

1-4) 

 
mask - the simd_mask object 
value - reference to the object that mask applies on 

 
5-6) 

 
mask - the mask of type bool 
value - reference to the scalar that mask applies on

<h2>Return value</h2>

The constructed const_where_expression or where_expression. 

<h2>Notes</h2>

5-6) uses implementation defined type of mask, so that implicit conversions from other types to bool is disabled. 

<h2>Example</h2>


