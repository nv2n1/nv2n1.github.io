---
title: "stdonce_flag(3)"
name: "stdonce_flag"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdonce_flag/"
---

std::once_flag - std::once_flag

<h2>Synopsis</h2>

Defined in header &lt;mutex&gt; 
class once_flag; <i>(since C++11)</i> 
The class std::once_flag is a helper structure for std::call_once. 
An object of type std::once_flag that is passed to multiple calls to std::call_once allows those calls to coordinate with each other such that only one of the calls will actually run to completion. 
std::once_flag is neither copyable nor movable. 

<h2>Member functions</h2>

&nbsp;std::once_flag::once_flag 

 

 
constexpr once_flag() noexcept; 

 
Constructs an once_flag object. The internal state is set to indicate that no function has been called yet.

<h2>Parameters</h2>

<i>(none)</i>

<h2>See also</h2>

call_once invokes a function only once even if called from multiple threads 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
