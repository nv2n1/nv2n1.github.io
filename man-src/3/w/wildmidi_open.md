---
title: "wildmidi_open(3)"
name: "wildmidi_open"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wildmidi_open/"
description: "WildMidi_Open – Open a midi file for processing"
---

<p>WildMidi_Open &#8211; Open a midi file for processing</p>
<h2>Library</h2>
<p><code>libWildMidi</code> </p>
<h2>Synopsis</h2>
<p><code>#include &lt;wildmidi_lib.h&gt;</code> </p>
<p> <code>midi *WildMidi_Open (const char *</code><i>midifile</i>) </p>
<h2>Description</h2>
<p>Open a MIDI file pointed to by <i>midifile</i> for processing. This file must be in standard midi format. </p>
<h2>Return Value</h2>
<p>Returns NULL on error and sends a message to stderr, otherwise returns a handle for the midi file opened. This handle is used by most functions in libWildMidi to identify which midi file we are referring to. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-wildmidi_getstring/">WildMidi_GetString</a></code>(3)<code>,</code> <code><a href="/docs/linux/man/3-wildmidi_init/">WildMidi_Init</a></code>(3)<code>,</code> <code><a href="/docs/linux/man/3-wildmidi_mastervolume/">WildMidi_MasterVolume</a></code>(3)<code>,</code> <code><a href="/docs/linux/man/3-wildmidi_openbuffer/">WildMidi_OpenBuffer</a></code>(3)<code>,</code> <code><a href="/docs/linux/man/3-wildmidi_setoption/">WildMidi_SetOption</a></code>(3)<code>,</code> <code><a href="/docs/linux/man/3-wildmidi_getoutput/">WildMidi_GetOutput</a></code>(3)<code>,</code> <code><a href="/docs/linux/man/3-wildmidi_getinfo/">WildMidi_GetInfo</a></code>(3)<code>,</code> <code><a href="/docs/linux/man/3-wildmidi_fastseek/">WildMidi_FastSeek</a></code>(3)<code>,</code> <code><a href="/docs/linux/man/3-wildmidi_close/">WildMidi_Close</a></code>(3)<code>,</code> <code><a href="/docs/linux/man/3-wildmidi_shutdown/">WildMidi_Shutdown</a></code>(3)<code>,</code> <code><a href="/docs/linux/man/5-wildmidi-cfg/">wildmidi.cfg</a></code>(5) </p>
<h2>Author</h2>
<p>Chris Ison &lt;wildcode [at] users.sf.net&gt; Bret Curtis &lt;psi29a [at] gmail.com&gt; </p>
<h2>Copyright</h2>
<p>Copyright (C) Chris Ison 2001-2010 Copyright (C) Bret Curtis 2013-2014 </p>
<p> This file is part of WildMIDI. </p>
<p> WildMIDI is free software: you can redistribute and/or modify the player under the terms of the GNU General Public License and you can redistribute and/or modify the library under the terms of the GNU Lesser General Public License as published by the Free Software Foundation, either version 3 of the licenses, or(at your option) any later version. </p>
<p> WildMIDI is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License and the GNU Lesser General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License and the GNU Lesser General Public License along with WildMIDI. If not, see &lt;<a rel="nofollow" href="http://www.gnu.org/licenses/">http://www.gnu.org/licenses/</a>&gt;. </p>
<p> This manpage is licensed under the Creative Commons Attribution-Share Alike 3.0 Unported License. To view a copy of this license, visit <a rel="nofollow" href="http://creativecommons.org/licenses/by-sa/3.0/">http://creativecommons.org/licenses/by-sa/3.0/</a> or send a letter to Creative Commons, 171 Second Street, Suite 300, San Francisco, California, 94105, USA.</p>
