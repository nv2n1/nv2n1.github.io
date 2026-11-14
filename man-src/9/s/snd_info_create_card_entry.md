---
title: "snd_info_create_card_entry(9)"
name: "snd_info_create_card_entry"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_info_create_card_entry/"
description: "snd_info_create_card_entry – create an info entry for the given card"
---

<p>snd_info_create_card_entry &#8211; create an info entry for the given card</p>
<h2>Synopsis</h2>
<pre><code>struct snd_info_entry *snd_info_create_card_entry(struct snd_card *card, const char *name, struct snd_info_entry *parent);</code></pre>
<h2>Arguments</h2>
<p><i>card</i></p>
<dl>
<dd>
<dd>the card instance</dl>
<p> <i>name</i></p>
<dl>
<dd>the file name</dl>
<p> <i>parent</i></p>
<dl>
<dd>the parent directory</dl>
<h2>Description</h2>
<p>Creates a new info entry and assigns it to the given card.</p>
<h2>Return</h2>
<p>The pointer of the new instance, or <code>NULL</code> on failure.</p>
<h2>Copyright</h2>
