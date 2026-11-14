---
title: "wildmidi_setoption(3)"
name: "wildmidi_setoption"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wildmidi_setoption/"
description: "WildMidi_SetOption – Set a library option for a specific midi"
---

<p>WildMidi_SetOption &#8211; Set a library option for a specific midi </p>
<h2>Library</h2>
<p><code>libWildMidi</code> </p>
<h2>Synopsis</h2>
<p><code>#include &lt;wildmidi_lib.h&gt;</code> </p>
<p> <code>int WildMidi_SetOption (midi *</code><i>handle</i>, unsigned short int <i>options</i>, unsigned short int <i>setting</i>) </p>
<h2>Description</h2>
<p>Set a library option for a specific midi. </p>
<dl COMPACT>
<dt><i>handle</i></p>
<dd>The identifier obtained from opening a midi file with <code><a href="/docs/linux/man/3-wildmidi_open/">WildMidi_Open</a></code>(3) or <code><a href="/docs/linux/man/3-wildmidi_openbuffer/">WildMidi_OpenBuffer</a></code>(3)</dl>
<p> <i>options</i> The option or options you wish to change. </p>
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
</dl>
<dl COMPACT>
<dt>setting</p>
<dd>To turn on an option, repeat that option here. To turn off an option, do not put the option here.</dl>
<dl COMPACT>
<dt>Example: To turn on Reverb</p>
<dd>WildMidi_SetOption(handle, WM_MO_REVERB, WM_MO_REVERB);</p>
<dt>Example: To turn off Reverb</p>
<dd>WildMidi_SetOption(handle, WM_MO_REVERB, 0);</p>
<dt>Example: To turn on Reverb and Enhanced Resampling</p>
<dd>WildMidi_SetOption(handle, (WM_MO_REVERB | WM_MO_ENHANCED_RESAMPLING), (WM_MO_REVERB | WM_MO_ENHANCED_RESAMPLING));</dl>
<h2>Return Value</h2>
<p>Returns -1 on error, otherwise returns 0.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-wildmidi_getstring/">WildMidi_GetString</a></code>(3)<code>,</code> <code><a href="/docs/linux/man/3-wildmidi_init/">WildMidi_Init</a></code>(3)<code>,</code> <code><a href="/docs/linux/man/3-wildmidi_mastervolume/">WildMidi_MasterVolume</a></code>(3)<code>,</code> <code><a href="/docs/linux/man/3-wildmidi_open/">WildMidi_Open</a></code>(3)<code>,</code> <code><a href="/docs/linux/man/3-wildmidi_openbuffer/">WildMidi_OpenBuffer</a></code>(3)<code>,</code> <code><a href="/docs/linux/man/3-wildmidi_setoption/">WildMidi_SetOption</a></code>(3)<code>,</code> <code><a href="/docs/linux/man/3-wildmidi_getoutput/">WildMidi_GetOutput</a></code>(3)<code>,</code> <code><a href="/docs/linux/man/3-wildmidi_getinfo/">WildMidi_GetInfo</a></code>(3)<code>,</code> <code><a href="/docs/linux/man/3-wildmidi_fastseek/">WildMidi_FastSeek</a></code>(3)<code>,</code> <code><a href="/docs/linux/man/3-wildmidi_close/">WildMidi_Close</a></code>(3)<code>,</code> <code><a href="/docs/linux/man/3-wildmidi_shutdown/">WildMidi_Shutdown</a></code>(3)<code>,</code> <code><a href="/docs/linux/man/5-wildmidi-cfg/">wildmidi.cfg</a></code>(5) </p>
<h2>Author</h2>
<p>Chris Ison &lt;wildcode [at] users.sf.net&gt; Bret Curtis &lt;psi29a [at] gmail.com&gt; </p>
<h2>Copyright</h2>
<p>Copyright (C) Chris Ison 2001-2010 Copyright (C) Bret Curtis 2013-2014 </p>
<p> This file is part of WildMIDI. </p>
<p> WildMIDI is free software: you can redistribute and/or modify the player under the terms of the GNU General Public License and you can redistribute and/or modify the library under the terms of the GNU Lesser General Public License as published by the Free Software Foundation, either version 3 of the licenses, or(at your option) any later version. </p>
<p> WildMIDI is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License and the GNU Lesser General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License and the GNU Lesser General Public License along with WildMIDI. If not, see &lt;<a rel="nofollow" href="http://www.gnu.org/licenses/">http://www.gnu.org/licenses/</a>&gt;. </p>
<p> This manpage is licensed under the Creative Commons Attribution-Share Alike 3.0 Unported License. To view a copy of this license, visit <a rel="nofollow" href="http://creativecommons.org/licenses/by-sa/3.0/">http://creativecommons.org/licenses/by-sa/3.0/</a> or send a letter to Creative Commons, 171 Second Street, Suite 300, San Francisco, California, 94105, USA.</p>
