---
title: "stdpromiseset_exception_at_thread_exit(3)"
name: "stdpromiseset_exception_at_thread_exit"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdpromiseset_exception_at_thread_exit/"
---

std::promise&lt;R&gt;::set_exception_at_thread_exit - std::promise&lt;R&gt;::set_exception_at_thread_exit

<h2>Synopsis</h2>

<pre><code>void set_exception_at_thread_exit(std::exception_ptr p);
(since C++ 11)</code></pre> 
Stores the exception pointer p into the shared state without making the state ready immediately. The state is made ready when the current thread exits, after all variables with thread-local storage duration have been destroyed. 
The operation behaves as though set_value, set_exception, set_value_at_thread_exit, and set_exception_at_thread_exit acquire a single mutex associated with the promise object while updating the promise object. 
An exception is thrown if there is no shared state or the shared state already stores a value or exception. 
Calls to this function do not introduce data races with calls to get_future (but they need not synchronize with each other). 

<h2>Parameters</h2>

p - exception pointer to store. The behavior is undefined if p is null.

<h2>Return value</h2>

<i>(none)</i> 

<h2>Exceptions</h2>

std::future_error on the following conditions: 

 
* *this has no shared state. The error category is set to no_state. 

 

 
* The shared state already stores a value or exception. The error category is set to promise_already_satisfied.

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sets the result to indicate an exception 
set_exception <i>(public member function)</i> 
