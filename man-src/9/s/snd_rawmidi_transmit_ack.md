---
title: "snd_rawmidi_transmit_ack(9)"
name: "snd_rawmidi_transmit_ack"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_rawmidi_transmit_ack/"
---

snd_rawmidi_transmit_ack - acknowledge the transmission

<h2>Synopsis</h2>

<pre><code>int snd_rawmidi_transmit_ack(struct snd_rawmidi_substream *substream, int count);</code></pre>

<h2>Arguments</h2>

<i>substream</i>
<dl><dd><dd>the rawmidi substream</dl>
 

 <i>count</i>
<dl><dd>the transferred count</dl>

<h2>Description</h2>

Advances the hardware pointer for the internal output buffer with the given size and updates the condition. Call after the transmission is finished.

<h2>Return</h2>

The advanced size if successful, or a negative error code on failure.

<h2>Copyright</h2>


