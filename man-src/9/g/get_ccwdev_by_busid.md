---
title: "get_ccwdev_by_busid(9)"
name: "get_ccwdev_by_busid"
section: "9"
letter: "g"
url: "/docs/linux/man/9-get_ccwdev_by_busid/"
description: "get_ccwdev_by_busid – obtain device from a bus id"
---

<p>get_ccwdev_by_busid &#8211; obtain device from a bus id</p>
<h2>Synopsis</h2>
<pre><code>struct ccw_device *get_ccwdev_by_busid(struct ccw_driver *cdrv, const char *bus_id);</code></pre>
<h2>Arguments</h2>
<p><i>cdrv</i></p>
<dl>
<dd>
<dd>driver the device is owned by</dl>
<p> <i>bus_id</i></p>
<dl>
<dd>bus id of the device to be searched</dl>
<h2>Description</h2>
<p>This function searches all devices owned by <i>cdrv</i> for a device with a bus id matching <i>bus_id</i>.</p>
<h2>Return</h2>
<p>If a match is found, its reference count of the found device is increased and it is returned; else <code>NULL</code> is returned.</p>
<h2>Author</h2>
<p><code>Cornelia Huck</code> &lt;cornelia.huck [at] de.ibm.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
