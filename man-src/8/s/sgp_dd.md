---
title: "sgp_dd(8)"
name: "sgp_dd"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sgp_dd/"
description: "sgp_dd – copy data to and from files and devices, especially SCSI devices"
---

<p>sgp_dd &#8211; copy data to and from files and devices, especially SCSI devices</p>
<h2>Synopsis</h2>
<p><code>sgp_dd</code> [<i>bs=BS</i>] [<i>count=COUNT</i>] [<i>ibs=BS</i>] [<i>if=IFILE</i>] [<i>iflag=FLAGS</i>] [<i>obs=BS</i>] [<i>of=OFILE</i>] [<i>oflag=FLAGS</i>] [<i>seek=SEEK</i>] [<i>skip=SKIP</i>] [<i>&#8211;help</i>] [<i>&#8211;version</i>] </p>
<p> [<i>bpt=BPT</i>] [<i>coe=</i>0|1] [<i>cdbsz=</i>6|10|12|16] [<i>deb=VERB</i>] [<i>dio=</i>0|1] [<i>sync=</i>0|1] [<i>thr=THR</i>] [<i>time=</i>0|1] [<i>verbose=VERB</i>]</p>
<h2>Description</h2>
<p>Copy data to and from any files. Specialised for &quot;files&quot; that are Linux SCSI generic (sg) and raw devices. Similar syntax and semantics to <code><a href="/docs/linux/man/1-dd/">dd</a>(1)</code> but does not perform any conversions. Uses POSIX threads to increase the amount of parallelism. This improves speed in some cases. </p>
<p> The first group in the synopsis above are &quot;standard&quot; Unix <code><a href="/docs/linux/man/1-dd/">dd</a>(1)</code> operands. The second group are extra options added by this utility. Both groups are defined below.</p>
<h2>Options</h2>
<dl>
<dt><code>bpt</code>=<i>BPT</i></p>
<dd>each IO transaction will be made using <i>BPT</i> blocks (or less if near the end of the copy). Default is 128 for block sizes less that 2048 bytes, otherwise the default is 32. So for bs=512 the reads and writes will each convey 64 KiB of data by default (less if near the end of the transfer or memory restrictions). When cd/dvd drives are accessed, the block size is typically 2048 bytes and bpt defaults to 32 which again implies 64 KiB transfers.</p>
<dt><code>bs</code>=<i>BS</i></p>
<dd>where <i>BS</i> <code>must</code> be the block size of the physical device. Note that this differs from <code><a href="/docs/linux/man/1-dd/">dd</a>(1)</code> which permits &#8216;bs&#8217; to be an integral multiple of the actual device block size. Default is 512 which is usually correct for disks but incorrect for cdroms (which normally have 2048 byte blocks).</p>
<dt><code>cdbsz</code>=6 | 10 | 12 | 16</p>
<dd>size of SCSI READ and/or WRITE commands issued on sg device names. Default is 10 byte SCSI command blocks (unless calculations indicate that a 4 byte block number may be exceeded, in which case it defaults to 16 byte SCSI commands).</p>
<dt><code>coe</code>=0 | 1</p>
<dd>set to 1 for continue on error. Only applies to errors on sg devices. Thus errors on other files will stop sgp_dd. Default is 0 which implies stop on any error. See the &#8216;coe&#8217; flag for more information.</p>
<dt><code>count</code>=<i>COUNT</i></p>
<dd>copy <i>COUNT</i> blocks from <i>IFILE</i> to <i>OFILE</i>. Default is the minimum (of <i>IFILE</i> and <i>OFILE</i>) number of blocks that sg devices report from SCSI READ CAPACITY commands or that block devices (or their partitions) report. Normal files are not probed for their size. If <i>skip=SKIP</i> or <i>skip=SEEK</i> are given and the count is deduced (i.e. not explicitly given) then that count is scaled back so that the copy will not overrun the device. If the file name is a block device partition and <i>COUNT</i> is not given then the size of the partition rather than the size of the whole device is used. If <i>COUNT</i> is not given and cannot be deduced then an error message is issued and no copy takes place.</p>
<dt><code>deb</code>=<i>VERB</i></p>
<dd>outputs debug information. If <i>VERB</i> is 0 (default) then there is minimal debug information and as <i>VERB</i> increases so does the amount of debug (max debug output when <i>VERB</i> is 9).</p>
<dt><code>dio</code>=0 | 1</p>
<dd>default is 0 which selects indirect IO. Value of 1 attempts direct IO which, if not available, falls back to indirect IO and notes this at completion. If direct IO is selected and /proc/scsi/sg/allow_dio has the value of 0 then a warning is issued (and indirect IO is performed) For finer grain control use &#8216;iflag=dio&#8217; or &#8216;oflag=dio&#8217;.</p>
<dt><code>ibs</code>=<i>BS</i></p>
<dd>if given must be the same as <i>BS</i> given to &#8216;bs=&#8217; option.</p>
<dt><code>if</code>=<i>IFILE</i></p>
<dd>read from <i>IFILE</i> instead of stdin. If <i>IFILE</i> is &#8216;-&#8216; then stdin is read. Starts reading at the beginning of <i>IFILE</i> unless <i>SKIP</i> is given.</p>
<dt><code>iflag</code>=<i>FLAGS</i></p>
<dd>where <i>FLAGS</i> is a comma separated list of one or more flags outlined below. These flags are associated with <i>IFILE</i> and are ignored when <i>IFILE</i> is stdin.</p>
<dt><code>obs</code>=<i>BS</i></p>
<dd>if given must be the same as <i>BS</i> given to &#8216;bs=&#8217; option.</p>
<dt><code>of</code>=<i>OFILE</i></p>
<dd>write to <i>OFILE</i> instead of stdout. If <i>OFILE</i> is &#8216;-&#8216; then writes to stdout. If <i>OFILE</i> is /dev/null then no actual writes are performed. If <i>OFILE</i> is &#8216;.&#8217; (period) then it is treated the same way as /dev/null (this is a shorthand notation). If <i>OFILE</i> exists then it is _not_ truncated; it is overwritten from the start of <i>OFILE</i> unless &#8216;oflag=append&#8217; or <i>SEEK</i> is given.</p>
<dt><code>oflag</code>=<i>FLAGS</i></p>
<dd>where <i>FLAGS</i> is a comma separated list of one or more flags outlined below. These flags are associated with <i>OFILE</i> and are ignored when <i>OFILE</i> is /dev/null, &#8216;.&#8217; (period), or stdout.</p>
<dt><code>seek</code>=<i>SEEK</i></p>
<dd>start writing <i>SEEK</i> bs-sized blocks from the start of <i>OFILE</i>. Default is block 0 (i.e. start of file).</p>
<dt><code>skip</code>=<i>SKIP</i></p>
<dd>start reading <i>SKIP</i> bs-sized blocks from the start of <i>IFILE</i>. Default is block 0 (i.e. start of file).</p>
<dt><code>sync</code>=0 | 1</p>
<dd>when 1, does SYNCHRONIZE CACHE command on <i>OFILE</i> at the end of the transfer. Only active when <i>OFILE</i> is a sg device file name.</p>
<dt><code>thr</code>=<i>THR</i></p>
<dd>where <i>THR</i> is the number or worker threads (default 4) that attempt to copy in parallel. Minimum is 1 and maximum is 16.</p>
<dt><code>time</code>=0 | 1</p>
<dd>when 1, the transfer is timed and throughput calculation is performed, outputting the results (to stderr) at completion. When 0 (default) no timing is performed.</p>
<dt><code>verbose</code>=<i>VERB</i></p>
<dd>increase verbosity. Same as <i>deb=VERB</i>. Added for compatibility with sg_dd and sgm_dd.</p>
<dt><code>&#8211;help</code></p>
<dd>outputs usage message and exits.</p>
<dt><code>&#8211;version</code></p>
<dd>outputs version number information and exits.</dl>
<h2>Flags</h2>
<p>Here is a list of flags and their meanings:</p>
<dl>
<dt>append</p>
<dd>causes the O_APPEND flag to be added to the open of <i>OFILE</i>. For normal files this will lead to data appended to the end of any existing data. Cannot be used together with the <i>seek=SEEK</i> option as they conflict. The default action of this utility is to overwrite any existing data from the beginning of the file or, if <i>SEEK</i> is given, starting at block <i>SEEK</i>. Note that attempting to &#8216;append&#8217; to a device file (e.g. a disk) will usually be ignored or may cause an error to be reported.</p>
<dt>coe</p>
<dd>continue on error. When given with &#8216;iflag=&#8217;, an error that is detected in a single SCSI command (typically &#8216;bpt&#8217; blocks) is noted (by an error message sent to stderr), then zeros are substituted into the buffer for the corresponding write operation and the copy continues. Note that the <code>sg_dd</code> utility is more sophisticated in such error situations when &#8216;iflag=coe&#8217;. When given with &#8216;oflag=&#8217;, any error reported by a SCSI WRITE command is reported to stderr and the copy continues (as if nothing went wrong).</p>
<dt>dio</p>
<dd>request the sg device node associated with this flag does direct IO. If direct IO is not available, falls back to indirect IO and notes this at completion. If direct IO is selected and /proc/scsi/sg/allow_dio has the value of 0 then a warning is issued (and indirect IO is performed).</p>
<dt>direct</p>
<dd>causes the O_DIRECT flag to be added to the open of <i>IFILE</i> and/or <i>OFILE</i>. This flag requires some memory alignment on IO. Hence user memory buffers are aligned to the page size. Has no effect on sg, normal or raw files.</p>
<dt>dpo</p>
<dd>set the DPO bit (disable page out) in SCSI READ and WRITE commands. Not supported for 6 byte cdb variants of READ and WRITE. Indicates that data is unlikely to be required to stay in device (e.g. disk) cache. May speed media copy and/or cause a media copy to have less impact on other device users.</p>
<dt>dsync</p>
<dd>causes the O_SYNC flag to be added to the open of <i>IFILE</i> and/or <i>OFILE</i>. The &#8216;d&#8217; is prepended to lower confusion with the &#8216;sync=0|1&#8217; option which has another action (i.e. a synchronisation to media at the end of the transfer).</p>
<dt>excl</p>
<dd>causes the O_EXCL flag to be added to the open of <i>IFILE</i> and/or <i>OFILE</i>.</p>
<dt>fua</p>
<dd>causes the FUA (force unit access) bit to be set in SCSI READ and/or WRITE commands. This only has effect with sg devices. The 6 byte variants of the SCSI READ and WRITE commands do not support the FUA bit. Only active for sg device file names.</p>
<dt>null</p>
<dd>has no affect, just a placeholder.</dl>
<h2>Retired Options</h2>
<p>Here are some retired options that are still present:</p>
<dl>
<dt>coe=0 | 1</p>
<dd>continue on error is 0 (off) by default. When it is 1, it is equivalent to &#8216;iflag=coe oflag=coe&#8217; described in the FLAGS section above. Similar to &#8216;conv=noerror,sync&#8217; in <code><a href="/docs/linux/man/1-dd/">dd</a>(1)</code> utility. Default is 0 which implies stop on error. More advanced coe=1 processing on reads is performed by the sg_dd utility.</p>
<dt>
<dt>fua=0 | 1 | 2 | 3</p>
<dd>
<dd>force unit access bit. When 3, fua is set on both <i>IFILE</i> and <i>OFILE</i>; when 2, fua is set on <i>IFILE</i>;, when 1, fua is set on <i>OFILE</i>; when 0 (default), fua is cleared on both. See the &#8216;fua&#8217; flag.</dl>
<h2>Notes</h2>
<p>A raw device must be bound to a block device prior to using sgp_dd. See <code><a href="/docs/linux/man/8-raw/">raw</a>(8)</code> for more information about binding raw devices. To be safe, the sg device mapping to SCSI block devices should be checked with &#8216;cat /proc/scsi/scsi&#8217; before use. </p>
<p> Raw device partition information can often be found with <code><a href="/docs/linux/man/8-fdisk/">fdisk</a>(8)</code> [the &quot;-ul&quot; argument is useful in this respect]. </p>
<p> Various numeric arguments (e.g. <i>SKIP</i>) may include multiplicative suffixes or be given in hexadecimal. See the &quot;NUMERIC ARGUMENTS&quot; section in the <a href="/docs/linux/man/8-sg3_utils/">sg3_utils</a>(8) man page. </p>
<p> The <i>COUNT</i>, <i>SKIP</i> and <i>SEEK</i> arguments can take 64 bit values (i.e. very big numbers). Other values are limited to what can fit in a signed 32 bit number. </p>
<p> Data usually gets to the user space in a 2 stage process: first the SCSI adapter DMAs into kernel buffers and then the sg driver copies this data into user memory (write operations reverse this sequence). This is called &quot;indirect IO&quot; and there is a &#8216;dio&#8217; option to select &quot;direct IO&quot; which will DMA directly into user memory. Due to some issues &quot;direct IO&quot; is disabled in the sg driver and needs a configuration change to activate it. </p>
<p> All informative, warning and error output is sent to stderr so that dd&#8217;s output file can be stdout and remain unpolluted. If no options are given, then the usage message is output and nothing else happens. </p>
<p> Why use sgp_dd? Because in some cases it is twice as fast as dd (mainly with sg devices, raw devices give some improvement). Another reason is that big copies fill the block device caches which has a negative impact on other machine activity.</p>
<h2>Signals</h2>
<p>The signal handling has been borrowed from dd: SIGINT, SIGQUIT and SIGPIPE output the number of remaining blocks to be transferred and the records in + out counts; then they have their default action. SIGUSR1 causes the same information to be output yet the copy continues. All output caused by signals is sent to stderr.</p>
<h2>Examples</h2>
<p>Looks quite similar in usage to dd: </p>
<pre><code>sgp_dd if=/dev/sg0 of=t bs=512 count=1MB</code></pre>
<p> This will copy 1 million 512 byte blocks from the device associated with /dev/sg0 (which should have 512 byte blocks) to a file called t. Assuming /dev/sda and /dev/sg0 are the same device then the above is equivalent to: dd if=/dev/sda of=t bs=512 count=1000000 although dd&#8217;s speed may improve if bs was larger and count was correspondingly scaled. Using a raw device to do something similar on a ATA disk: raw /dev/raw/raw1 /dev/hda</p>
<p>sgp_dd if=/dev/raw/raw1 of=t bs=512 count=1MB To copy a SCSI disk partition to an ATA disk partition: raw /dev/raw/raw2 /dev/hda3</p>
<p>sgp_dd if=/dev/sg0 skip=10123456 of=/dev/raw/raw2 bs=512 This assumes a valid partition is found on the SCSI disk at the given skip block address (past the 5 GB point of that disk) and that the partition goes to the end of the SCSI disk. An explicit count is probably a safer option. To do a fast copy from one SCSI disk to another one with similar geometry (stepping over errors on the source disk): </p>
<pre><code>sgp_dd if=/dev/sg0 of=/dev/sg1 bs=512 coe=1</code></pre>
<h2>Exit Status</h2>
<p>The exit status of sgp_dd is 0 when it is successful. Otherwise see the <a href="/docs/linux/man/8-sg3_utils/">sg3_utils</a>(8) man page. Since this utility works at a higher level than individual commands, and there are &#8216;coe&#8217; and &#8216;retries&#8217; flags, individual SCSI command failures do not necessary cause the process to exit.</p>
<h2>Authors</h2>
<p>Written by Douglas Gilbert and Peter Allworth.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;dgilbert at interlog dot com&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2000-2012 Douglas Gilbert<br />
 This software is distributed under the GPL version 2. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p>A simpler, non-threaded version of this utility but with more advanced &quot;continue on error&quot; logic is called <code>sg_dd</code> and is also found in the sg3_utils package. The lmbench package contains <code>lmdd</code> which is also interesting. <code><a href="/docs/linux/man/8-raw/">raw</a>(8), <a href="/docs/linux/man/1-dd/">dd</a>(1)</code> </p>
