---
title: "get_audio_stream_buffer(3)"
name: "get_audio_stream_buffer"
section: "3"
letter: "g"
url: "/docs/linux/man/3-get_audio_stream_buffer/"
description: "get_audio_stream_buffer – Tells you if you need to fill the audiostream or not. Allegro game programming library."
---

<h2>NAME</h2>
<p> get_audio_stream_buffer &#8211; Tells you if you need to fill the audiostream or not. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>void *get_audio_stream_buffer(AUDIOSTREAM *stream);</code></p>
<h2>DESCRIPTION</h2>
<p> You must call this function at regular intervals while an audio stream is playing, to provide the next buffer of sample data (the smaller the stream buffer size, the more often it must be called). This function should not be called from a timer handler. Example: </p>
<pre><code>
void *mem_chunk;
... while (TRUE)
{
    ... mem_chunk = get_audio_stream_buffer(buffer);
    if (mem_chunk != NULL) {
        /* Refill the stream buffer. */
    }
}
</code></pre>
<h2>RETURN VALUE</h2>
<p> If it returns NULL, the stream is still playing the previous lot of data, so you don&#8217;t need to do anything. If it returns a value, that is the location of the next buffer to be played, and you should load the appropriate number of samples (however many you specified when creating the stream) to that address, for example using an fread() from a disk file. After filling the buffer with data, call free_audio_stream_buffer() to indicate that the new data is now valid. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-play_audio_stream/">play_audio_stream</a></code>(3), <code><a href="/docs/linux/man/3-free_audio_stream_buffer/">free_audio_stream_buffer</a></code>(3), <code><a href="/docs/linux/man/3-exstream/">exstream</a></code>(3) </p>
<h2>Index</h2>
