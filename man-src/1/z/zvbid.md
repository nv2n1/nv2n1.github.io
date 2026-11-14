---
title: "zvbid(1)"
name: "zvbid"
section: "1"
letter: "z"
url: "/docs/linux/man/1-zvbid/"
description: "zvbid – VBI proxy daemon"
---

<h2>NAME</h2>
<p> zvbid &#8211; VBI proxy daemon</p>
<h2>SYNOPSIS</h2>
<p> <code>zvbid [ options ]</code></p>
<h2>DESCRIPTION</h2>
<p> <code>zvbid</code> is a proxy for VBI devices, i.e. it forwards one or more VBI data streams to one or more connected clients and manages channel change requests.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-dev</code> path</p>
<dd> Path of a device from which to read data. This argument can be given several times with different devices.</p>
<dt><code>-buffers</code> count</p>
<dd> Number of buffers to allocate for capturing VBI raw data from devices which support streaming (currently only video4linux, rev. 2) A higher number of buffers can prevent data loss in case of high latency. The downside is higher memory consumption (typically 65kB per buffer.) Default count is 8, maximum is 32.</p>
<dt><code>-nodetach</code></p>
<dd> Daemon process remains connected to the terminal from which it was started (e.g. so that you can stop it by pressing Control-C keys). Intended for trouble shooting only.</p>
<dt><code>-kill</code></p>
<dd> Terminates a proxy daemon running for the given device.</p>
<dt><code>-debug</code> level</p>
<dd> Enables debug output: 0= off(default); 1= general messages; In addition 2, 4, 8, &#8230; can be added to enable debug output for various categories.</p>
<dt><code>-syslog</code> level</p>
<dd> Enables syslog output.</p>
<dt><code>-loglevel</code> level</p>
<dd> Log file level</p>
<dt><code>-logfile</code> path</p>
<dd> Path to the log file.</p>
<dt><code>-maxclients</code> count</p>
<dd> Max. number of clients which are allowed to connect simultaneously.</p>
<dt><code>-help</code></p>
<dd> Print a short description of all command line options. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-zvbi-chains/">zvbi-chains</a>(1), <a href="/docs/linux/man/8-v4l-conf/">v4l-conf</a>(8)<br />
 <a rel="nofollow" href="http://zapping.sourceforge.net/">http://zapping.sourceforge.net/</a> (homepage)</p>
<h2>AUTHOR</h2>
<p> Tom Zoerner (tomzo AT users.sourceforge.net)</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2003,2004 Tom Zoerner </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA. </p>
<h2>Index</h2>
