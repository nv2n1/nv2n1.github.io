---
title: "clk_is_match(9)"
name: "clk_is_match"
section: "9"
letter: "c"
url: "/docs/linux/man/9-clk_is_match/"
description: "clk_is_match – check if two clk’s point to the same hardware clock"
---

<p>clk_is_match &#8211; check if two clk&#8217;s point to the same hardware clock</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>bool clk_is_match(const struct clk&nbsp;<wbr>*&nbsp;<wbr></code><i>p</i><code>, const struct clk&nbsp;<wbr>*&nbsp;<wbr></code><i>q</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>p</i></p>
<dl>
<dd>
<dd>clk compared against q</dl>
<p> <i>q</i></p>
<dl>
<dd>clk compared against p</dl>
<h2>Description</h2>
<p>Returns true if the two struct clk pointers both point to the same hardware clock node. Put differently, returns true if struct clk *p and struct clk *q share the same struct clk_core object. </p>
<p> Returns false otherwise. Note that two NULL clks are treated as matching.</p>
<h2>Copyright</h2>
