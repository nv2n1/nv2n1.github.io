---
title: "snd_ac97_pcm_close(9)"
name: "snd_ac97_pcm_close"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_ac97_pcm_close/"
---

snd_ac97_pcm_close - closes the given AC97 pcm

<h2>Synopsis</h2>

<pre><code>int snd_ac97_pcm_close(struct ac97_pcm *pcm);</code></pre>

<h2>Arguments</h2>

<i>pcm</i>
<dl><dd><dd>the ac97 pcm instance</dl>

<h2>Description</h2>

It frees the locked AC97 slots.

<h2>Return</h2>

Zero.

<h2>Copyright</h2>


