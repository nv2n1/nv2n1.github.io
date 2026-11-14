---
title: "free_audio_stream_buffer(3)"
name: "free_audio_stream_buffer"
section: "3"
letter: "f"
url: "/docs/linux/man/3-free_audio_stream_buffer/"
description: "free_audio_stream_buffer – Tells the audio stream player new data can be played. Allegro game programming library."
---

<h2>NAME</h2>
<p> free_audio_stream_buffer &#8211; Tells the audio stream player new data can be played. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>void free_audio_stream_buffer(AUDIOSTREAM *stream);</code></p>
<h2>DESCRIPTION</h2>
<p> Call this function after get_audio_stream_buffer() returns a non-NULL address, to indicate that you have loaded a new block of samples to that location and the data is now ready to be played. Example: </p>
<pre><code>
mem_chunk = get_audio_stream_buffer(buffer);
if (mem_chunk != NULL) {
    /* Refill the stream buffer. */
    ... free_audio_stream_buffer(buffer);
}
</code></pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-get_audio_stream_buffer/">get_audio_stream_buffer</a></code>(3), <code><a href="/docs/linux/man/3-exstream/">exstream</a></code>(3) </p>
<h2>Index</h2>
