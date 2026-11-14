---
title: "stdshared_timed_mutexshared_timed_mutex(3)"
name: "stdshared_timed_mutexshared_timed_mutex"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdshared_timed_mutexshared_timed_mutex/"
---

std::shared_timed_mutex::~shared_timed_mutex - std::shared_timed_mutex::~shared_timed_mutex

<h2>Synopsis</h2>

<pre><code>~shared_timed_mutex();</code></pre> 
Destroys the mutex. 
The behavior is undefined if the mutex is owned by any thread or if any thread terminates while holding any ownership of the mutex. 

<h2>See also</h2>


