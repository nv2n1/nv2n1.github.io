---
title: "struct_iio_trigger_ops(9)"
name: "struct_iio_trigger_ops"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_iio_trigger_ops/"
description: "struct_iio_trigger_ops – operations structure for an iio_trigger."
---

<p>struct_iio_trigger_ops &#8211; operations structure for an iio_trigger.</p>
<h2>Synopsis</h2>
<pre><code>struct iio_trigger_ops {
    struct module *owner;
    int (*set_trigger_state)(struct iio_trigger *trig, bool state);
    int (*try_reenable)(struct iio_trigger *trig);
    int (*validate_device)(struct iio_trigger *trig, struct iio_dev *indio_dev);
};</code></pre>
<h2>Members</h2>
<p>owner</p>
<dl>
<dd>used to monitor usage count of the trigger.</dl>
<p> set_trigger_state</p>
<dl>
<dd>switch on/off the trigger on demand</dl>
<p> try_reenable</p>
<dl>
<dd>function to reenable the trigger when the use count is zero (may be NULL)</dl>
<p> validate_device</p>
<dl>
<dd>function to validate the device when the current trigger gets changed.</dl>
<h2>Description</h2>
<p>This is typically static const within a driver and shared by instances of a given device.</p>
<h2>Author</h2>
<p><code>Daniel Baluta</code> &lt;daniel.baluta [at] intel.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
