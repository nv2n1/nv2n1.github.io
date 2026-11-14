---
title: "w1_reset_select_slave(9)"
name: "w1_reset_select_slave"
section: "9"
letter: "w"
url: "/docs/linux/man/9-w1_reset_select_slave/"
description: "w1_reset_select_slave – reset and select a slave"
---

<p>w1_reset_select_slave &#8211; reset and select a slave</p>
<h2>Synopsis</h2>
<pre><code>int w1_reset_select_slave(struct w1_slave *sl);</code></pre>
<h2>Arguments</h2>
<p><i>sl</i></p>
<dl>
<dd>
<dd>the slave to select</dl>
<h2>Description</h2>
<p>Resets the bus and then selects the slave by sending either a skip rom or a rom match. A skip rom is issued if there is only one device registered on the bus. The w1 master lock must be held.</p>
<h2>Return</h2>
<p>0=success, anything else=error</p>
<h2>Author</h2>
<p><code>David Fries</code> &lt;David [at] Fries.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
