---
title: "stdexperimentalrangesintegral(3)"
name: "stdexperimentalrangesintegral"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangesintegral/"
---

std::experimental::ranges::Integral - std::experimental::ranges::Integral

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;experimental/ranges/concepts&gt;

template &lt; class T &gt;                                 (ranges TS)

concept bool Integral = std::is_integral&lt;T&gt;::value;</code></pre> 
The concept Integral&lt;T&gt; is satisfied if and only if T is an integral type. 
There need not be any subsumption relationship between Integral&lt;T&gt; and std::is_integral&lt;T&gt;::value. 

<h2>See also</h2>

is_integral checks if a type is an integral type 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
