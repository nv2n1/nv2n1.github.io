---
title: "stdshared_lockoperator(3)"
name: "stdshared_lockoperator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdshared_lockoperator/"
---

std::shared_lock&lt;Mutex&gt;::operator= - std::shared_lock&lt;Mutex&gt;::operator=

<h2>Synopsis</h2>

<pre><code>shared_lock&amp; operator=( shared_lock&amp;&amp; other ) noexcept;  (since C++14)</code></pre> 
Move assignment operator. Replaces the contents with those of other using move semantics. 
If, prior to this call, *this has an associated mutex ((mutex() returns a non-null pointer) and has acquired ownership of it (owns() returns true), the mutex is unlocked by calling unlock_shared(). 
After this call, other has no associated mutex. 

<h2>Parameters</h2>

other - another shared_lock to replace the state with

<h2>Return value</h2>

*this 
