---
title: "wildmidi_getoutput(3)"
name: "wildmidi_getoutput"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wildmidi_getoutput/"
description: "WildMidi_GetOutput – retrieve raw audio data"
---

<p>WildMidi_GetOutput &#8211; retrieve raw audio data </p>
<h2>Library</h2>
<p><code>libWildMidi</code> </p>
<h2>Synopsis</h2>
<p><code>#include &lt;wildmidi_lib.h&gt;</code> </p>
<p> <code>int WildMidi_GetOutput (midi *</code><i>handle</i>, char *<i>buffer</i>, unsigned long int <i>size</i>); </p>
<h2>Description</h2>
<p>Places <i>size</i> bytes of audio data from a <i>handle</i>, previously opened by <code><a href="/docs/linux/man/3-wildmidi_open/">WildMidi_Open</a></code>(3) or <code><a href="/docs/linux/man/3-wildmidi_openbuffer/">WildMidi_OpenBuffer</a></code>(3), into a buffer pointer to by <i>buffer</i>. </p>
<p> <i>buffer</i> must be at least <i>size</i> bytes, with <i>size</i> being a multiple of 4 as the data is stored in 16bit interleaved stereo format. </p>
<dl COMPACT>
<dt><i>handle</i></p>
<dd>The identifier obtained from opening a midi file with <code><a href="/docs/linux/man/3-wildmidi_open/">WildMidi_Open</a></code>(3) or <code><a href="/docs/linux/man/3-wildmidi_openbuffer/">WildMidi_OpenBuffer</a></code>(3)</dl>
<dl COMPACT>
<dt><i>buffer</i></p>
<dd>The location supplied by the calling program where libWildMidi is to store the audio data. The audio data will be stored as signed 16bit interleaved stereo in little endian byte order.</dl>
<dl COMPACT>
<dt><i>size</i></p>
<dd>The size of the buffer in bytes. Since libWildMidi processes the audio in 16bit interleaved stereo format, this value needs to be a multiple of 4.</dl>
<h2>Return Value</h2>
<p>Returns -1 on error along with an error message sent to stderr, 0 when there is no more audio data, otherwise the number of bytes of audio data written to <i>buffer</i>. </p>
<p> NOTE: if the return value is less than the size you gave, this does not denote an error, it simply means the lib reached the end of the midi before it could fill the buffer. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-wildmidi_getstring/">WildMidi_GetString</a></code>(3)<code>,</code> <code><a href="/docs/linux/man/3-wildmidi_init/">WildMidi_Init</a></code>(3)<code>,</code> <code><a href="/docs/linux/man/3-wildmidi_mastervolume/">WildMidi_MasterVolume</a></code>(3)<code>,</code> <code><a href="/docs/linux/man/3-wildmidi_open/">WildMidi_Open</a></code>(3)<code>,</code> <code><a href="/docs/linux/man/3-wildmidi_openbuffer/">WildMidi_OpenBuffer</a></code>(3)<code>,</code> <code><a href="/docs/linux/man/3-wildmidi_setoption/">WildMidi_SetOption</a></code>(3)<code>,</code> <code><a href="/docs/linux/man/3-wildmidi_getinfo/">WildMidi_GetInfo</a></code>(3)<code>,</code> <code><a href="/docs/linux/man/3-wildmidi_fastseek/">WildMidi_FastSeek</a></code>(3)<code>,</code> <code><a href="/docs/linux/man/3-wildmidi_close/">WildMidi_Close</a></code>(3)<code>,</code> <code><a href="/docs/linux/man/3-wildmidi_shutdown/">WildMidi_Shutdown</a></code>(3)<code>,</code> <code><a href="/docs/linux/man/5-wildmidi-cfg/">wildmidi.cfg</a></code>(5) </p>
<h2>Author</h2>
<p>Chris Ison &lt;wildcode [at] users.sf.net&gt; Bret Curtis &lt;psi29a [at] gmail.com&gt; </p>
<h2>Copyright</h2>
<p>Copyright (C) Chris Ison 2001-2010 Copyright (C) Bret Curtis 2013-2014 </p>
<p> This file is part of WildMIDI. </p>
<p> WildMIDI is free software: you can redistribute and/or modify the player under the terms of the GNU General Public License and you can redistribute and/or modify the library under the terms of the GNU Lesser General Public License as published by the Free Software Foundation, either version 3 of the licenses, or(at your option) any later version. </p>
<p> WildMIDI is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License and the GNU Lesser General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License and the GNU Lesser General Public License along with WildMIDI. If not, see &lt;<a rel="nofollow" href="http://www.gnu.org/licenses/">http://www.gnu.org/licenses/</a>&gt;. </p>
<p> This manpage is licensed under the Creative Commons Attribution-Share Alike 3.0 Unported License. To view a copy of this license, visit <a rel="nofollow" href="http://creativecommons.org/licenses/by-sa/3.0/">http://creativecommons.org/licenses/by-sa/3.0/</a> or send a letter to Creative Commons, 171 Second Street, Suite 300, San Francisco, California, 94105, USA.</p>
