---
title: "sg_rmsn(8)"
name: "sg_rmsn"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sg_rmsn/"
description: "sg_rmsn – send SCSI READ MEDIA SERIAL NUMBER command"
---

<p>sg_rmsn &#8211; send SCSI READ MEDIA SERIAL NUMBER command</p>
<h2>Synopsis</h2>
<p><code>sg_rmsn</code> [<i>&#8211;help</i>] [<i>&#8211;raw</i>] [<i>&#8211;readonly</i>] [<i>&#8211;verbose</i>] [<i>&#8211;version</i>] <i>DEVICE</i></p>
<h2>Description</h2>
<p>Send a SCSI READ MEDIA SERIAL NUMBER command to <i>DEVICE</i> and outputs the response. </p>
<p> This command is described in SPC-3 found at <a rel="nofollow" href="http://www.t10.org">www.t10.org</a> . It was originally added to SPC-3 in revision 11 (2003/2/12). It is not an mandatory command and the author has not seen any SCSI devices that support it.</p>
<h2>Options</h2>
<p>Arguments to long options are mandatory for short options as well.</p>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>output the usage message then exit.</p>
<dt><code>-r</code>, <code>&#8211;raw</code></p>
<dd>sends the serial number (if found) to stdout. This output may contain non-printable characters (e.g. the serial number is padded with NULLs at the end so its length is a multiple of 4). The default action is to print the serial number out in ASCII-HEX with ASCII characters to the right. All error messages are sent to stderr.</p>
<dt><code>-R</code>, <code>&#8211;readonly</code></p>
<dd>opens the DEVICE read-only rather than read-write which is the default. The Linux sg driver needs read-write access for the SCSI READ MEDIA SERIAL NUMBER command but other access methods may require read-only access.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>increase the level of verbosity, (i.e. debug output).</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>print the version string and then exit.</dl>
<h2>Notes</h2>
<p>Device identification information is also found in a standard INQUIRY response and its VPD pages (see sg_vpd). The relevant VPD pages are the &quot;device identification page&quot; (VPD page 0x83) and the &quot;unit serial number&quot; page (VPD page 0x80). </p>
<p> The MMC-4 command set for CD/DVD/HD-DVD/BD drives has a &quot;media serial number&quot; feature (0x109) [and a &quot;logical unit serial number&quot; feature]. These can be viewed with sg_get_config.</p>
<h2>Exit Status</h2>
<p>The exit status of sg_rmsn is 0 when it is successful. Otherwise see the <a href="/docs/linux/man/8-sg3_utils/">sg3_utils</a>(8) man page.</p>
<h2>Authors</h2>
<p>Written by Douglas Gilbert.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;dgilbert at interlog dot com&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2005-2012 Douglas Gilbert<br />
 This software is distributed under a FreeBSD license. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code>sg_vpd(sg3_utils), sg_get_config(sg3_utils)</code> </p>
