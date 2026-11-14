---
title: "snd_ctl_remove(9)"
name: "snd_ctl_remove"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_ctl_remove/"
description: "snd_ctl_remove – remove the control from the card and release it"
---

<p>snd_ctl_remove &#8211; remove the control from the card and release it</p>
<h2>Synopsis</h2>
<pre><code>int snd_ctl_remove(struct snd_card *card, struct snd_kcontrol *kcontrol);</code></pre>
<h2>Arguments</h2>
<p><i>card</i></p>
<dl>
<dd>
<dd>the card instance</dl>
<p> <i>kcontrol</i></p>
<dl>
<dd>the control instance to remove</dl>
<h2>Description</h2>
<p>Removes the control from the card and then releases the instance. You don&#8217;t need to call <code>snd_ctl_free_one</code>. You must be in the write lock &#8211; down_write(card-&gt;controls_rwsem).</p>
<h2>Return</h2>
<p>0 if successful, or a negative error code on failure.</p>
<h2>Copyright</h2>
