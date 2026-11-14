---
title: "stdhashstdexperimentalshared_ptr(3)"
name: "stdhashstdexperimentalshared_ptr"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdhashstdexperimentalshared_ptr/"
---

std::hash(std::experimental::shared_ptr) - std::hash(std::experimental::shared_ptr)

<h2>Synopsis</h2>

template&lt;class T&gt; struct hash&lt;std::experimental::shared_ptr&lt;T&gt;&gt;; (library fundamentals TS) 
The template specialization of std::hash for std::experimental::shared_ptr&lt;T&gt; allows users to obtain hashes of objects of type std::experimental::shared_ptr&lt;T&gt;. 
For a given std::experimental::shared_ptr&lt;T&gt; p, this specialization ensures that std::hash&lt;std::experimental::shared_ptr&lt;T&gt;&gt;()(p) == std::hash&lt;T*&gt;()(p.get()). 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

hash hash function object 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
