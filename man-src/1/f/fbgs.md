---
title: "fbgs(1)"
name: "fbgs"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fbgs/"
description: "fbgs – Poor man’s PostScript/pdf viewer for the linux framebuffer console. # #"
---

<p>#</p>
<h2>SYNOPSIS</h2>
<p> <code>fbgs</code><br />
&nbsp;<wbr>[<code>-l</code>|<code>-xl</code>|<code>-xxl</code>|<code>-r</code>&nbsp;<wbr><i>n</i>]&nbsp;<wbr>[<code>-c</code>]&nbsp;<wbr>[<code>-b</code>]&nbsp;<wbr>[<code>-p</code>&nbsp;<wbr><i>password</i>]&nbsp;<wbr>[<code>&#8211;fp</code>&nbsp;<wbr><i>number</i>]&nbsp;<wbr>[<code>&#8211;lp</code>&nbsp;<wbr><i>number</i>]&nbsp;<wbr>[<i>fbi options</i>]&nbsp;<wbr><i>file</i> # #</p>
<h2>DESCRIPTION</h2>
<p> <code>Fbgs</code> is a simple wrapper script which takes a <i>PostScript</i> (PS) or <i>Portable Document Format</i> (PDF) file as input, renders the pages using <code><a href="/docs/linux/man/1-gs/">gs</a></code>(1) &#8211; GhostScript &#8211; into a temporary directory and finally calls <code><a href="/docs/linux/man/1-fbi/">fbi</a></code>(1) to display them.</p>
<h2>OPTIONS</h2>
<p> <code>Fbgs</code> understands all <code><a href="/docs/linux/man/1-fbi/">fbi</a></code>(1) options (they are passed through), except: store, list, text, (no)comments, e, (no)edit, (no)backup, (no)preserve, (no)readahead, cachemem, blend. </p>
<p> Additionally you can specify:</p>
<dl>
<dt><code>-h, &#8211;help</code></dt>
<dd> Print usage info (overwrites fbi option).</dd>
<dt><code>-b, &#8211;bell</code></dt>
<dd> Emit a beep when the document is ready.</dd>
<dt><code>-c, &#8211;color</code></dt>
<dd> To render the pages in color (default is N&amp;B).</dd>
<dt><code>-l</code></dt>
<dd> To get the pages rendered with 100 dpi (default is 75).</dd>
<dt><code>-xl</code></dt>
<dd> To get the pages rendered with 120 dpi.</dd>
<dt><code>-xxl</code></dt>
<dd> To get the pages rendered with 150 dpi.</dd>
<dt><code>-r</code><i>&nbsp;<wbr>n</i><code>, &#8211;resolution</code><i>&nbsp;<wbr>n</i></dt>
<dd> To get the pages rendered with <i>n</i> dpi (overwrites fbi option).</dd>
<dt><code>-fp</code><i>&nbsp;<wbr>number</i><code>, &#8211;firstpage</code><i>&nbsp;<wbr>number</i></dt>
<dd> Begins interpreting on the designated page of the document.</dd>
<dt><code>-lp</code><i>&nbsp;<wbr>number</i><code>, &#8211;lastpage</code><i>&nbsp;<wbr>number</i></dt>
<dd> Stops interpreting after the designated page of the document.</dd>
<dt><code>-p</code><i>&nbsp;<wbr>password</i><code>, &#8211;password</code><i>&nbsp;<wbr>password</i></dt>
<dd> You can use this option if your PDF file requires a <i>password</i>. # #</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-fbi/">fbi</a></code>(1), <code><a href="/docs/linux/man/1-gs/">gs</a></code>(1) # #</p>
<h2>AUTHOR</h2>
<p> Gerd Hoffmann <code>&lt;gerd [at] kraxel.org&gt;</code> # #</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 1999-2012 Gerd Hoffmann &lt;gerd [at] kraxel.org&gt; </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA. </p>
