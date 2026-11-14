---
title: "stdexperimentalfunctionswap(3)"
name: "stdexperimentalfunctionswap"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalfunctionswap/"
---

std::experimental::function&lt;R(Args...)&gt;::swap - std::experimental::function&lt;R(Args...)&gt;::swap

<h2>Synopsis</h2>

<pre><code>void swap(function &amp;other);
(library fundamentals TS)</code></pre> 
Exchanges the stored callable objects of *this and other. 
The allocators of *this and other are not exchanged. 
The behavior is undefined if *this-&gt;get_memory_resource() != *other.get_memory_resource(). 

<h2>Parameters</h2>

other - function wrapper to exchange the stored callable object with

<h2>Return value</h2>

<i>(none)</i> 
