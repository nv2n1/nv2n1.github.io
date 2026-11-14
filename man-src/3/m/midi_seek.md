---
title: "midi_seek(3)"
name: "midi_seek"
section: "3"
letter: "m"
url: "/docs/linux/man/3-midi_seek/"
description: "midi_seek – Seeks to the given midi_pos in the current MIDI file. Allegro game programming library."
---

<h2>NAME</h2>
<p> midi_seek &#8211; Seeks to the given midi_pos in the current MIDI file. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int midi_seek(int target);</code></p>
<h2>DESCRIPTION</h2>
<p> Seeks to the given midi_pos in the current MIDI file. If the target is earlier in the file than the current midi_pos it seeks from the beginning; otherwise it seeks from the current position.</p>
<h2>RETURN VALUE</h2>
<p> Returns zero if it could successfully seek to the requested position. Otherwise, a return value of 1 means it stopped playing, and midi_pos is set to the negative length of the MIDI file (so you can use this function to determine the length of a MIDI file). A return value of 2 means the MIDI file looped back to the start. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-play_midi/">play_midi</a></code>(3), <code><a href="/docs/linux/man/3-midi_pos/">midi_pos</a></code>(3) </p>
<h2>Index</h2>
