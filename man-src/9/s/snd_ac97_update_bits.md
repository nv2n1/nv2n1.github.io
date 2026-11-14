---
title: "snd_ac97_update_bits(9)"
name: "snd_ac97_update_bits"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_ac97_update_bits/"
---

snd_ac97_update_bits - update the bits on the given register

<h2>Synopsis</h2>

<pre><code>int snd_ac97_update_bits(struct snd_ac97 *ac97, unsigned short reg, unsigned short mask, unsigned short value);</code></pre>

<h2>Arguments</h2>

<i>ac97</i>
<dl><dd><dd>the ac97 instance</dl>
 

 <i>reg</i>
<dl><dd>the register to change</dl>
 

 <i>mask</i>
<dl><dd>the bit-mask to change</dl>
 

 <i>value</i>
<dl><dd>the value to set</dl>

<h2>Description</h2>

Updates the masked-bits on the given register only when the value is changed.

<h2>Return</h2>

1 if the bits are changed, 0 if no change, or a negative code on failure.

<h2>Copyright</h2>


