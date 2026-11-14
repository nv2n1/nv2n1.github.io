---
title: "kfifo_out_spinlocked(9)"
name: "kfifo_out_spinlocked"
section: "9"
letter: "k"
url: "/docs/linux/man/9-kfifo_out_spinlocked/"
description: "kfifo_out_spinlocked – get data from the fifo using a spinlock for locking"
---

<p>kfifo_out_spinlocked &#8211; get data from the fifo using a spinlock for locking</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>kfifo_out_spinlocked(</code><i>fifo</i><code>, </code><i>buf</i><code>, </code><i>n</i><code>, </code><i>lock</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>fifo</i></p>
<dl>
<dd>
<dd>address of the fifo to be used</dl>
<p> <i>buf</i></p>
<dl>
<dd>pointer to the storage buffer</dl>
<p> <i>n</i></p>
<dl>
<dd>max. number of elements to get</dl>
<p> <i>lock</i></p>
<dl>
<dd>pointer to the spinlock to use for locking</dl>
<h2>Description</h2>
<p>This macro get the data from the fifo and return the numbers of elements copied.</p>
<h2>Copyright</h2>
