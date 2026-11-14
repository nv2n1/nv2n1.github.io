---
title: "stdshared_mutextry_lock_shared(3)"
name: "stdshared_mutextry_lock_shared"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdshared_mutextry_lock_shared/"
---

std::shared_mutex::try_lock_shared - std::shared_mutex::try_lock_shared

<h2>Synopsis</h2>

bool try_lock_shared(); <i>(since C++17)</i> 
Tries to lock the mutex in shared mode. Returns immediately. On successful lock acquisition returns true, otherwise returns false. 
This function is allowed to fail spuriously and return false even if the mutex is not currenly exclusively locked by any other thread. 
Prior unlock() operation on the same mutex synchronizes-with (as defined in std::memory_order) this operation if it returns true. 
The behavior is undefined if the calling thread already owns the mutex in any mode. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

true if the lock was acquired successfully, otherwise false. 

<h2>Exceptions</h2>

<i>(none)</i>

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
