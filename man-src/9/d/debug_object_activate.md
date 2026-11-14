---
title: "debug_object_activate(9)"
name: "debug_object_activate"
section: "9"
letter: "d"
url: "/docs/linux/man/9-debug_object_activate/"
description: "debug_object_activate – debug checks when an object is activated"
---

<p>debug_object_activate &#8211; debug checks when an object is activated</p>
<h2>Synopsis</h2>
<pre><code>int debug_object_activate(void *addr, struct debug_obj_descr *descr);</code></pre>
<h2>Arguments</h2>
<p><i>addr</i></p>
<dl>
<dd>
<dd>address of the object</dl>
<p> <i>descr</i></p>
<dl>
<dd>pointer to an object specific debug description structure Returns 0 for success, -EINVAL for check failed.</dl>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
