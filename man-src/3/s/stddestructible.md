---
title: "stddestructible(3)"
name: "stddestructible"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stddestructible/"
---

std::Destructible - std::Destructible

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;concepts&gt;

template &lt; class T &gt;                                       (since C++20)

concept Destructible = std::is_nothrow_destructible_v&lt;T&gt;;</code></pre> 
The concept Destructible specifies the concept of all types whose instances can safely be destroyed at the end of their lifetime (including reference types). 

<h2>Notes</h2>

Unlike the Destructible named requirement, std::Destructible requires the destructor to be noexcept(true), not merely non-throwing when invoked, and allows reference types and array types. 

<h2>See also</h2>

is_destructible 
is_trivially_destructible 
is_nothrow_destructible checks if a type has a non-deleted destructor 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
