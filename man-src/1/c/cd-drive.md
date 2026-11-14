---
title: "cd-drive(1)"
name: "cd-drive"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cd-drive/"
description: "cd-drive – show CD-ROM drive characteristics"
---

<h2>NAME</h2>
<p> cd-drive &#8211; show CD-ROM drive characteristics</p>
<h2>SYNOPSIS</h2>
<p> <code>cd-drive</code> [<i>OPTION</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<dl>
<dt><code>-d</code>, <code>&#8211;debug</code>=<i>INT</i></p>
<dd> Set debugging to LEVEL</p>
<dt><code>-i</code>, <code>&#8211;cdrom-device</code>[=<i>DEVICE</i>]</p>
<dd> show only info about CD-ROM device</p>
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
<p> Rocky Bernstein rocky [at] gnu.org</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2003-2005, 2007-2008, 2011-2013 R. Bernstein<br />
 This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. Have driver: GNU/Linux ioctl and MMC driver Have driver: cdrdao (TOC) disk image driver Have driver: bin/cuesheet disk image driver Have driver: Nero NRG disk image driver Default CD-ROM device: /dev/sr0</p>
<h2>SEE ALSO</h2>
<p> <tt><a href="/docs/linux/man/1-cd-info/">cd-info</a>(1)</tt> for information about the CD inside a CD-ROM. </p>
<h2>Index</h2>
