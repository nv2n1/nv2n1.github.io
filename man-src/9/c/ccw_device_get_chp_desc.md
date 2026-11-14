---
title: "ccw_device_get_chp_desc(9)"
name: "ccw_device_get_chp_desc"
section: "9"
letter: "c"
url: "/docs/linux/man/9-ccw_device_get_chp_desc/"
description: "ccw_device_get_chp_desc – return newly allocated channel-path descriptor"
---

<p>ccw_device_get_chp_desc &#8211; return newly allocated channel-path descriptor</p>
<h2>Synopsis</h2>
<pre><code>struct channel_path_desc *ccw_device_get_chp_desc(struct ccw_device *cdev, int chp_idx);</code></pre>
<h2>Arguments</h2>
<p><i>cdev</i></p>
<dl>
<dd>
<dd>device to obtain the descriptor for</dl>
<p> <i>chp_idx</i></p>
<dl>
<dd>index of the channel path</dl>
<h2>Description</h2>
<p>On success return a newly allocated copy of the channel-path description data associated with the given channel path. Return <code>NULL</code> on error.</p>
<h2>Author</h2>
<p><code>Cornelia Huck</code> &lt;cornelia.huck [at] de.ibm.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
