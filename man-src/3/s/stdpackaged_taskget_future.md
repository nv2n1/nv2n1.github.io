---
title: "stdpackaged_taskget_future(3)"
name: "stdpackaged_taskget_future"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdpackaged_taskget_future/"
---

std::packaged_task&lt;R(Args...)&gt;::get_future - std::packaged_task&lt;R(Args...)&gt;::get_future

<h2>Synopsis</h2>

std::future&lt;R&gt; get_future(); <i>(since C++11)</i> 
Returns a future which shares the same shared state as *this. 
get_future can be called only once for each packaged_task. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

A future which shares the same shared state as *this. 

<h2>Exceptions</h2>

std::future_error on the following error conditions: 

 
* The shared state has already been retrieved via a call to get_future. The error category is set to future_already_retrieved. 
* *this has no shared state. The error category is set to no_state.
