---
title: "stdshared_lockowns_lock(3)"
name: "stdshared_lockowns_lock"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdshared_lockowns_lock/"
---

std::shared_lock&lt;Mutex&gt;::owns_lock - std::shared_lock&lt;Mutex&gt;::owns_lock

<h2>Synopsis</h2>

bool owns_lock() const noexcept; <i>(since C++14)</i> 
Checks whether *this owns a locked mutex or not. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

true if *this has an associated mutex and has acquired shared ownership of it, false otherwise. 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tests whether the lock owns its associated mutex 
operator_bool <i>(public member function)</i> 
