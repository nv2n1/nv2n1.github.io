---
title: "iio_buffer_get(9)"
name: "iio_buffer_get"
section: "9"
letter: "i"
url: "/docs/linux/man/9-iio_buffer_get/"
description: "iio_buffer_get – Grab a reference to the buffer"
---

<p>iio_buffer_get &#8211; Grab a reference to the buffer</p>
<h2>Synopsis</h2>
<pre><code>struct iio_buffer *iio_buffer_get(struct iio_buffer *buffer);</code></pre>
<h2>Arguments</h2>
<p><i>buffer</i></p>
<dl>
<dd>
<dd>The buffer to grab a reference for, may be NULL</dl>
<h2>Description</h2>
<p>Returns the pointer to the buffer that was passed into the function.</p>
<h2>Author</h2>
<p><code>Daniel Baluta</code> &lt;daniel.baluta [at] intel.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
