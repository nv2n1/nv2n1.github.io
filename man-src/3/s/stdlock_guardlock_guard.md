---
title: "stdlock_guardlock_guard(3)"
name: "stdlock_guardlock_guard"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdlock_guardlock_guard/"
---

std::lock_guard&lt;Mutex&gt;::~lock_guard - std::lock_guard&lt;Mutex&gt;::~lock_guard

<h2>Synopsis</h2>

~lock_guard(); <i>(since C++11)</i> 
Releases the ownership of the owned mutex. 
Effectively calls m.unlock() where m is the mutex passed to the lock_guard's constructor. 
