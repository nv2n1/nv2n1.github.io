---
title: "stdexperimentallatchcount_down(3)"
name: "stdexperimentallatchcount_down"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentallatchcount_down/"
---

std::experimental::latch::count_down - std::experimental::latch::count_down

<h2>Synopsis</h2>

<pre><code>void count_down(ptrdiff_t n = 1);
(1)(concurrency TS)</code></pre> 
Atomically decrements the internal counter by n without blocking the caller. 
If n is greater than the value of the internal counter or is negative, the behavior is undefined. 
This operation synchronizes_with all calls that block on this latch and all is_ready calls on this latch that returns true. 

<h2>Parameters</h2>

n - the value by which the internal counter is decreased

<h2>Return value</h2>

<i>(none)</i> 

<h2>Exceptions</h2>

Throws nothing.
