---
title: "snd_pcm_stop(9)"
name: "snd_pcm_stop"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_pcm_stop/"
---

snd_pcm_stop - try to stop all running streams in the substream group

<h2>Synopsis</h2>

<pre><code>int snd_pcm_stop(struct snd_pcm_substream *substream, snd_pcm_state_t state);</code></pre>

<h2>Arguments</h2>

<i>substream</i>
<dl><dd><dd>the PCM substream instance</dl>
 

 <i>state</i>
<dl><dd>PCM state after stopping the stream</dl>

<h2>Description</h2>

The state of each stream is then changed to the given state unconditionally.

<h2>Return</h2>

Zero if successful, or a negative error code.

<h2>Copyright</h2>


