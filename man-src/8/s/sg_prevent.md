---
title: "sg_prevent(8)"
name: "sg_prevent"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sg_prevent/"
description: "sg_prevent – send SCSI PREVENT ALLOW MEDIUM REMOVAL command"
---

<p>sg_prevent &#8211; send SCSI PREVENT ALLOW MEDIUM REMOVAL command</p>
<h2>Synopsis</h2>
<p><code>sg_prevent</code> [<i>&#8211;allow</i>] [<i>&#8211;help</i>] [<i>&#8211;prevent=PC</i>] [<i>&#8211;verbose</i>] [<i>&#8211;version</i>] <i>DEVICE</i></p>
<h2>Description</h2>
<p>Sends a SCSI PREVENT ALLOW MEDIUM REMOVAL command to <i>DEVICE</i>. The default action of this utility is to prevent the removing or ejecting of the medium from a drive. This is done by ignoring the SCSI START STOP UNIT command (see sg_start) and ignoring the eject button on the drive when the user presses it. Drives that hold removable disks, tape cartridges or cd/dvd media typically implement this command. The definition of the &quot;prevent&quot; codes for this command differ between disks and tapes (covered by SBC-3 and SSC-3) and cd/dvd drives (covered by MMC-5). The &quot;prevent codes&quot; described here are from MMC-5.</p>
<h2>Options</h2>
<p>Arguments to long options are mandatory for short options as well.</p>
<dl>
<dt><code>-a</code>, <code>&#8211;allow</code></p>
<dd>allow medium removal. This is equivalent to setting to &#8216;&#8211;prevent=2&#8217;. Cannot be used with <i>&#8211;prevent=PC</i> option (i.e. either use no options (hence prevent removal), this option or <i>&#8211;prevent=PC</i>).</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>output the usage message then exit.</p>
<dt><code>-p</code>, <code>&#8211;prevent</code>=<i>PC</i></p>
<dd>where <i>PC</i> is a prevent code value. Defined values are: 0 allows removal, 1 prevents removal (default), 2 allows persistent removal while 3 prevents persistent removal. &quot;Persistent&quot; in this context means that the initiator (port) that successfully uses code 3 blocks other initiators (ports) from allowing removal. A &quot;persistent prevent&quot; state can be cleared by the owner allowing persistent removal (code 2) or a power cycle (or anything that resets the device (LU)) or some special commands (e.g. various service actions of Persistent Reserve Out, see SPC-3).</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>increase the level of verbosity, (i.e. debug output).</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>print the version string and then exit.</dl>
<h2>Exit Status</h2>
<p>The exit status of sg_prevent is 0 when it is successful. Otherwise see the <a href="/docs/linux/man/8-sg3_utils/">sg3_utils</a>(8) man page.</p>
<h2>Authors</h2>
<p>Written by Douglas Gilbert.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;dgilbert at interlog dot com&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2004-2012 Douglas Gilbert<br />
 This software is distributed under a FreeBSD license. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code>sg_start(sg3_utils), sg_persist(sg3_utils)</code> </p>
