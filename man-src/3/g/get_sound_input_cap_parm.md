---
title: "get_sound_input_cap_parm(3)"
name: "get_sound_input_cap_parm"
section: "3"
letter: "g"
url: "/docs/linux/man/3-get_sound_input_cap_parm/"
description: "get_sound_input_cap_parm – Detects if the specified recording parameters are supported. Allegro game programming library."
---

<h2>NAME</h2>
<p> get_sound_input_cap_parm &#8211; Detects if the specified recording parameters are supported. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int get_sound_input_cap_parm(int rate, int bits, int stereo);</code></p>
<h2>DESCRIPTION</h2>
<p> Checks whether the specified recording frequency, number of bits, and mono/stereo mode are supported (and how) by the current audio driver.</p>
<h2>RETURN VALUE</h2>
<p> The function returns one of the following possible values: </p>
<pre>
   0  = It is impossible to record in this format.
   1  = Recording is possible, but audio output
        will be suspended.
   2  = Recording is possible at the same time as
        playing other sounds (full duplex sound card).
   -n = Sampling rate not supported, but rate 'n'
        would work instead.
</pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-start_sound_input/">start_sound_input</a></code>(3), <code><a href="/docs/linux/man/3-get_sound_input_cap_bits/">get_sound_input_cap_bits</a></code>(3), <code><a href="/docs/linux/man/3-get_sound_input_cap_rate/">get_sound_input_cap_rate</a></code>(3), <code><a href="/docs/linux/man/3-get_sound_input_cap_stereo/">get_sound_input_cap_stereo</a></code>(3) </p>
<h2>Index</h2>
