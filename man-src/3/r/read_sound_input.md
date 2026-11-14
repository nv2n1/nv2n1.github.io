---
title: "read_sound_input(3)"
name: "read_sound_input"
section: "3"
letter: "r"
url: "/docs/linux/man/3-read_sound_input/"
description: "read_sound_input – Retrieves the last recorded audio buffer. Allegro game programming library."
---

<p>read_sound_input &#8211; Retrieves the last recorded audio buffer. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

int read_sound_input(void *buffer);</code></pre>
<h2>Description</h2>
<p>Retrieves the most recently recorded audio buffer into the specified location. The buffer size can be obtained by checking the return value from start_sound_input(). You must be sure to call this function at regular intervals during the recording (typically around 100 times a second), or some data will be lost. If you are unable to do this often enough from the mainline code, use the digi_recorder() callback to store the waveform into a larger buffer of your own. </p>
<p> Note: many cards produce a click or popping sound when switching between record and playback modes, so it is often a good idea to discard the first buffer after you start a recording. The waveform is always stored in unsigned format, with stereo data consisting of alternate left/right samples.</p>
<h2>Return Value</h2>
<p>The function will return non-zero if a buffer has been copied or zero if no new data is yet available (you were too fast checking the input). </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-start_sound_input/">start_sound_input</a></code>(3) </p>
