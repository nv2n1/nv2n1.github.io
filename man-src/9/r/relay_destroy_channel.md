---
title: "relay_destroy_channel(9)"
name: "relay_destroy_channel"
section: "9"
letter: "r"
url: "/docs/linux/man/9-relay_destroy_channel/"
description: "relay_destroy_channel – free the channel struct"
---

<p>relay_destroy_channel &#8211; free the channel struct</p>
<h2>Synopsis</h2>
<pre><code>void relay_destroy_channel(struct kref *kref);</code></pre>
<h2>Arguments</h2>
<p><i>kref</i></p>
<dl>
<dd>
<dd>target kernel reference that contains the relay channel</dl>
<h2>Description</h2>
<p>Should only be called from <code>kref_put</code>.</p>
<h2>Copyright</h2>
