---
title: "zvbi-chains(1)"
name: "zvbi-chains"
section: "1"
letter: "z"
url: "/docs/linux/man/1-zvbi-chains/"
description: "zvbi-chains – VBI proxy wrapper"
---

<h2>NAME</h2>
<p> zvbi-chains &#8211; VBI proxy wrapper</p>
<h2>SYNOPSIS</h2>
<p> <code>zvbi-chains [ options ]</code></p>
<h2>DESCRIPTION</h2>
<p> <code>zvbi-chains</code> is a small wrapper which executes the VBI application given on the command line while overloading several C library calls (such as <a href="/docs/linux/man/2-open/">open</a>(2) and <a href="/docs/linux/man/2-read/">read</a>(2)) so that the application can be forced to access VBI devices via the VBI proxy instead of device files directly. </p>
<p> LD_PRELOAD is used to intercept C library calls and call functions in the libzvbi-chain shared library instead. Parameters given on the command line (e.g. device path) are passed to the library by means of environment variables.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-dev</code> path</p>
<dd> Path of a VBI device from which to read data.</p>
<dt><code>-debug</code> level</p>
<dd> Enables debug output: 0 = off (default); 1 = warnings, 2 = all messages.</p>
<dt><code>-help</code></p>
<dd> Print a short description of all command line options. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-zvbid/">zvbid</a>(1), <a href="/docs/linux/man/8-v4l-conf/">v4l-conf</a>(8)<br />
 <a rel="nofollow" href="http://zapping.sourceforge.net/">http://zapping.sourceforge.net/</a> (homepage)</p>
<h2>AUTHOR</h2>
<p> Tom Zoerner (tomzo AT users.sourceforge.net)</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2003, 2004 Tom Zoerner </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA. </p>
<h2>Index</h2>
