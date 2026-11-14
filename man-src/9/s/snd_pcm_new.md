---
title: "snd_pcm_new(9)"
name: "snd_pcm_new"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_pcm_new/"
description: "snd_pcm_new – create a new PCM instance"
---

<p>snd_pcm_new &#8211; create a new PCM instance</p>
<h2>Synopsis</h2>
<pre><code>int snd_pcm_new(struct snd_card *card, const char *id, int device, int playback_count, int capture_count, struct snd_pcm **rpcm);</code></pre>
<h2>Arguments</h2>
<p><i>card</i></p>
<dl>
<dd>
<dd>the card instance</dl>
<p> <i>id</i></p>
<dl>
<dd>the id string</dl>
<p> <i>device</i></p>
<dl>
<dd>the device index (zero based)</dl>
<p> <i>playback_count</i></p>
<dl>
<dd>the number of substreams for playback</dl>
<p> <i>capture_count</i></p>
<dl>
<dd>the number of substreams for capture</dl>
<p> <i>rpcm</i></p>
<dl>
<dd>the pointer to store the new pcm instance</dl>
<h2>Description</h2>
<p>Creates a new PCM instance. </p>
<p> The pcm operators have to be set afterwards to the new instance via <code>snd_pcm_set_ops</code>.</p>
<h2>Return</h2>
<p>Zero if successful, or a negative error code on failure.</p>
<h2>Copyright</h2>
