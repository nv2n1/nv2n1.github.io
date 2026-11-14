---
title: "stdshared_mutexshared_mutex(3)"
name: "stdshared_mutexshared_mutex"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdshared_mutexshared_mutex/"
---

std::shared_mutex::~shared_mutex - std::shared_mutex::~shared_mutex

<h2>Synopsis</h2>

<pre><code>~shared_mutex();</code></pre> 
Destroys the mutex. 
The behavior is undefined if the mutex is owned by any thread or if any thread terminates while holding any ownership of the mutex. 

<h2>See also</h2>


