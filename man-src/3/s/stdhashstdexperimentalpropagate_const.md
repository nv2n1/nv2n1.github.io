---
title: "stdhashstdexperimentalpropagate_const(3)"
name: "stdhashstdexperimentalpropagate_const"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdhashstdexperimentalpropagate_const/"
---

std::hash(std::experimental::propagate_const) - std::hash(std::experimental::propagate_const)

<h2>Synopsis</h2>

Defined in header &lt;experimental/propagate_const&gt; 
template&lt;class T&gt; struct hash&lt;std::experimental::propagate_const&lt;T&gt;&gt;; (library fundamentals TS v2) 
The template specialization of std::hash for std::experimental::propagate_const&lt;T&gt; allows users to obtain hashes of objects of type std::experimental::propagate_const&lt;T&gt;. 
For a given std::experimental::propagate_const&lt;T&gt; p, this specialization ensures that std::hash&lt;std::experimental::propagate_const&lt;T&gt;&gt;()(p) == std::hash&lt;T&gt;()(p.t_), where p.t_ is the pointer-like object wrapped by p. 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

hash hash function object 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
