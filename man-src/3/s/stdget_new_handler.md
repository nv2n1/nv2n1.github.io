---
title: "stdget_new_handler(3)"
name: "stdget_new_handler"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdget_new_handler/"
---

std::get_new_handler - std::get_new_handler

<h2>Synopsis</h2>

Defined in header &lt;new&gt; 
std::new_handler get_new_handler() noexcept; <i>(since C++11)</i> 
Returns the currently installed new-handler, which may be a null pointer. 
This function is thread-safe. Previous call to std::set_new_handler synchronizes-with (see std::memory_order) the subsequent calls to std::get_new_handler. <i>(since C++11)</i> 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

The currently installed new-handler, which may be a null pointer value. 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;allocation functions 
operator_new <i>(function)</i> 
operator_new[] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;registers a new handler 
set_new_handler <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;function pointer type of the new handler 
new_handler <i>(typedef)</i> 
