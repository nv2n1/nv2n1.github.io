---
title: "cmf_readall(9)"
name: "cmf_readall"
section: "9"
letter: "c"
url: "/docs/linux/man/9-cmf_readall/"
description: "cmf_readall – read the current channel measurement block"
---

<p>cmf_readall &#8211; read the current channel measurement block</p>
<h2>Synopsis</h2>
<pre><code>int cmf_readall(struct ccw_device *cdev, struct cmbdata *data);</code></pre>
<h2>Arguments</h2>
<p><i>cdev</i></p>
<dl>
<dd>
<dd>the channel to be read</dl>
<p> <i>data</i></p>
<dl>
<dd>a pointer to a data block that will be filled</dl>
<h2>Description</h2>
<p>Returns <code>0</code> on success, a negative error value otherwise.</p>
<h2>Context</h2>
<p>any</p>
<h2>Author</h2>
<p><code>Cornelia Huck</code> &lt;cornelia.huck [at] de.ibm.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
