---
title: "ccwgroup_set_online(9)"
name: "ccwgroup_set_online"
section: "9"
letter: "c"
url: "/docs/linux/man/9-ccwgroup_set_online/"
description: "ccwgroup_set_online – enable a ccwgroup device"
---

<p>ccwgroup_set_online &#8211; enable a ccwgroup device</p>
<h2>Synopsis</h2>
<pre><code>int ccwgroup_set_online(struct ccwgroup_device *gdev);</code></pre>
<h2>Arguments</h2>
<p><i>gdev</i></p>
<dl>
<dd>
<dd>target ccwgroup device</dl>
<h2>Description</h2>
<p>This function attempts to put the ccwgroup device into the online state.</p>
<h2>Return</h2>
<p><code>0</code> on success and a negative error value on failure.</p>
<h2>Author</h2>
<p><code>Cornelia Huck</code> &lt;cornelia.huck [at] de.ibm.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
