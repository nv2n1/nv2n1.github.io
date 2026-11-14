---
title: "stdexperimentalmake_observer(3)"
name: "stdexperimentalmake_observer"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalmake_observer/"
---

std::experimental::make_observer - std::experimental::make_observer

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;experimental/memory&gt;

template &lt;class W&gt;                                                (library fundamentals TS v2)

std::experimental::observer_ptr&lt;W&gt; make_observer(W* p) noexcept;</code></pre> 
Creates an observer_ptr object, deducing the template argument from the type of the function argument. 

<h2>Parameters</h2>

p - pointer to the object to be watched by the observer_ptr object

<h2>Return value</h2>

A observer_ptr object, created as if by std::experimental::observer_ptr&lt;W&gt;(p). 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 
