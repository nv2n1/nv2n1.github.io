---
title: "midi_out(3)"
name: "midi_out"
section: "3"
letter: "m"
url: "/docs/linux/man/3-midi_out/"
description: "midi_out – Streams a block of MIDI commands into the player. Allegro game programming library."
---

<h2>NAME</h2>
<p> midi_out &#8211; Streams a block of MIDI commands into the player. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>void midi_out(unsigned char *data, int length);</code></p>
<h2>DESCRIPTION</h2>
<p> Streams a block of MIDI commands into the player in real-time, allowing you to trigger notes, jingles, etc, over the top of whatever MIDI file is currently playing. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-install_sound/">install_sound</a></code>(3), <code><a href="/docs/linux/man/3-load_midi_patches/">load_midi_patches</a></code>(3), <code><a href="/docs/linux/man/3-midi_recorder/">midi_recorder</a></code>(3) </p>
<h2>Index</h2>
