---
title: "gplink(1)"
name: "gplink"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gplink/"
description: "gplink – GNU PIC linker"
---

<h2>NAME</h2>
<p> gplink &#8211; GNU PIC linker</p>
<h2>SYNOPSIS</h2>
<p> <code>gplink [options] [objects] [libraries]</code></p>
<h2>WARNING</h2>
<p> The information in this man page is an extract from the full documentation of gputils and is limited to the meaning of the options. For complete and current documentation, refer to &quot;gputils.ps&quot; located in the gputils docs directory.</p>
<h2>DESCRIPTION</h2>
<p> <code>gplink</code> combines a number of object and archive files, relocates their data, and ties up their symbol references. It outputs an executable for Microchip (TM) PIC (TM) micro-controllers. <code>gplink</code> is part of gputils. Check the <code><a href="/docs/linux/man/1-gputils/">gputils</a></code>(1) manpage for details on other GNU PIC utilities.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a FMT</code>,<code> &#8211;hex-format FMT</code></p>
<dd> gplink supports inhx8m, inhx8s, inhx16, and inhx32 hex file formats. This option controls which hex file format is used. The default is inhx32.</p>
<dt><code>-c</code>, &#8211;object</p>
<dd> Output an executable object.</p>
<dt><code>-d</code>, &#8211;debug</p>
<dd> Display debug messages.</p>
<dt><code>-f VALUE</code>,<code> &#8211;fill VALUE</code></p>
<dd> Fill unused unprotected program memory with value. The value supercedes the linker script fill value. The value must not be greater than 0xffff. The value is hex. The value may be preceeded by &quot;0x&quot;.</p>
<dt><code>-h</code>, &#8211;help</p>
<dd> Show the usage message and exit.</p>
<dt><code>-I DIR</code>,<code> &#8211;include DIR</code></p>
<dd> Specify include directory.</p>
<dt><code>-l</code>, &#8211;no-list</p>
<dd> Disable list file output.</p>
<dt><code>-m</code>, &#8211;map</p>
<dd> Output a map file.</p>
<dt><code>&#8211;mplink-compatible</code></p>
<dd> This option sets the MPLINK compatibility mode.</p>
<dt><code>-o FILE</code>,<code> &#8211;output FILE</code></p>
<dd> Alternate name of the output file.</p>
<dt><code>-O OPT</code>,<code> &#8211;optimize OPT</code></p>
<dd> Optimization level. Default value is 1.</p>
<dt><code>-q</code>, &#8211;quiet</p>
<dd> Suppress anything sent to standard output.</p>
<dt><code>-r</code>, &#8211;use-shared</p>
<dd> Attempt to relocate unshared data sections to shared memory if relocation fails.</p>
<dt><code>-s FILE</code>,<code> &#8211;script FILE</code></p>
<dd> Linker script.</p>
<dt><code>-t SIZE</code>,<code> &#8211;stack SIZE</code></p>
<dd> Create a stack section.</p>
<dt><code>-u</code>,<code> &#8211;macro symbol=[value]</code></p>
<dd> Add macro value for script.</p>
<dt><code>-v</code>, &#8211;version</p>
<dd> Show the version information and exit.</p>
<dt><code>-w</code>, &#8211;processor-mismatch</p>
<dd> Disable &quot;processor mismatch&quot; warning.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gputils/">gputils</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> Craig Franklin &lt;craigfranklin [at] users.sourceforge.net&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2002, 2003, 2004, 2005 Craig Franklin </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA. </p>
<h2>Index</h2>
