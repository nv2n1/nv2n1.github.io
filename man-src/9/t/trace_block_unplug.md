---
title: "trace_block_unplug(9)"
name: "trace_block_unplug"
section: "9"
letter: "t"
url: "/docs/linux/man/9-trace_block_unplug/"
description: "trace_block_unplug – release of operations requests in request queue"
---

<p>trace_block_unplug &#8211; release of operations requests in request queue</p>
<h2>Synopsis</h2>
<pre><code>void trace_block_unplug(struct request_queue *q, unsigned int depth, bool explicit);</code></pre>
<h2>Arguments</h2>
<p><i>q</i></p>
<dl>
<dd>
</dd><dd>request queue to unplug</dd></dl>
<p> <i>depth</i></p>
<dl>
<dd>number of requests just added to the queue</dd></dl>
<p> <i>explicit</i></p>
<dl>
<dd>whether this was an explicit unplug, or one from <code>schedule</code></dd></dl>
<h2>Description</h2>
<p>Unplug request queue <i>q</i> because device driver is scheduled to work on elements in the request queue.</p>
<h2>Authors</h2>
<p><code>Jason Baron</code> &lt;jbaron [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dd></dl>
<p> <code>William Cohen</code> &lt;wcohen [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dd></dl>
<h2>Copyright</h2>
