---
title: "kfifo_put(9)"
name: "kfifo_put"
section: "9"
letter: "k"
url: "/docs/linux/man/9-kfifo_put/"
description: "kfifo_put – put data into the fifo"
---

<p>kfifo_put &#8211; put data into the fifo</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>kfifo_put(</code><i>fifo</i><code>, </code><i>val</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>fifo</i></p>
<dl>
<dd>
<dd>address of the fifo to be used</dl>
<p> <i>val</i></p>
<dl>
<dd>the data to be added</dl>
<h2>Description</h2>
<p>This macro copies the given value into the fifo. It returns 0 if the fifo was full. Otherwise it returns the number processed elements. </p>
<p> Note that with only one concurrent reader and one concurrent writer, you don&#8217;t need extra locking to use these macro.</p>
<h2>Copyright</h2>
