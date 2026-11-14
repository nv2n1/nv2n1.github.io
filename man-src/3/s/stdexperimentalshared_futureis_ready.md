---
title: "stdexperimentalshared_futureis_ready(3)"
name: "stdexperimentalshared_futureis_ready"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalshared_futureis_ready/"
---

std::experimental::shared_future&lt;T&gt;::is_ready - std::experimental::shared_future&lt;T&gt;::is_ready

<h2>Synopsis</h2>

<pre><code>bool is_ready() const;</code></pre> 
Checks if the associated shared state is ready. 
The behavior is undefined if valid() is false. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

true if the associated shared state is ready, otherwise false. 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks if the future has a shared state 
valid <i>(public member function of std::shared_future&lt;T&gt;)</i> 
