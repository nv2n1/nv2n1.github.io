---
title: "ccw_device_set_options_mask(9)"
name: "ccw_device_set_options_mask"
section: "9"
letter: "c"
url: "/docs/linux/man/9-ccw_device_set_options_mask/"
description: "ccw_device_set_options_mask – set some options and unset the rest"
---

<p>ccw_device_set_options_mask &#8211; set some options and unset the rest</p>
<h2>Synopsis</h2>
<pre><code>int ccw_device_set_options_mask(struct ccw_device *cdev, unsigned long flags);</code></pre>
<h2>Arguments</h2>
<p><i>cdev</i></p>
<dl>
<dd>
<dd>device for which the options are to be set</dl>
<p> <i>flags</i></p>
<dl>
<dd>options to be set</dl>
<h2>Description</h2>
<p>All flags specified in <i>flags</i> are set, all flags not specified in <i>flags</i> are cleared.</p>
<h2>Return</h2>
<p><code>0</code> on success, &#8211;<code>EINVAL</code> on an invalid flag combination.</p>
<h2>Author</h2>
<p><code>Cornelia Huck</code> &lt;cornelia.huck [at] de.ibm.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
