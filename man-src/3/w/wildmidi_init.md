---
title: "wildmidi_init(3)"
name: "wildmidi_init"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wildmidi_init/"
description: "WildMidi_Init – Initialize the library"
---

<p>WildMidi_Init &#8211; Initialize the library </p>
<h2>Library</h2>
<p><code>libWildMidi</code> </p>
<h2>Synopsis</h2>
<p><code>#include &lt;wildmidi_lib.h&gt;</code> </p>
<p> <code>WildMidi_Init (const char *</code><i>config_file</i>, unsigned short int <i>rate</i>, unsigned short int <i>options</i>) </p>
<h2>Description</h2>
<p>Initializes libWildMidi in preparation for playback. This function only needs to be called once by the program using libWildMidi. </p>
<dl COMPACT>
<dt><i>config-file</i></p>
<dd>The file that contains the instrument configuration for the library.</dl>
<dl COMPACT>
<dt><i>rate</i></p>
<dd>The sound rate you want the the audio data output at. Rates accepted by libWildMidi are 11025 &#8211; 65000.</dl>
<dl COMPACT>
<dt><i>options</i></p>
<dd>The initial options to set for the library. see below.</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>WM_MO_LOG_VOLUME</p>
<dd>By default the library uses linear volume levels typically used in computer MIDI players. These can differ somewhat to volume levels found on some midi hardware which may use a volume curve based on decibels. This option sets the volume levels to what you&#8217;d expect on such devices.</dl>
<dl COMPACT>
<dt>WM_MO_ENHANCED_RESAMPLING</p>
<dd>By default libWildMidi uses linear interpolation for the resampling of the sound samples. Setting this option enables the library to use a resampling method that attempts to fill in the gaps giving richer sound.</dl>
<dl COMPACT>
<dt>WM_MO_REVERB</p>
<dd>libWildMidi has an 8 reflection reverb engine. Use this option to give more depth to the output.</dl>
<dl COMPACT>
<dt>WM_MO_WHOLETEMPO</p>
<dd>Ignores the fractional or decimal part of a tempo setting. If you are having timing issues try <i>WM_MO_ROUNDTEMPO</i> before trying this option. This option added due to some software not supporting fractional tempos allowable in the MIDI specification.</dl>
<dl COMPACT>
<dt>WM_MO_ROUNDTEMPO</p>
<dd>Rounds the fractional or decimal part of a tempo setting. Try this option is you are having timing issues, if this fails then try <i>WM_MO_WHOLETEMPO</i>. This option added due to some software not supporting fractional tempos allowable in the MIDI specification.</dl>
</dl>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-wildmidi_getstring/">WildMidi_GetString</a></code>(3)<code>,</code> <code><a href="/docs/linux/man/3-wildmidi_mastervolume/">WildMidi_MasterVolume</a></code>(3)<code>,</code> <code><a href="/docs/linux/man/3-wildmidi_open/">WildMidi_Open</a></code>(3)<code>,</code> <code><a href="/docs/linux/man/3-wildmidi_openbuffer/">WildMidi_OpenBuffer</a></code>(3)<code>,</code> <code><a href="/docs/linux/man/3-wildmidi_setoption/">WildMidi_SetOption</a></code>(3)<code>,</code> <code><a href="/docs/linux/man/3-wildmidi_getoutput/">WildMidi_GetOutput</a></code>(3)<code>,</code> <code><a href="/docs/linux/man/3-wildmidi_getinfo/">WildMidi_GetInfo</a></code>(3)<code>,</code> <code><a href="/docs/linux/man/3-wildmidi_fastseek/">WildMidi_FastSeek</a></code>(3)<code>,</code> <code><a href="/docs/linux/man/3-wildmidi_close/">WildMidi_Close</a></code>(3)<code>,</code> <code><a href="/docs/linux/man/3-wildmidi_shutdown/">WildMidi_Shutdown</a></code>(3)<code>,</code> <code><a href="/docs/linux/man/5-wildmidi-cfg/">wildmidi.cfg</a></code>(5) </p>
<h2>Author</h2>
<p>Chris Ison &lt;wildcode [at] users.sf.net&gt; Bret Curtis &lt;psi29a [at] gmail.com&gt; </p>
<h2>Copyright</h2>
<p>Copyright (C) Chris Ison 2001-2010 Copyright (C) Bret Curtis 2013-2014 </p>
<p> This file is part of WildMIDI. </p>
<p> WildMIDI is free software: you can redistribute and/or modify the player under the terms of the GNU General Public License and you can redistribute and/or modify the library under the terms of the GNU Lesser General Public License as published by the Free Software Foundation, either version 3 of the licenses, or(at your option) any later version. </p>
<p> WildMIDI is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License and the GNU Lesser General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License and the GNU Lesser General Public License along with WildMIDI. If not, see &lt;<a rel="nofollow" href="http://www.gnu.org/licenses/">http://www.gnu.org/licenses/</a>&gt;. </p>
<p> This manpage is licensed under the Creative Commons Attribution-Share Alike 3.0 Unported License. To view a copy of this license, visit <a rel="nofollow" href="http://creativecommons.org/licenses/by-sa/3.0/">http://creativecommons.org/licenses/by-sa/3.0/</a> or send a letter to Creative Commons, 171 Second Street, Suite 300, San Francisco, California, 94105, USA.</p>
