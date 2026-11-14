---
title: "scsi_ready(8)"
name: "scsi_ready"
section: "8"
letter: "s"
url: "/docs/linux/man/8-scsi_ready/"
description: "scsi_ready – do SCSI TEST UNIT READY on devices"
---

<p>scsi_ready &#8211; do SCSI TEST UNIT READY on devices</p>
<h2>Synopsis</h2>
<p><code>scsi_ready</code> [<i>&#8211;brief</i>] [<i>&#8211;help</i>] [<i>&#8211;verbose</i>] <i>DEVICE</i> [<i>DEVICE</i>]*</p>
<h2>Description</h2>
<p>This bash shell script calls the sg_turs utility on each given <i>DEVICE</i>. This will send a SCSI TEST UNIT READY command to each <i>DEVICE</i>. Disks, tape drives and DVD/BD players amongst others may respond to this SCSI command.</p>
<h2>Options</h2>
<p>Arguments to long options are mandatory for short options as well.</p>
<dl>
<dt><code>-b</code>, <code>&#8211;brief</code></p>
<dd>for each <i>DEVICE</i> given output a line containing either &#8216; ready&#8217; or &#8216; device not ready&#8217;. If <i>DEVICE</i> is not found or there is another serious error then an error message will appear instead.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>print out the usage message then exit.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>increase level or verbosity.</dl>
<h2>Exit Status</h2>
<p>The exit status of this script is 0 when it is successful. Otherwise the exit status is that of the last sg_turs utility called. See the <a href="/docs/linux/man/8-sg3_utils/">sg3_utils</a>(8) man page.</p>
<h2>Authors</h2>
<p>Written by D. Gilbert</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2009-2013 Douglas Gilbert<br />
 This software is distributed under a FreeBSD license. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code>sg_turs (sg3_utils)</code> </p>
