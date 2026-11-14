---
title: "stdexperimentalsimd_mask(3)"
name: "stdexperimentalsimd_mask"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalsimd_mask/"
description: "std::experimental::simd_mask – std::experimental::simd_mask"
---

<p>std::experimental::simd_mask &#8211; std::experimental::simd_mask</p>
<h2>Synopsis</h2>
<pre><code>Defined in header &lt;experimental/simd&gt;

template&lt; class T, class Abi = simd_abi::compatible&lt;T&gt; &gt;

class simd_mask;</code></pre>
<p>The class template simd_mask is a data-parallel type with the element type bool. The width of a given simd_mask instantiation is a constant expression, determined by the template parameters. Specifically, simd_mask&lt;T, Abi&gt;::size() is always simd&lt;T, Abi&gt;::size(). </p>
<h2>Template parameters</h2>
<p>T &#8211; the element type simd_mask applies on<br />
Abi &#8211; the ABI type simd_mask applies on </p>
<p>Helper alias templates </p>
<p>Template Definition<br />
template &lt;class T, int N&gt; using fixed_size_simd_mask simd_mask&lt;T, simd_abi::fixed_size&lt;N&gt;&gt;<br />
template &lt;class T&gt; using native_simd_mask simd_mask&lt;T, simd_abi::native&gt;</p>
<h2>Member types</h2>
<p>Member type Definition<br />
value_type bool<br />
reference implementation-defined<br />
simd_type simd&lt;T, Abi&gt;<br />
abi_type Abi</p>
<h2>Member functions</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs a simd_mask object<br />
constructor <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;loads from address<br />
copy_from <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;stores to address<br />
copy_to <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;accesses specified element<br />
operator[] <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;negates each element<br />
operator! <i>(public member function)</i> </p>
<p>size returns the number of elements<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function)</i><br />
<code>[static]</code></p>
<h2>Non-member functions</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;element-wise logic operators<br />
operator&amp;&amp;_ <i>(function)</i><br />
operator|| </p>
<p>operator&amp;_ element-wise bitwise operators<br />
operator|_ <i>(function)</i><br />
operator^ </p>
<p>operator&amp;=_ element-wise compound operators<br />
operator|=_ <i>(function)</i><br />
operator^=<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;element-wise relation operators<br />
operator==_ <i>(function)</i><br />
operator!=</p>
<h2>Example</h2>
