---
title: "kfifo_out(9)"
name: "kfifo_out"
section: "9"
letter: "k"
url: "/docs/linux/man/9-kfifo_out/"
description: "kfifo_out – get data from the fifo"
---

<p>kfifo_out &#8211; get data from the fifo</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>kfifo_out(</code><i>fifo</i><code>, </code><i>buf</i><code>, </code><i>n</i><code>);</code></dl>
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
<h2>Description</h2>
<p>This macro get some data from the fifo and return the numbers of elements copied. </p>
<p> Note that with only one concurrent reader and one concurrent writer, you don&#8217;t need extra locking to use these macro.</p>
<h2>Copyright</h2>
