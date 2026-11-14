---
title: "snd_soc_component_read(9)"
name: "snd_soc_component_read"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_soc_component_read/"
---

snd_soc_component_read - Read register value

<h2>Synopsis</h2>

<pre><code>int snd_soc_component_read(struct snd_soc_component *component, unsigned int reg, unsigned int *val);</code></pre>

<h2>Arguments</h2>

<i>component</i>
<dl><dd><dd>Component to read from</dl>
 

 <i>reg</i>
<dl><dd>Register to read</dl>
 

 <i>val</i>
<dl><dd>Pointer to where the read value is stored</dl>

<h2>Return</h2>

0 on success, a negative error code otherwise.

<h2>Copyright</h2>


