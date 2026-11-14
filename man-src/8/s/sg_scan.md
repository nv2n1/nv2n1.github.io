---
title: "sg_scan(8)"
name: "sg_scan"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sg_scan/"
description: "sg_scan – scans sg devices (or SCSI/ATAPI/ATA devices) and prints results"
---

<p>sg_scan &#8211; scans sg devices (or SCSI/ATAPI/ATA devices) and prints results</p>
<h2>Synopsis</h2>
<p><code>sg_scan</code> [<i>-a</i>] [<i>-i</i>] [<i>-n</i>] [<i>-w</i>] [<i>-x</i>] [<i>DEVICE</i>]*</p>
<h2>Description</h2>
<p>If no <i>DEVICE</i> names are given, sg_scan does a scan of the sg devices and outputs a line of information for each sg device that is currently bound to a SCSI device. If one or more <i>DEVICE</i>s are given only those devices are scanned. Each device is opened with the O_NONBLOCK flag so that the scan will not &quot;hang&quot; on any device that another process holds an O_EXCL lock on. </p>
<p> Any given <i>DEVICE</i> name is expected to comply with (to some extent) the Storage Architecture Model (SAM see <a rel="nofollow" href="http://www.t10.org">www.t10.org</a>). Any device names associated with the Linux SCSI subsystem (e.g. /dev/sda and /dev/st0m) are suitable. Devices names associated with ATAPI devices (e.g. most CD/DVD drives and ATAPI tape drives) are also suitable. If the device does not fall into the above categories then an ATA IDENTIFY command is tried. </p>
<p> In Linux 2.6 and 3 series kernels, the lsscsi utility may be helpful. Apart from providing more information (by data-mining in the sysfs pseudo file system), it does not need root permissions to execute, as this utility would typically need.</p>
<h2>Options</h2>
<dl>
<dt><code>-a</code></p>
<dd>do alphabetical scan (i.e. sga, sgb, sgc). Note that sg device nodes with an alphabetical index have been deprecated since the Linux kernel 2.2 series.</p>
<dt><code>-i</code></p>
<dd>do a SCSI INQUIRY, output results in a second (indented) line. If the device is an ATA disk then output information from an ATA IDENTIFY command</p>
<dt><code>-n</code></p>
<dd>do numeric scan (i.e. sg0, sg1&#8230;) [default]</p>
<dt><code>-w</code></p>
<dd>use a read/write flag when opening sg device (default is read-only)</p>
<dt><code>-x</code></p>
<dd>extra information output about queuing</dl>
<h2>Notes</h2>
<p>This utility was written at a time when hotplugging of SCSI devices was not supported in Linux. It used a simple algorithm to scan sg device nodes in ascending numeric or alphabetical order, stopping after there were 4 consecutive errors. </p>
<p> In the Linux kernel 2.6 series, this utility uses sysfs to find which sg device nodes are active and only checks those. Hence there can be large &quot;holes&quot; in the numbering of sg device nodes (e.g. after an adapter has been removed) and still all active sg device nodes will be listed. This utility assumes that sg device nodes are named using the normal conventions and searches from /dev/sg0 to /dev/sg4095 inclusive.</p>
<h2>Exit Status</h2>
<p>The exit status of sg_scan is 0 when it is successful. Otherwise see the <a href="/docs/linux/man/8-sg3_utils/">sg3_utils</a>(8) man page.</p>
<h2>Authors</h2>
<p>Written by D. Gilbert and F. Jansen</p>
<h2>Copyright</h2>
<p>Copyright &#169; 1999-2013 Douglas Gilbert<br />
 This software is distributed under the GPL version 2. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-lsscsi/">lsscsi</a>(8)</code> </p>
