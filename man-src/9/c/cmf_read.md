---
title: "cmf_read(9)"
name: "cmf_read"
section: "9"
letter: "c"
url: "/docs/linux/man/9-cmf_read/"
description: "cmf_read – read one value from the current channel measurement block"
---

<p>cmf_read &#8211; read one value from the current channel measurement block</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>u64 cmf_read(struct ccw_device&nbsp;<wbr>*&nbsp;<wbr></code><i>cdev</i><code>, int&nbsp;<wbr></code><i>index</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>cdev</i></p>
<dl>
<dd>
<dd>the channel to be read</dl>
<p> <i>index</i></p>
<dl>
<dd>the index of the value to be read</dl>
<h2>Description</h2>
<p>Returns the value read or <code>0</code> if the value cannot be read.</p>
<h2>Context</h2>
<p>any</p>
<h2>Author</h2>
<p><code>Cornelia Huck</code> &lt;cornelia.huck [at] de.ibm.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
