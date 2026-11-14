---
title: "ccwgroup_probe_ccwdev(9)"
name: "ccwgroup_probe_ccwdev"
section: "9"
letter: "c"
url: "/docs/linux/man/9-ccwgroup_probe_ccwdev/"
description: "ccwgroup_probe_ccwdev – probe function for slave devices"
---

<p>ccwgroup_probe_ccwdev &#8211; probe function for slave devices</p>
<h2>Synopsis</h2>
<pre><code>int ccwgroup_probe_ccwdev(struct ccw_device *cdev);</code></pre>
<h2>Arguments</h2>
<p><i>cdev</i></p>
<dl>
<dd>
<dd>ccw device to be probed</dl>
<h2>Description</h2>
<p>This is a dummy probe function for ccw devices that are slave devices in a ccw group device.</p>
<h2>Return</h2>
<p>always <code>0</code></p>
<h2>Author</h2>
<p><code>Cornelia Huck</code> &lt;cornelia.huck [at] de.ibm.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
