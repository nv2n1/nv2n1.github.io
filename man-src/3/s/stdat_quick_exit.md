---
title: "stdat_quick_exit(3)"
name: "stdat_quick_exit"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdat_quick_exit/"
---

std::at_quick_exit - std::at_quick_exit

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cstdlib&gt;

    int at_quick_exit(/*atexit-handler*/ *func) noexcept;
(1)(since C++ 11)

    int at_quick_exit(/*c-atexit-handler*/ *func) noexcept;

extern &quot;C++&quot; using /*atexit-handler*/ = void(); // exposition-only (2)

extern &quot;C&quot; using /*c-atexit-handler*/ = void(); // exposition-only</code></pre> 
Registers the function pointed to by func to be called on quick program termination (via std::quick_exit). 
Calling the function from several threads does not induce a data race. The implementation shall support the registration of at least 32 functions. 
The registered functions will not be called on normal_program_termination. If a function need to be called in that case, std::atexit must be used. 

<h2>Parameters</h2>

func - pointer to a function to be called on quick program termination

<h2>Return value</h2>

0 if the registration succeeds, nonzero value otherwise. 

<h2>Notes</h2>

The two overloads are distinct because the types of the parameter func are distinct (language_linkage is part of its type) 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;causes abnormal program termination (without cleaning up) 
abort <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;causes normal program termination with cleaning up 
exit <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;registers a function to be called on std::exit() invocation 
atexit <i>(function)</i> 
quick_exit causes quick program termination without completely cleaning up 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 
