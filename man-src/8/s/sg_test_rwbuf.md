---
title: "sg_test_rwbuf(8)"
name: "sg_test_rwbuf"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sg_test_rwbuf/"
description: "sg_test_rwbuf – test a SCSI host adapter by issuing dummy writes and reads"
---

<p>sg_test_rwbuf &#8211; test a SCSI host adapter by issuing dummy writes and reads</p>
<h2>Synopsis</h2>
<p><code>sg_test_rwbuf</code> [<i>&#8211;addrd=AR</i>] [<i>&#8211;addwr=AW</i>] [<i>&#8211;help</i>] [<i>&#8211;quick</i>] <i>&#8211;size=SZ</i> [<i>&#8211;times=NUM</i>] [<i>&#8211;verbose</i>] [<i>&#8211;version</i>] <i>DEVICE</i> </p>
<p> or an older deprecated format <code>sg_test_rwbuf</code> <i>DEVICE</i> <i>SZ</i> [<i>AW</i>] [<i>AR</i>]</p>
<h2>Description</h2>
<p>sg_test_rwbuf writes and reads back <i>SZ</i> bytes to the internal buffer of <i>DEVICE</i> (e.g. /dev/sda or /dev/sg0). A pseudo random pattern is written to the data buffer on the device then read back. If the same pattern is found &#8216;Success&#8217; is reported. If they do not match (checksums unequal) then this is reported and up to 24 bytes from the first point of mismatch are reported; the first line shows what was written and the second line shows what was received. For testing purposes, you can ask it to write <i>AW</i> or read <i>AR</i> additional bytes.</p>
<h2>Options</h2>
<p>Arguments to long options are mandatory for short options as well.</p>
<dl>
<dt><code>-r</code>, <code>&#8211;addrd</code>=<i>AR</i></p>
<dd>Read an additional <i>AR</i> bytes (than indicated by <i>SZ</i>) from the data buffer. Checksum is performed over the first <i>SZ</i> bytes.</p>
<dt><code>-w</code>, <code>&#8211;addwr</code>=<i>AW</i></p>
<dd>Write an additional <i>AW</i> bytes (than indicated by <i>SZ</i>) of zeros into the data buffer. Checksum is generated over the first <i>SZ</i> bytes.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>Print out a usage message the exit.</p>
<dt><code>-q</code>, <code>&#8211;quick</code></p>
<dd>Perform a READ BUFFER descriptor command to find out the available data buffer length and offset, print them out then exit (without testing with write/read sequences).</p>
<dt><code>-s</code>, <code>&#8211;size</code>=<i>SZ</i></p>
<dd>where <i>SZ</i> is the size of buffer in bytes to be written then read and checked. This number needs to be less than or equal to the size of the device&#8217;s data buffer which can be seen from the <i>&#8211;quick</i> option. Either this option or the <i>&#8211;quick</i> option should be given.</p>
<dt><code>-t</code>, <code>&#8211;times</code>=<i>NUM</i></p>
<dd>where <i>NUM</i> is the number of times to repeat the write/read to buffer test. Default value is 1 .</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>increase verbosity of output.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>print version number (and data of last change) then exit.</dl>
<h2>Notes</h2>
<p>The microcode in a SCSI device is _not_ modified by doing a WRITE BUFFER command with its mode set to &quot;data&quot; (0x2) as done by this utility. Therefore this utility is safe in that respect. [Mode values 0x4, 0x5, 0x6 and 0x7 are the dangerous ones :-)] </p>
<p> <code>WARNING</code>: If you access the device at the same time (e.g. because it&#8217;s a hard disk with a mounted file system on it) the device&#8217;s buffer may be used by the device itself for other data at the same time, and overwriting it may or may not cause data corruption! <code>HOWEVER</code> the SPC-3 draft standard does state in its WRITE BUFFER command: &quot;This command shall not alter any medium of the logical unit when data mode &#8230; is specified&quot;. This implies that it _is_ safe to use this utility with devices that have mounted file systems on them. Following this theme further, a disk with active mounted file systems may cause the data read back to be different (due to caching activity) to what was written and hence a checksum error.</p>
<h2>Exit Status</h2>
<p>The exit status of sg_test_rwbuf is 0 when it is successful. Otherwise see the <a href="/docs/linux/man/8-sg3_utils/">sg3_utils</a>(8) man page.</p>
<h2>Authors</h2>
<p>Written by D. Gilbert and K. Garloff</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2000-2012 Douglas Gilbert, Kurt Garloff<br />
 This software is distributed under the GPL version 2. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
