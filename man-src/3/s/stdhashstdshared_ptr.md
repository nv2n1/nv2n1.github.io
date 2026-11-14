---
title: "stdhashstdshared_ptr(3)"
name: "stdhashstdshared_ptr"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdhashstdshared_ptr/"
---

std::hash(std::shared_ptr) - std::hash(std::shared_ptr)

<h2>Synopsis</h2>

template&lt;class T&gt; struct hash&lt;shared_ptr&lt;T&gt;&gt;; <i>(since C++11)</i> 
The template specialization of std::hash for std::shared_ptr&lt;T&gt; allows users to obtain hashes of objects of type std::shared_ptr&lt;T&gt;. 
For a given std::shared_ptr&lt;T&gt; p, this specialization ensures that 
std::hash&lt;std::shared_ptr&lt;T&gt;&gt;()(p) == std::hash&lt;T*&gt;()(p.get()). <i>(until C++17)</i> 
std::hash&lt;std::shared_ptr&lt;T&gt;&gt;()(p) == std::hash&lt;typename std::shared_ptr&lt;T&gt;::element_type*&gt;()(p.get()). <i>(since C++17)</i> 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

hash hash function object 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
