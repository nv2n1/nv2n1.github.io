---
title: "cdev_del(9)"
name: "cdev_del"
section: "9"
letter: "c"
url: "/docs/linux/man/9-cdev_del/"
description: "cdev_del – remove a cdev from the system"
---

<p>cdev_del &#8211; remove a cdev from the system</p>
<h2>Synopsis</h2>
<pre><code>void cdev_del(struct cdev *p);</code></pre>
<h2>Arguments</h2>
<p><i>p</i></p>
<dl>
<dd>
<dd>the cdev structure to be removed</dl>
<h2>Description</h2>
<p><code>cdev_del</code> removes <i>p</i> from the system, possibly freeing the structure itself.</p>
<h2>Copyright</h2>
