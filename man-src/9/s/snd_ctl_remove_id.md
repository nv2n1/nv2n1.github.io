---
title: "snd_ctl_remove_id(9)"
name: "snd_ctl_remove_id"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_ctl_remove_id/"
---

snd_ctl_remove_id - remove the control of the given id and release it

<h2>Synopsis</h2>

<pre><code>int snd_ctl_remove_id(struct snd_card *card, struct snd_ctl_elem_id *id);</code></pre>

<h2>Arguments</h2>

<i>card</i>
<dl><dd><dd>the card instance</dl>
 

 <i>id</i>
<dl><dd>the control id to remove</dl>

<h2>Description</h2>

Finds the control instance with the given id, removes it from the card list and releases it.

<h2>Return</h2>

0 if successful, or a negative error code on failure.

<h2>Copyright</h2>


