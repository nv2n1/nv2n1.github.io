---
title: "stdconstructible(3)"
name: "stdconstructible"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdconstructible/"
---

std::Constructible - std::Constructible

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;concepts&gt;

template &lt; class T, class... Args &gt;

concept Constructible =                                       (since C++20)

std::Destructible&lt;T&gt; &amp;&amp; std::is_constructible_v&lt;T, Args...&gt;;</code></pre> 
The Constructible concept specifies that a variable of type T can be initialized with the given set of argument types Args.... 

<h2>See also</h2>

is_constructible 
is_trivially_constructible 
is_nothrow_constructible checks if a type has a constructor for specific arguments 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
