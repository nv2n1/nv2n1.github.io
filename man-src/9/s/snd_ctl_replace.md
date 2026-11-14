---
title: "snd_ctl_replace(9)"
name: "snd_ctl_replace"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_ctl_replace/"
---

snd_ctl_replace - replace the control instance of the card

<h2>Synopsis</h2>

<pre><code>int snd_ctl_replace(struct snd_card *card, struct snd_kcontrol *kcontrol, bool add_on_replace);</code></pre>

<h2>Arguments</h2>

<i>card</i>
<dl><dd><dd>the card instance</dl>
 

 <i>kcontrol</i>
<dl><dd>the control instance to replace</dl>
 

 <i>add_on_replace</i>
<dl><dd>add the control if not already added</dl>

<h2>Description</h2>

Replaces the given control. If the given control does not exist and the add_on_replace flag is set, the control is added. If the control exists, it is destroyed first. 

 It frees automatically the control which cannot be added or replaced.

<h2>Return</h2>

Zero if successful, or a negative error code on failure.

<h2>Copyright</h2>


