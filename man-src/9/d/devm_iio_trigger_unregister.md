---
title: "devm_iio_trigger_unregister(9)"
name: "devm_iio_trigger_unregister"
section: "9"
letter: "d"
url: "/docs/linux/man/9-devm_iio_trigger_unregister/"
description: "devm_iio_trigger_unregister – Resource-managed iio_trigger_unregister"
---

<p>devm_iio_trigger_unregister &#8211; Resource-managed <code>iio_trigger_unregister</code></p>
<h2>Synopsis</h2>
<pre><code>void devm_iio_trigger_unregister(struct device *dev, struct iio_trigger *trig_info);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>device this iio_trigger belongs to</dl>
<p> <i>trig_info</i></p>
<dl>
<dd>the trigger associated with the device</dl>
<h2>Description</h2>
<p>Unregister trigger registered with <code>devm_iio_trigger_register</code>.</p>
<h2>Author</h2>
<p><code>Daniel Baluta</code> &lt;daniel.baluta [at] intel.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
