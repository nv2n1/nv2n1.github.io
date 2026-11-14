---
title: "snd_pcm_stop_xrun(9)"
name: "snd_pcm_stop_xrun"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_pcm_stop_xrun/"
description: "snd_pcm_stop_xrun – stop the running streams as XRUN"
---

<p>snd_pcm_stop_xrun &#8211; stop the running streams as XRUN</p>
<h2>Synopsis</h2>
<pre><code>int snd_pcm_stop_xrun(struct snd_pcm_substream *substream);</code></pre>
<h2>Arguments</h2>
<p><i>substream</i></p>
<dl>
<dd>
<dd>the PCM substream instance</dl>
<h2>Description</h2>
<p>This stops the given running substream (and all linked substreams) as XRUN. Unlike <code>snd_pcm_stop</code>, this function takes the substream lock by itself.</p>
<h2>Return</h2>
<p>Zero if successful, or a negative error code.</p>
<h2>Copyright</h2>
