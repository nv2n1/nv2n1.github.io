---
title: "stdshared_timed_mutexlock_shared(3)"
name: "stdshared_timed_mutexlock_shared"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdshared_timed_mutexlock_shared/"
---

std::shared_timed_mutex::lock_shared - std::shared_timed_mutex::lock_shared

<h2>Synopsis</h2>

<pre><code>void lock_shared();
(since C++ 14)</code></pre> 
Acquires shared ownership of the mutex. If another thread is holding the mutex in exclusive ownership, a call to lock_shared will block execution until shared ownership can be acquired. 
If lock_shared is called by a thread that already owns the mutex in any mode (exclusive or shared), the behavior is undefined. 
If more than the implementation-defined maximum number of shared owners already locked the mutex in shared mode, lock_shared blocks execution until the number of shared owners is reduced. The maximum number of owners is guaranteed to be at least 10000. 
Prior unlock() operation on the same mutex synchronizes-with (as defined in std::memory_order) this operation. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

<i>(none)</i> 

<h2>Exceptions</h2>

Throws std::system_error when errors occur, including errors from the underlying operating system that would prevent lock from meeting its specifications. The mutex is not locked in the case of any exception being thrown.

<h2>Notes</h2>

lock_shared() is usually not called directly: std::shared_lock is used to manage shared locking. 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;locks the mutex, blocks if the mutex is not available 
lock <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tries to lock the mutex for shared ownership, returns if the mutex is not available 
try_lock_shared <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unlocks the mutex (shared ownership) 
unlock_shared <i>(public member function)</i> 
