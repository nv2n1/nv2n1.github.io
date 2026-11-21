---
title: "aplaymidi(1)"
name: "aplaymidi"
section: "1"
letter: "a"
url: "/docs/linux/man/1-aplaymidi/"
description: "aplaymidi – play Standard MIDI Files"
---

<h2>SYNOPSIS</h2>
<p> <code>aplaymidi</code> -p client:port[,&#8230;] [-d delay] midifile &#8230; </p>
<h2>DESCRIPTION</h2>
<p> <code>aplaymidi</code> is a command-line utility that plays the specified MIDI file(s) to one or more ALSA sequencer ports. </p>
<h2>OPTIONS</h2>
<dl>
<dt><i>-h, &#8211;help</i></dt>
<dd> Prints a list of options. </dd>
<dt><i>-V, &#8211;version</i></dt>
<dd> Prints the current version. </dd>
<dt><i>-l, &#8211;list</i></dt>
<dd> Prints a list of possible output ports. </dd>
<dt><i>-p, &#8211;port=client:port,&#8230;</i></dt>
<dd> Sets the sequencer port(s) to which the events in the MIDI file(s) are sent. </dd>
<p> A client can be specified by its number, its name, or a prefix of its name. A port is specified by its number; for port 0 of a client, the &quot;:0&quot; part of the port specification can be omitted. </p>
<p> Multiple ports can be specified to allow playback of MIDI file(s) that contain events for multiple devices (ports), as specified by &quot;Port Number&quot; meta events. </p>
<p> For compatibility with <code>pmidi(1),</code> the port specification is taken from the <i>ALSA_OUTPUT_PORTS</i> environment variable if none is given on the command line. </p>
<dt><i>-d, &#8211;delay=seconds</i></dt>
<dd> Specifies how long to wait after the end of each MIDI file, to allow the last notes to die away. </dd>
</dl>
<h2>BUGS</h2>
<p> <code>aplaymidi</code> handles &quot;Port Number&quot; meta events, but not &quot;Port Name&quot; meta events. </p>
<h2>SEE ALSO</h2>
<p> pmidi(1)<br />
 playmidi(1) </p>
<h2>AUTHOR</h2>
<p> Clemens Ladisch &lt;clemens [at] ladisch.de&gt; </p>
