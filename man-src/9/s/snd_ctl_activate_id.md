---
title: "snd_ctl_activate_id(9)"
name: "snd_ctl_activate_id"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_ctl_activate_id/"
---

snd_ctl_activate_id - activate/inactivate the control of the given id

<h2>Synopsis</h2>

<pre><code>int snd_ctl_activate_id(struct snd_card *card, struct snd_ctl_elem_id *id, int active);</code></pre>

<h2>Arguments</h2>

<i>card</i>
<dl><dd><dd>the card instance</dl>
 

 <i>id</i>
<dl><dd>the control id to activate/inactivate</dl>
 

 <i>active</i>
<dl><dd>non-zero to activate</dl>

<h2>Description</h2>

Finds the control instance with the given id, and activate or inactivate the control together with notification, if changed. The given ID data is filled with full information.

<h2>Return</h2>

0 if unchanged, 1 if changed, or a negative error code on failure.

<h2>Copyright</h2>


