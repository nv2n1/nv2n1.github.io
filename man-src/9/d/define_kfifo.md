---
title: "define_kfifo(9)"
name: "define_kfifo"
section: "9"
letter: "d"
url: "/docs/linux/man/9-define_kfifo/"
description: "DEFINE_KFIFO – macro to define and initialize a fifo"
---

<p>DEFINE_KFIFO &#8211; macro to define and initialize a fifo</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>DEFINE_KFIFO(</code><i>fifo</i><code>, </code><i>type</i><code>, </code><i>size</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>fifo</i></p>
<dl>
<dd>
<dd>name of the declared fifo datatype</dl>
<p> <i>type</i></p>
<dl>
<dd>type of the fifo elements</dl>
<p> <i>size</i></p>
<dl>
<dd>the number of elements in the fifo, this must be a power of 2</dl>
<h2>Note</h2>
<p>the macro can be used for global and local fifo data type variables.</p>
<h2>Copyright</h2>
