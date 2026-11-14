---
title: "stdpackaged_taskpackaged_task(3)"
name: "stdpackaged_taskpackaged_task"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdpackaged_taskpackaged_task/"
---

std::packaged_task&lt;R(Args...)&gt;::~packaged_task - std::packaged_task&lt;R(Args...)&gt;::~packaged_task

<h2>Synopsis</h2>

<pre><code>~packaged_task();</code></pre> 
Abandons the shared state and destroys the stored task object. 
As with std::promise::~promise, if the shared state is abandoned before it was made ready, an std::future_error exception is stored with the error code std::future_errc::broken_promise). 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 
