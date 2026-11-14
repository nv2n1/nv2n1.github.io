---
title: "snd_ctl_find_numid(9)"
name: "snd_ctl_find_numid"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_ctl_find_numid/"
description: "snd_ctl_find_numid – find the control instance with the given number-id"
---

<p>snd_ctl_find_numid &#8211; find the control instance with the given number-id</p>
<h2>Synopsis</h2>
<pre><code>struct snd_kcontrol *snd_ctl_find_numid(struct snd_card *card, unsigned int numid);</code></pre>
<h2>Arguments</h2>
<p><i>card</i></p>
<dl>
<dd>
<dd>the card instance</dl>
<p> <i>numid</i></p>
<dl>
<dd>the number-id to search</dl>
<h2>Description</h2>
<p>Finds the control instance with the given number-id from the card. </p>
<p> The caller must down card-&gt;controls_rwsem before calling this function (if the race condition can happen).</p>
<h2>Return</h2>
<p>The pointer of the instance if found, or <code>NULL</code> if not.</p>
<h2>Copyright</h2>
