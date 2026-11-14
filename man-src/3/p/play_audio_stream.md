---
title: "play_audio_stream(3)"
name: "play_audio_stream"
section: "3"
letter: "p"
url: "/docs/linux/man/3-play_audio_stream/"
description: "play_audio_stream – Creates a new audio stream and starts playing it. Allegro game programming library."
---

<p>play_audio_stream &#8211; Creates a new audio stream and starts playing it. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;
</code></pre>
<p> <code>AUDIOSTREAM *play_audio_stream(int len, int bits, int stereo,</code> <code>int freq, int vol, int pan);</code></p>
<h2>Description</h2>
<p>This function creates a new audio stream and starts playing it. The length is the size of each transfer buffer in sample frames (not bytes), where a sample frame is a single sample value for mono data or a pair of interleaved sample values (left first) for stereo data. The length should normally be (but doesn&#8217;t have to be) a power of 2 somewhere around 1k in size. Larger buffers are more efficient and require fewer updates, but result in more latency between you providing the data and it actually being played. The `bits&#8217; parameter must be 8 or 16. `freq&#8217; is the sample rate of the data in Hertz. The `vol&#8217; and `pan&#8217; values use the same 0-255 ranges as the regular sample playing functions. The `stereo&#8217; parameter should be set to 1 for stereo streams, or 0 otherwise. If you want to adjust the pitch, volume, or panning of a stream once it is playing, you can use the regular voice_*() functions with stream-&gt;voice as a parameter. The format of the sample data is described in the SAMPLE entry of the &quot;Structures and types defined by Allegro&quot; chapter. The formula to get the size of the buffers in bytes could be: </p>
<pre> bytes = length * (bits / 8) * (stereo ? 2 : 1)</pre>
<p>Example: </p>
<pre><code>/* Create a 22KHz 8bit mono audio stream. */
stream = play_audio_stream(1024, 8, FALSE, 22050, 255, 128);
if (!stream)
    abort_on_error(&quot;Error creating audio stream!
&quot;);</code></pre>
<h2>Return Value</h2>
<p>This function returns a pointer to the audio stream or NULL if it could not be created. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-install_sound/">install_sound</a></code>(3), <code><a href="/docs/linux/man/3-get_audio_stream_buffer/">get_audio_stream_buffer</a></code>(3), <code><a href="/docs/linux/man/3-stop_audio_stream/">stop_audio_stream</a></code>(3), <code><a href="/docs/linux/man/3-audiostream/">AUDIOSTREAM</a></code>(3), <code><a href="/docs/linux/man/3-exstream/">exstream</a></code>(3) </p>
