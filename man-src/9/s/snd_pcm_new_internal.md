---
title: "snd_pcm_new_internal(9)"
name: "snd_pcm_new_internal"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_pcm_new_internal/"
description: "snd_pcm_new_internal – create a new internal PCM instance"
---

<p>snd_pcm_new_internal &#8211; create a new internal PCM instance</p>
<h2>Synopsis</h2>
<pre><code>int snd_pcm_new_internal(struct snd_card *card, const char *id, int device, int playback_count, int capture_count, struct snd_pcm **rpcm);</code></pre>
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
<dd>the device index (zero based &#8211; shared with normal PCMs)</dl>
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
<p>Creates a new internal PCM instance with no userspace device or procfs entries. This is used by ASoC Back End PCMs in order to create a PCM that will only be used internally by kernel drivers. i.e. it cannot be opened by userspace. It provides existing ASoC components drivers with a substream and access to any private data. </p>
<p> The pcm operators have to be set afterwards to the new instance via <code>snd_pcm_set_ops</code>.</p>
<h2>Return</h2>
<p>Zero if successful, or a negative error code on failure.</p>
<h2>Copyright</h2>
