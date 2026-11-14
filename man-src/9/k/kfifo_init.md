---
title: "kfifo_init(9)"
name: "kfifo_init"
section: "9"
letter: "k"
url: "/docs/linux/man/9-kfifo_init/"
description: "kfifo_init – initialize a fifo using a preallocated buffer"
---

<p>kfifo_init &#8211; initialize a fifo using a preallocated buffer</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>kfifo_init(</code><i>fifo</i><code>, </code><i>buffer</i><code>, </code><i>size</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>fifo</i></p>
<dl>
<dd>
<dd>the fifo to assign the buffer</dl>
<p> <i>buffer</i></p>
<dl>
<dd>the preallocated buffer to be used</dl>
<p> <i>size</i></p>
<dl>
<dd>the size of the internal buffer, this have to be a power of 2</dl>
<h2>Description</h2>
<p>This macro initialize a fifo using a preallocated buffer. </p>
<p> The numer of elements will be rounded-up to a power of 2. Return 0 if no error, otherwise an error code.</p>
<h2>Copyright</h2>
