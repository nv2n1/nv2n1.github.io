---
title: "stdexperimentalsimd(3)"
name: "stdexperimentalsimd"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalsimd/"
description: "std::experimental::simd – std::experimental::simd"
---

<p>std::experimental::simd &#8211; std::experimental::simd</p>
<h2>Synopsis</h2>
<pre><code>Defined in header &lt;experimental/simd&gt;

template&lt; class T, class Abi = simd_abi::compatible&lt;T&gt; &gt;

class simd;</code></pre>
<p>The class template simd is a data-parallel type. The width of a given simd instantiation is a constant expression, determined by the template parameters.<br />
An ABI tag is a type in the simd_abi namespace that indicates a choice of size and binary representation for objects of data-parallel type. </p>
<h2>Template parameters</h2>
<p>T &#8211; element type<br />
Abi &#8211; tag type used to determine the number of elements and storage </p>
<p>Helper alias templates </p>
<p>template&lt; class T, int N &gt;<br />
using fixed_size_simd = std::experimental::simd&lt;T, std::experimental::simd_abi::fixed_size&lt;N&gt;&gt;;<br />
template&lt; class T, int N &gt;<br />
using native_simd = std::experimental::simd&lt;T, std::experimental::simd_abi::native&gt;;</p>
<h2>Member types</h2>
<p>Member type Definition<br />
value_type T<br />
reference implementation-defined<br />
mask_type simd_mask&lt;T, Abi&gt;<br />
abi_type Abi</p>
<h2>Member functions</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs a simd object<br />
constructor <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;loads from address<br />
copy_from <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;stores to address<br />
copy_to <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;accesses specified element<br />
operator[] <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;element-wise increment and decrement<br />
operator++_ <i>(public member function)</i><br />
operator&#8211; </p>
<p>operator!_ element-wise unary operators<br />
operator~_ <i>(public member function)</i><br />
operator+_<br />
operator- </p>
<p>size returns the number of elements<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function)</i><br />
<code>[static]</code></p>
<h2>Non-member functions</h2>
<p>operator+_<br />
operator-_<br />
operator*_<br />
operator/_<br />
operator%_ element-wise binary operators<br />
operator&amp;_ <i>(function)</i><br />
operator|_<br />
operator^_<br />
operator&lt;&lt;_<br />
operator&gt;&gt;_<br />
operator&lt;&lt;_<br />
operator&gt;&gt; </p>
<p>operator+=_<br />
operator-=_<br />
operator*=_<br />
operator/=_<br />
operator%=_ element-wise compound binary operators<br />
operator&amp;=_ <i>(function)</i><br />
operator|=_<br />
operator^=_<br />
operator&lt;&lt;=_<br />
operator&gt;&gt;=_<br />
operator&lt;&lt;=_<br />
operator&gt;&gt;= </p>
<p>operator==_<br />
operator!=_ element-wise relational operators<br />
operator&gt;=_ <i>(function)</i><br />
operator&lt;=_<br />
operator&gt;_<br />
operator&lt;</p>
<h2>Example</h2>
