---
title: "stdshared_futurevalid(3)"
name: "stdshared_futurevalid"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdshared_futurevalid/"
---

std::shared_future&lt;T&gt;::valid - std::shared_future&lt;T&gt;::valid

<h2>Synopsis</h2>

bool valid() const noexcept; <i>(since C++11)</i> 
Checks if the future refers to a shared state. 
This is the case only for futures that were not default-constructed or moved from. Unlike std::future, std::shared_future's shared state is not invalidated when get() is called. 
The behavior is undefined if any member function other than the destructor, the copy-assignment operator, the move-assignment operator, or valid is called on a shared_future that does not refer to shared state (although implementations are encouraged to throw std::future_error indicating no_state in this case). It is valid to move or copy from a shared_future object for which valid() is false 

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
