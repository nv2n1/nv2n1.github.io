---
title: "rq_flush_dcache_pages(9)"
name: "rq_flush_dcache_pages"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rq_flush_dcache_pages/"
---

rq_flush_dcache_pages - Helper function to flush all pages in a request

<h2>Synopsis</h2>

<pre><code>void rq_flush_dcache_pages(struct request *rq);</code></pre>

<h2>Arguments</h2>

<i>rq</i>
<dl><dd><dd>the request to be flushed</dl>

<h2>Description</h2>

Flush all pages in <i>rq</i>.

<h2>Copyright</h2>


