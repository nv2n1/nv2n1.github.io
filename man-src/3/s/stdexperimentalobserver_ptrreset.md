---
title: "stdexperimentalobserver_ptrreset(3)"
name: "stdexperimentalobserver_ptrreset"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalobserver_ptrreset/"
---

std::experimental::observer_ptr&lt;W&gt;::reset - std::experimental::observer_ptr&lt;W&gt;::reset

<h2>Synopsis</h2>

<pre><code>constexpr void reset(element_type *p = nullptr) noexcept;
(library fundamentals TS v2)</code></pre> 
Set *this to watch the object pointed to by p. get() returns p after the call. 

<h2>Parameters</h2>

ptr - pointer to a new object to watch

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns a pointer to the watched object and stops watching the object 
release <i>(public member function)</i> 
