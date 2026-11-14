---
title: "stdshared_lockshared_lock(3)"
name: "stdshared_lockshared_lock"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdshared_lockshared_lock/"
---

std::shared_lock&lt;Mutex&gt;::~shared_lock - std::shared_lock&lt;Mutex&gt;::~shared_lock

<h2>Synopsis</h2>

~shared_lock(); <i>(since C++14)</i> 
Destroys the lock. 
If *this has an associated mutex ((mutex() returns a non-null pointer) and has acquired ownership of it (owns() returns true), the mutex is unlocked by calling unlock_shared(). 
