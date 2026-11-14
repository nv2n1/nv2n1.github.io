---
title: "snd_card_free(9)"
name: "snd_card_free"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_card_free/"
---

snd_card_free - frees given soundcard structure

<h2>Synopsis</h2>

<pre><code>int snd_card_free(struct snd_card *card);</code></pre>

<h2>Arguments</h2>

<i>card</i>
<dl><dd><dd>soundcard structure</dl>

<h2>Description</h2>

This function releases the soundcard structure and the all assigned devices automatically. That is, you don't have to release the devices by yourself. 

 This function waits until the all resources are properly released.

<h2>Return</h2>

Zero. Frees all associated devices and frees the control interface associated to given soundcard.

<h2>Copyright</h2>


