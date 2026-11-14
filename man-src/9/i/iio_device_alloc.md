---
title: "iio_device_alloc(9)"
name: "iio_device_alloc"
section: "9"
letter: "i"
url: "/docs/linux/man/9-iio_device_alloc/"
description: "iio_device_alloc – allocate an iio_dev from a driver"
---

<p>iio_device_alloc &#8211; allocate an iio_dev from a driver</p>
<h2>Synopsis</h2>
<pre><code>struct iio_dev *iio_device_alloc(int sizeof_priv);</code></pre>
<h2>Arguments</h2>
<p><i>sizeof_priv</i></p>
<dl>
<dd>
<dd>Space to allocate for private structure.</dl>
<h2>Author</h2>
<p><code>Daniel Baluta</code> &lt;daniel.baluta [at] intel.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
