---
title: "idr_replace(9)"
name: "idr_replace"
section: "9"
letter: "i"
url: "/docs/linux/man/9-idr_replace/"
description: "idr_replace – replace pointer for given id"
---

<p>idr_replace &#8211; replace pointer for given id</p>
<h2>Synopsis</h2>
<pre><code>void *idr_replace(struct idr *idp, void *ptr, int id);</code></pre>
<h2>Arguments</h2>
<p><i>idp</i></p>
<dl>
<dd>
<dd>idr handle</dl>
<p> <i>ptr</i></p>
<dl>
<dd>pointer you want associated with the id</dl>
<p> <i>id</i></p>
<dl>
<dd>lookup key</dl>
<h2>Description</h2>
<p>Replace the pointer registered with an id and return the old value. A <code>-ENOENT</code> return indicates that <i>id</i> was not found. A <code>-EINVAL</code> return indicates that <i>id</i> was not within valid constraints. </p>
<p> The caller must serialize with writers.</p>
<h2>Copyright</h2>
