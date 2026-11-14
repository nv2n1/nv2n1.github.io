---
title: "devm_iio_trigger_alloc(9)"
name: "devm_iio_trigger_alloc"
section: "9"
letter: "d"
url: "/docs/linux/man/9-devm_iio_trigger_alloc/"
description: "devm_iio_trigger_alloc – Resource-managed iio_trigger_alloc"
---

<p>devm_iio_trigger_alloc &#8211; Resource-managed <code>iio_trigger_alloc</code></p>
<h2>Synopsis</h2>
<pre><code>struct iio_trigger *devm_iio_trigger_alloc(struct device *dev, const char *fmt, ...);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>Device to allocate iio_trigger for</dl>
<p> <i>fmt</i></p>
<dl>
<dd>trigger name format. If it includes format specifiers, the additional arguments following format are formatted and inserted in the resulting string replacing their respective specifiers.</dl>
<p> <i>&#8230;</i></p>
<dl>
<dd>variable arguments</dl>
<h2>Description</h2>
<p>Managed iio_trigger_alloc. iio_trigger allocated with this function is automatically freed on driver detach. </p>
<p> If an iio_trigger allocated with this function needs to be freed separately, <code>devm_iio_trigger_free</code> must be used.</p>
<h2>Return</h2>
<p>Pointer to allocated iio_trigger on success, NULL on failure.</p>
<h2>Author</h2>
<p><code>Daniel Baluta</code> &lt;daniel.baluta [at] intel.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
