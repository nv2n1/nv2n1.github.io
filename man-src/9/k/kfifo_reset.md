---
title: "kfifo_reset(9)"
name: "kfifo_reset"
section: "9"
letter: "k"
url: "/docs/linux/man/9-kfifo_reset/"
description: "kfifo_reset – removes the entire fifo content"
---

<p>kfifo_reset &#8211; removes the entire fifo content</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>kfifo_reset(</code><i>fifo</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>fifo</i></p>
<dl>
<dd>
<dd>address of the fifo to be used</dl>
<h2>Note</h2>
<p>usage of <code>kfifo_reset</code> is dangerous. It should be only called when the fifo is exclusived locked or when it is secured that no other thread is accessing the fifo.</p>
<h2>Copyright</h2>
