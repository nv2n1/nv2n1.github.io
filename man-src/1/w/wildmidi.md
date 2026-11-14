---
title: "wildmidi(1)"
name: "wildmidi"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wildmidi/"
description: "wildmidi – example player for libWildMidi"
---

<h2>NAME</h2>
<p> wildmidi &#8211; example player for libWildMidi </p>
<h2>LIBRARY</h2>
<p> <code>libWildMidi</code> </p>
<h2>FILES</h2>
<p> <code>/etc/wildmidi/wildmidi.cfg</code> </p>
<h2>SYNOPSIS</h2>
<p> <code>wildmidi [-behlvwn] [-c </code><i>config-file</i><code>] [-d </code><i>audiodev</i><code>] [-m </code><i>volume-level</i><code>] [-o </code><i>wav-file</i><code>] </code><i>midifile &#8230;</i> </p>
<h2>DESCRIPTION</h2>
<p> This is a demonstration program to show the capabilities of libWildMidi. </p>
<p> <i>midifile</i> is processed by libWildMidi and the resulting audio is output by the player. </p>
<p> You can have more than one <i>midifile</i> on the command line and <code>wildmidi</code> will pass them to libWildMidi for processing, one after the other. You can also use wildcards, for example: <code>wildmidi *.mid</code> </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-b</code> | <code>&#8211;reverb</code></p>
<dd> Turns on an 8 point reverb engine that adds depth to the final mix.</dl>
<dl>
<dt><code>-c</code> <i>config-file</i> | <code>&#8211;config</code> <i>config-file</i></p>
<dd> Uses the configuration file stated by <i>config-file</i> instead of /etc/wildmidi/wildmidi.cfg</dl>
<dl>
<dt><code>-d</code> <i>audiodev</i> | <code>&#8211;device=</code><i>audiodev</i></p>
<dd> Send the audio to <i>audiodev</i> instead of the default. ALSA defaults to the system &quot;default&quot; while OSS defaults to &quot;/dev/dsp&quot;. Other environments do not support this option.</dl>
<dl>
<dt><code>-e</code> | <code>&#8211;enhanced</code></p>
<dd> Switches to a gauss based resampling algorithm which can improve the shape of the sound.</dl>
<dl>
<dt><code>-h</code> | <code>&#8211;help</code></p>
<dd> Displays command line options</dl>
<dl>
<dt><code>-l</code> | <code>&#8211;log_vol</code></p>
<dd> Some MIDI files have been recorded on hardware that uses a volume curve, making them sound really badly mixed on other MIDI devices. Use this option to use volume curves.</dl>
<dl>
<dt><code>-m</code> <i>volume-level</i> | <code>&#8211;mastervol=</code><i>volume-level</i></p>
<dd> Set the overall volume level to <i>volume-level</i>. The minimum is 0 and the maximum is 127, with the default being 100.</dl>
<dl>
<dt><code>-o</code> <i>wav-file</i> | <code>&#8211;wavout=</code><i>wav-file</i></p>
<dd> Records the audio in wav format to <i>wav-file</i>.</dl>
<dl>
<dt><code>-r</code> <i>sndrate</i> | <code>&#8211;rate=</code><i>sndrate</i></p>
<dd> Set the audio output rate to <i>sndrate</i>. The default rate is 32072.</dl>
<dl>
<dt><code>-w</code> | <code>&#8211;wholetempo</code></p>
<dd> Round down tempo to whole number</dl>
<dl>
<dt><code>-n</code> | <code>&#8211;roundtempo</code></p>
<dd> Round tempo to nearest whole number</dl>
<dl>
<dt><code>-v</code> | <code>&#8211;version</code></p>
<dd> Display version and copyright information</dl>
<h2>TEST OPTIONS</h2>
<p> These options are not designed for general use. Instead these options are designed to make it easier to listen to specific sound samples. </p>
<p> Note: These options are not displayed by <code>-h</code> | <code>&#8211;help</code> </p>
<dl>
<dt><code>-k</code> <i>N</i> | <code>&#8211;test_bank=</code><i>N</i></p>
<dd> Set the test bank to <i>N</i>. Range is 0 to 127.</dl>
<dl>
<dt><code>-p</code> <i>N</i> | <code>&#8211;test_patch=</code><i>N</i></p>
<dd> Set the test patch to <i>N</i>. Range is 0 to 127.</dl>
<dl>
<dt><code>-t</code> | <code>&#8211;test_midi</code></p>
<dd> Plays the built in test midi which plays all 127 notes.</dl>
<h2>USER INTERFACE</h2>
<p> The player accepts limited user input that allows some interaction while playing midi files. </p>
<dl>
<dt><code>+</code></p>
<dd> Turns the master volume up.</dl>
<dl>
<dt><code>&#8211;</code></p>
<dd> Turns the master volume down.</dl>
<dl>
<dt><code>e</code></p>
<dd> Turns enhanced resampling on and off.</dl>
<dl>
<dt><code>l</code></p>
<dd> Turns volume curves on and off.</dl>
<dl>
<dt><code>r</code></p>
<dd> Turns the final mix reverb on and off.</dl>
<dl>
<dt><code>n</code></p>
<dd> Play the next midi on the command line.</dl>
<dl>
<dt><code>p</code></p>
<dd> Pause the playback. Note: since the audio is buffered it will stop when the audio buffer is empty.</dl>
<dl>
<dt><code>.</code></p>
<dd> Seek forward 1 second. Note: Clears active midi events and will only play midi events from after the new position.</dl>
<dl>
<dt><code>,</code></p>
<dd> Seek backwards 1 second. Note: Clears active midi events and will only play midi events from after the new position.</dl>
<dl>
<dt><code>q</code></p>
<dd> Quit wildmidi.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-wildmidi-cfg/">wildmidi.cfg</a></code>(5) </p>
<h2>AUTHOR</h2>
<p> Chris Ison &lt;wildcode [at] users.sf.net&gt; Bret Curtis &lt;psi29a [at] gmail.com&gt; </p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) Chris Ison 2001-2010 Copyright (C) Bret Curtis 2013-2014 </p>
<p> This file is part of WildMIDI. </p>
<p> WildMIDI is free software: you can redistribute and/or modify the player under the terms of the GNU General Public License and you can redistribute and/or modify the library under the terms of the GNU Lesser General Public License as published by the Free Software Foundation, either version 3 of the licenses, or(at your option) any later version. </p>
<p> WildMIDI is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License and the GNU Lesser General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License and the GNU Lesser General Public License along with WildMIDI. If not, see &lt;<a rel="nofollow" href="http://www.gnu.org/licenses/">http://www.gnu.org/licenses/</a>&gt;. </p>
<p> This manpage is licensed under the Creative Commons AttributionShare Alike 3.0 Unported License. To view a copy of this license, visit <a rel="nofollow" href="http://creativecommons.org/licenses/by-sa/3.0/">http://creativecommons.org/licenses/by-sa/3.0/</a> or send a letter to Creative Commons, 171 Second Street, Suite 300, San Francisco, California, 94105, USA. </p>
<h2>Index</h2>
