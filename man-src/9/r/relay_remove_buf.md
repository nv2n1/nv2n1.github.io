---
title: "relay_remove_buf(9)"
name: "relay_remove_buf"
section: "9"
letter: "r"
url: "/docs/linux/man/9-relay_remove_buf/"
description: "relay_remove_buf – remove a channel buffer"
---

<p>relay_remove_buf &#8211; remove a channel buffer</p>
<h2>Synopsis</h2>
<pre><code>void relay_remove_buf(struct kref *kref);</code></pre>
<h2>Arguments</h2>
<p><i>kref</i></p>
<dl>
<dd>
<dd>target kernel reference that contains the relay buffer</dl>
<h2>Description</h2>
<p>Removes the file from the filesystem, which also frees the rchan_buf_struct and the channel buffer. Should only be called from <code>kref_put</code>.</p>
<h2>Copyright</h2>
