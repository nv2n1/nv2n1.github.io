---
title: "iso-read(1)"
name: "iso-read"
section: "1"
letter: "i"
url: "/docs/linux/man/1-iso-read/"
description: "iso-read – reads portions of an ISO 9660 image"
---

<h2>NAME</h2>
<p> iso-read &#8211; reads portions of an ISO 9660 image</p>
<h2>SYNOPSIS</h2>
<p> <code>iso-read</code> [<i>OPTION</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<dl>
<dt><code>-d</code>, <code>&#8211;debug</code>=<i>INT</i></p>
<dd> Set debugging to LEVEL.</p>
<dt><code>-i</code>, <code>&#8211;image</code>=<i>FILE</i></p>
<dd> Read from ISO-9660 image. This option is mandatory</p>
<dt><code>-e</code>, <code>&#8211;extract</code>=<i>FILE</i></p>
<dd> Extract FILE from ISO-9660 image. This option is mandatory.</p>
<dt><code>-k</code>, <code>&#8211;ignore</code></p>
<dd> Ignore read error(s), i.e. keep going</p>
<dt><code>&#8211;no-header</code></p>
<dd> Don&#8217;t display header and copyright (for regression testing)</p>
<dt><code>-o</code>, <code>&#8211;output-file</code>=<i>FILE</i></p>
<dd> Output file. This option is mandatory.</p>
<dt><code>-U</code> <code>&#8211;udf</code></p>
<dd> Contents are in UDF format</p>
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
<p> <tt><a href="/docs/linux/man/1-iso-info/">iso-info</a>(1)</tt> for information about an ISO-9660 image. <tt><a href="/docs/linux/man/1-cd-read/">cd-read</a>(1)</tt> to read portions of an ISO 9660 image. </p>
<h2>Index</h2>
