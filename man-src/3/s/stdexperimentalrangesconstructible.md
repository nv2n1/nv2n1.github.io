---
title: "stdexperimentalrangesconstructible(3)"
name: "stdexperimentalrangesconstructible"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangesconstructible/"
---

std::experimental::ranges::Constructible - std::experimental::ranges::Constructible

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;experimental/ranges/concepts&gt;

template &lt; class T, class... Args &gt;

concept bool Constructible =                                  (ranges TS)

Destructible&lt;T&gt; &amp;&amp; std::is_constructible&lt;T, Args...&gt;::value;</code></pre> 
The Constructible concept specifies that a variable of type T can be initialized with the given set of argument types Args.... 
There need not be any subsumption relationship between Constructible&lt;T, Args...&gt; and std::is_constructible&lt;T, Args...&gt;::value. 

<h2>See also</h2>

is_constructible 
is_trivially_constructible 
is_nothrow_constructible checks if a type has a constructor for specific arguments 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
