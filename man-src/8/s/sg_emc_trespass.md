---
title: "sg_emc_trespass(8)"
name: "sg_emc_trespass"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sg_emc_trespass/"
description: "sg_emc_trespass – change ownership of SCSI LUN from another Service-Processor to this one"
---

<p>sg_emc_trespass &#8211; change ownership of SCSI LUN from another Service-Processor to this one</p>
<h2>Synopsis</h2>
<p><code>sg_emc_trespass</code> [<i>-d</i>] [<i>-hr</i>] [<i>-s</i>] [<i>-V</i>] <i>DEVICE</i></p>
<h2>Description</h2>
<p>sg_emc_trespass sends an EMC-specific Trespass Command to the <i>DEVICE</i> with the selected options. This Mode Select changes the ownership of the LUN of the device from another Service-Processor to the one the command was received on.</p>
<h2>Options</h2>
<p>Arguments to long options are mandatory for short options as well.</p>
<dl>
<dt><code>-d</code></p>
<dd>outputs some extra debug information associated with executing this command</p>
<dt><code>-hr</code></p>
<dd>Sets the &#8216;Honor Reservation&#8217; bit in the command. If set, the trespass will only succeed to change the ownership from the Peer SP if the Peer SP does not have an outstanding SCSI reservation for the LUN. By default, the reservation state will be ignored.</p>
<dt><code>-s</code></p>
<dd>Send the short version of the trespass command instead of the long version. The short version is supported on the EMC FC5300, FC4500 and FC4700. The long version (default) is supported on the CLARiiON CX and AX family arrays.</p>
<dt><code>-V</code></p>
<dd>print out version string then exit.</dl>
<p> In the 2.4 series of Linux kernels the <i>DEVICE</i> must be a SCSI generic (sg) device. In the 2.6 series block devices (e.g. SCSI disks and DVD drives) can also be specified. For example &quot;sg_start 0 /dev/sda&quot; will work in the 2.6 series kernels.</p>
<h2>Exit Status</h2>
<p>The exit status of sg_emc_trespass is 0 when it is successful. Otherwise see the <a href="/docs/linux/man/8-sg3_utils/">sg3_utils</a>(8) man page.</p>
<h2>Author</h2>
<p>Written by Lars Marowsky-Bree, based on sg_start.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;dgilbert at interlog dot com&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2004-2012 Lars Marowsky-Bree, Douglas Gilbert.<br />
 This software is distributed under the GPL version 2. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
