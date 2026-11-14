---
title: "stdtuple_sizestdspan(3)"
name: "stdtuple_sizestdspan"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdtuple_sizestdspan/"
description: "std::tuple_size(std::span) – std::tuple_size(std::span)"
---

<p>std::tuple_size(std::span) &#8211; std::tuple_size(std::span)</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;span&gt;<br />
template&lt; class T, std::size_t N &gt;<br />
class tuple_size&lt; std::span&lt;T, N&gt; &gt; : <code>(1)</code> <i>(since C++20)</i><br />
public std::integral_constant&lt;std::size_t, N&gt;<br />
{ };<br />
template&lt; class T &gt; <code>(2)</code> <i>(since C++20)</i><br />
class tuple_size&lt; std::span&lt;T, std::dynamic_extent&gt; &gt;; // Not defined<br />
Provides access to the number of elements in a static-extent span as a compile-time constant expression. If the span has dynamic extent, the tuple_size specialization is an incomplete type.<br />
Inherited from std::integral_constant </p>
<h2>Member constants</h2>
<p>value N, the number of elements in the span<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code></p>
<h2>Member functions</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;converts the object to std::size_t, returns value<br />
operator std::size_t <i>(public member function)</i> </p>
<p>operator() returns value<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public member function)</i><br />
<i>(C++14)</i></p>
<h2>Member types</h2>
<p>Type Definition<br />
value_type std::size_t<br />
type std::integral_constant&lt;std::size_t, value&gt;</p>
<h2>Example</h2>
<p>&nbsp;This section is incomplete<br />
&nbsp;Reason: no example </p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;obtains the size of tuple at compile time<br />
tuple_size <i>(class template specialization)</i> </p>
