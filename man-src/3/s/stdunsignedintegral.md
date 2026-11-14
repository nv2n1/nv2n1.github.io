---
title: "stdunsignedintegral(3)"
name: "stdunsignedintegral"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdunsignedintegral/"
---

std::UnsignedIntegral - std::UnsignedIntegral

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;concepts&gt;

template &lt; class T &gt;                                                     (since C++20)

concept UnsignedIntegral = std::Integral&lt;T&gt; &amp;&amp; !std::SignedIntegral&lt;T&gt;;</code></pre> 
The concept UnsignedIntegral&lt;T&gt; is satisfied if and only if T is an integral type and std::is_signed_v&lt;T&gt; is false. 

<h2>Notes</h2>

UnsignedIntegral&lt;T&gt; may be satisfied by a type that is not a unsigned_integer_type, for example, bool. 

<h2>See also</h2>

is_integral checks if a type is an integral type 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
is_signed checks if a type is a signed arithmetic type 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
