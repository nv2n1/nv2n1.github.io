---
title: "stdpromiseget_future(3)"
name: "stdpromiseget_future"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdpromiseget_future/"
---

std::promise&lt;R&gt;::get_future - std::promise&lt;R&gt;::get_future

<h2>Synopsis</h2>

std::future&lt;T&gt; get_future(); <i>(since C++11)</i> 
Returns a future object associated with the same shared state as *this. 
An exception is thrown if *this has no shared state or get_future has already been called. To get multiple &quot;pop&quot; ends of the promise-future communication channel, use std::future::share. 
Calls to this function do not introduce data races with calls to set_value, set_exception, set_value_at_thread_exit, or set_exception_at_thread_exit (but they need not synchronize with each other). 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

A future referring to the shared state of *this 

<h2>Exceptions</h2>

std::future_error on the following conditions: 

 
* *this has no shared state. The error category is set to no_state. 

 

 
* get_future() has already been called on a promise with the same shared state as *this. The error category is set to future_already_retrieved.
