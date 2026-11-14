---
title: "stdshared_lockunlock(3)"
name: "stdshared_lockunlock"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdshared_lockunlock/"
---

std::shared_lock&lt;Mutex&gt;::unlock - std::shared_lock&lt;Mutex&gt;::unlock

<h2>Synopsis</h2>

<pre><code>void unlock();
(since C++ 14)</code></pre> 
Unlocks the associated mutex from shared mode. Effectively calls mutex()-&gt;unlock_shared() 
std::system_error is thrown if there is no associated mutex or if the mutex is not locked. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

<i>(none)</i> 

<h2>Exceptions</h2>

* Any exceptions thrown by mutex()-&gt;unlock_shared() 

 

 
* If there is no associated mutex, std::system_error with an error code of std::errc::operation_not_permitted

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;locks the associated mutex 
lock <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;disassociates the mutex without unlocking 
release <i>(public member function)</i> 
