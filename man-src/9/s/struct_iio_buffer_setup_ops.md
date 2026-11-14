---
title: "struct_iio_buffer_setup_ops(9)"
name: "struct_iio_buffer_setup_ops"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_iio_buffer_setup_ops/"
description: "struct_iio_buffer_setup_ops – buffer setup related callbacks"
---

<p>struct_iio_buffer_setup_ops &#8211; buffer setup related callbacks</p>
<h2>Synopsis</h2>
<pre><code>struct iio_buffer_setup_ops {
    int (*preenable)(struct iio_dev *);
    int (*postenable)(struct iio_dev *);
    int (*predisable)(struct iio_dev *);
    int (*postdisable)(struct iio_dev *);
    bool (*validate_scan_mask)(struct iio_dev *indio_dev, const unsigned long *scan_mask);
};</code></pre>
<h2>Members</h2>
<p>preenable</p>
<dl>
<dd>[DRIVER] function to run prior to marking buffer enabled</dl>
<p> postenable</p>
<dl>
<dd>[DRIVER] function to run after marking buffer enabled</dl>
<p> predisable</p>
<dl>
<dd>[DRIVER] function to run prior to marking buffer disabled</dl>
<p> postdisable</p>
<dl>
<dd>[DRIVER] function to run after marking buffer disabled</dl>
<p> validate_scan_mask</p>
<dl>
<dd>[DRIVER] function callback to check whether a given scan mask is valid for the device.</dl>
<h2>Author</h2>
<p><code>Daniel Baluta</code> &lt;daniel.baluta [at] intel.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
