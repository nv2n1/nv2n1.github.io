---
title: "snd_rawmidi_receive(9)"
name: "snd_rawmidi_receive"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_rawmidi_receive/"
---

snd_rawmidi_receive - receive the input data from the device

<h2>Synopsis</h2>

<pre><code>int snd_rawmidi_receive(struct snd_rawmidi_substream *substream, const unsigned char *buffer, int count);</code></pre>

<h2>Arguments</h2>

<i>substream</i>
<dl><dd><dd>the rawmidi substream</dl>
 

 <i>buffer</i>
<dl><dd>the buffer pointer</dl>
 

 <i>count</i>
<dl><dd>the data size to read</dl>

<h2>Description</h2>

Reads the data from the internal buffer.

<h2>Return</h2>

The size of read data, or a negative error code on failure.

<h2>Copyright</h2>


