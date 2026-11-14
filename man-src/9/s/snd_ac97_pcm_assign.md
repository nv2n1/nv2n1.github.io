---
title: "snd_ac97_pcm_assign(9)"
name: "snd_ac97_pcm_assign"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_ac97_pcm_assign/"
---

snd_ac97_pcm_assign - assign AC97 slots to given PCM streams

<h2>Synopsis</h2>

<pre><code>int snd_ac97_pcm_assign(struct snd_ac97_bus *bus, unsigned short pcms_count, const struct ac97_pcm *pcms);</code></pre>

<h2>Arguments</h2>

<i>bus</i>
<dl><dd><dd>the ac97 bus instance</dl>
 

 <i>pcms_count</i>
<dl><dd>count of PCMs to be assigned</dl>
 

 <i>pcms</i>
<dl><dd>PCMs to be assigned</dl>

<h2>Description</h2>

It assigns available AC97 slots for given PCMs. If none or only some slots are available, pcm-&gt;xxx.slots and pcm-&gt;xxx.rslots[] members are reduced and might be zero.

<h2>Return</h2>

Zero if successful, or a negative error code on failure.

<h2>Copyright</h2>


