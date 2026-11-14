---
title: "stdexperimentalconst_where_expression(3)"
name: "stdexperimentalconst_where_expression"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalconst_where_expression/"
---

std::experimental::const_where_expression - std::experimental::const_where_expression

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;experimental/simd&gt;

template &lt; class M, class V &gt;

class const_where_expression;</code></pre> 
The class template const_where_expression abstracts the notion of selected elements of a given const object of arithmetic or data-parallel type. Selected elements signifies the elements data[i] for all i ∈ {j ∈ ℕ0 | j &lt; M::size() ⋀ mask[j]}. 

<h2>Template parameters</h2>

M - The mask type 
V - The value type M applies on 

 
Valid combinations of (M, V) are: (simd_mask&lt;T, Abi&gt;, const simd&lt;T, Abi&gt;), (simd_mask&lt;T, Abi&gt;, const simd_mask&lt;T, Abi&gt;), (bool, const T).

<h2>Member functions</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;negates selected elements 
operator- <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;stores selected elements to address 
copy_to <i>(public member function)</i>

<h2>Example</h2>


