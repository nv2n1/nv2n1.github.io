---
title: "stdstack(3)"
name: "stdstack"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdstack/"
---

std::stack&lt;T,Container&gt;::~stack - std::stack&lt;T,Container&gt;::~stack

<h2>Synopsis</h2>

<pre><code>~stack();</code></pre> 
Destructs the container adaptor. The destructors of the elements are called and the used storage is deallocated. Note, that if the elements are pointers, the pointed-to objects are not destroyed. 

<h2>Complexity</h2>

Linear in the size of the container adaptor.
