---
title: "ccw_device_resume(9)"
name: "ccw_device_resume"
section: "9"
letter: "c"
url: "/docs/linux/man/9-ccw_device_resume/"
description: "ccw_device_resume – resume channel program execution"
---

<p>ccw_device_resume &#8211; resume channel program execution</p>
<h2>Synopsis</h2>
<pre><code>int ccw_device_resume(struct ccw_device *cdev);</code></pre>
<h2>Arguments</h2>
<p><i>cdev</i></p>
<dl>
<dd>
<dd>target ccw device</dl>
<h2>Description</h2>
<p><code>ccw_device_resume</code> calls rsch on <i>cdev</i>&#8216;s subchannel.</p>
<h2>Return</h2>
<p><code>0</code> on success, &#8211;<code>ENODEV</code> on device not operational, &#8211;<code>EINVAL</code> on invalid device state, &#8211;<code>EBUSY</code> on device busy or interrupt pending.</p>
<h2>Context</h2>
<p>Interrupts disabled, ccw device lock held</p>
<h2>Author</h2>
<p><code>Cornelia Huck</code> &lt;cornelia.huck [at] de.ibm.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
