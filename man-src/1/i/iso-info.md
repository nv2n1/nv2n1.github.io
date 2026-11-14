---
title: "iso-info(1)"
name: "iso-info"
section: "1"
letter: "i"
url: "/docs/linux/man/1-iso-info/"
description: "iso-info – shows Information about an ISO 9660 image"
---

<h2>NAME</h2>
<p> iso-info &#8211; shows Information about an ISO 9660 image</p>
<h2>SYNOPSIS</h2>
<p> <code>iso-info</code> [<i>OPTION</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<dl>
<dt><code>-d</code>, <code>&#8211;debug</code>=<i>UINT</i></p>
<dd> Set debugging to LEVEL</p>
<dt><code>-i</code>, <code>&#8211;input</code>[=<i>FILE</i>]</p>
<dd> Filename to read ISO-9960 image from</p>
<dt><code>-f</code></p>
<dd> Generate output similar to &#8216;find . <code>-print</code>&#8216;</p>
<dt><code>-l</code>, <code>&#8211;iso9660</code></p>
<dd> output similar to &#8216;ls <code>-lR</code>&#8216; for an ISO 9660 fs</p>
<dt><code>-U</code>, <code>&#8211;udf</code></p>
<dd> output similar to &#8216;ls <code>-lR</code>&#8216; for a UDF fs</p>
<dt><code>&#8211;no-header</code></p>
<dd> Don&#8217;t display header and copyright (for regression</p>
<dt><code>&#8211;no-joliet</code></p>
<dd> Don&#8217;t use Joliet-extension information</p>
<dt><code>&#8211;no-rock-ridge</code></p>
<dd> Don&#8217;t use Rock-Ridge-extension information</p>
<dt><code>&#8211;no-xa</code></p>
<dd> Don&#8217;t use XA-extension information</p>
<dt><code>-r</code> <code>&#8211;show-rock-ridge</code> UINT Show if image uses Rock-Ridge extensions</p>
<dd> A maximum of UINT files will be considered. Use 0 for all files.</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd> Don&#8217;t produce warning output</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> display version and copyright information and exit</dl>
<h3>Help options:</h3>
<dl>
<dt>-?, <code>&#8211;help</code></p>
<dd> Show this help message</p>
<dt><code>&#8211;usage</code></p>
<dd> Display brief usage message</dl>
<h2>AUTHOR</h2>
<p> Rocky Bernstein &lt;rocky [at] gnu.org&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2003-2005, 2007-2008, 2011-2013 R. Bernstein<br />
 This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. Have driver: GNU/Linux ioctl and MMC driver Have driver: cdrdao (TOC) disk image driver Have driver: bin/cuesheet disk image driver Have driver: Nero NRG disk image driver Default CD-ROM device: /dev/sr0</p>
<h2>SEE ALSO</h2>
<p> <tt><a href="/docs/linux/man/1-cd-info/">cd-info</a>(1)</tt> for information about an ISO-9660 image. <tt><a href="/docs/linux/man/1-cd-read/">cd-read</a>(1)</tt> to read portions of an ISO 9660 image. </p>
<h2>Index</h2>
