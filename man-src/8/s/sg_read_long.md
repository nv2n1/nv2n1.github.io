---
title: "sg_read_long(8)"
name: "sg_read_long"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sg_read_long/"
description: "sg_read_long – send a SCSI READ LONG command"
---

<p>sg_read_long &#8211; send a SCSI READ LONG command</p>
<h2>Synopsis</h2>
<p><code>sg_read_long</code> [<i>&#8211;16</i>] [<i>&#8211;correct</i>] [<i>&#8211;help</i>] [<i>&#8211;lba=LBA</i>] [<i>&#8211;out=OF</i>] [<i>&#8211;pblock</i>] [<i>&#8211;readonly</i>] [<i>&#8211;verbose</i>] [<i>&#8211;version</i>] [<i>&#8211;xfer_len=BTL</i>] <i>DEVICE</i></p>
<h2>Description</h2>
<p>Send SCSI READ LONG command to <i>DEVICE</i>. The read buffer is output in hex and ASCII to stdout or placed in a file. Note that the data returned includes the logical block data (typically 512 bytes for a disk) plus ECC information (whose format is proprietary) plus optionally other proprietary data.</p>
<h2>Options</h2>
<p>Arguments to long options are mandatory for short options as well.</p>
<dl>
<dt><code>-S</code>, <code>&#8211;16</code></p>
<dd>uses a SCSI READ LONG(16) command. The default action is to use a SCSI READ LONG(10) command. The READ LONG(10) command has a 32 bit field for the lba while READ LONG(16) has a 64 bit field.</p>
<dt><code>-c</code>, <code>&#8211;correct</code></p>
<dd>sets the &#8216;CORRCT&#8217; bit in the SCSI READ LONG command. When set the data is corrected by the ECC before being transferred back to this utility. The default is to leave the &#8216;CORRCT&#8217; bit clear in which case the data is not corrected.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>output the usage message then exit.</p>
<dt><code>-l</code>, <code>&#8211;lba</code>=<i>LBA</i></p>
<dd>where <i>LBA</i> is the logical block address of the sector to read. Assumed to be in decimal unless prefixed with &#8216;0x&#8217; (or has a trailing &#8216;h&#8217;). Defaults to lba 0. If the lba is larger than can fit in 32 bits then the <i>&#8211;16</i> option should be used.</p>
<dt><code>-o</code>, <code>&#8211;out</code>=<i>OF</i></p>
<dd>instead of outputting ASCII hex to stdout, send it in binary to the file called <i>OF</i>. If &#8216;-&#8216; is given for <i>OF</i> then the (binary) output is sent to stdout. Note that all informative and error output is sent to stderr.</p>
<dt><code>-p</code>, <code>&#8211;pblock</code></p>
<dd>sets the &#8216;PBLOCK&#8217; bit in the SCSI READ LONG command. When set the physical block (plus ECC data) containing the requested logical block address is read. The default is to leave the &#8216;PBLOCK&#8217; bit clear in which case the logical block (plus any ECC data) is read.</p>
<dt><code>-r</code>, <code>&#8211;readonly</code></p>
<dd>opens the DEVICE read-only rather than read-write which is the default. The Linux sg driver needs read-write access for the SCSI READ LONG command but other access methods may require read-only access.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>increase the level of verbosity, (i.e. debug output).</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>print the version string and then exit.</p>
<dt><code>-x</code>, <code>&#8211;xfer_len</code>=<i>BTL</i></p>
<dd>where <i>BTL</i> is the byte transfer length (default to 520). If the given value (or the default) does not match the &quot;long&quot; block size of the device, the appropriate <i>BTL</i> is deduced from the error response and printed (to stderr). The idea is that the user will retry this utility with the correct transfer length.</dl>
<h2>Notes</h2>
<p>If a defective block is found and its contents, if any, has been retrieved then &quot;sg_reassign&quot; could be used to map out the defective block. Associated with such an action the number of elements in the &quot;grown&quot; defect list could be monitored (with &quot;sg_reassign &#8211;grown&quot;) as the disk could be nearing the end of its useful lifetime. </p>
<p> Various numeric arguments (e.g. <i>LBA</i>) may include multiplicative suffixes or be given in hexadecimal. See the &quot;NUMERIC ARGUMENTS&quot; section in the <a href="/docs/linux/man/8-sg3_utils/">sg3_utils</a>(8) man page. </p>
<p> As a data point, Fujitsu uses a 54 byte ECC (per block) which is capable of correcting up to a single burst error or 216 bits &quot;on the fly&quot;. [Information obtained from MAV20xxrc product manual.]</p>
<h2>Exit Status</h2>
<p>The exit status of sg_read_long is 0 when it is successful. Otherwise see the <a href="/docs/linux/man/8-sg3_utils/">sg3_utils</a>(8) man page.</p>
<h2>Authors</h2>
<p>Written by Douglas Gilbert.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;dgilbert at interlog dot com&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2004-2010 Douglas Gilbert<br />
 This software is distributed under the GPL version 2. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code>sg_reassign, sg_write_long, sg_dd</code> </p>
