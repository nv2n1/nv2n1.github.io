---
title: "start_sound_input(3)"
name: "start_sound_input"
section: "3"
letter: "s"
url: "/docs/linux/man/3-start_sound_input/"
description: "start_sound_input – Starts recording in the specified format. Allegro game programming library."
---

<p>start_sound_input &#8211; Starts recording in the specified format. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

int start_sound_input(int rate, int bits, int stereo);</code></pre>
<h2>Description</h2>
<p>Starts recording in the specified format, suspending audio playback as necessary if the card is not full duplex.</p>
<h2>Return Value</h2>
<p>Returns the buffer size in bytes if successful, or zero on error. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-install_sound_input/">install_sound_input</a></code>(3), <code><a href="/docs/linux/man/3-read_sound_input/">read_sound_input</a></code>(3), <code><a href="/docs/linux/man/3-stop_sound_input/">stop_sound_input</a></code>(3), <code><a href="/docs/linux/man/3-digi_recorder/">digi_recorder</a></code>(3), <code><a href="/docs/linux/man/3-set_sound_input_source/">set_sound_input_source</a></code>(3), <code><a href="/docs/linux/man/3-get_sound_input_cap_parm/">get_sound_input_cap_parm</a></code>(3), <code><a href="/docs/linux/man/3-get_sound_input_cap_bits/">get_sound_input_cap_bits</a></code>(3), <code><a href="/docs/linux/man/3-get_sound_input_cap_rate/">get_sound_input_cap_rate</a></code>(3), <code><a href="/docs/linux/man/3-get_sound_input_cap_stereo/">get_sound_input_cap_stereo</a></code>(3) </p>
