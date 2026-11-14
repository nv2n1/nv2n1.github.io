---
title: "clk_round_rate(9)"
name: "clk_round_rate"
section: "9"
letter: "c"
url: "/docs/linux/man/9-clk_round_rate/"
description: "clk_round_rate – adjust a rate to the exact rate a clock can provide"
---

<p>clk_round_rate &#8211; adjust a rate to the exact rate a clock can provide</p>
<h2>Synopsis</h2>
<pre><code>long clk_round_rate(struct clk *clk, unsigned long rate);</code></pre>
<h2>Arguments</h2>
<p><i>clk</i></p>
<dl>
<dd>
<dd>clock source</dl>
<p> <i>rate</i></p>
<dl>
<dd>desired clock rate in Hz</dl>
<h2>Description</h2>
<p>This answers the question &#8220;if I were to pass <i>rate</i> to <code>clk_set_rate</code>, what clock rate would I end up with?&#8221; without changing the hardware in any way. In other words: clk_set_rate(clk, r); rate = clk_get_rate(clk); and: </p>
<pre><code>clk_set_rate(clk, r); rate = clk_get_rate(clk);</code></pre>
<p> are equivalent except the former does not modify the clock hardware in any way. Returns rounded clock rate in Hz, or negative errno.</p>
<h2>Copyright</h2>
