---
title: "stdget_terminate(3)"
name: "stdget_terminate"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdget_terminate/"
---

std::get_terminate - std::get_terminate

<h2>Synopsis</h2>

Defined in header &lt;exception&gt; 
std::terminate_handler get_terminate() noexcept; <i>(since C++11)</i> 
Returns the currently installed std::terminate_handler, which may be a null pointer. 
This function is thread-safe. Prior call to std::set_terminate synchronizes-with (see std::memory_order) this function. <i>(since C++11)</i> 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

The currently installed std::terminate_handler. 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the type of the function called by std::terminate 
terminate_handler <i>(typedef)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;changes the function to be called by std::terminate 
set_terminate <i>(function)</i> 
