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
<p> <code>gpstrip [options] [file(s)]</code></p>
<h2>WARNING</h2>
<p> The information in this man page is an extract from the full documentation of gputils and is limited to the meaning of the options. For complete and current documentation, refer to &quot;gputils.ps&quot; located in the gputils docs directory.</p>
<p> <code>gpstrip</code> discards symbols from GNU PIC object files. <code>gpstrip</code> is part of gputils. Check the <code><a href="/docs/linux/man/1-gputils/">gputils</a></code>(1) manpage for details on other GNU PIC utilities.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-g</code>, &#8211;strip-debug</dt>
<dd> Strip debug symbols.</dd>
<dt><code>-h</code>, &#8211;help</dt>
<dd> Show the usage message and exit.</dd>
<dt><code>-k SYMBOL</code>,<code> &#8211;keep-symbol SYMBOL</code></dt>
<dd> Keep symbol.</dd>
<dt><code>-n SYMBOL</code>,<code> &#8211;strip-symbol SYMBOL</code></dt>
<dd> Remove symbol.</dd>
<dt><code>-o FILE</code>,<code> &#8211;output FILE</code></dt>
<dd> Alternate name of output file.</dd>
<dt><code>-p</code>, &#8211;preserve-dates</dt>
<dd> Preserve dates.</dd>
<dt><code>-r SECTION</code>,<code> &#8211;remove-section SECTION</code></dt>
<dd> Remove section.</dd>
<dt><code>-s</code>, &#8211;strip-all</dt>
<dd> Remove all symbols.</dd>
<dt><code>-u</code>, &#8211;strip-unneeded</dt>
<dd> Strip symbols not need for relocations.</dd>
<dt><code>-v</code>, &#8211;version</dt>
<dd> Show the version information and exit.</dd>
<dt><code>-V</code>, &#8211;verbose</dt>
<dd> Verbose mode.</dd>
<dt><code>-x</code>, &#8211;discard-all</dt>
<dd> Remove non-global symbols.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gputils/">gputils</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> Craig Franklin &lt;craigfranklin [at] users.sourceforge.net&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2005 Craig Franklin </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA. </p>
