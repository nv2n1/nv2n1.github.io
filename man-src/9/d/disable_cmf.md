---
title: "disable_cmf(9)"
name: "disable_cmf"
section: "9"
letter: "d"
url: "/docs/linux/man/9-disable_cmf/"
description: "disable_cmf – switch off the channel measurement for a specific device"
---

<p>disable_cmf &#8211; switch off the channel measurement for a specific device</p>
<h2>Synopsis</h2>
<pre><code>int disable_cmf(struct ccw_device *cdev);</code></pre>
<h2>Arguments</h2>
<p><i>cdev</i></p>
<dl>
<dd>
<dd>The ccw device to be disabled</dl>
<h2>Description</h2>
<p>Returns <code>0</code> for success or a negative error value.</p>
<h2>Context</h2>
<p>non-atomic</p>
<h2>Author</h2>
<p><code>Cornelia Huck</code> &lt;cornelia.huck [at] de.ibm.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
