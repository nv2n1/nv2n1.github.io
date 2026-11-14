---
title: "gpstrip(1)"
name: "gpstrip"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gpstrip/"
description: "gpstrip – discard symbols from object file"
---

<h2>NAME</h2>
<p> gpstrip &#8211; discard symbols from object file</p>
<h2>SYNOPSIS</h2>
<p> <code>gpstrip [options] [file(s)]</code></p>
<h2>WARNING</h2>
<p> The information in this man page is an extract from the full documentation of gputils and is limited to the meaning of the options. For complete and current documentation, refer to &quot;gputils.ps&quot; located in the gputils docs directory.</p>
<h2>DESCRIPTION</h2>
<p> <code>gpstrip</code> discards symbols from GNU PIC object files. <code>gpstrip</code> is part of gputils. Check the <code><a href="/docs/linux/man/1-gputils/">gputils</a></code>(1) manpage for details on other GNU PIC utilities.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-g</code>, &#8211;strip-debug</p>
<dd> Strip debug symbols.</p>
<dt><code>-h</code>, &#8211;help</p>
<dd> Show the usage message and exit.</p>
<dt><code>-k SYMBOL</code>,<code> &#8211;keep-symbol SYMBOL</code></p>
<dd> Keep symbol.</p>
<dt><code>-n SYMBOL</code>,<code> &#8211;strip-symbol SYMBOL</code></p>
<dd> Remove symbol.</p>
<dt><code>-o FILE</code>,<code> &#8211;output FILE</code></p>
<dd> Alternate name of output file.</p>
<dt><code>-p</code>, &#8211;preserve-dates</p>
<dd> Preserve dates.</p>
<dt><code>-r SECTION</code>,<code> &#8211;remove-section SECTION</code></p>
<dd> Remove section.</p>
<dt><code>-s</code>, &#8211;strip-all</p>
<dd> Remove all symbols.</p>
<dt><code>-u</code>, &#8211;strip-unneeded</p>
<dd> Strip symbols not need for relocations.</p>
<dt><code>-v</code>, &#8211;version</p>
<dd> Show the version information and exit.</p>
<dt><code>-V</code>, &#8211;verbose</p>
<dd> Verbose mode.</p>
<dt><code>-x</code>, &#8211;discard-all</p>
<dd> Remove non-global symbols.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gputils/">gputils</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> Craig Franklin &lt;craigfranklin [at] users.sourceforge.net&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2005 Craig Franklin </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA. </p>
<h2>Index</h2>
