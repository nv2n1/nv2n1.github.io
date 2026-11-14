---
title: "snd_soc_component_async_complete(9)"
name: "snd_soc_component_async_complete"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_soc_component_async_complete/"
description: "snd_soc_component_async_complete – Ensure asynchronous I/O has completed"
---

<p>snd_soc_component_async_complete &#8211; Ensure asynchronous I/O has completed</p>
<h2>Synopsis</h2>
<pre><code>void snd_soc_component_async_complete(struct snd_soc_component *component);</code></pre>
<h2>Arguments</h2>
<p><i>component</i></p>
<dl>
<dd>
<dd>Component for which to wait</dl>
<h2>Description</h2>
<p>This function blocks until all asynchronous I/O which has previously been scheduled using <code>snd_soc_component_update_bits_async</code> has completed.</p>
<h2>Copyright</h2>
