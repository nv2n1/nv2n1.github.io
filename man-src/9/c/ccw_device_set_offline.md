---
title: "ccw_device_set_offline(9)"
name: "ccw_device_set_offline"
section: "9"
letter: "c"
url: "/docs/linux/man/9-ccw_device_set_offline/"
description: "ccw_device_set_offline – disable a ccw device for I/O"
---

<p>ccw_device_set_offline &#8211; disable a ccw device for I/O</p>
<h2>Synopsis</h2>
<pre><code>int ccw_device_set_offline(struct ccw_device *cdev);</code></pre>
<h2>Arguments</h2>
<p><i>cdev</i></p>
<dl>
<dd>
<dd>target ccw device</dl>
<h2>Description</h2>
<p>This function calls the driver&#8217;s <code>set_offline</code> function for <i>cdev</i>, if given, and then disables <i>cdev</i>.</p>
<h2>Return</h2>
<p><code>0</code> on success and a negative error value on failure.</p>
<h2>Context</h2>
<p>enabled, ccw device lock not held</p>
<h2>Author</h2>
<p><code>Cornelia Huck</code> &lt;cornelia.huck [at] de.ibm.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
