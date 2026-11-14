---
title: "trace_workqueue_execute_start(9)"
name: "trace_workqueue_execute_start"
section: "9"
letter: "t"
url: "/docs/linux/man/9-trace_workqueue_execute_start/"
description: "trace_workqueue_execute_start – called immediately before the workqueue callback"
---

<p>trace_workqueue_execute_start &#8211; called immediately before the workqueue callback</p>
<h2>Synopsis</h2>
<pre><code>void trace_workqueue_execute_start(struct work_struct *work);</code></pre>
<h2>Arguments</h2>
<p><i>work</i></p>
<dl>
<dd>
<dd>pointer to struct work_struct</dl>
<h2>Description</h2>
<p>Allows to track workqueue execution.</p>
<h2>Authors</h2>
<p><code>Jason Baron</code> &lt;jbaron [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>William Cohen</code> &lt;wcohen [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
