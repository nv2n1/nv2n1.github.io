---
title: "sg_raw(8)"
name: "sg_raw"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sg_raw/"
description: "sg_raw – send arbitrary SCSI command to a device"
---

<p>sg_raw &#8211; send arbitrary SCSI command to a device</p>
<h2>Synopsis</h2>
<p><code>sg_raw [</code><i>OPTIONS</i>] <i>DEVICE</i> CDB0 CDB1 &#8230;</p>
<h2>Description</h2>
<p>This utility sends an arbitrary SCSI command (between 6 and 256 bytes) to the <i>DEVICE</i>. There may be no associated data transfer; or data may be read from a file and sent to the <i>DEVICE</i>; or data may be received from the <i>DEVICE</i> and then displayed or written to a file. If supported by the pass through, bidirectional commands may be sent (i.e. containing both data to be sent to the <i>DEVICE</i> and received from the <i>DEVICE</i>). </p>
<p> The SCSI command may be between 6 and 256 bytes long. Each command byte is specified in plain hex format (00..FF) without a prefix or suffix. See EXAMPLES section below. </p>
<p> The commands pass through a generic SCSI interface which is implemented for several operating systems including Linux, FreeBSD and Windows.</p>
<h2>Options</h2>
<p>Arguments to long options are mandatory for short options as well.</p>
<dl>
<dt><code>-b</code>, <code>&#8211;binary</code></p>
<dd>Dump data in binary form, even when writing to stdout.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>Display usage information and exit.</p>
<dt><code>-i</code>, <code>&#8211;infile</code>=<i>IFILE</i></p>
<dd>Read data from <i>IFILE</i> instead of stdin. This option is ignored if <code>&#8211;send</code> is not specified.</p>
<dt><code>-k</code>, <code>&#8211;skip</code>=<i>LEN</i></p>
<dd>Skip the first <i>LEN</i> bytes of the input file or stream. This option is ignored if <code>&#8211;send</code> is not specified.</p>
<dt><code>-n</code>, <code>&#8211;nosense</code></p>
<dd>Don&#8217;t display SCSI Sense information.</p>
<dt><code>-o</code>, <code>&#8211;outfile</code>=<i>OFILE</i></p>
<dd>Write data received from the <i>DEVICE</i> to <i>OFILE</i>. The data is written in binary. By default, data is dumped in hex format to stdout. If <i>OFILE</i> is &#8216;-&#8216; then data is dumped in binary to stdout. This option is ignored if <code>&#8211;request</code> is not specified.</p>
<dt><code>-r</code>, <code>&#8211;request</code>=<i>RLEN</i></p>
<dd>Expect to receive up to <i>RLEN</i> bytes of data from the <i>DEVICE</i>. <i>RLEN</i> may be suffixed with &#8216;k&#8217; to use kilobytes (1024 bytes) instead of bytes.</p>
<dt><code>-R</code>, <code>&#8211;readonly</code></p>
<dd>Open <i>DEVICE</i> read-only. The default (without this option) is to open it read-write.</p>
<dt><code>-s</code>, <code>&#8211;send</code>=<i>SLEN</i></p>
<dd>Read <i>SLEN</i> bytes of data, either from stdin or from a file, and send them to the <i>DEVICE</i>.</p>
<dt><code>-t</code>, <code>&#8211;timeout</code>=<i>SEC</i></p>
<dd>Wait up to <i>SEC</i> seconds for command completion (default: 20). Note that if a command times out the operating system may start by aborting the command and if that is unsuccessful it may attempt to reset the device.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>Increase level of verbosity. Can be used multiple times.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>Display version and license information and exit.</dl>
<h2>Notes</h2>
<p>The sg_inq utility can be used to send an INQUIRY command to a device to determine its peripheral device type (e.g. &#8216;1&#8217; for a streaming device (tape drive)) which determines which SCSI command sets a device should support (e.g. SPC and SSC). The sg_vpd utility probes the Vital Product Pages of a devices which may contain useful information. </p>
<p> The ability to send more than a 16 byte CDB (in some cases 12 byte CDB) may be restricted by the pass-through interface, the low level driver or the transport.</p>
<h2>Examples</h2>
<p>These examples, apart from the last one, use Linux device names. For suitable device names in other supported Operating Systems see the <a href="/docs/linux/man/8-sg3_utils/">sg3_utils</a>(8) man page.</p>
<dl>
<dt>sg_raw /dev/scd0 1b 00 00 00 02 00</p>
<dd>Eject the medium in CD drive /dev/scd0.</p>
<dt>sg_raw -r 1k /dev/sg0 12 00 00 00 60 00</p>
<dd>Perform an INQUIRY on /dev/sg0 and dump the response data (up to 1024 bytes) to stdout.</p>
<dt>sg_raw -s 512 -i i512.bin /dev/sda 3b 02 00 00 00 00 00 02 00 00</p>
<dd>Showing an example of writing 512 bytes to a sector on a disk is a little dangerous. Instead this example will read i512.bin (assumed to be 512 bytes long) and use the SCSI WRITE BUFFER command to send it to the &quot;data&quot; buffer (that is mode 2). This is a safe operation.</p>
<dt>sg_raw -r 512 -o o512.bin /dev/sda 3c 02 00 00 00 00 00 02 00 00</p>
<dd>This will use the SCSI READ BUFFER command to read 512 bytes from the &quot;data&quot; buffer (i.e. mode 2) then write it to the o512.bin file. When used in conjunction with the previous example, if both commands work then &#8216;cmp i512.bin o512.bin&#8217; should show a match.</p>
<dt>sg_raw &#8211;infile=urandom.bin &#8211;send=512 &#8211;request=512 &#8211;outfile=out.bin &quot;/dev/bsg/7:0:0:0&quot; 53 00 00 00 00 00 00 00 01 00</p>
<dd>This is a bidirectional XDREADWRITE(10) command being sent via a Linux bsg device. Note that data is being read from &quot;urandom.bin&quot; and sent to the device (data-out) while resulting data (data-in) is placed in the &quot;out.bin&quot; file. Also note the length of both is 512 bytes which corresponds to the transfer length of 1 (block) in the cdb (i.e. the second last byte).</p>
<dt>sg_raw.exe PhysicalDrive1 a1 0c 0e 00 00 00 00 00 00 e0 00 00</p>
<dd>This example is from Windows and shows a ATA STANDBY IMMEDIATE command being sent to PhysicalDrive1. That ATA command is contained within the SCSI ATA PASS-THROUGH(12) command (see the SAT or SAT-2 standard at <a rel="nofollow" href="http://www.t10.org">http://www.t10.org</a>). Notice that the STANDBY IMMEDIATE command does not send or receive any additional data, however if it fails sense data should be returned and displayed.</dl>
<h2>Exit Status</h2>
<p>The exit status of sg_raw is 0 when it is successful. Otherwise see the <a href="/docs/linux/man/8-sg3_utils/">sg3_utils</a>(8) man page.</p>
<h2>Author</h2>
<p>Written by Ingo van Lil</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;inguin at gmx dot de&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2001-2012 Ingo van Lil<br />
 This software is distributed under the GPL version 2. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code>sg_inq, sg_vpd, sg3_utils (sg3_utils), plscsi</code> </p>
