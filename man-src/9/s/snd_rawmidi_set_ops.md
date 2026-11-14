---
title: "snd_rawmidi_set_ops(9)"
name: "snd_rawmidi_set_ops"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_rawmidi_set_ops/"
---

snd_rawmidi_set_ops - set the rawmidi operators

<h2>Synopsis</h2>

<pre><code>void snd_rawmidi_set_ops(struct snd_rawmidi *rmidi, int stream, struct snd_rawmidi_ops *ops);</code></pre>

<h2>Arguments</h2>

<i>rmidi</i>
<dl><dd><dd>the rawmidi instance</dl>
 

 <i>stream</i>
<dl><dd>the stream direction, SNDRV_RAWMIDI_STREAM_XXX</dl>
 

 <i>ops</i>
<dl><dd>the operator table</dl>

<h2>Description</h2>

Sets the rawmidi operators for the given stream direction.

<h2>Copyright</h2>


