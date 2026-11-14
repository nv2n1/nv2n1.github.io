---
title: "sg_dd(8)"
name: "sg_dd"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sg_dd/"
description: "sg_dd – copy data to and from files and devices, especially SCSI devices"
---

<p>sg_dd &#8211; copy data to and from files and devices, especially SCSI devices</p>
<h2>Synopsis</h2>
<p><code>sg_dd</code> [<i>bs=BS</i>] [<i>conv=CONV</i>] [<i>count=COUNT</i>] [<i>ibs=BS</i>] [<i>if=IFILE</i>] [<i>iflag=FLAGS</i>] [<i>obs=BS</i>] [<i>of=OFILE</i>] [<i>oflag=FLAGS</i>] [<i>seek=SEEK</i>] [<i>skip=SKIP</i>] [<i>&#8211;help</i>] [<i>&#8211;version</i>] </p>
<p> [<i>blk_sgio=</i>{0|1}] [<i>bpt=BPT</i>] [<i>cdbsz=</i>{6|10|12|16}] [<i>coe=</i>{0|1|2|3}] [<i>coe_limit=CL</i>] [<i>dio=</i>{0|1}] [<i>odir=</i>{0|1}] [<i>of2=OFILE2</i>] [<i>retries=RETR</i>] [<i>sync=</i>{0|1}] [<i>time=</i>{0|1}] [<i>verbose=VERB</i>] [<i>-V</i>]</p>
<h2>Description</h2>
<p>Copy data to and from any files. Specialized for &quot;files&quot; that are Linux SCSI generic (sg) devices, raw devices or other devices that support the SG_IO ioctl (which are only found in the lk 2.6 series). Similar syntax and semantics to <code><a href="/docs/linux/man/1-dd/">dd</a>(1)</code> command. </p>
<p> The first group in the synopsis above are &quot;standard&quot; Unix <code><a href="/docs/linux/man/1-dd/">dd</a>(1)</code> operands. The second group are extra options added by this utility. Both groups are defined below. </p>
<p> This utility is only supported on Linux whereas most other utilities in the sg3_utils package have been ported to other operating systems. A utility called &quot;ddpt&quot; has similar syntax and functionality to sg_dd. ddpt drops some Linux specific features while adding some other generic features. This allows ddpt to be ported to other operating systems.</p>
<h2>Options</h2>
<dl>
<dt><code>blk_sgio</code>={0|1}</p>
<dd>when set to 0, block devices (e.g. /dev/sda) are treated like normal files (i.e. <code><a href="/docs/linux/man/2-read/">read</a>(2)</code> and <code><a href="/docs/linux/man/2-write/">write</a>(2)</code> are used for IO). When set to 1, block devices are assumed to accept the SG_IO ioctl and SCSI commands are issued for IO. This is only supported for 2.6 series kernels. Note that ATAPI devices (e.g. cd/dvd players) use the SCSI command set but ATA disks do not (unless there is a protocol conversion as often occurs in the USB mass storage class). If the input or output device is a block device partition (e.g. /dev/sda3) then setting this option causes the partition information to be ignored (since access is directly to the underlying device). Default is 0. See the &#8216;sgio&#8217; flag.</p>
<dt><code>bpt</code>=<i>BPT</i></p>
<dd>each IO transaction will be made using <i>BPT</i> blocks (or less if near the end of the copy). Default is 128 for block sizes less that 2048 bytes, otherwise the default is 32. So for bs=512 the reads and writes will each convey 64 KiB of data by default (less if near the end of the transfer or memory restrictions). When cd/dvd drives are accessed, the block size is typically 2048 bytes and bpt defaults to 32 which again implies 64 KiB transfers. The block layer when the blk_sgio=1 option is used has relatively low upper limits for transfer sizes (compared to sg device nodes, see /sys/block/&lt;dev_name&gt;/queue/max_sectors_kb ).</p>
<dt><code>bs</code>=<i>BS</i></p>
<dd>where <i>BS</i> <code>must</code> be the block size of the physical device (if either the input or output files are accessed via SCSI commands). Note that this differs from <code><a href="/docs/linux/man/1-dd/">dd</a>(1)</code> which permits <i>BS</i> to be an integral multiple. Default is 512 which is usually correct for disks but incorrect for cdroms (which normally have 2048 byte blocks). For this utility the maximum size of each individual IO operation is <i>BS</i> * <i>BPT</i> bytes.</p>
<dt><code>cdbsz</code>={6|10|12|16}</p>
<dd>size of SCSI READ and/or WRITE commands issued on sg device names (or block devices when &#8216;iflag=sgio&#8217; and/or &#8216;oflag=sgio&#8217; is given). Default is 10 byte SCSI command blocks (unless calculations indicate that a 4 byte block number may be exceeded or <i>BPT</i> is greater than 16 bits (65535), in which case it defaults to 16 byte SCSI commands).</p>
<dt><code>coe</code>={0|1|2|3}</p>
<dd>set to 1 or more for continue on error. Only applies to errors on sg devices or block devices with the &#8216;sgio&#8217; flag set. Thus errors on other files will stop sg_dd. Default is 0 which implies stop on any error. See the &#8216;coe&#8217; flag for more information.</p>
<dt><code>coe_limit</code>=<i>CL</i></p>
<dd>where <i>CL</i> is the maximum number of consecutive bad blocks stepped over (due to &quot;coe&gt;0&quot;) on reads before the copy terminates. This only applies when <i>IFILE</i> is accessed via the SG_IO ioctl. The default is 0 which is interpreted as no limit. This option is meant to stop the copy soon after unrecorded media is detected while still offering &quot;continue on error&quot; capability.</p>
<dt><code>conv</code>=<code>sparse</code></p>
<dd>see the CONVERSIONS section below.</p>
<dt><code>count</code>=<i>COUNT</i></p>
<dd>copy <i>COUNT</i> blocks from <i>IFILE</i> to <i>OFILE</i>. Default is the minimum (of <i>IFILE</i> and <i>OFILE</i>) number of blocks that sg devices report from SCSI READ CAPACITY commands or that block devices (or their partitions) report. Normal files are not probed for their size. If <i>skip=SKIP</i> or <i>skip=SEEK</i> are given and the count is derived (i.e. not explicitly given) then the derived count is scaled back so that the copy will not overrun the device. If the file name is a block device partition and <i>COUNT</i> is not given then the size of the partition rather than the size of the whole device is used. If <i>COUNT</i> is not given (or <i>count=-1</i>) and cannot be derived then an error message is issued and no copy takes place.</p>
<dt><code>dio</code>={0|1}</p>
<dd>default is 0 which selects indirect (buffered) IO on sg devices. Value of 1 attempts direct IO which, if not available, falls back to indirect IO and notes this at completion. If direct IO is selected and /proc/scsi/sg/allow_dio has the value of 0 then a warning is issued (and indirect IO is performed). For finer grain control use &#8216;iflag=dio&#8217; or &#8216;oflag=dio&#8217;.</p>
<dt><code>ibs</code>=<i>BS</i></p>
<dd>if given must be the same as <i>BS</i> given to &#8216;bs=&#8217; option.</p>
<dt><code>if</code>=<i>IFILE</i></p>
<dd>read from <i>IFILE</i> instead of stdin. If <i>IFILE</i> is &#8216;-&#8216; then stdin is read. Starts reading at the beginning of <i>IFILE</i> unless <i>SKIP</i> is given.</p>
<dt><code>iflag</code>=<i>FLAGS</i></p>
<dd>where <i>FLAGS</i> is a comma separated list of one or more flags outlined below. These flags are associated with <i>IFILE</i> and are ignored when <i>IFILE</i> is stdin.</p>
<dt><code>obs</code>=<i>BS</i></p>
<dd>if given must be the same as <i>BS</i> given to &#8216;bs=&#8217; option.</p>
<dt><code>odir</code>={0|1}</p>
<dd>when set to one opens block devices (e.g. /dev/sda) with the O_DIRECT flag. User memory buffers are aligned to the page size when set. The default is 0 (i.e. the O_DIRECT flag is not used). Has no effect on sg, normal or raw files. If blk_sgio is also set then both are honoured: block devices are opened with the O_DIRECT flag and SCSI commands are issued via the SG_IO ioctl.</p>
<dt><code>of</code>=<i>OFILE</i></p>
<dd>write to <i>OFILE</i> instead of stdout. If <i>OFILE</i> is &#8216;-&#8216; then writes to stdout. If <i>OFILE</i> is /dev/null then no actual writes are performed. If <i>OFILE</i> is &#8216;.&#8217; (period) then it is treated the same way as /dev/null (this is a shorthand notation). If <i>OFILE</i> exists then it is _not_ truncated; it is overwritten from the start of <i>OFILE</i> unless &#8216;oflag=append&#8217; or <i>SEEK</i> is given.</p>
<dt><code>of2</code>=<i>OFILE2</i></p>
<dd>write output to <i>OFILE2</i>. The default action is not to do this additional write (i.e. when this option is not given). <i>OFILE2</i> is assumed to be a normal file or a fifo (i.e. a named pipe). <i>OFILE2</i> is opened for writing, created if necessary, and closed at the end of the transfer. If <i>OFILE2</i> is a fifo (named pipe) then some other command should be consuming that data (e.g. &#8216;md5sum OFILE2&#8217;), otherwise this utility will block.</p>
<dt><code>oflag</code>=<i>FLAGS</i></p>
<dd>where <i>FLAGS</i> is a comma separated list of one or more flags outlined below. These flags are associated with <i>OFILE</i> and are ignored when <i>OFILE</i> is /dev/null, &#8216;.&#8217; (period), or stdout.</p>
<dt><code>retries</code>=<i>RETR</i></p>
<dd>sometimes retries at the host are useful, for example when there is a transport error. When <i>RETR</i> is greater than zero then SCSI READs and WRITEs are retried on error, <i>RETR</i> times. Default value is zero.</p>
<dt><code>seek</code>=<i>SEEK</i></p>
<dd>start writing <i>SEEK</i> bs-sized blocks from the start of <i>OFILE</i>. Default is block 0 (i.e. start of file).</p>
<dt><code>skip</code>=<i>SKIP</i></p>
<dd>start reading <i>SKIP</i> bs-sized blocks from the start of <i>IFILE</i>. Default is block 0 (i.e. start of file).</p>
<dt><code>sync</code>={0|1}</p>
<dd>when 1, does SYNCHRONIZE CACHE command on <i>OFILE</i> at the end of the transfer. Only active when <i>OFILE</i> is a sg device file name or a block device and &#8216;blk_sgio=1&#8217; is given.</p>
<dt><code>time</code>={0|1}</p>
<dd>when 1, times transfer and does throughput calculation, outputting the results (to stderr) at completion. When 0 (default) doesn&#8217;t perform timing.</p>
<dt><code>verbose</code>=<i>VERB</i></p>
<dd>as <i>VERB</i> increases so does the amount of debug output sent to stderr. Default value is zero which yields the minimum amount of debug output. A value of 1 reports extra information that is not repetitive. A value 2 reports cdbs and responses for SCSI commands that are not repetitive (i.e. other that READ and WRITE). Error processing is not considered repetitive. Values of 3 and 4 yield output for all SCSI commands (and Unix read() and write() calls) so there can be a lot of output. This only occurs for scsi generic (sg) devices and block devices when the &#8216;blk_sgio=1&#8217; option is set.</p>
<dt><code>&#8211;help</code></p>
<dd>outputs usage message and exits.</p>
<dt><code>&#8211;version</code></p>
<dd>outputs version number information and exits.</p>
<dt><code>-V</code></p>
<dd>outputs version number information and exits.</dl>
<h2>Conversions</h2>
<p>One or more conversions can be given to the &quot;conv=&quot; option. If more than one is given, they should be comma separated. sg_dd does not perform the traditional dd conversions (e.g. ASCII to EBCDIC). Recently added conversions overlap somewhat with the flags so some conversions are now supported by sg_dd.</p>
<dl>
<dt>noerror</p>
<dd>this conversion is very close to &quot;iflag=coe&quot; and is treated as such. See the &quot;coe&quot; flag. Note that an error on <i>OFILE</i> will stop the copy.</p>
<dt>notrunc</p>
<dd>this conversion is accepted for compatibilty with dd and ignored since the default action of this utility is not to truncate <i>OFILE</i>.</p>
<dt>null</p>
<dd>has no affect, just a placeholder.</p>
<dt>sparse</p>
<dd>FreeBSD supports &quot;conv=sparse&quot; so the same syntax is supported in sg_dd. See &quot;sparse&quot; in the FLAGS sections for more information.</p>
<dt>sync</p>
<dd>is ignored by sg_dd. With dd it means supply zero fill (rather than skip) and is typically used like this &quot;conv=noerror,sync&quot; to have the same functionality as sg_dd&#8217;s &quot;iflag=coe&quot;.</dl>
<h2>Flags</h2>
<p>Here is a list of flags and their meanings:</p>
<dl>
<dt>append</p>
<dd>causes the O_APPEND flag to be added to the open of <i>OFILE</i>. For regular files this will lead to data appended to the end of any existing data. Cannot be used together with the <i>seek=SEEK</i> option as they conflict. The default action of this utility is to overwrite any existing data from the beginning of the file or, if <i>SEEK</i> is given, starting at block <i>SEEK</i>. Note that attempting to &#8216;append&#8217; to a device file (e.g. a disk) will usually be ignored or may cause an error to be reported.</p>
<dt>coe</p>
<dd>continue on error. Only active for sg devices and block devices that have the &#8216;sgio&#8217; flag set. &#8216;iflag=coe oflag=coe&#8217; and &#8216;coe=1&#8217; are equivalent. Use this flag twice (e.g. &#8216;iflag=coe,coe&#8217;) to have the same action as the &#8216;coe=2&#8217;. A medium, hardware or blank check error while reading will re-read blocks prior to the bad block, then try to recover the bad block, supplying zeros if that fails, and finally reread the blocks after the bad block. A medium, hardware or blank check error while writing is noted and ignored. The recovery of the bad block when reading uses the SCSI READ LONG command if &#8216;coe&#8217; given twice or more (also with the command line option &#8216;coe=2&#8217;). Further, the READ LONG will set its CORRCT bit if &#8216;coe&#8217; given thrice. SCSI disks may automatically try and remap faulty sectors (see the AWRE and ARRE in the read write error recovery mode page (the sdparm utility can access and possibly change these attributes)). Errors occurring on other files types will stop sg_dd. Error messages are sent to stderr. This flag is similar<br />
&nbsp;<wbr>o&nbsp;<wbr>&#8216;conv=noerror,sync&#8217;&nbsp;<wbr>in the <code><a href="/docs/linux/man/1-dd/">dd</a>(1)</code> utility. See note about READ LONG below.</p>
<dt>dio</p>
<dd>request the sg device node associated with this flag does direct IO. If direct IO is not available, falls back to indirect IO and notes this at completion. If direct IO is selected and /proc/scsi/sg/allow_dio has the value of 0 then a warning is issued (and indirect IO is performed).</p>
<dt>direct</p>
<dd>causes the O_DIRECT flag to be added to the open of <i>IFILE</i> and/or <i>OFILE</i>. This flag requires some memory alignment on IO. Hence user memory buffers are aligned to the page size. Has no effect on sg, normal or raw files. If &#8216;iflag=sgio&#8217; and/or &#8216;oflag=sgio&#8217; is also set then both are honoured: block devices are opened with the O_DIRECT flag and SCSI commands are issued via the SG_IO ioctl.</p>
<dt>dpo</p>
<dd>set the DPO bit (disable page out) in SCSI READ and WRITE commands. Not supported for 6 byte cdb variants of READ and WRITE. Indicates that data is unlikely to be required to stay in device (e.g. disk) cache. May speed media copy and/or cause a media copy to have less impact on other device users.</p>
<dt>dsync</p>
<dd>causes the O_SYNC flag to be added to the open of <i>IFILE</i> and/or <i>OFILE</i>. The &#8216;d&#8217; is prepended to lower confusion with the &#8216;sync=0|1&#8217; option which has another action (i.e. a synchronisation to media at the end of the transfer).</p>
<dt>excl</p>
<dd>causes the O_EXCL flag to be added to the open of <i>IFILE</i> and/or <i>OFILE</i>.</p>
<dt>flock</p>
<dd>after opening the associated file (i.e. <i>IFILE</i> and/or <i>OFILE</i>) an attempt is made to get an advisory exclusive lock with the flock() system call. The flock arguments are &quot;FLOCK_EX | FLOCK_NB&quot; which will cause the lock to be taken if available else a &quot;temporarily unavailable&quot; error is generated. An exit status of 90 is produced in the latter case and no copy is done.</p>
<dt>fua</p>
<dd>causes the FUA (force unit access) bit to be set in SCSI READ and/or WRITE commands. This only has an effect with sg devices or block devices that have the &#8216;sgio&#8217; flag set. The 6 byte variants of the SCSI READ and WRITE commands do not support the FUA bit.</p>
<dt>nocache</p>
<dd>use posix_fadvise() to advise corresponding file there is no need to fill the file buffer with recently read or written blocks.</p>
<dt>null</p>
<dd>has no affect, just a placeholder.</p>
<dt>sgio</p>
<dd>causes block devices to be accessed via the SG_IO ioctl rather than standard UNIX read() and write() commands. When the SG_IO ioctl is used the SCSI READ and WRITE commands are used directly to move data. sg devices always use the SG_IO ioctl. This flag offers finer grain control compared to the otherwise identical &#8216;blk_sgio=1&#8217; option.</p>
<dt>sparse</p>
<dd>after each <i>BS</i> * <i>BPT</i> byte segment is read from the input, it is checked for being all zeros. If so, nothing is written to the output file unless this is the last segment of the transfer. This flag is only active with the oflag option. It cannot be used when the output is not seekable (e.g. stdout). It is ignored if the output file is /dev/null . Note that this utility does not remove the <i>OFILE</i> prior to starting to write to it. Hence it may be advantageous to manually remove the <i>OFILE</i> if it is large prior to using oflag=sparse. The last segment is always written so regular files will show the same length and so programs like md5sum and sha1sum will generate the same value regardless of whether oflag=sparse is given or not. This option may be used when the <i>OFILE</i> is a raw device but is probably only useful if the device is known to contain zeros (e.g. a SCSI disk after a FORMAT command).</dl>
<h2>Retired Options</h2>
<p>Here are some retired options that are still present:</p>
<dl>
<dt>append=0 | 1</p>
<dd>when set, equivalent to &#8216;oflag=append&#8217;. When clear the action is to overwrite the existing file (if it exists); this is the default. See the &#8216;append&#8217; flag.</p>
<dt>fua=0 | 1 | 2 | 3</p>
<dd>force unit access bit. When 3, fua is set on both <i>IFILE</i> and <i>OFILE</i>; when 2, fua is set on <i>IFILE</i>;, when 1, fua is set on <i>OFILE</i>; when 0 (default), fua is cleared on both. See the &#8216;fua&#8217; flag.</dl>
<h2>Notes</h2>
<p>Block devices (e.g. /dev/sda and /dev/hda) can be given for <i>IFILE</i>. If neither &#8216;-iflag=direct&#8217;, &#8216;iflag=sgio&#8217; nor &#8216;blk_sgio=1&#8217; is given then normal block IO involving buffering and caching is performed. If only &#8216;-iflag=direct&#8217; is given then the buffering and caching is bypassed (this is applicable to both SCSI devices and ATA disks). If &#8216;iflag=sgio&#8217; or &#8216;blk_sgio=1&#8217; is given then the SG_IO ioctl is used on the given file causing SCSI commands to be sent to the device and that also bypasses most of the actions performed by the block layer (this is only applicable to SCSI devices, not ATA disks). The same applies for block devices given for <i>OFILE</i>. Various numeric arguments (e.g. <i>SKIP</i>) may include multiplicative suffixes or be given in hexadecimal. See the &quot;NUMERIC ARGUMENTS&quot; section in the <a href="/docs/linux/man/8-sg3_utils/">sg3_utils</a>(8) man page. The <i>COUNT</i>, <i>SKIP</i> and <i>SEEK</i> arguments can take 64 bit values (i.e. very big numbers). Other values are limited to what can fit in a signed 32 bit number. Data usually gets to the user space in a 2 stage process: first the SCSI adapter DMAs into kernel buffers and then the sg driver copies this data into user memory (write operations reverse this sequence). This is called &quot;indirect IO&quot; and there is a &#8216;dio&#8217; option to select &quot;direct IO&quot; which will DMA directly into user memory. Due to some issues &quot;direct IO&quot; is disabled in the sg driver and needs a configuration change to activate it. This is typically done with &#8216;echo 1 &gt; /proc/scsi/sg/allow_dio&#8217;. All informative, warning and error output is sent to stderr so that dd&#8217;s output file can be stdout and remain unpolluted. If no options are given, then the usage message is output and nothing else happens. Even if READ LONG succeeds on a &quot;bad&quot; block when &#8216;coe=2&#8217; (or &#8216;coe=3&#8217;) is given, the recovered data may not be useful. There are no guarantees that the user data will appear &quot;as is&quot; in the first 512 bytes. A raw device must be bound to a block device prior to using sg_dd. See <code><a href="/docs/linux/man/8-raw/">raw</a>(8)</code> for more information about binding raw devices. To be safe, the sg device mapping to SCSI block devices should be checked with &#8216;cat /proc/scsi/scsi&#8217;, or sg_map before use. Disk partition information can often be found with <code><a href="/docs/linux/man/8-fdisk/">fdisk</a>(8)</code> [the &quot;-ul&quot; argument is useful in this respect]. For sg devices (and block devices when blk_sgio=1 is given) this utility issues SCSI READ and WRITE (SBC) commands which are appropriate for disks and reading from CD/DVD/HD-DVD/BD drives. Those commands are not formatted correctly for tape devices so sg_dd should not be used on tape devices. If the largest block address of the requested transfer exceeds a 32 bit block number (i.e 0xffff) then a warning is issued and the sg device is accessed via SCSI READ(16) and WRITE(16) commands. The attributes of a block device (partition) are ignored when &#8216;blk_sgio=1&#8217; is used. Hence the whole device is read (rather than just the second partition) by this invocation: </p>
<pre><code>sg_dd if=/dev/sdb2 blk_sgio=1 of=t bs=512</code></pre>
<h2>Examples</h2>
<p>Looks quite similar in usage to dd: mkfifo fif</p>
<p>md5sum fif &amp;</p>
<p>sg_dd if=/dev/sg3 iflag=coe of=sg3.img oflag=sparse of2=fif bs=512 This will copy 1 million 512 byte blocks from the device associated with /dev/sg0 (which should have 512 byte blocks) to a file called t. Assuming /dev/sda and /dev/sg0 are the same device then the above is equivalent to: mkfifo fif</p>
<p>md5sum fif &amp;</p>
<p>sg_dd if=/dev/sg3 iflag=coe of=sg3.img oflag=sparse of2=fif bs=512 although dd&#8217;s speed may improve if bs was larger and count was suitably reduced. The use of the &#8216;iflag=direct&#8217; option bypasses the buffering and caching that is usually done on a block device. Using a raw device to do something similar on a ATA disk: mkfifo fif</p>
<p>md5sum fif &amp;</p>
<p>sg_dd if=/dev/sg3 iflag=coe of=sg3.img oflag=sparse of2=fif bs=512 To copy a SCSI disk partition to an ATA disk partition: mkfifo fif</p>
<p>md5sum fif &amp;</p>
<p>sg_dd if=/dev/sg3 iflag=coe of=sg3.img oflag=sparse of2=fif bs=512 This assumes a valid partition is found on the SCSI disk at the given skip block address (past the 5 GB point of that disk) and that the partition goes to the end of the SCSI disk. An explicit count is probably a safer option. The partition is copied to /dev/hda3 which is an offset into the ATA disk /dev/hda . The exact number of blocks read from /dev/sg0 are written to /dev/hda (i.e. no padding). To time a streaming read of the first 1 GB (2 ** 30 bytes) on a disk this utility could be used: mkfifo fif</p>
<p>md5sum fif &amp;</p>
<p>sg_dd if=/dev/sg3 iflag=coe of=sg3.img oflag=sparse of2=fif bs=512 On completion this will output a line like: &quot;time to transfer data was 18.779506 secs, 57.18 MB/sec&quot;. The &quot;MB/sec&quot; in this case is 1,000,000 bytes per second. The &#8216;of2=&#8217; option can be used to copy data and take a md5sum of it without needing to re-read the data: </p>
<pre><code>mkfifo fif

md5sum fif &amp;

sg_dd if=/dev/sg3 iflag=coe of=sg3.img oflag=sparse of2=fif bs=512</code></pre>
<p> This will image /dev/sg3 (e.g. an unmounted disk) and place the contents in the (sparse) file sg3.img . Without re-reading the data it will also perform a md5sum calculation on the image.</p>
<h2>Signals</h2>
<p>The signal handling has been borrowed from dd: SIGINT, SIGQUIT and SIGPIPE output the number of remaining blocks to be transferred and the records in + out counts; then they have their default action. SIGUSR1 causes the same information to be output yet the copy continues. All output caused by signals is sent to stderr.</p>
<h2>Exit Status</h2>
<p>The exit status of sg_dd is 0 when it is successful. Otherwise see the <a href="/docs/linux/man/8-sg3_utils/">sg3_utils</a>(8) man page. Since this utility works at a higher level than individual commands, and there are &#8216;coe&#8217; and &#8216;retries&#8217; flags, individual SCSI command failures do not necessary cause the process to exit. </p>
<p> An additional exit status of 90 is generated if the flock flag is given and some other process holds the advisory exclusive lock.</p>
<h2>Authors</h2>
<p>Written by Douglas Gilbert and Peter Allworth.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;dgilbert at interlog dot com&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2000-2013 Douglas Gilbert<br />
 This software is distributed under the GPL version 2. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p>There is a web page discussing sg_dd at <a rel="nofollow" href="http://sg.danny.cz/sg/sg_dd.html">http://sg.danny.cz/sg/sg_dd.html</a> A POSIX threads version of this utility called <code>sgp_dd</code> is in the sg3_utils package. Another version from that package is called <code>sgm_dd</code> and it uses memory mapped IO to speed transfers from sg devices. The lmbench package contains <code>lmdd</code> which is also interesting. For moving data to and from tapes see <code>dt</code> which is found at <a rel="nofollow" href="http://www.scsifaq.org/RMiller_Tools/index.html">http://www.scsifaq.org/RMiller_Tools/index.html</a> To change mode parameters that effect a SCSI device&#8217;s caching and error recovery see <code>sdparm(sdparm)</code> To verify the data on the media or to verify it against some other copy of the data see <code>sg_verify(sg3_utils)</code> See also <code><a href="/docs/linux/man/8-raw/">raw</a>(8), <a href="/docs/linux/man/1-dd/">dd</a>(1), ddrescue(GNU), ddpt</code> </p>
