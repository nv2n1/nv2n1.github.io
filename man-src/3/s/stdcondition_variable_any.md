---
title: "stdcondition_variable_any(3)"
name: "stdcondition_variable_any"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdcondition_variable_any/"
---

std::condition_variable_any - std::condition_variable_any

<h2>Synopsis</h2>

Defined in header &lt;condition_variable&gt; 
class condition_variable_any; <i>(since C++11)</i> 
The condition_variable_any class is a generalization of std::condition_variable. Whereas std::condition_variable works only on std::unique_lock&lt;std::mutex&gt;, condition_variable_any can operate on any lock that meets the BasicLockable requirements. 
See std::condition_variable for the description of the semantics of condition variables. 
The class std::condition_variable_any is a StandardLayoutType. It is not CopyConstructible, MoveConstructible, CopyAssignable, or MoveAssignable. 
If the lock is std::unique_lock, std::condition_variable may provide better performance. 

<h2>Member functions</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs the object 
constructor <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;destructs the object 
destructor <i>(public member function)</i> 

 
operator= not copy-assignable 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public member function)</i> 
[deleted]

<h2>Notification</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;notifies one waiting thread 
notify_one <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;notifies all waiting threads 
notify_all <i>(public member function)</i>

<h2>Waiting</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;blocks the current thread until the condition variable is woken up 
wait <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;blocks the current thread until the condition variable is woken up or after the specified timeout duration 
wait_for <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;blocks the current thread until the condition variable is woken up or until specified time point has been reached 
wait_until <i>(public member function)</i>

<h2>Notes</h2>

std::condition_variable_any can be used with std::shared_lock in order to wait on a std::shared_mutex in shared ownership mode. 
A possible use for std::condition_variable_any with custom Lockable types is to provide convenient interruptible waits: the custom lock operation would both lock the associated mutex as expected, and also perform the necessary setup to notify this condition variable when the interrupting signal is received.[1] 

<h2>References</h2>

&nbsp;<wbr>&nbsp;1. ↑ A. Williams (2012), &quot;C++ concurrency in action&quot; 9.2.4 Interrupting a wait on std::condition_variable_any
