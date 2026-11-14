---
title: "debug_object_init_on_stack(9)"
name: "debug_object_init_on_stack"
section: "9"
letter: "d"
url: "/docs/linux/man/9-debug_object_init_on_stack/"
description: "debug_object_init_on_stack – debug checks when an object on stack is initialized"
---

<p>debug_object_init_on_stack &#8211; debug checks when an object on stack is initialized</p>
<h2>Synopsis</h2>
<pre><code>void debug_object_init_on_stack(void *addr, struct debug_obj_descr *descr);</code></pre>
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
