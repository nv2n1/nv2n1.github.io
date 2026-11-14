---
title: "kfifo_peek(9)"
name: "kfifo_peek"
section: "9"
letter: "k"
url: "/docs/linux/man/9-kfifo_peek/"
description: "kfifo_peek – get data from the fifo without removing"
---

<p>kfifo_peek &#8211; get data from the fifo without removing</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>kfifo_peek(</code><i>fifo</i><code>, </code><i>val</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>fifo</i></p>
<dl>
<dd>
<dd>address of the fifo to be used</dl>
<p> <i>val</i></p>
<dl>
<dd>address where to store the data</dl>
<h2>Description</h2>
<p>This reads the data from the fifo without removing it from the fifo. It returns 0 if the fifo was empty. Otherwise it returns the number processed elements. </p>
<p> Note that with only one concurrent reader and one concurrent writer, you don&#8217;t need extra locking to use these macro.</p>
<h2>Copyright</h2>
