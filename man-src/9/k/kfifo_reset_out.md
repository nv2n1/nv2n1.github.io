---
title: "kfifo_reset_out(9)"
name: "kfifo_reset_out"
section: "9"
letter: "k"
url: "/docs/linux/man/9-kfifo_reset_out/"
description: "kfifo_reset_out – skip fifo content"
---

<p>kfifo_reset_out &#8211; skip fifo content</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>kfifo_reset_out(</code><i>fifo</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>fifo</i></p>
<dl>
<dd>
<dd>address of the fifo to be used</dl>
<h2>Note</h2>
<p>The usage of <code>kfifo_reset_out</code> is safe until it will be only called from the reader thread and there is only one concurrent reader. Otherwise it is dangerous and must be handled in the same way as <code>kfifo_reset</code>.</p>
<h2>Copyright</h2>
