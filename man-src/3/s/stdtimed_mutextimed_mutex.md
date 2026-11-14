---
title: "stdtimed_mutextimed_mutex(3)"
name: "stdtimed_mutextimed_mutex"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdtimed_mutextimed_mutex/"
---

std::timed_mutex::~timed_mutex - std::timed_mutex::~timed_mutex

<h2>Synopsis</h2>

<pre><code>~timed_mutex();</code></pre> 
Destroys the mutex. 
The behavior is undefined if the mutex is owned by any thread or if any thread terminates while holding any ownership of the mutex. 

<h2>See also</h2>


