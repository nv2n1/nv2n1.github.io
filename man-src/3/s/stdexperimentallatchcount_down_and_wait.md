---
title: "stdexperimentallatchcount_down_and_wait(3)"
name: "stdexperimentallatchcount_down_and_wait"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentallatchcount_down_and_wait/"
---

std::experimental::latch::count_down_and_wait - std::experimental::latch::count_down_and_wait

<h2>Synopsis</h2>

<pre><code>void count_down_and_wait();
(1)(concurrency TS)</code></pre> 
Atomically decrements the internal counter by 1 and (if necessary) blocks the calling thread until the counter reaches zero. 
The behavior is undefined if the internal counter is already zero. 
This operation synchronizes_with all calls that block on this latch and all is_ready calls on this latch that returns true. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

<i>(none)</i> 

<h2>Exceptions</h2>

Throws nothing.
