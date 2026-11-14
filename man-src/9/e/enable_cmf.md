---
title: "enable_cmf(9)"
name: "enable_cmf"
section: "9"
letter: "e"
url: "/docs/linux/man/9-enable_cmf/"
description: "enable_cmf – switch on the channel measurement for a specific device"
---

<p>enable_cmf &#8211; switch on the channel measurement for a specific device</p>
<h2>Synopsis</h2>
<pre><code>int enable_cmf(struct ccw_device *cdev);</code></pre>
<h2>Arguments</h2>
<p><i>cdev</i></p>
<dl>
<dd>
<dd>The ccw device to be enabled</dl>
<h2>Description</h2>
<p>Returns <code>0</code> for success or a negative error value.</p>
<h2>Note</h2>
<p>If this is called on a device for which channel measurement is already enabled a reset of the measurement data is triggered.</p>
<h2>Context</h2>
<p>non-atomic</p>
<h2>Author</h2>
<p><code>Cornelia Huck</code> &lt;cornelia.huck [at] de.ibm.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
