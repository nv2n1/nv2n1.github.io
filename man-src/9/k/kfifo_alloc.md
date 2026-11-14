---
title: "kfifo_alloc(9)"
name: "kfifo_alloc"
section: "9"
letter: "k"
url: "/docs/linux/man/9-kfifo_alloc/"
description: "kfifo_alloc – dynamically allocates a new fifo buffer"
---

<p>kfifo_alloc &#8211; dynamically allocates a new fifo buffer</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>kfifo_alloc(</code><i>fifo</i><code>, </code><i>size</i><code>, </code><i>gfp_mask</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>fifo</i></p>
<dl>
<dd>
<dd>pointer to the fifo</dl>
<p> <i>size</i></p>
<dl>
<dd>the number of elements in the fifo, this must be a power of 2</dl>
<p> <i>gfp_mask</i></p>
<dl>
<dd>get_free_pages mask, passed to <code>kmalloc</code></dl>
<h2>Description</h2>
<p>This macro dynamically allocates a new fifo buffer. </p>
<p> The numer of elements will be rounded-up to a power of 2. The fifo will be release with <code>kfifo_free</code>. Return 0 if no error, otherwise an error code.</p>
<h2>Copyright</h2>
