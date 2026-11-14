---
title: "snd_ctl_find_id(9)"
name: "snd_ctl_find_id"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_ctl_find_id/"
description: "snd_ctl_find_id – find the control instance with the given id"
---

<p>snd_ctl_find_id &#8211; find the control instance with the given id</p>
<h2>Synopsis</h2>
<pre><code>struct snd_kcontrol *snd_ctl_find_id(struct snd_card *card, struct snd_ctl_elem_id *id);</code></pre>
<h2>Arguments</h2>
<p><i>card</i></p>
<dl>
<dd>
<dd>the card instance</dl>
<p> <i>id</i></p>
<dl>
<dd>the id to search</dl>
<h2>Description</h2>
<p>Finds the control instance with the given id from the card. </p>
<p> The caller must down card-&gt;controls_rwsem before calling this function (if the race condition can happen).</p>
<h2>Return</h2>
<p>The pointer of the instance if found, or <code>NULL</code> if not.</p>
<h2>Copyright</h2>
