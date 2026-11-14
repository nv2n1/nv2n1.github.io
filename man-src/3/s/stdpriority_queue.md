---
title: "stdpriority_queue(3)"
name: "stdpriority_queue"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdpriority_queue/"
---

std::priority_queue&lt;T,Container,Compare&gt;::~priority_queue - std::priority_queue&lt;T,Container,Compare&gt;::~priority_queue

<h2>Synopsis</h2>

<pre><code>~priority_queue();</code></pre> 
Destructs the container adaptor. The destructors of the elements are called and the used storage is deallocated. Note, that if the elements are pointers, the pointed-to objects are not destroyed. 

<h2>Complexity</h2>

Linear in the size of the container adaptor.
