---
title: "stdoptionalswap(3)"
name: "stdoptionalswap"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdoptionalswap/"
---

std::optional&lt;T&gt;::swap - std::optional&lt;T&gt;::swap

<h2>Synopsis</h2>

<pre><code>void swap(optional &amp;other) noexcept(/* see below */);
(since C++ 17)</code></pre> 
Swaps the contents with those of other. 
* If neither *this nor other contain a value, the function has no effect. 
* If only one of *this and other contains a value (let's call this object in and the other un), the contained value of un is direct-initialized from std::move(*in), followed by destruction of the contained value of in as if by in-&gt;T::~T(). After this call, in does not contain a value; un contains a value. 
* If both *this and other contain values, the contained values are exchanged by calling using std::swap; swap(**this, *other). T lvalues must satisfy Swappable. 

<h2>Parameters</h2>

other - the optional object to exchange the contents with

<h2>Return value</h2>

<i>(none)</i> 

<h2>Exceptions</h2>

noexcept specification: 
noexcept(std::is_nothrow_move_constructible_v&lt;T&gt; &amp;&amp; 
std::is_nothrow_swappable_v&lt;T&gt;) 
In the case of thrown exception, the states of the contained values of *this and other are determined by the exception safety guarantees of swap of type T or T's move constructor, whichever is called. For both *this and other, if the object contained a value, it is left containing a value, and the other way round.

<h2>See also</h2>

std::swap(std::optional) specializes the std::swap algorithm 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++17)</i> 
