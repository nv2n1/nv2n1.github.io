---
title: "stdfunctionassign(3)"
name: "stdfunctionassign"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfunctionassign/"
---

std::function&lt;R(Args...)&gt;::assign - std::function&lt;R(Args...)&gt;::assign

<h2>Synopsis</h2>

template&lt; class F, class Alloc &gt; <i>(since C++11)</i> 
void assign( F&amp;&amp; f, const Alloc&amp; alloc ); (removed in C++17) 
Initializes the target with f. alloc is used to allocate memory for any internal data structures that the function might use. 
Equivalent to function(allocator_arg, alloc, std::forward&lt;F&gt;(f)).swap(*this) 

<h2>Parameters</h2>

f - callable function to initialize the target with 
alloc - allocator to use to allocate memory for the internal data structures

<h2>Return value</h2>

<i>(none)</i> 

<h2>Exceptions</h2>

<i>(none)</i>

<h2>See also</h2>

<pre><code>assigns a new target

operator= (public member function)




</code></pre>
