---
title: "trace_block_sleeprq(9)"
name: "trace_block_sleeprq"
section: "9"
letter: "t"
url: "/docs/linux/man/9-trace_block_sleeprq/"
description: "trace_block_sleeprq – waiting to get a free request entry in queue for block IO operation"
---

<p>trace_block_sleeprq &#8211; waiting to get a free request entry in queue for block IO operation</p>
<h2>Synopsis</h2>
<pre><code>void trace_block_sleeprq(struct request_queue *q, struct bio *bio, int rw);</code></pre>
<h2>Arguments</h2>
<p><i>q</i></p>
<dl>
<dd>
<dd>queue for operation</dl>
<p> <i>bio</i></p>
<dl>
<dd>pending block IO operation</dl>
<p> <i>rw</i></p>
<dl>
<dd>low bit indicates a read (<code>0</code>) or a write (<code>1</code>)</dl>
<h2>Description</h2>
<p>In the case where a request struct cannot be provided for queue <i>q</i> the process needs to wait for an request struct to become available. This tracepoint event is generated each time the process goes to sleep waiting for request struct become available.</p>
<h2>Authors</h2>
<p><code>Jason Baron</code> &lt;jbaron [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>William Cohen</code> &lt;wcohen [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
