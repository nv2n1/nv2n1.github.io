---
title: "ccw_device_clear(9)"
name: "ccw_device_clear"
section: "9"
letter: "c"
url: "/docs/linux/man/9-ccw_device_clear/"
description: "ccw_device_clear – terminate I/O request processing"
---

<p>ccw_device_clear &#8211; terminate I/O request processing</p>
<h2>Synopsis</h2>
<pre><code>int ccw_device_clear(struct ccw_device *cdev, unsigned long intparm);</code></pre>
<h2>Arguments</h2>
<p><i>cdev</i></p>
<dl>
<dd>
<dd>target ccw device</dl>
<p> <i>intparm</i></p>
<dl>
<dd>interruption parameter; value is only used if no I/O is outstanding, otherwise the intparm associated with the I/O request is returned</dl>
<h2>Description</h2>
<p><code>ccw_device_clear</code> calls csch on <i>cdev</i>&#8216;s subchannel.</p>
<h2>Return</h2>
<p><code>0</code> on success, &#8211;<code>ENODEV</code> on device not operational, &#8211;<code>EINVAL</code> on invalid device state.</p>
<h2>Context</h2>
<p>Interrupts disabled, ccw device lock held</p>
<h2>Author</h2>
<p><code>Cornelia Huck</code> &lt;cornelia.huck [at] de.ibm.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
