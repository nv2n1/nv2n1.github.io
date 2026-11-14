---
title: "snd_rawmidi_new(9)"
name: "snd_rawmidi_new"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_rawmidi_new/"
description: "snd_rawmidi_new – create a rawmidi instance"
---

<p>snd_rawmidi_new &#8211; create a rawmidi instance</p>
<h2>Synopsis</h2>
<pre><code>int snd_rawmidi_new(struct snd_card *card, char *id, int device, int output_count, int input_count, struct snd_rawmidi **rrawmidi);</code></pre>
<h2>Arguments</h2>
<p><i>card</i></p>
<dl>
<dd>
<dd>the card instance</dl>
<p> <i>id</i></p>
<dl>
<dd>the id string</dl>
<p> <i>device</i></p>
<dl>
<dd>the device index</dl>
<p> <i>output_count</i></p>
<dl>
<dd>the number of output streams</dl>
<p> <i>input_count</i></p>
<dl>
<dd>the number of input streams</dl>
<p> <i>rrawmidi</i></p>
<dl>
<dd>the pointer to store the new rawmidi instance</dl>
<h2>Description</h2>
<p>Creates a new rawmidi instance. Use <code>snd_rawmidi_set_ops</code> to set the operators to the new instance.</p>
<h2>Return</h2>
<p>Zero if successful, or a negative error code on failure.</p>
<h2>Copyright</h2>
