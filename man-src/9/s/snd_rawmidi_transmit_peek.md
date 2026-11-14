---
title: "snd_rawmidi_transmit_peek(9)"
name: "snd_rawmidi_transmit_peek"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_rawmidi_transmit_peek/"
description: "snd_rawmidi_transmit_peek – copy data from the internal buffer"
---

<p>snd_rawmidi_transmit_peek &#8211; copy data from the internal buffer</p>
<h2>Synopsis</h2>
<pre><code>int snd_rawmidi_transmit_peek(struct snd_rawmidi_substream *substream, unsigned char *buffer, int count);</code></pre>
<h2>Arguments</h2>
<p><i>substream</i></p>
<dl>
<dd>
<dd>the rawmidi substream</dl>
<p> <i>buffer</i></p>
<dl>
<dd>the buffer pointer</dl>
<p> <i>count</i></p>
<dl>
<dd>data size to transfer</dl>
<h2>Description</h2>
<p>Copies data from the internal output buffer to the given buffer. </p>
<p> Call this in the interrupt handler when the midi output is ready, and call <code>snd_rawmidi_transmit_ack</code> after the transmission is finished.</p>
<h2>Return</h2>
<p>The size of copied data, or a negative error code on failure.</p>
<h2>Copyright</h2>
