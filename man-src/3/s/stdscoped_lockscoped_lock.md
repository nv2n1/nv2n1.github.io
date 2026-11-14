---
title: "stdscoped_lockscoped_lock(3)"
name: "stdscoped_lockscoped_lock"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdscoped_lockscoped_lock/"
---

std::scoped_lock&lt;MutexTypes...&gt;::~scoped_lock - std::scoped_lock&lt;MutexTypes...&gt;::~scoped_lock

<h2>Synopsis</h2>

~scoped_lock(); <i>(since C++17)</i> 
Releases the ownership of the owned mutexes. 
Effectively calls unlock() on every mutex from the pack of mutexes passed to the scoped_lock's constructor. 
