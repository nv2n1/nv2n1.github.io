---
title: "clk_disable(9)"
name: "clk_disable"
section: "9"
letter: "c"
url: "/docs/linux/man/9-clk_disable/"
description: "clk_disable – inform the system when the clock source is no longer required."
---

<p>clk_disable &#8211; inform the system when the clock source is no longer required.</p>
<h2>Synopsis</h2>
<pre><code>void clk_disable(struct clk *clk);</code></pre>
<h2>Arguments</h2>
<p><i>clk</i></p>
<dl>
<dd>
<dd>clock source</dl>
<h2>Description</h2>
<p>Inform the system that a clock source is no longer required by a driver and may be shut down. </p>
<p> May be called from atomic contexts. </p>
<p> Implementation detail: if the clock source is shared between multiple drivers, <code>clk_enable</code> calls must be balanced by the same number of <code>clk_disable</code> calls for the clock source to be disabled.</p>
<h2>Copyright</h2>
