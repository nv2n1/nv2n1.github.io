---
title: "snd_ac97_update_power(9)"
name: "snd_ac97_update_power"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_ac97_update_power/"
---

snd_ac97_update_power - update the powerdown register

<h2>Synopsis</h2>

<pre><code>int snd_ac97_update_power(struct snd_ac97 *ac97, int reg, int powerup);</code></pre>

<h2>Arguments</h2>

<i>ac97</i>
<dl><dd><dd>the codec instance</dl>
 

 <i>reg</i>
<dl><dd>the rate register, e.g. AC97_PCM_FRONT_DAC_RATE</dl>
 

 <i>powerup</i>
<dl><dd>non-zero when power up the part</dl>

<h2>Description</h2>

Update the AC97 powerdown register bits of the given part.

<h2>Return</h2>

Zero.

<h2>Copyright</h2>


