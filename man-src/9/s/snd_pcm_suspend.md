---
title: "snd_pcm_suspend(9)"
name: "snd_pcm_suspend"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_pcm_suspend/"
description: "snd_pcm_suspend – trigger SUSPEND to all linked streams"
---

<p>snd_pcm_suspend &#8211; trigger SUSPEND to all linked streams</p>
<h2>Synopsis</h2>
<pre><code>int snd_pcm_suspend(struct snd_pcm_substream *substream);</code></pre>
<h2>Arguments</h2>
<p><i>substream</i></p>
<dl>
<dd>
<dd>the PCM substream</dl>
<h2>Description</h2>
<p>After this call, all streams are changed to SUSPENDED state.</p>
<h2>Return</h2>
<p>Zero if successful (or <i>substream</i> is <code>NULL</code>), or a negative error code.</p>
<h2>Copyright</h2>
