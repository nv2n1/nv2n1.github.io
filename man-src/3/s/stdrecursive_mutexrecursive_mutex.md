---
title: "stdrecursive_mutexrecursive_mutex(3)"
name: "stdrecursive_mutexrecursive_mutex"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdrecursive_mutexrecursive_mutex/"
---

std::recursive_mutex::~recursive_mutex - std::recursive_mutex::~recursive_mutex

<h2>Synopsis</h2>

<pre><code>~recursive_mutex();</code></pre> 
Destroys the mutex. 
The behavior is undefined if the mutex is owned by any thread or if any thread terminates while holding any ownership of the mutex. 

<h2>See also</h2>


