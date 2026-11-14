---
title: "snd_card_register(9)"
name: "snd_card_register"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_card_register/"
---

snd_card_register - register the soundcard

<h2>Synopsis</h2>

<pre><code>int snd_card_register(struct snd_card *card);</code></pre>

<h2>Arguments</h2>

<i>card</i>
<dl><dd><dd>soundcard structure</dl>

<h2>Description</h2>

This function registers all the devices assigned to the soundcard. Until calling this, the ALSA control interface is blocked from the external accesses. Thus, you should call this function at the end of the initialization of the card.

<h2>Return</h2>

Zero otherwise a negative error code if the registration failed.

<h2>Copyright</h2>


