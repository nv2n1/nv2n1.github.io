---
title: "stdunique_lockunique_lock(3)"
name: "stdunique_lockunique_lock"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdunique_lockunique_lock/"
---

std::unique_lock&lt;Mutex&gt;::~unique_lock - std::unique_lock&lt;Mutex&gt;::~unique_lock

<h2>Synopsis</h2>

~unique_lock(); <i>(since C++11)</i> 
Destroys the lock. If *this has an associated mutex and has acquired ownership of it, the mutex is unlocked. 
