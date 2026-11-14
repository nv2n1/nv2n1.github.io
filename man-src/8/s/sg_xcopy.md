---
title: "sg_xcopy(8)"
name: "sg_xcopy"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sg_xcopy/"
description: "sg_xcopy – copy data to and from files and devices using SCSI EXTENDED COPY (XCOPY)"
---

<p>sg_xcopy &#8211; copy data to and from files and devices using SCSI EXTENDED COPY (XCOPY)</p>
<h2>Synopsis</h2>
<p><code>sg_xcopy</code> [<i>bs=BS</i>] [<i>conv=CONV</i>] [<i>count=COUNT</i>] [<i>ibs=BS</i>] [<i>if=IFILE</i>] [<i>iflag=FLAGS</i>] [<i>obs=BS</i>] [<i>of=OFILE</i>] [<i>oflag=FLAGS</i>] [<i>seek=SEEK</i>] [<i>skip=SKIP</i>] [<i>&#8211;help</i>] [<i>&#8211;version</i>] </p>
<p> [<i>bpt=BPT</i>] [<i>cat=</i>0|1] [<i>dc=</i>0|1] [<i>id_usage=</i>{hold|discard|disable}] [<i>list_id=ID</i>] [<i>prio=PRIO</i>] [<i>time=</i>0|1] [<i>verbose=VERB</i>] [<i>&#8211;on_dst|&#8211;on_src</i>] [<i>&#8211;verbose</i>]</p>
<h2>Description</h2>
<p>Copy data to and from any files. Specialized for &quot;files&quot; that are Linux SCSI devices that support the SCSI EXTENDED COPY (XCOPY) command. </p>
<p> During the draft stages of SPC-4 the T10 committee has expanded the XCOPY command so that it now has two variants: &quot;LID1&quot; (for a List Identifier length of 1 byte) and &quot;LID4&quot; (for a List Identifier length of 4 bytes). This utility supports the older, LID1 variant which is also found in SPC-3 and earlier. While the LID1 variant in SPC-4 is command level (binary) compatible with XCOPY as defined in SPC-3, some of the command naming has changed. This utility uses the older, SPC-3 XCOPY names. </p>
<p> This utility has similar syntax and semantics to <code><a href="/docs/linux/man/1-dd/">dd</a>(1)</code> but with no &quot;conversions&quot; is supported. </p>
<p> The first group in the synopsis above are &quot;standard&quot; Unix <code><a href="/docs/linux/man/1-dd/">dd</a>(1)</code> operands. The second group are extra options added by this utility. Both groups are defined below in combined, alphabetical order. </p>
<p> By default the XCOPY command is sent to <i>IFILE</i>. This can be changed with the <i>&#8211;on_dst</i> option which causes the XCOPY command to be sent to <i>OFILE</i> instead.</p>
<h2>Options</h2>
<dl>
<dt><code>bpt</code>=<i>BPT</i></p>
<dd>each IO transaction will be made using <i>BPT</i> blocks (or less if near the end of the copy). Default is 128 for block sizes less that 2048 bytes, otherwise the default is 32. So for bs=512 the reads and writes will each convey 64 KiB of data by default (less if near the end of the transfer or memory restrictions). When cd/dvd drives are accessed, the block size is typically 2048 bytes and bpt defaults to 32 which again implies 64 KiB transfers.</p>
<dt><code>bs</code>=<i>BS</i></p>
<dd>where <i>BS</i> <code>must</code> be the block size of the physical device (if either the input or output files are accessed via SCSI commands). Note that this differs from <code><a href="/docs/linux/man/1-dd/">dd</a>(1)</code> which permits <i>BS</i> to be an integral multiple. Defaults to the device block size.</p>
<dt><code>cat</code>={0|1}</p>
<dd>sets the SCSI EXTENDED COPY command segment descriptor CAT bit to 0 or 1 (default: 0). The CAT bit (in conjunction with the PAD bit) controls the handling of residual data. See section <code>HANDLING OF RESIDUAL DATA</code> for details.</p>
<dt><code>dc</code>={0|1}</p>
<dd>sets the SCSI EXTENDED COPY command segment descriptor DC bit to 0 or 1 (default: 0). The DC bit controls whether <i>COUNT</i> refers to the source (<i>dc=0</i>) or the target (<i>dc=1</i>) descriptor.</p>
<dt><code>conv</code>=<code>CONV</code></p>
<dd>all <code>CONV</code> arguments are ignored.</p>
<dt><code>count</code>=<i>COUNT</i></p>
<dd>copy <i>COUNT</i> blocks from <i>IFILE</i> to <i>OFILE</i>. Default is the minimum (<i>IFILE</i> if <i>dc=0</i> or <i>OFILE</i> if <i>dc=1</i>) number of blocks that SCSI devices report from SCSI READ CAPACITY commands or that block devices (or their partitions) report. Normal files are not probed for their size. If <i>skip=SKIP</i> or <i>skip=SEEK</i> are given and the count is derived (i.e. not explicitly given) then the derived count is scaled back so that the copy will not overrun the device. If the file name is a block device partition and <i>COUNT</i> is not given then the size of the partition rather than the size of the whole device is used. If <i>COUNT</i> is not given (or <i>count=-1</i>) and cannot be derived then an error message is issued and no copy takes place.</p>
<dt><code>ibs</code>=<i>BS</i></p>
<dd>if given must be the same as <i>BS</i> given to &#8216;bs=&#8217; option.</p>
<dt><code>id_usage</code>={hold|discard|disable}</p>
<dd>sets the SCSI EXTENDED COPY command parameter list field called LIST ID USAGE to 0 if the argument is &#8216;hold&#8217;, to 2 if the argument is &#8216;discard&#8217;, or to &#8216;3&#8217; if the argument is &#8216;disable&#8217;.</p>
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
<dt><code>list_id</code>=<i>ID</i></p>
<dd>sets the SCSI EXTENDED COPY command parameter list field called LIST IDENTIFIER to <i>ID</i>. <i>ID</i> should be a value between 0 and 255 (inclusive) and the default value is 1.</p>
<dt><code>prio</code>=<i>PRIO</i></p>
<dd>sets the SCSI EXTENDED COPY command parameter list field called PRIORITY to <i>PRIO</i>. The default value is 1.</p>
<dt><code>seek</code>=<i>SEEK</i></p>
<dd>start writing <i>SEEK</i> bs-sized blocks from the start of <i>OFILE</i>. Default is block 0 (i.e. start of file).</p>
<dt><code>skip</code>=<i>SKIP</i></p>
<dd>start reading <i>SKIP</i> bs-sized blocks from the start of <i>IFILE</i>. Default is block 0 (i.e. start of file).</p>
<dt><code>time</code>={0|1}</p>
<dd>when 1, times transfer and does throughput calculation, outputting the results (to stderr) at completion. When 0 (default) doesn&#8217;t perform timing.</p>
<dt><code>verbose</code>=<i>VERB</i></p>
<dd>as <i>VERB</i> increases so does the amount of debug output sent to stderr. Default value is zero which yields the minimum amount of debug output. A value of 1 reports extra information that is not repetitive. A value 2 reports cdbs and responses for SCSI commands that are not repetitive (i.e. other that READ and WRITE). Error processing is not considered repetitive. Values of 3 and 4 yield output for all SCSI commands (and Unix read() and write() calls) so there can be a lot of output.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>outputs usage message and exits.</p>
<dt><code>&#8211;on_dst</code></p>
<dd>send the XCOPY command to the output file/device.</p>
<dt><code>&#8211;on_src</code></p>
<dd>send the XCOPY command to the input file/device. This is the default when this option and <i>&#8211;on_dst</i> are not given.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>equivalent to <i>verbose=1</i>. When used twice, equivalent to <i>verbose=2</i>, etc.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>outputs version number information and exits.</dl>
<h2>Flags</h2>
<p>Here is a list of flags and their meanings:</p>
<dl>
<dt>append</p>
<dd>causes the O_APPEND flag to be added to the open of <i>OFILE</i>. For regular files this will lead to data appended to the end of any existing data. Cannot be used together with the <i>seek=SEEK</i> option as they conflict. The default action of this utility is to overwrite any existing data from the beginning of the file or, if <i>SEEK</i> is given, starting at block <i>SEEK</i>. Note that attempting to &#8216;append&#8217; to a device file (e.g. a disk) will usually be ignored or may cause an error to be reported.</p>
<dt>excl</p>
<dd>causes the O_EXCL flag to be added to the open of <i>IFILE</i> and/or <i>OFILE</i>.</p>
<dt>flock</p>
<dd>after opening the associated file (i.e. <i>IFILE</i> and/or <i>OFILE</i>) an attempt is made to get an advisory exclusive lock with the flock() system call. The flock arguments are &quot;FLOCK_EX | FLOCK_NB&quot; which will cause the lock to be taken if available else a &quot;temporarily unavailable&quot; error is generated. An exit status of 90 is produced in the latter case and no copy is done.</p>
<dt>null</p>
<dd>has no affect, just a placeholder.</p>
<dt>pad</p>
<dd>sets the SCSI EXTENDED COPY command segment descriptor PAD bit. The PAD bit (in conjunction with the CAT bit) controls the handling of residual data.(See section <code>HANDLING OF RESIDUAL DATA</code> for details.</p>
<dt>xcopy</p>
<dd>has no affect; for compatibility with ddpt.</dl>
<h2>Handling Of Residual Data</h2>
<p>The <i>pad</i> and <i>cat</i> bits control the handling of residual data. As the data can be specified either in terms of source or target block size and both might have different block sizes residual data is likely to happen in these cases. If both block sizes are identical these bits have no effect as residual data will not occur. </p>
<p> If none of these bits are set, the EXTENDED COPY command will be aborted with additional sense &#8216;UNEXPECTED INEXACT SEGMENT&#8217;. </p>
<p> If only the <i>cat</i> bit is set the residual data will be retained and made available for subsequent segment descriptors. Residual data will be discarded for the last segment descriptor. </p>
<p> If the <i>pad</i> bit is set for the source descriptor only, any residual data for both source or destination will be discarded. </p>
<p> If the <i>pad</i> bit is set for the target descriptor only any residual source data will be handled as if the <i>cat</i> bit is set, but any residual destination data will be padded to make a whole block transfer. </p>
<p> If the <i>pad</i> bit is set for both source and target any residual source data will be discarded, and any residual destination data will be padded.</p>
<h2>Retired Options</h2>
<p>Here are some retired options that are still present:</p>
<dl>
<dt>append=0 | 1</p>
<dd>when set, equivalent to &#8216;oflag=append&#8217;. When clear the action is to overwrite the existing file (if it exists); this is the default. See the &#8216;append&#8217; flag.</dl>
<h2>Notes</h2>
<p>Various numeric arguments (e.g. <i>SKIP</i>) may include multiplicative suffixes or be given in hexadecimal. See the &quot;NUMERIC ARGUMENTS&quot; section in the <a href="/docs/linux/man/8-sg3_utils/">sg3_utils</a>(8) man page. </p>
<p> The <i>COUNT</i>, <i>SKIP</i> and <i>SEEK</i> arguments can take 64 bit values (i.e. very big numbers). Other values are limited to what can fit in a signed 32 bit number. </p>
<p> All informative, warning and error output is sent to stderr so that dd&#8217;s output file can be stdout and remain unpolluted. If no options are given, then the usage message is output and nothing else happens. </p>
<p> If a device supports xcopy operations then it should set the 3PC field (3PC stands for Third Party Copy) in its standard INQUIRY response. This utility will attempt a xcopy operation irrespective of the value in the 3PC field but if it is zero (cleared) one would expect the xcopy operation to fail. </p>
<p> The status of the SCSI EXTENDED COPY command can be queried with <code>sg_copy_results(sg3_utils)</code> </p>
<p> Currently only block-to-block transfers are implemented; <i>IFILE</i> and <i>OFILE</i> must refer to a SCSI block device. </p>
<p> No account is taken of partitions so, for example, /dev/sbc2, /dev/sdc, /dev/sg2, and /dev/bsg/3:0:0:1 would all refer to the same thing: the whole logical unit (i.e. the whole disk) starting at LBA 0. So any partition indication (e.g. /dev/sdc2) is ignored. The user should set <i>SKIP</i>, <i>SEEK</i> and <i>COUNT</i> with information obtained from a command like &#8216;fdisk -l -u /dev/sdc&#8217; to account for partitions. </p>
<p> XCOPY (LID1) capability has been added to the ddpt utility which is in a package of the same name. The ddpt utility will run on other OSes (e.g. FreeBSD and Windows) while sg_xcopy only runs on Linux. Also ddpt permits the arguments to <i>ibs=</i> and <i>ibs=</i> to be different.</p>
<h2>Examples</h2>
<p>Copy 2M of data from the start of one device to another: </p>
<p> # sg_xcopy if=/dev/sdo of=/dev/sdp count=2048 list_id=2 dc=1<br />
 sg_xcopy: if=/dev/sdo skip=0 of=/dev/sdp seek=0 count=1024<br />
 Start of loop, count=1024, bpt=65535, lba_in=0, lba_out=0<br />
 sg_xcopy: 1024 blocks, 1 command </p>
<p> Check the status of the EXTENDED COPY command: </p>
<p> # sg_copy_results &#8211;status &#8211;list_id=2 /dev/sdp<br />
 Receive copy results (copy status):<br />
&nbsp;<wbr>Held data discarded: Yes<br />
&nbsp;<wbr>Copy manager status: Operation completed without errors<br />
&nbsp;<wbr>Segments processed: 1<br />
&nbsp;<wbr>Transfer count units: 0<br />
&nbsp;<wbr>Transfer count: 0</p>
<h2>Signals</h2>
<p>The signal handling has been borrowed from dd: SIGINT, SIGQUIT and SIGPIPE output the number of remaining blocks to be transferred and the records in + out counts; then they have their default action. SIGUSR1 causes the same information to be output yet the copy continues. All output caused by signals is sent to stderr.</p>
<h2>Exit Status</h2>
<p>The exit status of sg_xcopy is 0 when it is successful. Otherwise see the <a href="/docs/linux/man/8-sg3_utils/">sg3_utils</a>(8) man page. </p>
<p> An additional exit status of 90 is generated if the flock flag is given and some other process holds the advisory exclusive lock.</p>
<h2>Authors</h2>
<p>Written by Hannes Reinecke and Douglas Gilbert.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;dgilbert at interlog dot com&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2000-2013 Hannes Reinecke and Douglas Gilbert<br />
 This software is distributed under the GPL version 2. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p>There is a web page discussing sg_dd at <a rel="nofollow" href="http://sg.danny.cz/sg/sg_dd.html">http://sg.danny.cz/sg/sg_dd.html</a> A POSIX threads version of this utility called <code>sgp_dd</code> is in the sg3_utils package. Another version from that package is called <code>sgm_dd</code> and it uses memory mapped IO to speed transfers from sg devices. The lmbench package contains <code>lmdd</code> which is also interesting. For moving data to and from tapes see <code>dt</code> which is found at <a rel="nofollow" href="http://www.scsifaq.org/RMiller_Tools/index.html">http://www.scsifaq.org/RMiller_Tools/index.html</a> To change mode parameters that effect a SCSI device&#8217;s caching and error recovery see <code>sdparm(sdparm)</code> See also <code><a href="/docs/linux/man/1-dd/">dd</a>(1), sg_copy_results(sg3_utils), ddrescue(GNU), ddpt(ddpt)</code> </p>
