---
title: "midi_loop_end(3)"
name: "midi_loop_end"
section: "3"
letter: "m"
url: "/docs/linux/man/3-midi_loop_end/"
description: "midi_loop_start, midi_loop_end – Loop start and end points, set by play_looped_midi(). Allegro game programming library."
---

<h2>NAME</h2>
<p> midi_loop_start, midi_loop_end &#8211; Loop start and end points, set by play_looped_midi(). Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>extern long midi_loop_start;</code> </p>
<p> <code>extern long midi_loop_end;</code></p>
<h2>DESCRIPTION</h2>
<p> The loop start and end points, set by the play_looped_midi() function. These may safely be altered while the music is playing, but you should be sure they are always set to sensible values (start &lt; end). If you are changing them both at the same time, make sure to alter them in the right order in case a MIDI interrupt happens to occur in between your two writes! Setting these values to -1 represents the start and end of the file respectively. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-play_looped_midi/">play_looped_midi</a></code>(3) </p>
<h2>Index</h2>
