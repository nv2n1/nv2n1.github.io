---
title: "get_midi_length(3)"
name: "get_midi_length"
section: "3"
letter: "g"
url: "/docs/linux/man/3-get_midi_length/"
description: "get_midi_length – Determines the total playing time of a midi, in seconds. Allegro game programming library."
---

<h2>NAME</h2>
<p> get_midi_length &#8211; Determines the total playing time of a midi, in seconds. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int get_midi_length(MIDI *midi);</code></p>
<h2>DESCRIPTION</h2>
<p> This function will simulate playing the given MIDI, from start to end, to determine how long it takes to play. After calling this function, midi_pos will contain the negative number of beats, and midi_time the length of the midi, in seconds. </p>
<p> Note that any currently playing midi is stopped when you call this function. Usually you would call it before play_midi, to get the length of the midi to be played, like in this example: </p>
<pre><code>
length = get_midi_length(my_midi);
play_midi(my_midi);
do {
    pos = midi_time;
    textprintf_ex(screen, font, 0, 0, c, -1, "%d:%02d / %d:%02d
",
                  pos / 60, pos % 60, length / 60, length % 60);
    rest(100);
} while (pos &lt;= length);
</code></pre>
<h2>RETURN VALUE</h2>
<p> Returns the value of midi_time, the length of the midi. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-load_midi/">load_midi</a></code>(3), <code><a href="/docs/linux/man/3-midi_time/">midi_time</a></code>(3), <code><a href="/docs/linux/man/3-midi_pos/">midi_pos</a></code>(3), <code><a href="/docs/linux/man/3-exmidi/">exmidi</a></code>(3) </p>
<h2>Index</h2>
