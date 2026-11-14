---
title: "snd_ac97_write_cache(9)"
name: "snd_ac97_write_cache"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_ac97_write_cache/"
---

snd_ac97_write_cache - write a value on the given register and update the cache

<h2>Synopsis</h2>

<pre><code>void snd_ac97_write_cache(struct snd_ac97 *ac97, unsigned short reg, unsigned short value);</code></pre>

<h2>Arguments</h2>

<i>ac97</i>
<dl><dd><dd>the ac97 instance</dl>
 

 <i>reg</i>
<dl><dd>the register to change</dl>
 

 <i>value</i>
<dl><dd>the value to set</dl>

<h2>Description</h2>

Writes a value on the given register and updates the register cache. The cached values are used for the cached-read and the suspend/resume.

<h2>Copyright</h2>


