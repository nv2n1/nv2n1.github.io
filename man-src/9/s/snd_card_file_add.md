---
title: "snd_card_file_add(9)"
name: "snd_card_file_add"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_card_file_add/"
---

snd_card_file_add - add the file to the file list of the card

<h2>Synopsis</h2>

<pre><code>int snd_card_file_add(struct snd_card *card, struct file *file);</code></pre>

<h2>Arguments</h2>

<i>card</i>
<dl><dd><dd>soundcard structure</dl>
 

 <i>file</i>
<dl><dd>file pointer</dl>

<h2>Description</h2>

This function adds the file to the file linked-list of the card. This linked-list is used to keep tracking the connection state, and to avoid the release of busy resources by hotplug.

<h2>Return</h2>

zero or a negative error code.

<h2>Copyright</h2>


