---
title: "stdshared_locktry_lock(3)"
name: "stdshared_locktry_lock"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdshared_locktry_lock/"
---

std::shared_lock&lt;Mutex&gt;::try_lock - std::shared_lock&lt;Mutex&gt;::try_lock

<h2>Synopsis</h2>

bool try_lock(); <i>(since C++14)</i> 
Tries to lock the associated mutex in shared mode without blocking. Effectively calls mutex()-&gt;try_lock_shared(). 
std::system_error is thrown if there is no associated mutex or if the mutex is already locked. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

true if the ownership of the mutex has been acquired successfully, false otherwise. 

<h2>Exceptions</h2>

* Any exceptions thrown by mutex()-&gt;try_lock_shared() 

 

 
* If there is no associated mutex, std::system_error with an error code of std::errc::operation_not_permitted 

 

 
* If the mutex is already locked, std::system_error with an error code of std::errc::resource_deadlock_would_occur

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tries to lock the associated mutex 
try_lock <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;locks the associated mutex 
lock <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tries to lock the associated mutex, for the specified duration 
try_lock_for <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tries to lock the associated mutex, until a specified time point 
try_lock_until <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unlocks the associated mutex 
unlock <i>(public member function)</i> 
