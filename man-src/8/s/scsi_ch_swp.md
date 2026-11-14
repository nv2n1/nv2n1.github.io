---
title: "scsi_ch_swp(8)"
name: "scsi_ch_swp"
section: "8"
letter: "s"
url: "/docs/linux/man/8-scsi_ch_swp/"
description: "scsi_ch_swp – change SCSI Software WRITE Protect and block device settings"
---

<p>scsi_ch_swp &#8211; change SCSI Software WRITE Protect and block device settings</p>
<h2>Synopsis</h2>
<p><code>scsi_ch_swp</code> [<i>&#8211;help</i>] [<i>&#8211;set 0|1</i>] [<i>&#8211;verbose</i>] [<i>&#8211;wr</i>] <i>BLK_DEVICE</i></p>
<h2>Description</h2>
<p>This bash shell script attempts to read or change the Software Write Protect (SWP) bit in the SCSI Control mode page using the sdparm utility. If that change is successful then it uses the blockdev utility to change <i>BLK_DEVICE</i>&#8216;s read-write or read-only setting in sympathy. This script is only available in Linux since the blockdev utility is Linux specific. </p>
<p> If changing the SWP bit is supported, setting the SWP bit makes <i>BLK_DEVICE</i> read-only at the device (disk) itself. Clearing the SWP bit makes <i>BLK_DEVICE</i> read-write which is usually the default setting at device (disk) power up. </p>
<p> If no options are given then the current state of the SWP bit is printed out (using sdparm) together with blockdev&#8217;s RO bit. If they are both 1 then <i>BLK_DEVICE</i> is in read-only mode; if they are both 0 then <i>BLK_DEVICE</i> is in read-write mode.</p>
<h2>Options</h2>
<p>Arguments to long options are mandatory for short options as well.</p>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>print out the usage message then exit.</p>
<dt><code>-s</code>, <code>&#8211;set</code> <i>0|1</i></p>
<dd>when 0 is given then the SWP bit in the Control mode page is cleared (i.e. set that bit to 0) using sdparm; and blockdev is used to set <i>BLK_DEVICE</i> to read-write mode. When 1 is given then the SWP bit in the Control mode page is set using sdparm; and blockdev is used to set <i>BLK_DEVICE</i> to read-only mode. The default (i.e. when this option is not given) is to read the state of the SWP bit and <i>BLK_DEVICE</i>&#8216;s read-only mode and print those values out.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>increase level or verbosity.</p>
<dt><code>-w</code>, <code>&#8211;wr</code></p>
<dd>when the <i>BLK_DEVICE</i> is in read-only mode, Linux will not typically allow <i>BLK_DEVICE</i> to be opened read-write by sdparm, so the default action of this script is to use the sdparm <i>&#8211;readonly</i> option when <i>&#8211;set 0</i> has been invoked. It is possible that <i>BLK_DEVICE</i> could be a generic device (e.g. /dev/sg3) which has a different interpretation of the read-only open flag and may fail. For such rare cases the <i>&#8211;wr</i> option makes sdparm open <i>BLK_DEVICE</i> read-write when <i>&#8211;set 0</i> is invoked.</dl>
<h2>Exit Status</h2>
<p>The exit status of this script is 0 when it is successful. Otherwise the exit status is that of the sdparm or the blockdev utility, whichever is called last. See the <a href="/docs/linux/man/8-sdparm/">sdparm</a>(8) man page.</p>
<h2>Authors</h2>
<p>Written by D. Gilbert</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2013 Douglas Gilbert<br />
 This software is distributed under a FreeBSD license. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code>sdparm(sdparm), <a href="/docs/linux/man/8-blockdev/">blockdev</a>(8)</code> </p>
