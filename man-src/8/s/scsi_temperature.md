---
title: "scsi_temperature(8)"
name: "scsi_temperature"
section: "8"
letter: "s"
url: "/docs/linux/man/8-scsi_temperature/"
description: "scsi_temperature – fetch the temperature of a SCSI device"
---

<p>scsi_temperature &#8211; fetch the temperature of a SCSI device</p>
<h2>Synopsis</h2>
<p><code>scsi_temperature</code> [<i>&#8211;help</i>] [<i>&#8211;verbose</i>] <i>DEVICE</i> [<i>DEVICE</i>]*</p>
<h2>Description</h2>
<p>This bash shell script calls the sg_logs utility on each given <i>DEVICE</i> in order to find the device&#8217;s temperature. The Temperature log page is checked first and if it is not available then the Informational Exceptions log page is checked.</p>
<h2>Options</h2>
<p>Arguments to long options are mandatory for short options as well.</p>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>print out the usage message then exit.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>increase level or verbosity.</dl>
<h2>Exit Status</h2>
<p>The exit status of this script is 0 when it is successful. Otherwise the exit status is that of the last sg_logs utility called. See the <a href="/docs/linux/man/8-sg3_utils/">sg3_utils</a>(8) man page.</p>
<h2>Authors</h2>
<p>Written by D. Gilbert</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2011-2013 Douglas Gilbert<br />
 This software is distributed under a FreeBSD license. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code>sg_logs (sg3_utils)</code> </p>
