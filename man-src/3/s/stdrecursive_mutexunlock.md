---
title: "stdrecursive_mutexunlock(3)"
name: "stdrecursive_mutexunlock"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdrecursive_mutexunlock/"
---

std::recursive_mutex::unlock - std::recursive_mutex::unlock

<h2>Synopsis</h2>

<pre><code>void unlock();
(since C++ 11)</code></pre> 
Unlocks the mutex if its level of ownership is 1 (there was exactly one more call to lock() than there were calls to unlock() made by this thread), reduces the level of ownership by 1 otherwise. 
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
