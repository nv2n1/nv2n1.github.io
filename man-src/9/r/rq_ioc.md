---
title: "rq_ioc(9)"
name: "rq_ioc"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rq_ioc/"
description: "rq_ioc – determine io_context for request allocation"
---

<p>rq_ioc &#8211; determine io_context for request allocation</p>
<h2>Synopsis</h2>
<pre><code>struct io_context *rq_ioc(struct bio *bio);</code></pre>
<h2>Arguments</h2>
<p><i>bio</i></p>
<dl>
<dd>
<dd>request being allocated is for this bio (can be <code>NULL</code>)</dl>
<h2>Description</h2>
<p>Determine io_context to use for request allocation for <i>bio</i>. May return <code>NULL</code> if <code>current-</code>&gt;io_context doesn&#8217;t exist.</p>
<h2>Copyright</h2>
