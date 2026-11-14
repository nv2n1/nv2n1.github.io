---
title: "soxi(1)"
name: "soxi"
section: "1"
letter: "s"
url: "/docs/linux/man/1-soxi/"
description: "SoXI – Sound eXchange Information, display sound file metadata"
---

<h2>NAME</h2>
<p> SoXI &#8211; Sound eXchange Information, display sound file metadata</p>
<h2>SYNOPSIS</h2>
<p> <code>soxi</code> [<code>-V</code>[<i>level</i>]] [<code>-T</code>] [<code>-t</code>|<code>-r</code>|<code>-c</code>|<code>-s</code>|<code>-d</code>|<code>-D</code>|<code>-b</code>|<code>-B</code>|<code>-e</code>|<code>-a</code>] <i>infile1</i> &#8230;</p>
<h2>DESCRIPTION</h2>
<p> Displays information from the header of a given audio file or files. Supported audio file types are listed and described in <code><a href="/docs/linux/man/7-soxformat/">soxformat</a></code>(7). Note however, that <code>soxi</code> is intended for use only with audio files with a self-describing header. </p>
<p> By default, as much information as is available is shown. An option may be given to select just a single piece of information (perhaps for use in a script or batch-file).</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-V</code></p>
<dd> Set verbosity. See <code><a href="/docs/linux/man/1-sox/">sox</a></code>(1) for details.</p>
<dt><code>-T</code></p>
<dd> Used with multiple files; changes the behaviour of <code>-s</code>, <code>-d</code> and <code>-D</code> to display the total across all given files. Note that when used with <code>-s</code> with files with different sampling rates, this is of questionable value.</p>
<dt><code>-t</code></p>
<dd> Show detected file-type.</p>
<dt><code>-r</code></p>
<dd> Show sample-rate.</p>
<dt><code>-c</code></p>
<dd> Show number of channels.</p>
<dt><code>-s</code></p>
<dd> Show number of samples (0 if unavailable).</p>
<dt><code>-d</code></p>
<dd> Show duration in hours, minutes and seconds (0 if unavailable). Equivalent to number of samples divided by the sample-rate.</p>
<dt><code>-D</code></p>
<dd> Show duration in seconds (0 if unavailable).</p>
<dt><code>-b</code></p>
<dd> Show number of bits per sample.</p>
<dt><code>-B</code></p>
<dd> Show the bitrate averaged over the whole file (0 if unavailable).</p>
<dt><code>-e</code></p>
<dd> Show the name of the audio encoding.</p>
<dt><code>-a</code></p>
<dd> Show file comments (annotations) if available.</dl>
<h2>BUGS</h2>
<p> Please report any bugs found in this version of SoX to the mailing list (sox-users [at] lists.sourceforge.net).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-sox/">sox</a></code>(1), <code><a href="/docs/linux/man/7-soxformat/">soxformat</a></code>(7), <code><a href="/docs/linux/man/3-libsox/">libsox</a></code>(3) </p>
<p> The SoX web site at <a rel="nofollow" href="http://sox.sourceforge.net">http://sox.sourceforge.net</a></p>
<h2>LICENSE</h2>
<p> Copyright 2008-2013 by Chris Bagwell and SoX Contributors. </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.</p>
<h2>AUTHORS</h2>
<p> Chris Bagwell (cbagwell [at] users.sourceforge.net). Other authors and contributors are listed in the ChangeLog file that is distributed with the source code. </p>
<h2>Index</h2>
