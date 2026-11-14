---
title: "ccw_device_get_mdc(9)"
name: "ccw_device_get_mdc"
section: "9"
letter: "c"
url: "/docs/linux/man/9-ccw_device_get_mdc/"
description: "ccw_device_get_mdc – accumulate max data count"
---

<p>ccw_device_get_mdc &#8211; accumulate max data count</p>
<h2>Synopsis</h2>
<pre><code>int ccw_device_get_mdc(struct ccw_device *cdev, u8 mask);</code></pre>
<h2>Arguments</h2>
<p><i>cdev</i></p>
<dl>
<dd>
<dd>ccw device for which the max data count is accumulated</dl>
<p> <i>mask</i></p>
<dl>
<dd>mask of paths to use</dl>
<h2>Description</h2>
<p>Return the number of 64K-bytes blocks all paths at least support for a transport command. Return values &lt;= 0 indicate failures.</p>
<h2>Author</h2>
<p><code>Cornelia Huck</code> &lt;cornelia.huck [at] de.ibm.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
