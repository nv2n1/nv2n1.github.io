---
title: "stdshared_mutexunlock_shared(3)"
name: "stdshared_mutexunlock_shared"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdshared_mutexunlock_shared/"
---

std::shared_mutex::unlock_shared - std::shared_mutex::unlock_shared

<h2>Synopsis</h2>

<pre><code>void unlock_shared();
(since C++ 17)</code></pre> 
Releases the mutex from shared ownership by the calling thread. 
The mutex must be locked by the current thread of execution in shared mode, otherwise, the behavior is undefined. 
This operation synchronizes-with (as defined in std::memory_order) any subsequent lock() operation that obtains ownership of the same mutex. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

<i>(none)</i> 

<h2>Exceptions</h2>

<i>(none)</i>

<h2>Notes</h2>

unlock_shared() is usually not called directly: std::shared_lock is used to manage shared locking. 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;locks the mutex for shared ownership, blocks if the mutex is not available 
lock_shared <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unlocks the mutex 
unlock <i>(public member function)</i> 
