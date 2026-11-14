---
title: "stdsignedintegral(3)"
name: "stdsignedintegral"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdsignedintegral/"
---

std::SignedIntegral - std::SignedIntegral

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;concepts&gt;

template &lt; class T &gt;                                               (since C++20)

concept SignedIntegral = std::Integral&lt;T&gt; &amp;&amp; std::is_signed_v&lt;T&gt;;</code></pre> 
The concept SignedIntegral&lt;T&gt; is satisfied if and only if T is an integral type and std::is_signed_v&lt;T&gt; is true. 

<h2>Notes</h2>

SignedIntegral&lt;T&gt; may be satisfied by a type that is not a signed_integer_type, for example, char (on a system where char is signed). 

<h2>See also</h2>

is_integral checks if a type is an integral type 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
is_signed checks if a type is a signed arithmetic type 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
