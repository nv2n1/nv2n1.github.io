---
title: "stdunique_lockrelease(3)"
name: "stdunique_lockrelease"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdunique_lockrelease/"
---

std::unique_lock&lt;Mutex&gt;::release - std::unique_lock&lt;Mutex&gt;::release

<h2>Synopsis</h2>

mutex_type* release() noexcept; <i>(since C++11)</i> 
Breaks the association of the associated mutex, if any, and *this. 
No locks are unlocked. If the *this held ownership of the associated mutex prior to the call, the caller is now responsible to unlock the mutex. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

Pointer to the associated mutex or NULL if there was no associated mutex. 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unlocks the associated mutex 
unlock <i>(public member function)</i> 
