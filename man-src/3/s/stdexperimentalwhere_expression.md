---
title: "stdexperimentalwhere_expression(3)"
name: "stdexperimentalwhere_expression"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalwhere_expression/"
---

std::experimental::where_expression - std::experimental::where_expression

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;experimental/simd&gt;

template &lt; class M, class V &gt;

class where_expression;</code></pre> 
The class template where_expression abstracts the notion of selected elements of a given non-const object of arithmetic or data-parallel type. Selected elements signifies the elements data[i] for all i ∈ {j ∈ ℕ0 | j &lt; M::size() ⋀ mask[j]}. 

<h2>Template parameters</h2>

M - The mask type 
V - The value type M applies on 

 
Valid combinations of (M, V) are: (simd_mask&lt;T, Abi&gt;, simd&lt;T, Abi&gt;), (simd_mask&lt;T, Abi&gt;, simd_mask&lt;T, Abi&gt;), (bool, T).

<h2>Member functions</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;assigns to selected positions 
operator= <i>(public member function)</i> 

 
operator+=_ 
operator-=_ 
operator*=_ 
operator/=_ compound operators 
operator%=_ <i>(public member function)</i> 
operator&amp;=_ 
operator|=_ 
operator^=_ 
operator&lt;&lt;=_ 
operator&gt;&gt;= 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;increment and decrement operators 
operator++_ <i>(public member function)</i> 
operator-- 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;loads from address to selected positions 
copy_from <i>(public member function)</i>

<h2>Example</h2>


