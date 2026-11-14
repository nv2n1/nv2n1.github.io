---
title: "stdfuturevalid(3)"
name: "stdfuturevalid"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfuturevalid/"
---

std::future&lt;T&gt;::valid - std::future&lt;T&gt;::valid

<h2>Synopsis</h2>

bool valid() const noexcept; <i>(since C++11)</i> 
Checks if the future refers to a shared state. 
This is the case only for futures that were not default-constructed or moved from (i.e. returned by std::promise::get_future(), std::packaged_task::get_future() or std::async()) until the first time get() or share() is called. 
The behavior is undefined if any member function other than the destructor, the move-assignment operator, or valid is called on a future that does not refer to shared state (although implementations are encouraged to throw std::future_error indicating no_state in this case). It is valid to move from a future object for which valid() is false 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

true if *this refers to a shared state, otherwise false. 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;waits for the result to become available 
wait <i>(public member function)</i> 
