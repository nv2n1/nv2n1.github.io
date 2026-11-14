---
title: "ttv(1)"
name: "ttv"
section: "1"
letter: "t"
url: "/docs/linux/man/1-ttv/"
description: "ttv – display TV/video on a tty"
---

<h2>NAME</h2>
<p> ttv &#8211; display TV/video on a tty</p>
<h2>SYNOPSIS</h2>
<p> <code>ttv [ options ] [ station name ]</code></p>
<h2>DESCRIPTION</h2>
<p> <code>ttv</code> displays TV/video on a terminal, rendering the images using aalib.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code></p>
<dd> print help text.</p>
<dt><code>-f</code></p>
<dd> use fast aalib render function.</p>
<dt><code>-c device</code></p>
<dd> video4linux device (default is /dev/video0).</p>
<dt><code>-D driver</code></p>
<dd> video4linux driver (default is &quot;libv4l&quot;).</dl>
<p> There are also lots of options for aalib, check the aalib documentation for more details on them. The help text includes a list.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-xawtv/">xawtv</a>(1), <a href="/docs/linux/man/1-fbtv/">fbtv</a>(1)</p>
<h2>AUTHOR</h2>
<p> Gerd Knorr &lt;kraxel [at] bytesex.org&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2000 Gerd Knorr &lt;kraxel [at] bytesex.org&gt; </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA. </p>
<h2>Index</h2>
