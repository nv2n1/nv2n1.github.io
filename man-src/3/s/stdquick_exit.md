---
title: "stdquick_exit(3)"
name: "stdquick_exit"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdquick_exit/"
---

std::quick_exit - std::quick_exit

<h2>Synopsis</h2>

Defined in header &lt;cstdlib&gt; 
[[noreturn]] void quick_exit( int exit_code ) noexcept; <i>(since C++11)</i> 
Causes normal program termination to occur without completely cleaning the resources. 
Functions passed to std::at_quick_exit are called in reverse order of their registration. If an exception tries to propagate out of any of the functions, std::terminate is called. After calling the registered functions, calls std::_Exit(exit_code) 
Functions passed to std::atexit are not called. 

<h2>Parameters</h2>

exit_code - exit status of the program

<h2>Return value</h2>

<i>(none)</i> 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;causes abnormal program termination (without cleaning up) 
abort <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;causes normal program termination with cleaning up 
exit <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;registers a function to be called on std::exit() invocation 
atexit <i>(function)</i> 
at_quick_exit registers a function to be called on quick_exit invocation 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 
