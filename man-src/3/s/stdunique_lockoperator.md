---
title: "stdunique_lockoperator(3)"
name: "stdunique_lockoperator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdunique_lockoperator/"
---

std::unique_lock&lt;Mutex&gt;::operator= - std::unique_lock&lt;Mutex&gt;::operator=

<h2>Synopsis</h2>

<pre><code>unique_lock&amp; operator=( unique_lock&amp;&amp; other );  (since C++11)</code></pre> 
Move assignment operator. Replaces the contents with those of other using move semantics. 
If prior to the call *this has an associated mutex and has acquired ownership of it, the mutex is unlocked. 

<h2>Parameters</h2>

other - another unique_lock to replace the state with

<h2>Return value</h2>

*this 

<h2>Exceptions</h2>

Throws nothing
