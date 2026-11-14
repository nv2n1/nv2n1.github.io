---
title: "trace_workqueue_activate_work(9)"
name: "trace_workqueue_activate_work"
section: "9"
letter: "t"
url: "/docs/linux/man/9-trace_workqueue_activate_work/"
description: "trace_workqueue_activate_work – called when a work gets activated"
---

<p>trace_workqueue_activate_work &#8211; called when a work gets activated</p>
<h2>Synopsis</h2>
<pre><code>void trace_workqueue_activate_work(struct work_struct *work);</code></pre>
<h2>Arguments</h2>
<p><i>work</i></p>
<dl>
<dd>
<dd>pointer to struct work_struct</dl>
<h2>Description</h2>
<p>This event occurs when a queued work is put on the active queue, which happens immediately after queueing unless <i>max_active</i> limit is reached.</p>
<h2>Authors</h2>
<p><code>Jason Baron</code> &lt;jbaron [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>William Cohen</code> &lt;wcohen [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
