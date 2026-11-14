---
title: "clk_get_sys(9)"
name: "clk_get_sys"
section: "9"
letter: "c"
url: "/docs/linux/man/9-clk_get_sys/"
description: "clk_get_sys – get a clock based upon the device name"
---

<p>clk_get_sys &#8211; get a clock based upon the device name</p>
<h2>Synopsis</h2>
<pre><code>struct clk *clk_get_sys(const char *dev_id, const char *con_id);</code></pre>
<h2>Arguments</h2>
<p><i>dev_id</i></p>
<dl>
<dd>
<dd>device name</dl>
<p> <i>con_id</i></p>
<dl>
<dd>connection ID</dl>
<h2>Description</h2>
<p>Returns a struct clk corresponding to the clock producer, or valid <code>IS_ERR</code> condition containing errno. The implementation uses <i>dev_id</i> and <i>con_id</i> to determine the clock consumer, and thereby the clock producer. In contrast to <code>clk_get</code> this function takes the device name instead of the device itself for identification. </p>
<p> Drivers must assume that the clock source is not enabled. </p>
<p> clk_get_sys should not be called from within interrupt context.</p>
<h2>Copyright</h2>
