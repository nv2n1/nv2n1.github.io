---
title: "snd_soc_component_write(9)"
name: "snd_soc_component_write"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_soc_component_write/"
---

snd_soc_component_write - Write register value

<h2>Synopsis</h2>

<pre><code>int snd_soc_component_write(struct snd_soc_component *component, unsigned int reg, unsigned int val);</code></pre>

<h2>Arguments</h2>

<i>component</i>
<dl><dd><dd>Component to write to</dl>
 

 <i>reg</i>
<dl><dd>Register to write</dl>
 

 <i>val</i>
<dl><dd>Value to write to the register</dl>

<h2>Return</h2>

0 on success, a negative error code otherwise.

<h2>Copyright</h2>


