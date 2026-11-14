---
title: "snd_ctl_rename_id(9)"
name: "snd_ctl_rename_id"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_ctl_rename_id/"
---

snd_ctl_rename_id - replace the id of a control on the card

<h2>Synopsis</h2>

<pre><code>int snd_ctl_rename_id(struct snd_card *card, struct snd_ctl_elem_id *src_id, struct snd_ctl_elem_id *dst_id);</code></pre>

<h2>Arguments</h2>

<i>card</i>
<dl><dd><dd>the card instance</dl>
 

 <i>src_id</i>
<dl><dd>the old id</dl>
 

 <i>dst_id</i>
<dl><dd>the new id</dl>

<h2>Description</h2>

Finds the control with the old id from the card, and replaces the id with the new one.

<h2>Return</h2>

Zero if successful, or a negative error code on failure.

<h2>Copyright</h2>


