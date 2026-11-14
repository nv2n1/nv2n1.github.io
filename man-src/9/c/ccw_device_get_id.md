---
title: "ccw_device_get_id(9)"
name: "ccw_device_get_id"
section: "9"
letter: "c"
url: "/docs/linux/man/9-ccw_device_get_id/"
description: "ccw_device_get_id – obtain a ccw device id"
---

<p>ccw_device_get_id &#8211; obtain a ccw device id</p>
<h2>Synopsis</h2>
<pre><code>void ccw_device_get_id(struct ccw_device *cdev, struct ccw_dev_id *dev_id);</code></pre>
<h2>Arguments</h2>
<p><i>cdev</i></p>
<dl>
<dd>
<dd>device to obtain the id for</dl>
<p> <i>dev_id</i></p>
<dl>
<dd>where to fill in the values</dl>
<h2>Author</h2>
<p><code>Cornelia Huck</code> &lt;cornelia.huck [at] de.ibm.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
