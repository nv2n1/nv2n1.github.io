---
title: "snd_card_set_id(9)"
name: "snd_card_set_id"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_card_set_id/"
---

snd_card_set_id - set card identification name

<h2>Synopsis</h2>

<pre><code>void snd_card_set_id(struct snd_card *card, const char *nid);</code></pre>

<h2>Arguments</h2>

<i>card</i>
<dl><dd><dd>soundcard structure</dl>
 

 <i>nid</i>
<dl><dd>new identification string</dl>

<h2>Description</h2>

This function sets the card identification and checks for name collisions.

<h2>Copyright</h2>


