---
title: "atapi_drain_needed(9)"
name: "atapi_drain_needed"
section: "9"
letter: "a"
url: "/docs/linux/man/9-atapi_drain_needed/"
description: "atapi_drain_needed – Check whether data transfer may overflow"
---

<p>atapi_drain_needed &#8211; Check whether data transfer may overflow</p>
<h2>Synopsis</h2>
<pre><code>int atapi_drain_needed(struct request *rq);</code></pre>
<h2>Arguments</h2>
<p><i>rq</i></p>
<dl>
<dd>
<dd>request to be checked</dl>
<h2>Description</h2>
<p>ATAPI commands which transfer variable length data to host might overflow due to application error or hardware bug. This function checks whether overflow should be drained and ignored for <i>request</i>. </p>
<p> LOCKING: None.</p>
<h2>Return</h2>
<p>1 if ; otherwise, 0.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
