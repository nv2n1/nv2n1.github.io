---
title: "ida_get_new_above(9)"
name: "ida_get_new_above"
section: "9"
letter: "i"
url: "/docs/linux/man/9-ida_get_new_above/"
description: "ida_get_new_above – allocate new ID above or equal to a start id"
---

<p>ida_get_new_above &#8211; allocate new ID above or equal to a start id</p>
<h2>Synopsis</h2>
<pre><code>int ida_get_new_above(struct ida *ida, int starting_id, int *p_id);</code></pre>
<h2>Arguments</h2>
<p><i>ida</i></p>
<dl>
<dd>
<dd>ida handle</dl>
<p> <i>starting_id</i></p>
<dl>
<dd>id to start search at</dl>
<p> <i>p_id</i></p>
<dl>
<dd>pointer to the allocated handle</dl>
<h2>Description</h2>
<p>Allocate new ID above or equal to <i>starting_id</i>. It should be called with any required locks. </p>
<p> If memory is required, it will return <code>-EAGAIN</code>, you should unlock and go back to the <code>ida_pre_get</code> call. If the ida is full, it will return <code>-ENOSPC</code>. </p>
<p> <i>p_id</i> returns a value in the range <i>starting_id</i> &#8230; <code>0x7fffffff</code>.</p>
<h2>Copyright</h2>
