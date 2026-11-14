---
title: "kfifo_initialized(9)"
name: "kfifo_initialized"
section: "9"
letter: "k"
url: "/docs/linux/man/9-kfifo_initialized/"
description: "kfifo_initialized – Check if the fifo is initialized"
---

<p>kfifo_initialized &#8211; Check if the fifo is initialized</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>kfifo_initialized(</code><i>fifo</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>fifo</i></p>
<dl>
<dd>
<dd>address of the fifo to check</dl>
<h2>Description</h2>
<p>Return <code>true</code> if fifo is initialized, otherwise <code>false</code>. Assumes the fifo was 0 before.</p>
<h2>Copyright</h2>
