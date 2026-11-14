---
title: "get_sound_input_cap_rate(3)"
name: "get_sound_input_cap_rate"
section: "3"
letter: "g"
url: "/docs/linux/man/3-get_sound_input_cap_rate/"
description: "get_sound_input_cap_rate – Returns the maximum sample frequency for recording. Allegro game programming library."
---

<h2>NAME</h2>
<p> get_sound_input_cap_rate &#8211; Returns the maximum sample frequency for recording. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int get_sound_input_cap_rate(int bits, int stereo);</code></p>
<h2>DESCRIPTION</h2>
<p> Returns the maximum possible sample frequency for recording in the specified format, or zero if these settings are not supported. The bits parameter is the number of bits of the audio, and stereo is a boolean parameter. Pass zero for mono, non-zero for stereo input. Example: </p>
<pre><code>
int max_freq;
...
    /* What frequency can we record 8 bits mono at? */
    max_freq = get_sound_input_cap_rate(8, 0);
if (max_freq &gt; 22000) {
    /* Ok, 22KHz and above is good enough. */
}
</code></pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-start_sound_input/">start_sound_input</a></code>(3), <code><a href="/docs/linux/man/3-get_sound_input_cap_parm/">get_sound_input_cap_parm</a></code>(3), <code><a href="/docs/linux/man/3-get_sound_input_cap_bits/">get_sound_input_cap_bits</a></code>(3), <code><a href="/docs/linux/man/3-get_sound_input_cap_stereo/">get_sound_input_cap_stereo</a></code>(3) </p>
<h2>Index</h2>
