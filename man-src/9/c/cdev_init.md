---
title: "cdev_init(9)"
name: "cdev_init"
section: "9"
letter: "c"
url: "/docs/linux/man/9-cdev_init/"
description: "cdev_init – initialize a cdev structure"
---

<p>cdev_init &#8211; initialize a cdev structure</p>
<h2>Synopsis</h2>
<pre><code>void cdev_init(struct cdev *cdev, const struct file_operations *fops);</code></pre>
<h2>Arguments</h2>
<p><i>cdev</i></p>
<dl>
<dd>
<dd>the structure to initialize</dl>
<p> <i>fops</i></p>
<dl>
<dd>the file_operations for this device</dl>
<h2>Description</h2>
<p>Initializes <i>cdev</i>, remembering <i>fops</i>, making it ready to add to the system with <code>cdev_add</code>.</p>
<h2>Copyright</h2>
