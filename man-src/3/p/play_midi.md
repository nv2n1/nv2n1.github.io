---
title: "play_midi(3)"
name: "play_midi"
section: "3"
letter: "p"
url: "/docs/linux/man/3-play_midi/"
description: "play_midi – Starts playing the specified MIDI file. Allegro game programming library."
---

<p>play_midi &#8211; Starts playing the specified MIDI file. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

int play_midi(MIDI *midi, int loop);</code></pre>
<h2>Description</h2>
<p>Starts playing the specified MIDI file, first stopping whatever music was previously playing. If the loop flag is set to non-zero, the data will be repeated until replaced with something else, otherwise it will stop at the end of the file. Passing a NULL pointer will stop whatever music is currently playing.</p>
<h2>Return Value</h2>
<p>Returns non-zero if an error occurs (this may happen if a patch-caching wavetable driver is unable to load the required samples, or at least it might in the future when somebody writes some patch-caching wavetable drivers :-) </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-install_sound/">install_sound</a></code>(3), <code><a href="/docs/linux/man/3-load_midi/">load_midi</a></code>(3), <code><a href="/docs/linux/man/3-play_looped_midi/">play_looped_midi</a></code>(3), <code><a href="/docs/linux/man/3-stop_midi/">stop_midi</a></code>(3), <code><a href="/docs/linux/man/3-midi_pause/">midi_pause</a></code>(3), <code><a href="/docs/linux/man/3-midi_seek/">midi_seek</a></code>(3), <code><a href="/docs/linux/man/3-midi_pos/">midi_pos</a></code>(3), <code><a href="/docs/linux/man/3-midi_time/">midi_time</a></code>(3), <code><a href="/docs/linux/man/3-midi_msg_callback/">midi_msg_callback</a></code>(3), <code><a href="/docs/linux/man/3-exmidi/">exmidi</a></code>(3) </p>
