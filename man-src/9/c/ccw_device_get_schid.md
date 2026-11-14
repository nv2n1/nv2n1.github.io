---
title: "ccw_device_get_schid(9)"
name: "ccw_device_get_schid"
section: "9"
letter: "c"
url: "/docs/linux/man/9-ccw_device_get_schid/"
description: "ccw_device_get_schid – obtain a subchannel id"
---

<p>ccw_device_get_schid &#8211; obtain a subchannel id</p>
<h2>Synopsis</h2>
<pre><code>void ccw_device_get_schid(struct ccw_device *cdev, struct subchannel_id *schid);</code></pre>
<h2>Arguments</h2>
<p><i>cdev</i></p>
<dl>
<dd>
<dd>device to obtain the id for</dl>
<p> <i>schid</i></p>
<dl>
<dd>where to fill in the values</dl>
<h2>Author</h2>
<p><code>Cornelia Huck</code> &lt;cornelia.huck [at] de.ibm.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
