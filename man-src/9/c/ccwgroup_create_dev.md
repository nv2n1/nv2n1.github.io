---
title: "ccwgroup_create_dev(9)"
name: "ccwgroup_create_dev"
section: "9"
letter: "c"
url: "/docs/linux/man/9-ccwgroup_create_dev/"
description: "ccwgroup_create_dev – create and register a ccw group device"
---

<p>ccwgroup_create_dev &#8211; create and register a ccw group device</p>
<h2>Synopsis</h2>
<pre><code>int ccwgroup_create_dev(struct device *parent, struct ccwgroup_driver *gdrv, int num_devices, const char *buf);</code></pre>
<h2>Arguments</h2>
<p><i>parent</i></p>
<dl>
<dd>
<dd>parent device for the new device</dl>
<p> <i>gdrv</i></p>
<dl>
<dd>driver for the new group device</dl>
<p> <i>num_devices</i></p>
<dl>
<dd>number of slave devices</dl>
<p> <i>buf</i></p>
<dl>
<dd>buffer containing comma separated bus ids of slave devices</dl>
<h2>Description</h2>
<p>Create and register a new ccw group device as a child of <i>parent</i>. Slave devices are obtained from the list of bus ids given in <i>buf</i>.</p>
<h2>Return</h2>
<p><code>0</code> on success and an error code on failure.</p>
<h2>Context</h2>
<p>non-atomic</p>
<h2>Author</h2>
<p><code>Cornelia Huck</code> &lt;cornelia.huck [at] de.ibm.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
