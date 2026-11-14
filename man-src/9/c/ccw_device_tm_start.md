---
title: "ccw_device_tm_start(9)"
name: "ccw_device_tm_start"
section: "9"
letter: "c"
url: "/docs/linux/man/9-ccw_device_tm_start/"
description: "ccw_device_tm_start – perform start function"
---

<p>ccw_device_tm_start &#8211; perform start function</p>
<h2>Synopsis</h2>
<pre><code>int ccw_device_tm_start(struct ccw_device *cdev, struct tcw *tcw, unsigned long intparm, u8 lpm);</code></pre>
<h2>Arguments</h2>
<p><i>cdev</i></p>
<dl>
<dd>
<dd>ccw device on which to perform the start function</dl>
<p> <i>tcw</i></p>
<dl>
<dd>transport-command word to be started</dl>
<p> <i>intparm</i></p>
<dl>
<dd>user defined parameter to be passed to the interrupt handler</dl>
<p> <i>lpm</i></p>
<dl>
<dd>mask of paths to use</dl>
<h2>Description</h2>
<p>Start the tcw on the given ccw device. Return zero on success, non-zero otherwise.</p>
<h2>Author</h2>
<p><code>Cornelia Huck</code> &lt;cornelia.huck [at] de.ibm.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
