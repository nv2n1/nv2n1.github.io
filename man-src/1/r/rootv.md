---
title: "rootv(1)"
name: "rootv"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rootv/"
description: "rootv – display TV using the Xvideo extension"
---

<h2>NAME</h2>
<p> rootv &#8211; display TV using the Xvideo extension</p>
<h2>SYNOPSIS</h2>
<p> <code>rootv [ options ]</code></p>
<h2>DESCRIPTION</h2>
<p> <code>rootv</code> puts a video to some window. By default it creates its own window, but you can also ask it to use the root window (thus the name) or any other window. <code>rootv</code> needs the Xvideo extension. </p>
<p> <code>rootv</code> itself provides no way to control video/audio/tuner. You can use v4lctl to do this.</p>
<h2>OPTIONS</h2>
<p> <code>rootv</code> knows a number of command line options to modify the behaviour.</p>
<dl>
<dt><code>-help</code></p>
<dd> Print a short description of all command line options.</p>
<dt><code>-verbose</code></p>
<dd> Be verbose. That will dump some debug messages to stderr.</p>
<dt><code>-root</code></p>
<dd> Put the video onto the root window instead of creating a new window.</p>
<dt><code>-id &lt;win&gt;</code></p>
<dd> Put the video into the window &lt;win&gt; instead of creating a new window.</p>
<dt><code>-station &lt;st&gt;</code></p>
<dd> Tune station &lt;st&gt;. This just calls v4lctl, which in turn will look up the station in your ~/.xawtv config file.</p>
<dt><code>-no-mute</code></p>
<dd> Don&#8217;t toggle mute. By default rootv will unmute the TV card when it starts and mute it on exit. It does this using the XV_MUTE attribute (if available).</p>
<dt><code>-port &lt;n&gt;</code></p>
<dd> Use Xvideo port &lt;n&gt;. Try the -verbose switch if you want to know which ones are available.</p>
<dt><code>-bg</code></p>
<dd> Fork into background.</p>
<dt><code>-wm</code></p>
<dd> Print WindowMaker menu (set stations using v4lctl).</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-xawtv/">xawtv</a>(1), <a href="/docs/linux/man/1-fbtv/">fbtv</a>(1), <a href="/docs/linux/man/1-v4lctl/">v4lctl</a>(1)</p>
<h2>AUTHOR</h2>
<p> Gerd Knorr &lt;kraxel [at] bytesex.org&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2000-2002 Gerd Knorr &lt;kraxel [at] bytesex.org&gt; </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA. </p>
<h2>Index</h2>
