---
title: "iio_triggered_buffer_setup(9)"
name: "iio_triggered_buffer_setup"
section: "9"
letter: "i"
url: "/docs/linux/man/9-iio_triggered_buffer_setup/"
description: "iio_triggered_buffer_setup – Setup triggered buffer and pollfunc"
---

<p>iio_triggered_buffer_setup &#8211; Setup triggered buffer and pollfunc</p>
<h2>Synopsis</h2>
<pre><code>int iio_triggered_buffer_setup(struct iio_dev *indio_dev, irqreturn_t (*h)(int irq, void *p), irqreturn_t (*thread)(int irq, void *p), const struct iio_buffer_setup_ops *setup_ops);</code></pre>
<h2>Arguments</h2>
<p><i>indio_dev</i></p>
<dl>
<dd>
<dd>IIO device structure</dl>
<p> <i>h</i></p>
<dl>
<dd>Function which will be used as pollfunc top half</dl>
<p> <i>thread</i></p>
<dl>
<dd>Function which will be used as pollfunc bottom half</dl>
<p> <i>setup_ops</i></p>
<dl>
<dd>Buffer setup functions to use for this device. If NULL the default setup functions for triggered buffers will be used.</dl>
<h2>Description</h2>
<p>This function combines some common tasks which will normally be performed when setting up a triggered buffer. It will allocate the buffer and the pollfunc. </p>
<p> Before calling this function the indio_dev structure should already be completely initialized, but not yet registered. In practice this means that this function should be called right before <code>iio_device_register</code>. </p>
<p> To free the resources allocated by this function call <code>iio_triggered_buffer_cleanup</code>.</p>
<h2>Author</h2>
<p><code>Daniel Baluta</code> &lt;daniel.baluta [at] intel.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
