---
title: "ccw_device_tm_intrg(9)"
name: "ccw_device_tm_intrg"
section: "9"
letter: "c"
url: "/docs/linux/man/9-ccw_device_tm_intrg/"
description: "ccw_device_tm_intrg – perform interrogate function"
---

<p>ccw_device_tm_intrg &#8211; perform interrogate function</p>
<h2>Synopsis</h2>
<pre><code>int ccw_device_tm_intrg(struct ccw_device *cdev);</code></pre>
<h2>Arguments</h2>
<p><i>cdev</i></p>
<dl>
<dd>
<dd>ccw device on which to perform the interrogate function</dl>
<h2>Description</h2>
<p>Perform an interrogate function on the given ccw device. Return zero on success, non-zero otherwise.</p>
<h2>Author</h2>
<p><code>Cornelia Huck</code> &lt;cornelia.huck [at] de.ibm.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
