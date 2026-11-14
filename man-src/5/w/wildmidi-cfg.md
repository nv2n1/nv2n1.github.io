---
title: "wildmidi-cfg(5)"
name: "wildmidi-cfg"
section: "5"
letter: "w"
url: "/docs/linux/man/5-wildmidi-cfg/"
description: "wildmidi.cfg – Config file for libWildMidi"
---

<p>wildmidi.cfg &#8211; Config file for libWildMidi</p>
<h2>Library</h2>
<p><code>libWildMidi</code></p>
<h2>Description</h2>
<p>Contains the patch configuration for libWildMidi and location of Gravis Ultrasound compatible patch files. </p>
<pre>dir ~/guspats/
source /etc/wildmidi.cfg
bank 0
0 acpiano.pat amp=110 env_time4=300
1 brpiano.pat amp=100
drumset 0
25 snarerol keep=env amp=225 note=60
26 snap note=65</pre>
<h2>Syntax</h2>
<dl>
<dt><code>guspat_editor_author_cant_read_so_fix_release_time_for_me</code></p>
<dd>Some patch file editors switch the 4th and 5th envelopes around making the sound play much longer than intended in players that stuck to the Gravis Ultrasound patch standard. Including this option in the config enables a fix that detects this oversight, playing the sound samples as if they were correct.</p>
<dd>NOTE: This is a global setting. If it is found to affect good patch samples it will be moved to a per patch setting in a future version.</dl>
<dl>
<dt><code>auto_amp</code></p>
<dd>Forces WildMIDI to amplify samples to their maximum level ignoring the amp=% in the patch lines of the config.</dl>
<dl>
<dt><code>auto_amp_with_amp</code></p>
<dd>Forces WildMIDI to amplify samples to their maximum level then apply the amp=% in the patch lines of the config.</dl>
<dl>
<dt><code>dir</code> <i>dir-name</i></p>
<dd>Change the search path for config and patch files to <i>dir-name</i>. This is specific to the current config file and carried to any included config file unless they have their own <code>dir</code> setting. Any included file that has its own <code>dir</code> setting does not effect the <code>dir</code> setting of the current config file.</dl>
<dl>
<dt><code>source</code> <i>include-confg</i></p>
<dd>Include the settings from <i>include-config</i>. Any patch already set will be over-ridden by the included config file.</dl>
<dl>
<dt><code>bank</code> <i>N</i></p>
<dd>The patches following this setting belong to MIDI instrument bank <i>N</i>.</dl>
<dl>
<dt><code>drumset</code> <i>N</i></p>
<dd>The patches following this setting belong to MIDI drum bank <i>N</i>.</dl>
<dl>
<dt><i>patchno</i> <i>patchfile</i> [<code>amp=</code><i>volume</i>] [<code>note=</code><i>miodinte</i>] [<code>keep=loop</code>] [<code>keep=env</code>] [<code>remove=sustain</code>] [<code>remove=clamped</code>] [<code>env_level</code>[<i>0-5</i>]<code>=</code><i>level</i>] [<code>env_time</code>[<i>0-5</i>]<code>=</code><i>time</i>]</p>
<dd></dl>
<p> Example: 0 acpiano.pat amp=110 </p>
<dl>
<dd>
<dl>
<dt><i>patchno</i></p>
<dd>This is the MIDI patch number the instrument belongs to.</dl>
<dl>
<dt><i>patchfile</i></p>
<dd>The filename of the Gravis Ultrasound compatible patch file. If the filename is missing the .pat extension, libWildMidi will add .pat when attempting to load the file.</dl>
<dl>
<dt><code>amp=</code><i>volume</i></p>
<dd>Force the volume of the samples in this patch to <i>volume</i>% prior to using it.</dl>
<dl>
<dt><code>note=</code><i>midinote</i></p>
<dd>Use note <i>midinote</i> when playing the samples in this patch. NOTE: this is for instruments listed under drumset.</dl>
<dl>
<dt><code>keep=loop</code></p>
<dd>Play the samples in this patch with the loop, when normally we would not for this instrument.</dl>
<dl>
<dt><code>keep=env</code></p>
<dd>Use the envelope data in this patch, when normally we wouldn&#8217;t for this instrument.</dl>
<dl>
<dt><code>remove=sustain</code></p>
<dd>Do note hold the note after the 3rd envelope until note off, which is what happens if the sustain bit is set in the patch file.</dl>
<dl>
<dt><code>remove=clamped</code></p>
<dd>Do not jump to 6th envelope on note off, which is what happens if the clamped bit is set in the patch file.</dl>
<dl>
<dt><code>env_level</code>[<i>0-5</i>]<code>=</code><i>level</i></p>
<dd>Set the envelope level to <i>level</i> with 1.0 being maximum, and 0.0 being minimum.</p>
<dd>Example: set 5th envelope level to 10% &#8211; <code>env_level[0-5]=</code>0.1</dl>
<dl>
<dt><code>env_time</code>[<i>0-5</i>]<code>=</code><i>time</i></p>
<dd>Set the envelope time to <i>time</i> with a resolution of 1/1000th of a second. This setting is the time it should take for the envelope to reach maximum level.</p>
<dd>Example: set 1st envelope time to 1sec &#8211; <code>env_time0=</code>1000</p>
<dd>Example: set 3rd envelope time to 0.5secs &#8211; <code>env_time2=</code>500</dl>
</dl>
<dl>
<dt><code>reverb_room_width</code> <i>fval</i></p>
<dd>Set the room width for the reverb engine in meters. <i>fval</i> is a float value in meters. Minimum setting is 1.0 meter, maximum setting is 100.0 meters, and default is 15.0 meters.</p>
<dd>Example: set room width to 30 meters &#8211; <code>reverb_room_width 30</code></dl>
<dl>
<dt><code>reverb_room_length</code> <i>fval</i></p>
<dd>Set the room length for the reverb engine in meters. <i>fval</i> is a float value in meters. Minimum setting is 1.0 meter, maximum setting is 100.0 meters, and default is 20.0 meters.</p>
<dd>Example: set room length to 40 meters &#8211; <code>reverb_room_length 40</code></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-wildmidi/">wildmidi</a></code>(1) </p>
<h2>Author</h2>
<p>Chris Ison &lt;wildcode [at] users.sf.net&gt; Bret Curtis &lt;psi29a [at] gmail.com&gt;</p>
<h2>Copyright</h2>
<p>Copyright (C) Chris Ison 2001-2010 Copyright (C) Bret Curtis 2013-2016 </p>
<p> This file is part of WildMIDI. </p>
<p> WildMIDI is free software: you can redistribute and/or modify the player under the terms of the GNU General Public License and you can redistribute and/or modify the library under the terms of the GNU Lesser General Public License as published by the Free Software Foundation, either version 3 of the licenses, or(at your option) any later version. </p>
<p> WildMIDI is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License and the GNU Lesser General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License and the GNU Lesser General Public License along with WildMIDI. If not, see &lt;<a rel="nofollow" href="http://www.gnu.org/licenses/">http://www.gnu.org/licenses/</a>&gt;. </p>
<p> This manpage is licensed under the Creative Commons Attribution-Share Alike 3.0 Unported License. To view a copy of this license, visit <a rel="nofollow" href="http://creativecommons.org/licenses/by-sa/3.0/">http://creativecommons.org/licenses/by-sa/3.0/</a> or send a letter to Creative Commons, 171 Second Street, Suite 300, San Francisco, California, 94105, USA.</p>
