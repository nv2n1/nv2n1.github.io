---
title: "snd_ac97_tune_hardware(9)"
name: "snd_ac97_tune_hardware"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_ac97_tune_hardware/"
---

snd_ac97_tune_hardware - tune up the hardware

<h2>Synopsis</h2>

<pre><code>int snd_ac97_tune_hardware(struct snd_ac97 *ac97, const struct ac97_quirk *quirk, const char *override);</code></pre>

<h2>Arguments</h2>

<i>ac97</i>
<dl><dd><dd>the ac97 instance</dl>
 

 <i>quirk</i>
<dl><dd>quirk list</dl>
 

 <i>override</i>
<dl><dd>explicit quirk value (overrides the list if non-NULL)</dl>

<h2>Description</h2>

Do some workaround for each pci device, such as renaming of the headphone (true line-out) control as "Master". The quirk-list must be terminated with a zero-filled entry.

<h2>Return</h2>

Zero if successful, or a negative error code on failure.

<h2>Copyright</h2>


