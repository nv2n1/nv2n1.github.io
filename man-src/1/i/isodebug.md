---
title: "isodebug(1)"
name: "isodebug"
section: "1"
letter: "i"
url: "/docs/linux/man/1-isodebug/"
description: "isodebug – print genisoimage debug info from ISO-9660 image"
---

<h2>NAME</h2>
<p> isodebug &#8211; print genisoimage debug info from ISO-9660 image</p>
<h2>SYNOPSIS</h2>
<p> <code>isodebug</code> [ <i>options</i> ] [ <i>file</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>Isodebug</code> reads the debug info written by <code><a href="/docs/linux/man/8-genisoimage/">genisoimage</a></code>(8) from within a ISO-9660 file system image and prints them.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-help</code></p>
<dd> Prints a short summary of the <code>isodebug</code> options and exists.</p>
<dt><code>-version</code></p>
<dd> Prints the <code>isodebug</code> version number string and exists.</p>
<dt><code>-i</code><i> filename</i></p>
<dd> Filename to read ISO-9660 image from.</p>
<dt><code>dev=</code><i>target</i></p>
<dd> SCSI target to use as CD/DVD-Recorder. See <code><a href="/docs/linux/man/1-wodim/">wodim</a></code>(1) for more information on now to use this option.</dl>
<h2>FILES</h2>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-wodim/">wodim</a></code>(1), <code><a href="/docs/linux/man/1-genisoimage/">genisoimage</a></code>(1).</p>
<h2>AUTHOR</h2>
<pre>
Joerg Schilling
Seestr. 110
D-13353 Berlin
Germany
</pre>
<h2>AUTHOR</h2>
<pre>
Joerg Schilling
Seestr. 110
D-13353 Berlin
Germany
</pre>
<p> This manpage describes the program implementation of <code>isodebug</code> as shipped by the cdrkit distribution. See <code><a rel="nofollow" href="http://alioth.debian.org/projects/debburn/">http://alioth.debian.org/projects/debburn/</a></code> for details. It is a spinoff from the original program distributed in the cdrtools package [1]. However, the cdrtools developers are not involved in the development of this spinoff and therefore shall not be made responsible for any problem caused by it. Do not try to get support for this program by contacting the original author(s). </p>
<p> If you have support questions, send them to </p>
<p> <code>debburn-devel [at] lists.alioth.debian.org</code> </p>
<p> If you have definitely found a bug, send a mail to this list or to </p>
<p> <code>submit [at] bugs.debian.org</code> </p>
<p> writing at least a short description into the Subject and &quot;Package: cdrkit&quot; into the first line of the mail body. </p>
<p> [1] Cdrtools 2.01.01a08 from May 2006, <a rel="nofollow" href="http://cdrecord.berlios.de">http://cdrecord.berlios.de</a> </p>
<h2>Index</h2>
