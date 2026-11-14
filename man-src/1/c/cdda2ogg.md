---
title: "cdda2ogg(1)"
name: "cdda2ogg"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cdda2ogg/"
description: "cdda2ogg — extract audio CD audio tracks and encode them"
---

<h2>NAME</h2>
<p> cdda2ogg &#8212; extract audio CD audio tracks and encode them</p>
<h2>SYNOPSIS</h2>
<p> <code>cdda2ogg</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>cdda2ogg is a simple script that uses the</code> <code>icedax &lt;fileprefix&gt;</code> command to extract all audio tracks with the <code>icedax &lt;fileprefix&gt;</code> command and encode them using the <code>ogg123</code> encoder. The scripts are not intended to be full-featured music archiving programs, but only for quick storing of few audio data. It does not use databases like CDDB or have any extra features. You may look at <code>icedax</code> if you need them. </p>
<p> <code>ogg123</code> is provided by the <code>vorbis-tools</code> which needs to be installed separately. See <code><a rel="nofollow" href="http://www.ogg.org">www.ogg.org</a></code> for more information. </p>
<h2>CONFIGURATION</h2>
<p> <code>cdda2ogg</code> have predefined values for reading and labeling of the target files. You can overwrite them with following environment variables: </p>
<dl>
<dt>CDDA_DEVICE</p>
<dd> Source device specification to get the data from. </p>
<dt>LIST</p>
<dd> List of track numbers to be read, separated by spaces. </p>
<dt>CDDA2WAV</p>
<dd> Defines the command to run the cdda2wav program </p>
<dt>CDDA2WAV_OPTS</p>
<dd> Miscellaneous options passed to <i>$CDDA2WAV</i>. </p>
<dt>MP_CODER</p>
<dd> The encoder program. </p>
<dt>MP_OPTIONS</p>
<dd> Additional options passed to <i>$MP_CODER</i>.<br />
&nbsp;<wbr></p>
<dt>FILEPREFIX</p>
<dd> The base part of the filename of resulting audio files. This can also be specified as the first argument to the script. </p>
</dl>
<p> See cdda2ogg script file to get the default values </p>
<p> System administrator can also set default values by creating of a shell include file, defining the variables for the POSIX shell, and storing them as /etc/default/cdda2ogg.</p>
<h2>EXAMPLES</h2>
<p> <code>CDDA_DEVICE=/dev/cdrom1 cdda2ogg</code><br />
 just stores every track in this device in audiotrackNUMBER.ogg </p>
<p> <code>LIST=1 5 7 cdda2ogg PartsOfBestOfFoo</code><br />
 stores the selected tracks from the default cdrom device as 01-PartsOfBestOfFoo.ogg, 05-PartsOfBestOfFoo.ogg, 07-PartsOfBestOfFoo.ogg. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-icedax/">icedax</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> This manpage describes the program implementation of <code>cdda2ogg</code> as shipped by the cdrkit distribution. See <code><a rel="nofollow" href="http://alioth.debian.org/projects/debburn/">http://alioth.debian.org/projects/debburn/</a></code> for details. It is a spinoff from the original program distributed by the cdrtools project. However, the cdrtools developers are not involved in the development of this spinoff and therefore shall not be made responsible for any problem caused by it. Do not try to get support for this program by contacting the original authors. </p>
<p> If you have support questions, send them to </p>
<p> <code>debburn-devel [at] lists.alioth.debian.org</code> </p>
<p> If you have definitely found a bug, send a mail to this list or to </p>
<p> <code>submit [at] bugs.debian.org</code> </p>
<p> writing at least a short description into the Subject and &quot;Package: cdrkit&quot; into the first line of the mail body. </p>
<p> This manual page was written by Eduard Bloch (blade [at] debian.org) for the <code>Debian GNU/Linux system (but may be used by others). Permission is granted</code> to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 as published by the Free Software Foundation. </p>
<h2>Index</h2>
