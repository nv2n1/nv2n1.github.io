---
title: "snd_ac97_update(9)"
name: "snd_ac97_update"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_ac97_update/"
---

snd_ac97_update - update the value on the given register

<h2>Synopsis</h2>

<pre><code>int snd_ac97_update(struct snd_ac97 *ac97, unsigned short reg, unsigned short value);</code></pre>

<h2>Arguments</h2>

<i>ac97</i>
<dl><dd><dd>the ac97 instance</dl>
 

 <i>reg</i>
<dl><dd>the register to change</dl>
 

 <i>value</i>
<dl><dd>the value to set</dl>

<h2>Description</h2>

Compares the value with the register cache and updates the value only when the value is changed.

<h2>Return</h2>

1 if the value is changed, 0 if no change, or a negative code on failure.

<h2>Copyright</h2>


