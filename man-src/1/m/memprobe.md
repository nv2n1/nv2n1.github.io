---
title: "memprobe(1)"
name: "memprobe"
section: "1"
letter: "m"
url: "/docs/linux/man/1-memprobe/"
description: "memprobe – ROOT utility to examine memory usage"
---

<h2 class="name">NAME</h2>
<p> memprobe &#8211; ROOT utility to examine memory usage </p>
<h2>SYNOPSIS</h2>
<p> <code>memprobe</code> <i>[options]</i></p>
<h2>DESCRIPTION</h2>
<p> To activate the memory checker you have to set in the <code>.rootrc</code> file the resource <code>Root.MemCheck</code> to 1 (e.g.: <code>Root.MemCheck: 1</code>) and you have to link with <code>libNew.so</code> (e.g. use <code>root-config &#8211;new &#8211;libs</code>) or use <code>rootn.exe</code>. </p>
<p> When all this is the case you will find at the end of the program execution a file <code>memcheck.out</code> in the directory where you started your ROOT program. Alternatively you can set the resource <code>Root.MemCheckFile</code> to the name of a file to which the leak information will be written. The contents of this <code>memcheck.out</code> file can be analyzed and transformed into printable text via the <code>memprobe</code> program (in <code>/usr/bin</code>).</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-root/">root</a></i>(1) </p>
<p> See also the <code>ROOT</code> webpages: <i><a rel="nofollow" href="http://root.cern.ch">http://root.cern.ch</a></i></p>
<h2>ORIGINAL AUTHORS</h2>
<p> The ROOT team (see web page above):</p>
<dl>
<dt>
<dd> <code>Rene Brun</code> and <code>Fons Rademakers</code></dl>
<h2>COPYRIGHT</h2>
<p> This library is free software; you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation; either version 2.1 of the License, or (at your option) any later version. </p>
<p> This library is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more details. </p>
<p> You should have received a copy of the GNU Lesser General Public License along with this library; if not, write to the Free Software Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Christian Holm Christensen &lt;cholm [at] nbi.dk&gt;, for the Debian GNU/Linux system (but may be used by others). </p>
<h2>Index</h2>
