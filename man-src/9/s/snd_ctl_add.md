---
title: "snd_ctl_add(9)"
name: "snd_ctl_add"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_ctl_add/"
description: "snd_ctl_add – add the control instance to the card"
---

<p>snd_ctl_add &#8211; add the control instance to the card</p>
<h2>Synopsis</h2>
<pre><code>int snd_ctl_add(struct snd_card *card, struct snd_kcontrol *kcontrol);</code></pre>
<h2>Arguments</h2>
<p><i>card</i></p>
<dl>
<dd>
<dd>the card instance</dl>
<p> <i>kcontrol</i></p>
<dl>
<dd>the control instance to add</dl>
<h2>Description</h2>
<p>Adds the control instance created via <code>snd_ctl_new</code> or <code>snd_ctl_new1</code> to the given card. Assigns also an unique numid used for fast search. </p>
<p> It frees automatically the control which cannot be added.</p>
<h2>Return</h2>
<p>Zero if successful, or a negative error code on failure.</p>
<h2>Copyright</h2>
