---
title: "stdmutexmutex(3)"
name: "stdmutexmutex"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdmutexmutex/"
---

std::mutex::~mutex - std::mutex::~mutex

<h2>Synopsis</h2>

<pre><code>~mutex();</code></pre> 
Destroys the mutex. 
The behavior is undefined if the mutex is owned by any thread or if any thread terminates while holding any ownership of the mutex. 

<h2>See also</h2>


