---
title: "scsi_stop(8)"
name: "scsi_stop"
section: "8"
letter: "s"
url: "/docs/linux/man/8-scsi_stop/"
description: "scsi_stop – stop (spin down) one or more SCSI disks"
---

<p>scsi_stop &#8211; stop (spin down) one or more SCSI disks</p>
<h2>Synopsis</h2>
<p><code>scsi_stop</code> [<i>&#8211;help</i>] [<i>&#8211;verbose</i>] [<i>&#8211;wait</i>] <i>DEVICE</i> [<i>DEVICE</i>]*</p>
<h2>Description</h2>
<p>This bash shell script calls the sg_start utility on each given <i>DEVICE</i>. The purpose is to spin down (stop) each given <i>DEVICE</i>.</p>
<h2>Options</h2>
<p>Arguments to long options are mandatory for short options as well.</p>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>print out the usage message then exit.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>increase level or verbosity.</p>
<dt><code>-w</code>, <code>&#8211;wait</code></p>
<dd>wait for the spin down (stop) on each given <i>DEVICE</i> to complete. The default action is to do each stop in immediate mode.</dl>
<h2>Notes</h2>
<p>The sg_start utility calls the SCSI START STOP UNIT command and can either start (spin up) or stop (spin down) a SCSI disk depending on the given command line options.</p>
<h2>Exit Status</h2>
<p>The exit status of this script is 0 when it is successful. Otherwise the exit status is that of the last sg_start utility called. See the <a href="/docs/linux/man/8-sg3_utils/">sg3_utils</a>(8) man page.</p>
<h2>Authors</h2>
<p>Written by D. Gilbert</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2009-2013 Douglas Gilbert<br />
 This software is distributed under a FreeBSD license. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code>sg_start (sg3_utils)</code> </p>
