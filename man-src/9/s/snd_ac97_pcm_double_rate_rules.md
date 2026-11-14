---
title: "snd_ac97_pcm_double_rate_rules(9)"
name: "snd_ac97_pcm_double_rate_rules"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_ac97_pcm_double_rate_rules/"
---

snd_ac97_pcm_double_rate_rules - set double rate constraints

<h2>Synopsis</h2>

<pre><code>int snd_ac97_pcm_double_rate_rules(struct snd_pcm_runtime *runtime);</code></pre>

<h2>Arguments</h2>

<i>runtime</i>
<dl><dd><dd>the runtime of the ac97 front playback pcm</dl>

<h2>Description</h2>

Installs the hardware constraint rules to prevent using double rates and more than two channels at the same time.

<h2>Return</h2>

Zero if successful, or a negative error code on failure.

<h2>Copyright</h2>


