---
title: "ccw_device_siosl(9)"
name: "ccw_device_siosl"
section: "9"
letter: "c"
url: "/docs/linux/man/9-ccw_device_siosl/"
description: "ccw_device_siosl – initiate logging"
---

<p>ccw_device_siosl &#8211; initiate logging</p>
<h2>Synopsis</h2>
<pre><code>int ccw_device_siosl(struct ccw_device *cdev);</code></pre>
<h2>Arguments</h2>
<p><i>cdev</i></p>
<dl>
<dd>
<dd>ccw device</dl>
<h2>Description</h2>
<p>This function is used to invoke model-dependent logging within the channel subsystem.</p>
<h2>Author</h2>
<p><code>Cornelia Huck</code> &lt;cornelia.huck [at] de.ibm.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
