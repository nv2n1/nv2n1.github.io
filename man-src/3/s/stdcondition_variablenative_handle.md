---
title: "stdcondition_variablenative_handle(3)"
name: "stdcondition_variablenative_handle"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdcondition_variablenative_handle/"
---

std::condition_variable::native_handle - std::condition_variable::native_handle

<h2>Synopsis</h2>

native_handle_type native_handle(); <i>(since C++11)</i> 
Accesses the native handle of *this. 
The meaning and the type of the result of this function is implementation-defined. On a POSIX system, this may be a value of type pthread_cond_t*. On a Windows system, this may be a PCONDITION_VARIABLE. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

The native handle of this condition variable. 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the underlying implementation-defined thread handle 
native_handle <i>(public member function of std::thread)</i> 
