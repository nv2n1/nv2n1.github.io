---
title: "midi_pos(3)"
name: "midi_pos"
section: "3"
letter: "m"
url: "/docs/linux/man/3-midi_pos/"
description: "midi_pos – Stores the current position in the MIDI file. Allegro game programming library."
---

<h2>NAME</h2>
<p> midi_pos &#8211; Stores the current position in the MIDI file. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>extern volatile long midi_pos;</code></p>
<h2>DESCRIPTION</h2>
<p> Stores the current position (beat number) in the MIDI file, or contains a negative number if no music is currently playing. Useful for synchronising animations with the music, and for checking whether a MIDI file has finished playing. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-play_midi/">play_midi</a></code>(3), <code><a href="/docs/linux/man/3-midi_msg_callback/">midi_msg_callback</a></code>(3), <code><a href="/docs/linux/man/3-exmidi/">exmidi</a></code>(3) </p>
<h2>Index</h2>
