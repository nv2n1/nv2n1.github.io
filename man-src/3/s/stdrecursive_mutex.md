---
title: "stdrecursive_mutex(3)"
name: "stdrecursive_mutex"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdrecursive_mutex/"
---

std::recursive_mutex - std::recursive_mutex

<h2>Synopsis</h2>

Defined in header &lt;mutex&gt; 
class recursive_mutex; <i>(since C++11)</i> 
The recursive_mutex class is a synchronization primitive that can be used to protect shared data from being simultaneously accessed by multiple threads. 
recursive_mutex offers exclusive, recursive ownership semantics: 
* A calling thread owns a recursive_mutex for a period of time that starts when it successfully calls either lock or try_lock. During this period, the thread may make additional calls to lock or try_lock. The period of ownership ends when the thread makes a matching number of calls to unlock. 
* When a thread owns a recursive_mutex, all other threads will block (for calls to lock) or receive a false return value (for try_lock) if they attempt to claim ownership of the recursive_mutex. 
* The maximum number of times that a recursive_mutex may be locked is unspecified, but after that number is reached, calls to lock will throw std::system_error and calls to try_lock will return false. 
The behavior of a program is undefined if a recursive_mutex is destroyed while still owned by some thread. The recursive_mutex class satisfies all requirements of Mutex and StandardLayoutType. 

<h2>Member types</h2>

Member type Definition 
native_handle_type(optional) implementation-defined

<h2>Member functions</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs the mutex 
constructor <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;destroys the mutex 
destructor <i>(public member function)</i> 

 
operator= not copy-assignable 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public member function)</i> 
[deleted]

<h2>Locking</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;locks the mutex, blocks if the mutex is not available 
lock <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tries to lock the mutex, returns if the mutex is not available 
try_lock <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unlocks the mutex 
unlock <i>(public member function)</i>

<h2>Native handle</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the underlying implementation-defined native handle object 
native_handle <i>(public member function)</i>
