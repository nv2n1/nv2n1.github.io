---
title: "blk_rq_unmap_user(9)"
name: "blk_rq_unmap_user"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_rq_unmap_user/"
description: "blk_rq_unmap_user – unmap a request with user data"
---

<p>blk_rq_unmap_user &#8211; unmap a request with user data</p>
<h2>Synopsis</h2>
<pre><code>int blk_rq_unmap_user(struct bio *bio);</code></pre>
<h2>Arguments</h2>
<p><i>bio</i></p>
<dl>
<dd>
<dd>start of bio list</dl>
<h2>Description</h2>
<p>Unmap a rq previously mapped by <code>blk_rq_map_user</code>. The caller must supply the original rq-&gt;bio from the <code>blk_rq_map_user</code> return, since the I/O completion may have changed rq-&gt;bio.</p>
<h2>Copyright</h2>
