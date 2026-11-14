---
title: "debug_object_active_state(9)"
name: "debug_object_active_state"
section: "9"
letter: "d"
url: "/docs/linux/man/9-debug_object_active_state/"
description: "debug_object_active_state – debug checks object usage state machine"
---

<p>debug_object_active_state &#8211; debug checks object usage state machine</p>
<h2>Synopsis</h2>
<pre><code>void debug_object_active_state(void *addr, struct debug_obj_descr *descr, unsigned int expect, unsigned int next);</code></pre>
<h2>Arguments</h2>
<p><i>addr</i></p>
<dl>
<dd>
<dd>address of the object</dl>
<p> <i>descr</i></p>
<dl>
<dd>pointer to an object specific debug description structure</dl>
<p> <i>expect</i></p>
<dl>
<dd>expected state</dl>
<p> <i>next</i></p>
<dl>
<dd>state to move to if expected state is found</dl>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
