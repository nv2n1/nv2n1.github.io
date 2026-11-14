---
title: "stdcondition_variablecondition_variable(3)"
name: "stdcondition_variablecondition_variable"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdcondition_variablecondition_variable/"
description: "std::condition_variable::~condition_variable – std::condition_variable::~condition_variable"
---

<p>std::condition_variable::~condition_variable &#8211; std::condition_variable::~condition_variable</p>
<h2>Synopsis</h2>
<p>~condition_variable(); <code>(1)</code> <i>(since C++11)</i><br />
Destroys the object of type std::condition_variable<br />
It is only safe to invoke the destructor if all threads have been notified. It is not required that they have exited their respective wait functions: some threads may still be waiting to reacquire the associated lock, or may be waiting to be scheduled to run after reacquiring it.<br />
The programmer must ensure that no threads attempt to wait on *this once the destructor has been started, especially when the waiting threads are calling the wait functions in a loop or are using the overloads of the wait functions that take a predicate. </p>
<h2>Exceptions</h2>
<p><i>(none)</i></p>
<h2>See also</h2>
