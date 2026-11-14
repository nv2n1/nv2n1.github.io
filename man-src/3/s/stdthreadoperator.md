---
title: "stdthreadoperator(3)"
name: "stdthreadoperator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdthreadoperator/"
---

std::thread::operator= - std::thread::operator=

<h2>Synopsis</h2>

<pre><code>thread&amp; operator=( thread&amp;&amp; other ) noexcept;  (since C++11)</code></pre> 
If *this still has an associated running thread (i.e. joinable() == true), call std::terminate(). Otherwise, assigns the state of other to *this and sets other to a default constructed state. 
After this call, this-&gt;get_id() is equal to the value of other.get_id() prior to the call, and other no longer represents a thread of execution. 

<h2>Parameters</h2>

other - another thread object to assign to this thread object

<h2>Return value</h2>

*this 
