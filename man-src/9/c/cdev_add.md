---
title: "cdev_add(9)"
name: "cdev_add"
section: "9"
letter: "c"
url: "/docs/linux/man/9-cdev_add/"
description: "cdev_add – add a char device to the system"
---

<p>cdev_add &#8211; add a char device to the system</p>
<h2>Synopsis</h2>
<pre><code>int cdev_add(struct cdev *p, dev_t dev, unsigned count);</code></pre>
<h2>Arguments</h2>
<p><i>p</i></p>
<dl>
<dd>
<dd>the cdev structure for the device</dl>
<p> <i>dev</i></p>
<dl>
<dd>the first device number for which this device is responsible</dl>
<p> <i>count</i></p>
<dl>
<dd>the number of consecutive minor numbers corresponding to this device</dl>
<h2>Description</h2>
<p><code>cdev_add</code> adds the device represented by <i>p</i> to the system, making it live immediately. A negative error code is returned on failure.</p>
<h2>Copyright</h2>
