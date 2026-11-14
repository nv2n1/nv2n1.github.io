---
title: "stdunique_lockoperatorbool(3)"
name: "stdunique_lockoperatorbool"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdunique_lockoperatorbool/"
---

std::unique_lock&lt;Mutex&gt;::operatorbool - std::unique_lock&lt;Mutex&gt;::operatorbool

<h2>Synopsis</h2>

explicit operator bool() const noexcept; <i>(since C++11)</i> 
Checks whether *this owns a locked mutex or not. Effectively calls owns_lock(). 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

true if *this has an associated mutex and has acquired ownership of it, false otherwise. 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tests whether the lock owns its associated mutex 
owns_lock <i>(public member function)</i> 
