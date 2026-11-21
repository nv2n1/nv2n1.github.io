---
title: "scantv(1)"
name: "scantv"
section: "1"
letter: "s"
url: "/docs/linux/man/1-scantv/"
description: "scantv – scan a v4l device for TV stations."
---

<h2>NAME</h2>
<p> scantv &#8211; scan a v4l device for TV stations.</p>
<h2>SYNOPSIS</h2>
<p> <code>scantv [ options ]</code></p>
<h2>DESCRIPTION</h2>
<p> <code>scantv</code> scans a v4l device for available TV stations and writes a xawtv/fbtv config file.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-i input</code></dt>
<dd> set tv <code>i</code>nput (Television/Composite1/S-video and so on). Default is Television.</dd>
<dt><code>-n norm</code></dt>
<dd> set tv <code>n</code>orm. scantv will ask interactively if none is given.</dd>
<dt><code>-f table</code></dt>
<dd> set <code>f</code>requency table. scantv will ask interactively if none is given.</dd>
<dt><code>-o outfile</code></dt>
<dd> specify <code>o</code>utput file. If none is specified, scantv writes to stdout.</dd>
<dt><code>-c device</code></dt>
<dd> specify video device file. Default is /dev/video0.</dd>
<dt><code>-D driver</code></dt>
<dd> specify video driver name. Default is &quot;libv4l&quot;.</dd>
<dt><code>-C device</code></dt>
<dd> specify vbi device file. Default is /dev/vbi0.</dd>
<dt><code>-s</code></dt>
<dd> skip channel <code>s</code>can, just write norm + freqtab to the config file.</dd>
<dt><code>-a</code></dt>
<dd> Do a full scan (i.e. all frequencies, not just the ones from the frequency table).</dd></dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-xawtv/">xawtv</a>(1), <a href="/docs/linux/man/1-fbtv/">fbtv</a>(1)</p>
<h2>AUTHOR</h2>
<p> Gerd Knorr &lt;kraxel [at] bytesex.org&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2000 Gerd Knorr &lt;kraxel [at] bytesex.org&gt; </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA. </p>
