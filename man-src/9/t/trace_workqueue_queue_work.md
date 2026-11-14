---
title: "trace_workqueue_queue_work(9)"
name: "trace_workqueue_queue_work"
section: "9"
letter: "t"
url: "/docs/linux/man/9-trace_workqueue_queue_work/"
description: "trace_workqueue_queue_work – called when a work gets queued"
---

<p>trace_workqueue_queue_work &#8211; called when a work gets queued</p>
<h2>Synopsis</h2>
<pre><code>void trace_workqueue_queue_work(unsigned int req_cpu, struct pool_workqueue *pwq, struct work_struct *work);</code></pre>
<h2>Arguments</h2>
<p><i>req_cpu</i></p>
<dl>
<dd>
<dd>the requested cpu</dl>
<p> <i>pwq</i></p>
<dl>
<dd>pointer to struct pool_workqueue</dl>
<p> <i>work</i></p>
<dl>
<dd>pointer to struct work_struct</dl>
<h2>Description</h2>
<p>This event occurs when a work is queued immediately or once a delayed work is actually queued on a workqueue (ie: once the delay has been reached).</p>
<h2>Authors</h2>
<p><code>Jason Baron</code> &lt;jbaron [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>William Cohen</code> &lt;wcohen [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
