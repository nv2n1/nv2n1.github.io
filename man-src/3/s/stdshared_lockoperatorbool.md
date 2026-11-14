---
title: "stdshared_lockoperatorbool(3)"
name: "stdshared_lockoperatorbool"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdshared_lockoperatorbool/"
---

std::shared_lock&lt;Mutex&gt;::operatorbool - std::shared_lock&lt;Mutex&gt;::operatorbool

<h2>Synopsis</h2>

explicit operator bool() const noexcept; <i>(since C++14)</i> 
Checks whether *this owns a locked mutex or not. Effectively calls owns_lock(). 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

true if *this has an associated mutex and has acquired shared ownership of it, false otherwise. 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tests whether the lock owns its associated mutex 
owns_lock <i>(public member function)</i> 
