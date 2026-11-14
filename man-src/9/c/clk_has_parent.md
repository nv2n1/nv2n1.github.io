---
title: "clk_has_parent(9)"
name: "clk_has_parent"
section: "9"
letter: "c"
url: "/docs/linux/man/9-clk_has_parent/"
description: "clk_has_parent – check if a clock is a possible parent for another"
---

<p>clk_has_parent &#8211; check if a clock is a possible parent for another</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>bool clk_has_parent(struct clk&nbsp;<wbr>*&nbsp;<wbr></code><i>clk</i><code>, struct clk&nbsp;<wbr>*&nbsp;<wbr></code><i>parent</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>clk</i></p>
<dl>
<dd>
<dd>clock source</dl>
<p> <i>parent</i></p>
<dl>
<dd>parent clock source</dl>
<h2>Description</h2>
<p>This function can be used in drivers that need to check that a clock can be the parent of another without actually changing the parent. </p>
<p> Returns true if <i>parent</i> is a possible parent for <i>clk</i>, false otherwise.</p>
<h2>Copyright</h2>
