---
title: "clk_get_phase(9)"
name: "clk_get_phase"
section: "9"
letter: "c"
url: "/docs/linux/man/9-clk_get_phase/"
---

clk_get_phase - return the phase shift of a clock signal

<h2>Synopsis</h2>

<pre><code>int clk_get_phase(struct clk *clk);</code></pre>

<h2>Arguments</h2>

<i>clk</i>
<dl><dd><dd>clock signal source</dl>

<h2>Description</h2>

Returns the phase shift of a clock node in degrees, otherwise returns -EERROR.

<h2>Copyright</h2>


