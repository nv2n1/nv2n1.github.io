---
title: "arecordmidi(1)"
name: "arecordmidi"
section: "1"
letter: "a"
url: "/docs/linux/man/1-arecordmidi/"
description: "arecordmidi – record Standard MIDI Files"
---

<h2 class="name">NAME</h2>
<p> arecordmidi &#8211; record Standard MIDI Files</p>
<h2>SYNOPSIS</h2>
<p> <code>arecordmidi</code> -p client:port[,&#8230;] [options] midifile </p>
<h2>DESCRIPTION</h2>
<p> <code>arecordmidi</code> is a command-line utility that records a Standard MIDI File from one or more ALSA sequencer ports. </p>
<p> To stop recording, press Ctrl+C. </p>
<h2>OPTIONS</h2>
<dl>
<dt><i>-h,&#8211;help</i></p>
<dd> Prints a list of options. </p>
<dt><i>-V,&#8211;version</i></p>
<dd> Prints the current version. </p>
<dt><i>-l,&#8211;list</i></p>
<dd> Prints a list of possible input ports. </p>
<dt><i>-p,&#8211;port=client:port,&#8230;</i></p>
<dd> Sets the sequencer port(s) from which events are recorded. </p>
<p> A client can be specified by its number, its name, or a prefix of its name. A port is specified by its number; for port 0 of a client, the &quot;:0&quot; part of the port specification can be omitted. </p>
<dt><i>-b,&#8211;bpm=beats</i></p>
<dd> Sets the musical tempo of the MIDI file, in beats per minute. The default value is 120 BPM. </p>
<dt><i>-f,&#8211;fps=frames</i></p>
<dd> Sets the SMPTE resolution, in frames per second. Possible values are 24, 25, 29.97 (for 30 drop-frame), and 30. </p>
<dt><i>-t,&#8211;ticks=ticks</i></p>
<dd> Sets the resolution of timestamps (ticks) in the MIDI file, in ticks per beat (when using musical tempo) or ticks per frame (when using SMPTE timing). The default value is 384 ticks/beat or 40 ticks/frame, respectively. </p>
<dt><i>-s,&#8211;split-channels</i></p>
<dd> Specifies that the data for each MIDI channel should be written to a separate track in the MIDI file. This will result in a &quot;format 1&quot; file. Otherwise, when there is only one track, <code>arecordmidi</code> will generate a &quot;format 0&quot; file. </p>
<dt><i>-m,&#8211;metronome=client:port</i></p>
<dd> Plays a metronome signal on the specified sequencer port. </p>
<p> Metronome sounds are played on channel 10, MIDI notes 33 &amp; 34 (GM2/GS/XG metronome standard notes), with velocity 100 and duration 1. </p>
<dt><i>-i,&#8211;timesig=numerator:denominator</i></p>
<dd> Sets the time signature for the MIDI file and metronome. </p>
<p> The time signature is specified as usual with two numbers, representing the numerator and denominator of the time signature as it would be notated. The denominator must be a power of two. Both numbers should be separated by a colon. The time signature is 4:4 by default. </p>
</dl>
<h2>AUTHOR</h2>
<p> Clemens Ladisch &lt;clemens [at] ladisch.de&gt; </p>
<h2>Index</h2>
