---
title: "ccwgroup_remove_ccwdev(9)"
name: "ccwgroup_remove_ccwdev"
section: "9"
letter: "c"
url: "/docs/linux/man/9-ccwgroup_remove_ccwdev/"
description: "ccwgroup_remove_ccwdev – remove function for slave devices"
---

<p>ccwgroup_remove_ccwdev &#8211; remove function for slave devices</p>
<h2>Synopsis</h2>
<pre><code>void ccwgroup_remove_ccwdev(struct ccw_device *cdev);</code></pre>
<h2>Arguments</h2>
<p><i>cdev</i></p>
<dl>
<dd>
<dd>ccw device to be removed</dl>
<h2>Description</h2>
<p>This is a remove function for ccw devices that are slave devices in a ccw group device. It sets the ccw device offline and also deregisters the embedding ccw group device.</p>
<h2>Author</h2>
<p><code>Cornelia Huck</code> &lt;cornelia.huck [at] de.ibm.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
