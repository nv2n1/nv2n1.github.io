---
title: "stdshared_mutexunlock(3)"
name: "stdshared_mutexunlock"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdshared_mutexunlock/"
---

std::shared_mutex::unlock - std::shared_mutex::unlock

<h2>Synopsis</h2>

<pre><code>void unlock();
(since C++ 17)</code></pre> 
Unlocks the mutex. 
The mutex must be locked by the current thread of execution, otherwise, the behavior is undefined. 
This operation synchronizes-with (as defined in std::memory_order) any subsequent lock operation that obtains ownership of the same mutex. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

<i>(none)</i> 

<h2>Exceptions</h2>

<i>(none)</i>

<h2>Notes</h2>

unlock() is usually not called directly: std::unique_lock and std::lock_guard are used to manage exclusive locking. 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;locks the mutex, blocks if the mutex is not available 
lock <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tries to lock the mutex, returns if the mutex is not available 
try_lock <i>(public member function)</i> 
