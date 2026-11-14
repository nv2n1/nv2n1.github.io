---
title: "play_looped_midi(3)"
name: "play_looped_midi"
section: "3"
letter: "p"
url: "/docs/linux/man/3-play_looped_midi/"
description: "play_looped_midi – Starts playing a MIDI file with a user-defined loop position. Allegro game programming library."
---

<p>play_looped_midi &#8211; Starts playing a MIDI file with a user-defined loop position. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

int play_looped_midi(MIDI *midi, int loop_start, int loop_end);</code></pre>
<h2>Description</h2>
<p>Starts playing a MIDI file with a user-defined loop position. When the player reaches the loop end position or the end of the file (loop_end may be -1 to only loop at EOF), it will wind back to the loop start point. Both positions are specified in the same beat number format as the midi_pos variable.</p>
<h2>Return Value</h2>
<p>The return value has the same meaning as that of play_midi(): non-zero if an error occurs, zero otherwise. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-play_midi/">play_midi</a></code>(3), <code><a href="/docs/linux/man/3-midi_pos/">midi_pos</a></code>(3), <code><a href="/docs/linux/man/3-midi_loop_start/">midi_loop_start</a></code>(3) </p>
