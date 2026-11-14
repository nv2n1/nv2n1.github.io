---
title: "kfifo_from_user(9)"
name: "kfifo_from_user"
section: "9"
letter: "k"
url: "/docs/linux/man/9-kfifo_from_user/"
description: "kfifo_from_user – puts some data from user space into the fifo"
---

<p>kfifo_from_user &#8211; puts some data from user space into the fifo</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>kfifo_from_user(</code><i>fifo</i><code>, </code><i>from</i><code>, </code><i>len</i><code>, </code><i>copied</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>fifo</i></p>
<dl>
<dd>
<dd>address of the fifo to be used</dl>
<p> <i>from</i></p>
<dl>
<dd>pointer to the data to be added</dl>
<p> <i>len</i></p>
<dl>
<dd>the length of the data to be added</dl>
<p> <i>copied</i></p>
<dl>
<dd>pointer to output variable to store the number of copied bytes</dl>
<h2>Description</h2>
<p>This macro copies at most <i>len</i> bytes from the <i>from</i> into the fifo, depending of the available space and returns -EFAULT/0. </p>
<p> Note that with only one concurrent reader and one concurrent writer, you don&#8217;t need extra locking to use these macro.</p>
<h2>Copyright</h2>
