---
title: "snd_card_file_remove(9)"
name: "snd_card_file_remove"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_card_file_remove/"
description: "snd_card_file_remove – remove the file from the file list"
---

<p>snd_card_file_remove &#8211; remove the file from the file list</p>
<h2>Synopsis</h2>
<pre><code>int snd_card_file_remove(struct snd_card *card, struct file *file);</code></pre>
<h2>Arguments</h2>
<p><i>card</i></p>
<dl>
<dd>
<dd>soundcard structure</dl>
<p> <i>file</i></p>
<dl>
<dd>file pointer</dl>
<h2>Description</h2>
<p>This function removes the file formerly added to the card via <code>snd_card_file_add</code> function. If all files are removed and <code>snd_card_free_when_closed</code> was called beforehand, it processes the pending release of resources.</p>
<h2>Return</h2>
<p>Zero or a negative error code.</p>
<h2>Copyright</h2>
