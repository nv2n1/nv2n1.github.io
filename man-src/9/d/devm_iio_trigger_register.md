---
title: "devm_iio_trigger_register(9)"
name: "devm_iio_trigger_register"
section: "9"
letter: "d"
url: "/docs/linux/man/9-devm_iio_trigger_register/"
description: "devm_iio_trigger_register – Resource-managed iio_trigger_register"
---

<p>devm_iio_trigger_register &#8211; Resource-managed <code>iio_trigger_register</code></p>
<h2>Synopsis</h2>
<pre><code>int devm_iio_trigger_register(struct device *dev, struct iio_trigger *trig_info);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>device this trigger was allocated for</dl>
<p> <i>trig_info</i></p>
<dl>
<dd>trigger to register</dl>
<h2>Description</h2>
<p>Managed <code>iio_trigger_register</code>. The IIO trigger registered with this function is automatically unregistered on driver detach. This function calls <code>iio_trigger_register</code> internally. Refer to that function for more information. </p>
<p> If an iio_trigger registered with this function needs to be unregistered separately, <code>devm_iio_trigger_unregister</code> must be used.</p>
<h2>Return</h2>
<p>0 on success, negative error number on failure.</p>
<h2>Author</h2>
<p><code>Daniel Baluta</code> &lt;daniel.baluta [at] intel.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
