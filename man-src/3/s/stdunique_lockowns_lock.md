---
title: "stdunique_lockowns_lock(3)"
name: "stdunique_lockowns_lock"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdunique_lockowns_lock/"
---

std::unique_lock&lt;Mutex&gt;::owns_lock - std::unique_lock&lt;Mutex&gt;::owns_lock

<h2>Synopsis</h2>

bool owns_lock() const noexcept; <i>(since C++11)</i> 
Checks whether *this owns a locked mutex or not. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

true if *this has an associated mutex and has acquired ownership of it, false otherwise. 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tests whether the lock owns its associated mutex 
operator_bool <i>(public member function)</i> 
