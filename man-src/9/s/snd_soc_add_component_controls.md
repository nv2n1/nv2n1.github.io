---
title: "snd_soc_add_component_controls(9)"
name: "snd_soc_add_component_controls"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_soc_add_component_controls/"
---

snd_soc_add_component_controls - Add an array of controls to a component.

<h2>Synopsis</h2>

<pre><code>int snd_soc_add_component_controls(struct snd_soc_component *component, const struct snd_kcontrol_new *controls, unsigned int num_controls);</code></pre>

<h2>Arguments</h2>

<i>component</i>
<dl><dd><dd>Component to add controls to</dl>
 

 <i>controls</i>
<dl><dd>Array of controls to add</dl>
 

 <i>num_controls</i>
<dl><dd>Number of elements in the array</dl>

<h2>Return</h2>

0 for success, else error.

<h2>Copyright</h2>


