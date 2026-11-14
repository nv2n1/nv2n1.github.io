---
title: "declare_kfifo(9)"
name: "declare_kfifo"
section: "9"
letter: "d"
url: "/docs/linux/man/9-declare_kfifo/"
description: "DECLARE_KFIFO – macro to declare a fifo object"
---

<p>DECLARE_KFIFO &#8211; macro to declare a fifo object</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>DECLARE_KFIFO(</code><i>fifo</i><code>, </code><i>type</i><code>, </code><i>size</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>fifo</i></p>
<dl>
<dd>
<dd>name of the declared fifo</dl>
<p> <i>type</i></p>
<dl>
<dd>type of the fifo elements</dl>
<p> <i>size</i></p>
<dl>
<dd>the number of elements in the fifo, this must be a power of 2</dl>
<h2>Copyright</h2>
