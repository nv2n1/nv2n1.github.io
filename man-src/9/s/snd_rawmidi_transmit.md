---
title: "snd_rawmidi_transmit(9)"
name: "snd_rawmidi_transmit"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_rawmidi_transmit/"
---

snd_rawmidi_transmit - copy from the buffer to the device

<h2>Synopsis</h2>

<pre><code>int snd_rawmidi_transmit(struct snd_rawmidi_substream *substream, unsigned char *buffer, int count);</code></pre>

<h2>Arguments</h2>

<i>substream</i>
<dl><dd><dd>the rawmidi substream</dl>
 

 <i>buffer</i>
<dl><dd>the buffer pointer</dl>
 

 <i>count</i>
<dl><dd>the data size to transfer</dl>

<h2>Description</h2>

Copies data from the buffer to the device and advances the pointer.

<h2>Return</h2>

The copied size if successful, or a negative error code on failure.

<h2>Copyright</h2>


