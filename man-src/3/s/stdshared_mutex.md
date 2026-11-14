---
title: "stdshared_mutex(3)"
name: "stdshared_mutex"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdshared_mutex/"
---

std::shared_mutex - std::shared_mutex

<h2>Synopsis</h2>

Defined in header &lt;shared_mutex&gt; 
class shared_mutex; <i>(since C++17)</i> 
The shared_mutex class is a synchronization primitive that can be used to protect shared data from being simultaneously accessed by multiple threads. In contrast to other mutex types which facilitate exclusive access, a shared_mutex has two levels of access: 
* shared - several threads can share ownership of the same mutex. 
* exclusive - only one thread can own the mutex. 
Shared mutexes are usually used in situations when multiple readers can access the same resource at the same time without causing data races, but only one writer can do so. 
The shared_mutex class satisfies all requirements of SharedMutex and StandardLayoutType. 

<h2>Member types</h2>

Member type Definition 
native_handle_type(optional) implementation-defined

<h2>Member functions</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs the mutex 
constructor <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;destroys the mutex 
destructor <i>(public member function)</i> 

 
operator= not copy-assignable 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public member function)</i> 
[deleted] 

 
&nbsp;Exclusive locking 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;locks the mutex, blocks if the mutex is not available 
lock <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tries to lock the mutex, returns if the mutex is not available 
try_lock <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unlocks the mutex 
unlock <i>(public member function)</i>

<h2>Shared locking</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;locks the mutex for shared ownership, blocks if the mutex is not available 
lock_shared <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tries to lock the mutex for shared ownership, returns if the mutex is not available 
try_lock_shared <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unlocks the mutex (shared ownership) 
unlock_shared <i>(public member function)</i>

<h2>Native handle</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the underlying implementation-defined native handle object 
native_handle <i>(public member function)</i>

<h2>Example</h2>

// Run this code  
&nbsp;<wbr>&nbsp;// Explanation: The output below was generated on a single-core machine. When 
&nbsp;<wbr>&nbsp;// thread1 starts, it enters the loop for the first time and calls increment() 
&nbsp;<wbr>&nbsp;// followed by get(). However, before it can print the returned value to 
&nbsp;<wbr>&nbsp;// std::cout, the scheduler puts thread1 to sleep and wakes up thread2, which 
&nbsp;<wbr>&nbsp;// obviously has time enough to run all three loop iterations at once. Back to 
&nbsp;<wbr>&nbsp;// thread1, still in the first loop iteration, it finally prints its local copy 
&nbsp;<wbr>&nbsp;// of the counter's value, which is 1, to std::cout and then runs the remaining 
&nbsp;<wbr>&nbsp;// two loop iterations. On a multi-core machine, none of the threads is put to 
&nbsp;<wbr>&nbsp;// sleep and the output is more likely to be in ascending order. 

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;123084176803584 2 
&nbsp;<wbr>&nbsp;123084176803584 3 
&nbsp;<wbr>&nbsp;123084176803584 4 
&nbsp;<wbr>&nbsp;123084185655040 1 
&nbsp;<wbr>&nbsp;123084185655040 5 
&nbsp;<wbr>&nbsp;123084185655040 6

<h2>See also</h2>

shared_timed_mutex provides shared mutual exclusion facility and implements locking with a timeout 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class)</i> 
<i>(C++14)</i> 
