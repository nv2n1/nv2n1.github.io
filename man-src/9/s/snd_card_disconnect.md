---
title: "snd_card_disconnect(9)"
name: "snd_card_disconnect"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_card_disconnect/"
---

snd_card_disconnect - disconnect all APIs from the file-operations (user space)

<h2>Synopsis</h2>

<pre><code>int snd_card_disconnect(struct snd_card *card);</code></pre>

<h2>Arguments</h2>

<i>card</i>
<dl><dd><dd>soundcard structure</dl>

<h2>Description</h2>

Disconnects all APIs from the file-operations (user space).

<h2>Return</h2>

Zero, otherwise a negative error code.

<h2>Note</h2>

The current implementation replaces all active file-&gt;f_op with special dummy file operations (they do nothing except release).

<h2>Copyright</h2>


