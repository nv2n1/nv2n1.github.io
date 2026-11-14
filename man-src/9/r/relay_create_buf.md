---
title: "relay_create_buf(9)"
name: "relay_create_buf"
section: "9"
letter: "r"
url: "/docs/linux/man/9-relay_create_buf/"
description: "relay_create_buf – allocate and initialize a channel buffer"
---

<p>relay_create_buf &#8211; allocate and initialize a channel buffer</p>
<h2>Synopsis</h2>
<pre><code>struct rchan_buf *relay_create_buf(struct rchan *chan);</code></pre>
<h2>Arguments</h2>
<p><i>chan</i></p>
<dl>
<dd>
<dd>the relay channel</dl>
<h2>Description</h2>
<p>Returns channel buffer if successful, <code>NULL</code> otherwise.</p>
<h2>Copyright</h2>
