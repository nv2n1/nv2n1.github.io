---
title: "kfifo_in_spinlocked(9)"
name: "kfifo_in_spinlocked"
section: "9"
letter: "k"
url: "/docs/linux/man/9-kfifo_in_spinlocked/"
description: "kfifo_in_spinlocked – put data into the fifo using a spinlock for locking"
---

<p>kfifo_in_spinlocked &#8211; put data into the fifo using a spinlock for locking</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>kfifo_in_spinlocked(</code><i>fifo</i><code>, </code><i>buf</i><code>, </code><i>n</i><code>, </code><i>lock</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>fifo</i></p>
<dl>
<dd>
<dd>address of the fifo to be used</dl>
<p> <i>buf</i></p>
<dl>
<dd>the data to be added</dl>
<p> <i>n</i></p>
<dl>
<dd>number of elements to be added</dl>
<p> <i>lock</i></p>
<dl>
<dd>pointer to the spinlock to use for locking</dl>
<h2>Description</h2>
<p>This macro copies the given values buffer into the fifo and returns the number of copied elements.</p>
<h2>Copyright</h2>
