---
title: "snd_ac97_read(9)"
name: "snd_ac97_read"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_ac97_read/"
---

snd_ac97_read - read a value from the given register

<h2>Synopsis</h2>

<pre><code>unsigned short snd_ac97_read(struct snd_ac97 *ac97, unsigned short reg);</code></pre>

<h2>Arguments</h2>

<i>ac97</i>
<dl><dd><dd>the ac97 instance</dl>
 

 <i>reg</i>
<dl><dd>the register to read</dl>

<h2>Description</h2>

Reads a value from the given register. This will invoke the read callback directly after the register check.

<h2>Return</h2>

The read value.

<h2>Copyright</h2>


