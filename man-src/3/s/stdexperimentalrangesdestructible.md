---
title: "stdexperimentalrangesdestructible(3)"
name: "stdexperimentalrangesdestructible"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangesdestructible/"
---

std::experimental::ranges::Destructible - std::experimental::ranges::Destructible

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;experimental/ranges/concepts&gt;

template &lt; class T &gt;                                                 (ranges TS)

concept bool Destructible = std::is_nothrow_destructible&lt;T&gt;::value;</code></pre> 
The concept Destructible specifies the concept of all types whose instances can safely be destroyed at the end of their lifetime (including reference types). 
There need not be any subsumption relationship between Destructible&lt;T&gt; and std::is_nothrow_destructible&lt;T&gt;::value. 

<h2>Notes</h2>

Unlike the Destructible named requirement in the main C++ standard, Destructible requires the destructor to be noexcept(true), not merely non-throwing when invoked, and allows reference types and array types. 

<h2>See also</h2>

is_destructible 
is_trivially_destructible 
is_nothrow_destructible checks if a type has a non-deleted destructor 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
