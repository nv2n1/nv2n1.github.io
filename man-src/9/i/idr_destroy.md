---
title: "idr_destroy(9)"
name: "idr_destroy"
section: "9"
letter: "i"
url: "/docs/linux/man/9-idr_destroy/"
description: "idr_destroy – release all cached layers within an idr tree"
---

<p>idr_destroy &#8211; release all cached layers within an idr tree</p>
<h2>Synopsis</h2>
<pre><code>void idr_destroy(struct idr *idp);</code></pre>
<h2>Arguments</h2>
<p><i>idp</i></p>
<dl>
<dd>
<dd>idr handle</dl>
<h2>Description</h2>
<p>Free all id mappings and all idp_layers. After this function, <i>idp</i> is completely unused and can be freed / recycled. The caller is responsible for ensuring that no one else accesses <i>idp</i> during or after <code>idr_destroy</code>. </p>
<p> A typical clean-up sequence for objects stored in an idr tree will use <code>idr_for_each</code> to free all objects, if necessary, then <code>idr_destroy</code> to free up the id mappings and cached idr_layers.</p>
<h2>Copyright</h2>
