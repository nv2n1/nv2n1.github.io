---
title: "ccw_device_set_options(9)"
name: "ccw_device_set_options"
section: "9"
letter: "c"
url: "/docs/linux/man/9-ccw_device_set_options/"
description: "ccw_device_set_options – set some options"
---

<p>ccw_device_set_options &#8211; set some options</p>
<h2>Synopsis</h2>
<pre><code>int ccw_device_set_options(struct ccw_device *cdev, unsigned long flags);</code></pre>
<h2>Arguments</h2>
<p><i>cdev</i></p>
<dl>
<dd>
<dd>device for which the options are to be set</dl>
<p> <i>flags</i></p>
<dl>
<dd>options to be set</dl>
<h2>Description</h2>
<p>All flags specified in <i>flags</i> are set, the remainder is left untouched.</p>
<h2>Return</h2>
<p><code>0</code> on success, &#8211;<code>EINVAL</code> if an invalid flag combination would ensue.</p>
<h2>Author</h2>
<p><code>Cornelia Huck</code> &lt;cornelia.huck [at] de.ibm.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
