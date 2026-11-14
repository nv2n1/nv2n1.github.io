---
title: "trace_block_getrq(9)"
name: "trace_block_getrq"
section: "9"
letter: "t"
url: "/docs/linux/man/9-trace_block_getrq/"
description: "trace_block_getrq – get a free request entry in queue for block IO operations"
---

<p>trace_block_getrq &#8211; get a free request entry in queue for block IO operations</p>
<h2>Synopsis</h2>
<pre><code>void trace_block_getrq(struct request_queue *q, struct bio *bio, int rw);</code></pre>
<h2>Arguments</h2>
<p><i>q</i></p>
<dl>
<dd>
<dd>queue for operations</dl>
<p> <i>bio</i></p>
<dl>
<dd>pending block IO operation</dl>
<p> <i>rw</i></p>
<dl>
<dd>low bit indicates a read (<code>0</code>) or a write (<code>1</code>)</dl>
<h2>Description</h2>
<p>A request struct for queue <i>q</i> has been allocated to handle the block IO operation <i>bio</i>.</p>
<h2>Authors</h2>
<p><code>Jason Baron</code> &lt;jbaron [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>William Cohen</code> &lt;wcohen [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
