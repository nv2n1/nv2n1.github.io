---
title: "clk_set_phase(9)"
name: "clk_set_phase"
section: "9"
letter: "c"
url: "/docs/linux/man/9-clk_set_phase/"
---

clk_set_phase - adjust the phase shift of a clock signal

<h2>Synopsis</h2>

<pre><code>int clk_set_phase(struct clk *clk, int degrees);</code></pre>

<h2>Arguments</h2>

<i>clk</i>
<dl><dd><dd>clock signal source</dl>
 

 <i>degrees</i>
<dl><dd>number of degrees the signal is shifted</dl>

<h2>Description</h2>

Shifts the phase of a clock signal by the specified degrees. Returns 0 on success, -EERROR otherwise.

<h2>Copyright</h2>


