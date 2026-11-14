---
title: "wildmidi_openbuffer(3)"
name: "wildmidi_openbuffer"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wildmidi_openbuffer/"
description: "WildMidi_OpenBuffer – Open a midi file buffer for processing"
---

<p>WildMidi_OpenBuffer &#8211; Open a midi file buffer for processing </p>
<h2>Library</h2>
<p><code>libWildMidi</code> </p>
<h2>Synopsis</h2>
<p><code>#include &lt;wildmidi_lib.h&gt;</code> </p>
<p> <code>midi *WildMidi_OpenBuffer (unsigned char *</code><i>midibuffer</i>, unsigned long int <i>size</i>) </p>
<h2>Description</h2>
<p>Open a midi file, that you have buffered in memory, for processing. </p>
<dl COMPACT>
<dt><i>midibuffer</i></p>
<dd>The memory location of the buffered midi file. This buffer needs to be in standard midi file format. Once this function is called, any changes to the buffer will have no effect.</dl>
<dl COMPACT>
<dt><i>size</i></p>
<dd>This is the size of the midi file in bytes that is stored in memory.</dl>
<h2>Return Value</h2>
<p>Returns NULL on error, otherwise returns a handle for the midi buffer opened. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-wildmidi_getstring/">WildMidi_GetString</a></code>(3)<code>,</code> <code><a href="/docs/linux/man/3-wildmidi_init/">WildMidi_Init</a></code>(3)<code>,</code> <code><a href="/docs/linux/man/3-wildmidi_mastervolume/">WildMidi_MasterVolume</a></code>(3)<code>,</code> <code><a href="/docs/linux/man/3-wildmidi_open/">WildMidi_Open</a></code>(3)<code>,</code> <code><a href="/docs/linux/man/3-wildmidi_setoption/">WildMidi_SetOption</a></code>(3)<code>,</code> <code><a href="/docs/linux/man/3-wildmidi_getoutput/">WildMidi_GetOutput</a></code>(3)<code>,</code> <code><a href="/docs/linux/man/3-wildmidi_getinfo/">WildMidi_GetInfo</a></code>(3)<code>,</code> <code><a href="/docs/linux/man/3-wildmidi_fastseek/">WildMidi_FastSeek</a></code>(3)<code>,</code> <code><a href="/docs/linux/man/3-wildmidi_close/">WildMidi_Close</a></code>(3)<code>,</code> <code><a href="/docs/linux/man/3-wildmidi_shutdown/">WildMidi_Shutdown</a></code>(3)<code>,</code> <code><a href="/docs/linux/man/5-wildmidi-cfg/">wildmidi.cfg</a></code>(5) </p>
<h2>Author</h2>
<p>Chris Ison &lt;wildcode [at] users.sf.net&gt; Bret Curtis &lt;psi29a [at] gmail.com&gt; </p>
<h2>Copyright</h2>
<p>Copyright (C) Chris Ison 2001-2010 Copyright (C) Bret Curtis 2013-2014 </p>
<p> This file is part of WildMIDI. </p>
<p> WildMIDI is free software: you can redistribute and/or modify the player under the terms of the GNU General Public License and you can redistribute and/or modify the library under the terms of the GNU Lesser General Public License as published by the Free Software Foundation, either version 3 of the licenses, or(at your option) any later version. </p>
<p> WildMIDI is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License and the GNU Lesser General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License and the GNU Lesser General Public License along with WildMIDI. If not, see &lt;<a rel="nofollow" href="http://www.gnu.org/licenses/">http://www.gnu.org/licenses/</a>&gt;. </p>
<p> This manpage is licensed under the Creative Commons Attribution-Share Alike 3.0 Unported License. To view a copy of this license, visit <a rel="nofollow" href="http://creativecommons.org/licenses/by-sa/3.0/">http://creativecommons.org/licenses/by-sa/3.0/</a> or send a letter to Creative Commons, 171 Second Street, Suite 300, San Francisco, California, 94105, USA.</p>
