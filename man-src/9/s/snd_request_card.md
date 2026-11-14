---
title: "snd_request_card(9)"
name: "snd_request_card"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_request_card/"
---

snd_request_card - try to load the card module

<h2>Synopsis</h2>

<pre><code>void snd_request_card(int card);</code></pre>

<h2>Arguments</h2>

<i>card</i>
<dl><dd><dd>the card number</dl>

<h2>Description</h2>

Tries to load the module "snd-card-X" for the given card number via request_module. Returns immediately if already loaded.

<h2>Copyright</h2>


