---
title: "trace_workqueue_execute_end(9)"
name: "trace_workqueue_execute_end"
section: "9"
letter: "t"
url: "/docs/linux/man/9-trace_workqueue_execute_end/"
description: "trace_workqueue_execute_end – called immediately after the workqueue callback"
---

<p>trace_workqueue_execute_end &#8211; called immediately after the workqueue callback</p>
<h2>Synopsis</h2>
<pre><code>void trace_workqueue_execute_end(struct work_struct *work);</code></pre>
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
