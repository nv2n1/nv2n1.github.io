---
title: "sg_rbuf(8)"
name: "sg_rbuf"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sg_rbuf/"
description: "sg_rbuf – reads data using SCSI READ BUFFER command"
---

<p>sg_rbuf &#8211; reads data using SCSI READ BUFFER command</p>
<h2>Synopsis</h2>
<p><code>sg_rbuf</code> [<i>&#8211;buffer=EACH</i>] [<i>&#8211;dio</i>] [<i>&#8211;help</i>] [<i>&#8211;mmap</i>] [<i>&#8211;quick</i>] [<i>&#8211;size=OVERALL</i>] [<i>&#8211;test</i>] [<i>&#8211;verbose</i>] [<i>&#8211;version</i>] <i>DEVICE</i> </p>
<p> <code>sg_rbuf</code> [<i>-b=EACH_KIB</i>] [<i>-d</i>] [<i>-m</i>] [<i>-q</i>] [<i>-s=OVERALL_MIB</i>] [<i>-t</i>] [<i>-v</i>] [<i>-V</i>] <i>DEVICE</i></p>
<h2>Description</h2>
<p>This command reads data with the SCSI READ BUFFER command and then discards it. Typically the data being read is from a disk&#8217;s memory cache. It is assumed that the data is sourced quickly (although this is not guaranteed by the SCSI standards) so that it is faster than reading data from the media. This command is designed for timing transfer speeds across a SCSI transport. </p>
<p> To fetch the data with a SCSI READ BUFFER command and optionally decode it see the sg_read_buffer utility. There is also a sg_write_buffer utility useful for downloading firmware amongst other things. </p>
<p> This utility supports two command line syntaxes, the preferred one is shown first in the synopsis and explained in this section. A later section on the old command line syntax outlines the second group of options.</p>
<h2>Options</h2>
<p>Arguments to long options are mandatory for short options as well.</p>
<dl>
<dt><code>-b</code>, <code>&#8211;buffer</code>=<i>EACH</i></p>
<dd>where <i>EACH</i> is the number of bytes to be transferred by each READ BUFFER command. The default is the actual available buffer size returned by the READ BUFFER (descriptor) command. The maximum is the same as the default, hence this argument can only be used to reduce the size of each transfer to less than the device&#8217;s actual available buffer size.</p>
<dt><code>-d</code>, <code>&#8211;dio</code></p>
<dd>use direct IO if available. This option is only available if the <i>DEVICE</i> is a sg driver device node (e.g. /dev/sg1). In this case the sg driver will attempt to configure the DMA from the SCSI adapter to transfer directly into user memory. This will eliminate the copy via kernel buffers. If not available then this will be reported and indirect IO will be done instead.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>print usage message then exit.</p>
<dt><code>-m</code>, <code>&#8211;mmap</code></p>
<dd>use memory mapped IO if available. This option is only available if the <i>DEVICE</i> is a sg driver device node (e.g. /dev/sg1). In this case the sg driver will attempt to configure the DMA from the SCSI adapter to transfer directly into user memory. This will eliminate the copy via kernel buffers.</p>
<dt><code>-O</code>, <code>&#8211;old</code></p>
<dd>switch to older style options.</p>
<dt><code>-q</code>, <code>&#8211;quick</code></p>
<dd>only transfer the data into kernel buffers (typically by DMA from the SCSI adapter card) and do not move it into the user space. This option is only available if the <i>DEVICE</i> is a sg driver device node (e.g. /dev/sg1).</p>
<dt><code>-s</code>, <code>&#8211;size</code>=<i>OVERALL</i></p>
<dd>where <i>OVERALL</i> is the size of total transfer in bytes. The default is 200 MiB (200*1024*1024 bytes). The actual number of bytes transferred may be slightly less than requested since all transfers are the same size (and an integer division is involved rounding towards zero).</p>
<dt><code>-t</code>, <code>&#8211;time</code></p>
<dd>times the bulk data transfer component of this command. The elapsed time is printed out plus a MB/sec calculation. In this case &quot;MB&quot; is 1,000,000 bytes. The gettimeofday() system call is used internally for the time calculation.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>increase level of verbosity. Can be used multiple times.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>print out version string then exit.</dl>
<h2>Notes</h2>
<p>This command is typically used on modern SCSI disks which have a RAM cache in their drive electronics. If no IO to the magnetic media, or slower devices like flash RAM, is involved then the disk may be able to source data fast enough to saturate the bandwidth of the SCSI transport. The bottleneck may then be the DMA element in the HBA, the Linux drivers or the host machine&#8217;s hardware (e.g. speed of RAM). </p>
<p> Various numeric arguments (e.g. <i>OVERALL</i>) may include multiplicative suffixes or be given in hexadecimal. See the &quot;NUMERIC ARGUMENTS&quot; section in the <a href="/docs/linux/man/8-sg3_utils/">sg3_utils</a>(8) man page.</p>
<h2>Examples</h2>
<p>On the test system /dev/sg0 corresponds to a fast disk on a U2W SCSI bus (max 80 MB/sec). The disk specifications state that its cache is 4 MB. </p>
<p>$&nbsp;<wbr>time ./sg_rbuf&nbsp;<wbr>/dev/sg0<br />
 READ BUFFER reports: buffer capacity=3434944, </p>
<p>&nbsp;<wbr>offset boundary=6<br />
 Read 200 MiB (actual 199 MiB, 209531584 bytes), </p>
<p>&nbsp;<wbr>buffer size=3354 KiB<br />
 real 0m5.072s, user 0m0.000s, sys 0m2.280s </p>
<p> So that is approximately 40 MB/sec at 40 % utilization. Now with the addition of the &quot;-q&quot; option this throughput improves and the utilization drops to 0%. </p>
<p>$&nbsp;<wbr>time ./sg_rbuf -q&nbsp;<wbr>/dev/sg0<br />
 READ BUFFER reports: buffer capacity=3434944, </p>
<p>&nbsp;<wbr>offset boundary=6<br />
 Read 200 MiB (actual 199 MiB, 209531584 bytes), </p>
<p>&nbsp;<wbr>buffer size=3354 KiB<br />
 real 0m2.784s, user 0m0.000s, sys 0m0.000s</p>
<h2>Exit Status</h2>
<p>The exit status of sg_rbuf is 0 when it is successful. Otherwise see the <a href="/docs/linux/man/8-sg3_utils/">sg3_utils</a>(8) man page.</p>
<h2>Older Command Line Options</h2>
<p>The options in this section were the only ones available prior to sg3_utils version 1.23 . In sg3_utils version 1.23 and later these older options can be selected by either setting the SG3_UTILS_OLD_OPTS environment variable or using &#8216;&#8211;old&#8217; (or &#8216;-O) as the first option.</p>
<dl>
<dt><code>-b</code>=<i>EACH_KIB</i></p>
<dd>where <i>EACH_KIB</i> is the number of Kilobytes (i.e. 1024 byte units) to be transferred by each READ BUFFER command. Similar to the <i>&#8211;buffer=EACH</i> option in the main description but the units are different.</p>
<dt><code>-d</code></p>
<dd>use direct IO if available. Equivalent to the <i>&#8211;dio</i> option in the main description.</p>
<dt><code>-m</code></p>
<dd>use memory mapped IO if available. Equivalent to the <i>&#8211;mmap</i> option in the main description.</p>
<dt><code>-N</code></p>
<dd>switch to the newer style options.</p>
<dt><code>-q</code></p>
<dd>only transfer the data into kernel buffers (typically by DMA from the SCSI adapter card) and do not move it into the user space. Equivalent to the <i>&#8211;quick</i> option in the main description.</p>
<dt><code>-s</code>=<i>OVERALL_MIB</i></p>
<dd>where <i>OVERALL_MIB</i> is the size of total transfer in Megabytes (1048576 bytes). Similar to the <i>&#8211;size=OVERALL</i> option in the main description but the units are different.</p>
<dt><code>-t</code></p>
<dd>times the bulk data transfer component of this command. Equivalent to the <i>&#8211;time</i> option in the main description.</p>
<dt><code>-v</code></p>
<dd>increase level of verbosity. Can be used multiple times.</p>
<dt><code>-V</code></p>
<dd>print out version string then exit.</dl>
<h2>Author</h2>
<p>Written by Douglas Gilbert</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;dgilbert at interlog dot com&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2000-2007 Douglas Gilbert<br />
 This software is distributed under the GPL version 2. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code>sg_read_buffer, sg_write_buffer, sg_test_rwbuf(all in sg3_utils)</code> </p>
