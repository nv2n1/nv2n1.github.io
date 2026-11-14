---
title: "get_ccwdev_by_dev_id(9)"
name: "get_ccwdev_by_dev_id"
section: "9"
letter: "g"
url: "/docs/linux/man/9-get_ccwdev_by_dev_id/"
description: "get_ccwdev_by_dev_id – obtain device from a ccw device id"
---

<p>get_ccwdev_by_dev_id &#8211; obtain device from a ccw device id</p>
<h2>Synopsis</h2>
<pre><code>struct ccw_device *get_ccwdev_by_dev_id(struct ccw_dev_id *dev_id);</code></pre>
<h2>Arguments</h2>
<p><i>dev_id</i></p>
<dl>
<dd>
<dd>id of the device to be searched</dl>
<h2>Description</h2>
<p>This function searches all devices attached to the ccw bus for a device matching <i>dev_id</i>.</p>
<h2>Return</h2>
<p>If a device is found its reference count is increased and returned; else <code>NULL</code> is returned.</p>
<h2>Author</h2>
<p><code>Cornelia Huck</code> &lt;cornelia.huck [at] de.ibm.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
