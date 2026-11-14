---
title: "snd_rawmidi_transmit_empty(9)"
name: "snd_rawmidi_transmit_empty"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_rawmidi_transmit_empty/"
---

snd_rawmidi_transmit_empty - check whether the output buffer is empty

<h2>Synopsis</h2>

<pre><code>int snd_rawmidi_transmit_empty(struct snd_rawmidi_substream *substream);</code></pre>

<h2>Arguments</h2>

<i>substream</i>
<dl><dd><dd>the rawmidi substream</dl>

<h2>Return</h2>

1 if the internal output buffer is empty, 0 if not.

<h2>Copyright</h2>


