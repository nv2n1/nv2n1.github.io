---
title: "snd_ac97_pcm_open(9)"
name: "snd_ac97_pcm_open"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_ac97_pcm_open/"
---

snd_ac97_pcm_open - opens the given AC97 pcm

<h2>Synopsis</h2>

<pre><code>int snd_ac97_pcm_open(struct ac97_pcm *pcm, unsigned int rate, enum ac97_pcm_cfg cfg, unsigned short slots);</code></pre>

<h2>Arguments</h2>

<i>pcm</i>
<dl><dd><dd>the ac97 pcm instance</dl>
 

 <i>rate</i>
<dl><dd>rate in Hz, if codec does not support VRA, this value must be 48000Hz</dl>
 

 <i>cfg</i>
<dl><dd>output stream characteristics</dl>
 

 <i>slots</i>
<dl><dd>a subset of allocated slots (snd_ac97_pcm_assign) for this pcm</dl>

<h2>Description</h2>

It locks the specified slots and sets the given rate to AC97 registers.

<h2>Return</h2>

Zero if successful, or a negative error code on failure.

<h2>Copyright</h2>


