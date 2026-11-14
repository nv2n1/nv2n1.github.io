---
title: "blk_start_plug(9)"
name: "blk_start_plug"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_start_plug/"
description: "blk_start_plug – initialize blk_plug and track it inside the task_struct"
---

<p>blk_start_plug &#8211; initialize blk_plug and track it inside the task_struct</p>
<h2>Synopsis</h2>
<pre><code>void blk_start_plug(struct blk_plug *plug);</code></pre>
<h2>Arguments</h2>
<p><i>plug</i></p>
<dl>
<dd>
<dd>The struct blk_plug that needs to be initialized</dl>
<h2>Description</h2>
<p>Tracking blk_plug inside the task_struct will help with auto-flushing the pending I/O should the task end up blocking between <code>blk_start_plug</code> and <code>blk_finish_plug</code>. This is important from a performance perspective, but also ensures that we don&#8217;t deadlock. For instance, if the task is blocking for a memory allocation, memory reclaim could end up wanting to free a page belonging to that request that is currently residing in our private plug. By flushing the pending I/O when the process goes to sleep, we avoid this kind of deadlock.</p>
<h2>Copyright</h2>
