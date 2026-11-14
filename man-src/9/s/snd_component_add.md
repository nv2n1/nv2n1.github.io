---
title: "snd_component_add(9)"
name: "snd_component_add"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_component_add/"
---

snd_component_add - add a component string

<h2>Synopsis</h2>

<pre><code>int snd_component_add(struct snd_card *card, const char *component);</code></pre>

<h2>Arguments</h2>

<i>card</i>
<dl><dd><dd>soundcard structure</dl>
 

 <i>component</i>
<dl><dd>the component id string</dl>

<h2>Description</h2>

This function adds the component id string to the supported list. The component can be referred from the alsa-lib.

<h2>Return</h2>

Zero otherwise a negative error code.

<h2>Copyright</h2>


