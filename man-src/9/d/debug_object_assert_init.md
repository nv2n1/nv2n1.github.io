---
title: "debug_object_assert_init(9)"
name: "debug_object_assert_init"
section: "9"
letter: "d"
url: "/docs/linux/man/9-debug_object_assert_init/"
description: "debug_object_assert_init – debug checks when object should be init-ed"
---

<p>debug_object_assert_init &#8211; debug checks when object should be init-ed</p>
<h2>Synopsis</h2>
<pre><code>void debug_object_assert_init(void *addr, struct debug_obj_descr *descr);</code></pre>
<h2>Arguments</h2>
<p><i>addr</i></p>
<dl>
<dd>
<dd>address of the object</dl>
<p> <i>descr</i></p>
<dl>
<dd>pointer to an object specific debug description structure</dl>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
