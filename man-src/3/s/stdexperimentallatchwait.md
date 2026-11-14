---
title: "stdexperimentallatchwait(3)"
name: "stdexperimentallatchwait"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentallatchwait/"
---

std::experimental::latch::wait - std::experimental::latch::wait

<h2>Synopsis</h2>

<pre><code>void wait() const;
(1)(concurrency TS)</code></pre> 
Blocks the calling thread until the internal counter reaches 0. If it is zero already, returns immediately. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

<i>(none)</i> 

<h2>Exceptions</h2>

Throws nothing.
