---
title: "pia(1)"
name: "pia"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pia/"
description: "pia – play media files"
---

<h2>NAME</h2>
<p> pia &#8211; play media files</p>
<h2>SYNOPSIS</h2>
<p> <code>pia [ options ] movie</code></p>
<h2>DESCRIPTION</h2>
<p> <code>pia</code> is a small X11 tool which plays movie files.</p>
<h2>OPTIONS</h2>
<p> <code>pia</code> understands the usual toolkit options (-geometry + friends). Additional options are:</p>
<dl>
<dt><code>-h</code></dt>
<dd> display help text</dd>
<dt><code>-v</code></dt>
<dd> be verbose.</dd>
<dt><code>-debug</code></dt>
<dd> enable debug messages.</dd>
<dt><code>-dsp &lt;dev&gt;</code></dt>
<dd> Use OSS device &lt;dev&gt; for sound.</dd>
<dt><code>-noxv</code></dt>
<dd> Disable Xvideo extension.</dd>
<dt><code>-nogl</code></dt>
<dd> Disable OpenGL.</dd>
<dt><code>-noaudio</code></dt>
<dd> Don&#8217;t play sound.</dd>
<dt><code>-novideo</code></dt>
<dd> Don&#8217;t play video.</dd>
<dt><code>-slow n</code></dt>
<dd> Slowdown video playback by factor n. n=2 doubles playback time, &#8230; This also turns off audio playback.</dd></dl>
<h2>SUPPORTED MOVIE FORMATS</h2>
<p> Main purpose of this utility is to playback movie files recorded by xawtv, motv and streamer. It should be able to playback every AVI or QuickTime movie written by one of the mentioned utilities. Feel free to submit a bug report if this doesn&#8217;t work for some file.</p>
<h3>QuickTime</h3>
<p> <code>pia</code> uses libquicktime to decode quicktime movies, thus it should be able to decode and playback all movies with codecs supported by libquicktime.</p>
<h3>AVI</h3>
<p> AVI support is very limited. Video: uncompressed RGB data (15 and 24 bpp) and mjpeg is supported. Audio: only uncompressed PCM data works.</p>
<h3>WAV</h3>
<p> WAV files are playable too, with the same limitation like AVI audio: only uncompressed PCM data.</p>
<h2>AUTHOR</h2>
<p> Gerd Knorr &lt;kraxel [at] bytesex.org&gt;</p>
<h2>COPYRIGHT</h2>
<p> 2002 Gerd Knorr </p>
<p> Copyright (C) 2002 Gerd Knorr &lt;kraxel [at] bytesex.org&gt; </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA. </p>
