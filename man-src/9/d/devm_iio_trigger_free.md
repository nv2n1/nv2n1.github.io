---
title: "devm_iio_trigger_free(9)"
name: "devm_iio_trigger_free"
section: "9"
letter: "d"
url: "/docs/linux/man/9-devm_iio_trigger_free/"
description: "devm_iio_trigger_free – Resource-managed iio_trigger_free"
---

<p>devm_iio_trigger_free &#8211; Resource-managed <code>iio_trigger_free</code></p>
<h2>Synopsis</h2>
<pre><code>void devm_iio_trigger_free(struct device *dev, struct iio_trigger *iio_trig);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>Device this iio_dev belongs to</dl>
<p> <i>iio_trig</i></p>
<dl>
<dd>the iio_trigger associated with the device</dl>
<h2>Description</h2>
<p>Free iio_trigger allocated with <code>devm_iio_trigger_alloc</code>.</p>
<h2>Author</h2>
<p><code>Daniel Baluta</code> &lt;daniel.baluta [at] intel.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
