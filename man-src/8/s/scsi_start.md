---
title: "scsi_start(8)"
name: "scsi_start"
section: "8"
letter: "s"
url: "/docs/linux/man/8-scsi_start/"
description: "scsi_start – start one or more SCSI disks"
---

<p>scsi_start &#8211; start one or more SCSI disks</p>
<h2>Synopsis</h2>
<p><code>scsi_start</code> [<i>&#8211;help</i>] [<i>&#8211;verbose</i>] [<i>&#8211;wait</i>] <i>DEVICE</i> [<i>DEVICE</i>]*</p>
<h2>Description</h2>
<p>This bash shell script calls the sg_start utility on each given <i>DEVICE</i>. The purpose is to spin up (start) each given <i>DEVICE</i>.</p>
<h2>Options</h2>
<p>Arguments to long options are mandatory for short options as well.</p>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>print out the usage message then exit.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>increase level or verbosity.</p>
<dt><code>-w</code>, <code>&#8211;wait</code></p>
<dd>wait for the spin up (start) on each given <i>DEVICE</i> to complete. The default action is to do each start in immediate mode.</dl>
<h2>Notes</h2>
<p>If a large number of disks are spun up at the same time (i.e. without the <i>&#8211;wait</i> option) then the power supply may be overloaded.</p>
<h2>Exit Status</h2>
<p>The exit status of this script is 0 when it is successful. Otherwise the exit status is that of the last sg_start utility called. See the <a href="/docs/linux/man/8-sg3_utils/">sg3_utils</a>(8) man page.</p>
<h2>Authors</h2>
<p>Written by D. Gilbert</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2009-2013 Douglas Gilbert<br />
 This software is distributed under a FreeBSD license. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code>sg_start (sg3_utils)</code> </p>
