---
title: "kfifo_to_user(9)"
name: "kfifo_to_user"
section: "9"
letter: "k"
url: "/docs/linux/man/9-kfifo_to_user/"
description: "kfifo_to_user – copies data from the fifo into user space"
---

<p>kfifo_to_user &#8211; copies data from the fifo into user space</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>kfifo_to_user(</code><i>fifo</i><code>, </code><i>to</i><code>, </code><i>len</i><code>, </code><i>copied</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>fifo</i></p>
<dl>
<dd>
<dd>address of the fifo to be used</dl>
<p> <i>to</i></p>
<dl>
<dd>where the data must be copied</dl>
<p> <i>len</i></p>
<dl>
<dd>the size of the destination buffer</dl>
<p> <i>copied</i></p>
<dl>
<dd>pointer to output variable to store the number of copied bytes</dl>
<h2>Description</h2>
<p>This macro copies at most <i>len</i> bytes from the fifo into the <i>to</i> buffer and returns -EFAULT/0. </p>
<p> Note that with only one concurrent reader and one concurrent writer, you don&#8217;t need extra locking to use these macro.</p>
<h2>Copyright</h2>
