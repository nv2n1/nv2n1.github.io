---
title: "ccw_device_is_pathgroup(9)"
name: "ccw_device_is_pathgroup"
section: "9"
letter: "c"
url: "/docs/linux/man/9-ccw_device_is_pathgroup/"
description: "ccw_device_is_pathgroup – determine if paths to this device are grouped"
---

<p>ccw_device_is_pathgroup &#8211; determine if paths to this device are grouped</p>
<h2>Synopsis</h2>
<pre><code>int ccw_device_is_pathgroup(struct ccw_device *cdev);</code></pre>
<h2>Arguments</h2>
<p><i>cdev</i></p>
<dl>
<dd>
<dd>ccw device</dl>
<h2>Description</h2>
<p>Return non-zero if there is a path group, zero otherwise.</p>
<h2>Author</h2>
<p><code>Cornelia Huck</code> &lt;cornelia.huck [at] de.ibm.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
