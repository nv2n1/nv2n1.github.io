---
title: "blkparse(1)"
name: "blkparse"
section: "1"
letter: "b"
url: "/docs/linux/man/1-blkparse/"
description: "blkparse – produce formatted output of event streams of block devices"
---

<h2 class="name">NAME</h2>
<p> blkparse &#8211; produce formatted output of event streams of block devices </p>
<h2>SYNOPSIS</h2>
<p> <code>blkparse [ </code><i>options</i> ] </p>
<h2>DESCRIPTION</h2>
<p> The <i>blkparse</i> utility will attempt to combine streams of events for various devices on various CPUs, and produce a formatted output of the event information. Specifically, it will take the (machine-readable) output of the <i>blktrace</i> utility and convert it to a nicely formatted and human-readable form. </p>
<p> As with <i>blktrace</i>, some details concerning <i>blkparse</i> will help in understanding the command line options presented below. </p>
<dl>
<dt>&#8211;</p>
<dd> By default, <i>blkparse</i> expects to run in a post-processing mode; one where the trace events have been saved by a previous run of blktrace, and blkparse is combining event streams and dumping formatted data. </p>
<p> blkparse may be run in a live manner concurrently with blktrace by specifying <code>-i &#8211;</code> to blkparse, and combining it with the live option for blktrace. An example would be: </p>
<p>%&nbsp;<wbr>blktrace -d&nbsp;<wbr>/dev/sda -o &#8211; | blkparse -i &#8211; </p>
<dt>&#8211;</p>
<dd> You can set how many blkparse batches event reads via the <code>-b</code> option, the default is to handle events in batches of 512. </p>
<dt>&#8211;</p>
<dd> If you have saved event traces in blktrace with different output names (via the <code>-o</code> option to blktrace), you must specify the same input name via the <code>-i</code> option. </p>
<dt>&#8211;</p>
<dd> The format of the output data can be controlled via the <code>-f</code> or <code>-F</code> options &#8212; see OUTPUT DESCRIPTION AND FORMATTING for details. </p>
</dl>
<p> By default, blkparse sends formatted data to standard output. This may be changed via the <code>-o</code> option, or text output can be disabled via the <code>-O</code> option. A merged binary stream can be produced using the <code>-d</code> option. </p>
<h2>OPTIONS</h2>
<p> -A <i>hex-mask</i><br />
 &#8211;set-mask=<i>hex-mask</i></p>
<dl>
<dt>
<dd> Set filter mask to <i>hex-mask</i>, see blktrace (8) for masks</dl>
<p> -a <i>mask</i><br />
 &#8211;act-mask=<i>mask</i></p>
<dl>
<dt>
<dd> Add <i>mask</i> to current filter, see blktrace (8) for masks</dl>
<p> -D <i>dir</i><br />
 &#8211;input-directory=<i>dir</i></p>
<dl>
<dt>
<dd> Prepend <i>dir</i> to input file names</dl>
<p> -b <i>batch</i><br />
 &#8211;batch={batch}</p>
<dl>
<dt>
<dd> Standard input read batching</dl>
<p> -i <i>file</i><br />
 &#8211;input=<i>file</i></p>
<dl>
<dt>
<dd> Specifies base name for input files &#8212; default is <i>device</i>.blktrace.<i>cpu</i>. </p>
<p> As noted above, specifying <code>-i &#8211;</code> runs in live mode with blktrace (reading data from standard in).</dl>
<p> -F <i>typ,fmt</i><br />
 &#8211;format=<i>typ,fmt</i><br />
 -f <i>fmt</i><br />
 &#8211;format-spec=<i>fmt</i></p>
<dl>
<dt>
<dd> Sets output format (See OUTPUT DESCRIPTION AND FORMATTING for details.) </p>
<p> The -f form specifies a format for all events </p>
<p> The -F form allows one to specify a format for a specific event type. The single-character <i>typ</i> field is one of the action specifiers described in ACTION IDENTIFIERS.</dl>
<p> -M<br />
 &#8211;no-msgs</p>
<dl>
<dt>
<dd> When -d is specified, this will stop messages from being output to the file. (Can seriously reduce the size of the resultant file when using the CFQ I/O scheduler.)</dl>
<p> -h<br />
 &#8211;hash-by-name</p>
<dl>
<dt>
<dd> Hash processes by name, not by PID</dl>
<p> -o <i>file</i><br />
 &#8211;output=<i>file</i></p>
<dl>
<dt>
<dd> Output file</dl>
<p> -O<br />
 &#8211;no-text-output</p>
<dl>
<dt>
<dd> Do <i>not</i> produce text output, used for binary (<code>-d</code>) only</dl>
<p> -d <i>file</i><br />
 &#8211;dump-binary=<i>file</i></p>
<dl>
<dt>
<dd> Binary output file</dl>
<p> -q<br />
 &#8211;quiet</p>
<dl>
<dt>
<dd> Quiet mode</dl>
<p> -s<br />
 &#8211;per-program-stats</p>
<dl>
<dt>
<dd> Displays data sorted by program</dl>
<p> -t<br />
 &#8211;track-ios</p>
<dl>
<dt>
<dd> Display time deltas per IO</dl>
<p> -w <i>span</i><br />
 &#8211;stopwatch=<i>span</i></p>
<dl>
<dt>
<dd> Display traces for the <i>span</i> specified &#8212; where span can be:<br />
 <i>end-time</i> &#8212; Display traces from time 0 through <i>end-time</i> (in ns)<br />
 or<br />
 <i>start:end-time</i> &#8212; Display traces from time <i>start</i> through end-time (in ns).</dl>
<p> -v<br />
 &#8211;verbose</p>
<dl>
<dt>
<dd> More verbose marginal on marginal errors</dl>
<p> -V<br />
 &#8211;version</p>
<dl>
<dt>
<dd> Display version</dl>
<h2>TRACE ACTIONS</h2>
<p> The following trace actions are recognised: </p>
<dl>
<dt> <code>C &#8212; complete</code></p>
<dd>A previously issued request has been completed. The output will detail the sector and size of that request, as well as the success or failure of it. </p>
<dt> <code>D &#8212; issued</code></p>
<dd>A request that previously resided on the block layer queue or in the i/o scheduler has been sent to the driver. </p>
<dt> <code>I &#8212; inserted</code></p>
<dd>A request is being sent to the i/o scheduler for addition to the internal queue and later service by the driver. The request is fully formed at this time. </p>
<dt> <code>Q &#8212; queued</code></p>
<dd>This notes intent to queue i/o at the given location. No real requests exists yet. </p>
<dt> <code>B &#8212; bounced</code></p>
<dd>The data pages attached to this <i>bio</i> are not reachable by the hardware and must be bounced to a lower memory location. This causes a big slowdown in i/o performance, since the data must be copied to/from kernel buffers. Usually this can be fixed with using better hardware &#8212; either a better i/o controller, or a platform with an IOMMU. </p>
<dt> <code>M &#8212; back merge</code></p>
<dd>A previously inserted request exists that ends on the boundary of where this i/o begins, so the i/o scheduler can merge them together. </p>
<dt> <code>F &#8212; front merge</code></p>
<dd>Same as the back merge, except this i/o ends where a previously inserted requests starts. </p>
<dt> <code>M &#8211;front or back merge</code></p>
<dd>One of the above </p>
<dt> <code>M &#8212; front or back merge</code></p>
<dd>One of the above. </p>
<dt> <code>G &#8212; get request</code></p>
<dd>To send any type of request to a block device, a <i>struct request</i> container must be allocated first. </p>
<dt> <code>S &#8212; sleep</code></p>
<dd>No available request structures were available, so the issuer has to wait for one to be freed. </p>
<dt> <code>P &#8212; plug</code></p>
<dd>When i/o is queued to a previously empty block device queue, Linux will plug the queue in anticipation of future ios being added before this data is needed. </p>
<dt> <code>U &#8212; unplug</code></p>
<dd>Some request data already queued in the device, start sending requests to the driver. This may happen automatically if a timeout period has passed (see next entry) or if a number of requests have been added to the queue. </p>
<dt> <code>T &#8212; unplug due to timer</code></p>
<dd>If nobody requests the i/o that was queued after plugging the queue, Linux will automatically unplug it after a defined period has passed. </p>
<dt> <code>X &#8212; split</code></p>
<dd>On raid or device mapper setups, an incoming i/o may straddle a device or internal zone and needs to be chopped up into smaller pieces for service. This may indicate a performance problem due to a bad setup of that raid/dm device, but may also just be part of normal boundary conditions. dm is notably bad at this and will clone lots of i/o. </p>
<dt> <code>A &#8212; remap</code></p>
<dd>For stacked devices, incoming i/o is remapped to device below it in the i/o stack. The remap action details what exactly is being remapped to what. </p>
</dl>
<h2>OUTPUT DESCRIPTION AND FORMATTING</h2>
<p> The output from blkparse can be tailored for specific use &#8212; in particular, to ease parsing of output, and/or limit output fields to those the user wants to see. The data for fields which can be output include: </p>
<dl>
<dt><code>a</code></p>
<dd> Action, a (small) string (1 or 2 characters) &#8212; see table below for more details </p>
<dt><code>c</code></p>
<dd> CPU id </p>
<dt><code>C</code></p>
<dd> Command </p>
<dt><code>d</code></p>
<dd> RWBS field, a (small) string (1-3 characters) &#8212; see section below for more details </p>
<dt><code>D</code></p>
<dd> 7-character string containing the major and minor numbers of the event&#8217;s device (separated by a comma). </p>
<dt><code>e</code></p>
<dd> Error value </p>
<dt><code>m</code></p>
<dd> Minor number of event&#8217;s device. </p>
<dt><code>M</code></p>
<dd> Major number of event&#8217;s device. </p>
<dt><code>n</code></p>
<dd> Number of blocks </p>
<dt><code>N</code></p>
<dd> Number of bytes </p>
<dt><code>p</code></p>
<dd> Process ID </p>
<dt><code>P</code></p>
<dd> Display packet data &#8212; series of hexadecimal values </p>
<dt><code>s</code></p>
<dd> Sequence numbers </p>
<dt><code>S</code></p>
<dd> Sector number </p>
<dt><code>t</code></p>
<dd> Time stamp (nanoseconds) </p>
<dt><code>T</code></p>
<dd> Time stamp (seconds) </p>
<dt><code>u</code></p>
<dd> Elapsed value in microseconds (<i>-t</i> command line option) </p>
<dt><code>U</code></p>
<dd> Payload unsigned integer </p>
</dl>
<p> Note that the user can optionally specify field display width, and optionally a left-aligned specifier. These precede field specifiers, with a &#8216;%&#8217; character, followed by the optional left-alignment specifier (-) followed by the width (a decimal number) and then the field. </p>
<p> Thus, to specify the command in a 12-character field that is left aligned: </p>
<p>&nbsp;<wbr>-f&nbsp;<wbr>&quot;%-12C&quot; </p>
<h2>ACTION IDENTIFIERS</h2>
<p> The following table shows the various actions which may be output: </p>
<dl>
<dt>A</p>
<dd> IO was remapped to a different device </p>
<dt>B</p>
<dd> IO bounced </p>
<dt>C</p>
<dd> IO completion </p>
<dt>D</p>
<dd> IO issued to driver </p>
<dt>F</p>
<dd> IO front merged with request on queue </p>
<dt>G</p>
<dd> Get request </p>
<dt>I</p>
<dd> IO inserted onto request queue </p>
<dt>M</p>
<dd> IO back merged with request on queue </p>
<dt>P</p>
<dd> Plug request </p>
<dt>Q</p>
<dd> IO handled by request queue code </p>
<dt>S</p>
<dd> Sleep request </p>
<dt>T</p>
<dd> Unplug due to timeout </p>
<dt>U</p>
<dd> Unplug request </p>
<dt>X</p>
<dd> Split </p>
</dl>
<h2>RWBS DESCRIPTION</h2>
<p> This is a small string containing at least one character (&#8216;R&#8217; for read, &#8216;W&#8217; for write, or &#8216;D&#8217; for block discard operation), and optionally either a &#8216;B&#8217; (for barrier operations) or &#8216;S&#8217; (for synchronous operations). </p>
<h2>DEFAULT OUTPUT</h2>
<p> The standard header (or initial fields displayed) include: </p>
<p>&nbsp;<wbr>&quot;%D&nbsp;<wbr>%2c&nbsp;<wbr>%8s&nbsp;<wbr>%5T.%9t&nbsp;<wbr>%5p&nbsp;<wbr>%2a&nbsp;<wbr>%3d&quot; </p>
<p> Breaking this down: </p>
<dl>
<dt><code>%D</code></p>
<dd> Displays the event&#8217;s device major/minor as: %3d,%-3d. </p>
<dt><code>%2c</code></p>
<dd> CPU ID (2-character field). </p>
<dt><code>%8s</code></p>
<dd> Sequence number </p>
<dt><code>%5T.%9t</code></p>
<dd> 5-character field for the seconds portion of the time stamp and a 9-character field for the nanoseconds in the time stamp. </p>
<dt><code>%5p</code></p>
<dd> 5-character field for the process ID. </p>
<dt><code>%2a</code></p>
<dd> 2-character field for one of the actions. </p>
<dt><code>%3d</code></p>
<dd> 3-character field for the RWBS data. </p>
<p> Seeing this in action: </p>
<p>&nbsp;<wbr>8,0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>3&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0.000000000&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>697&nbsp;<wbr>&nbsp;<wbr>G&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>W 223490&nbsp;<wbr>+&nbsp;<wbr>8&nbsp;<wbr>[kjournald] </p>
<p> The header is the data in this line up to the 223490 (starting block). The default output for all event types includes this header. </p>
</dl>
<h2>DEFAULT OUTPUT PER ACTION</h2>
<p> <code>C &#8212; complete</code></p>
<dl>
<dt>
<dd> If a payload is present, this is presented between parenthesis following the header, followed by the error value. </p>
<p> If no payload is present, the sector and number of blocks are presented (with an intervening plus (+) character). If the <code>-t</code> option was specified, then the elapsed time is presented. In either case, it is followed by the error value for the completion.</dl>
<p> <code>B &#8212; bounced</code><br />
 <code>D &#8212; issued</code><br />
 <code>I &#8212; inserted</code><br />
 <code>Q &#8212; queued</code></p>
<dl>
<dt>
<dd> If a payload is present, the number of payload bytes is output, followed by the payload in hexadecimal between parenthesis. </p>
<p> If no payload is present, the sector and number of blocks are presented (with an intervening plus (+) character). If the <code>-t</code> option was specified, then the elapsed time is presented (in parenthesis). In either case, it is followed by the command associated with the event (surrounded by square brackets).</dl>
<p> <code>F &#8212; front merge</code><br />
 <code>G &#8212; get request</code><br />
 <code>M &#8212; back merge</code><br />
 <code>S &#8212; sleep</code></p>
<dl>
<dt>
<dd> The starting sector and number of blocks is output (with an intervening plus (+) character), followed by the command associated with the event (surrounded by square brackets).</dl>
<p> <code>P &#8212; plug</code></p>
<dl>
<dt>
<dd> The command associated with the event (surrounded by square brackets) is output.</dl>
<p> <code>U &#8212; unplug</code><br />
 <code>T &#8212; unplug due to timer</code></p>
<dl>
<dt>
<dd> The command associated with the event (surrounded by square brackets) is output, followed by the number of requests outstanding.</dl>
<p> <code>X &#8212; split</code></p>
<dl>
<dt>
<dd> The original starting sector followed by the new sector (separated by a slash (/) is output, followed by the command associated with the event (surrounded by square brackets).</dl>
<p> <code>A &#8212; remap</code></p>
<dl>
<dt>
<dd> Sector and length is output, along with the original device and sector offset.</dl>
<h2>EXAMPLES</h2>
<p> To trace the i/o on the device <i>/dev/hda</i><code> and parse the output to human readable form, use the following command: </p>
<p>&nbsp;<wbr>%&nbsp;<wbr>blktrace -d&nbsp;<wbr>/dev/sda -o &#8211; | blkparse -i &#8211; </p>
<p> (see </code><i>blktrace</i> (8) for more information). This same behaviour can be achieve with the convenience script <i>btrace</i>. The command </p>
<p>&nbsp;<wbr>%&nbsp;<wbr>btrace&nbsp;<wbr>/dev/sda </p>
<p> has exactly the same effect as the previous command. See <i>btrace</i> (8) for more information. </p>
<p> To trace the i/o on a device and save the output for later processing with <i>blkparse</i>, use <i>blktrace</i> like this: </p>
<p>&nbsp;<wbr>%&nbsp;<wbr>blktrace&nbsp;<wbr>/dev/sda&nbsp;<wbr>/dev/sdb </p>
<p> This will trace i/o on the devices <i>/dev/sda</i> and <i>/dev/sdb</i> and save the recorded information in the files <i>sda</i> and <i>sdb</i> in the current directory, for the two different devices, respectively. This trace information can later be parsed by the <i>blkparse</i> utility: </p>
<p>&nbsp;<wbr>%&nbsp;<wbr>blkparse sda sdb </p>
<p> which will output the previously recorded tracing information in human readable form to stdout. </p>
<h2>AUTHORS</h2>
<p> <i>blkparse</i> was written by Jens Axboe, Alan D. Brunelle and Nathan Scott. This man page was created from the <i>blktrace</i> documentation by Bas Zoetekouw. </p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;linux-btrace [at] vger.kernel.org&gt; </p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2006 Jens Axboe, Alan D. Brunelle and Nathan Scott.<br />
 This is free software. You may redistribute copies of it under the terms of the GNU General Public License &lt;<a rel="nofollow" href="http://www.gnu.org/licenses/gpl.html">http://www.gnu.org/licenses/gpl.html</a>&gt;. There is NO WARRANTY, to the extent permitted by law.<br />
 This manual page was created for Debian by Bas Zoetekouw. It was derived from the documentation provided by the authors and it may be used, distributed and modified under the terms of the GNU General Public License, version 2.<br />
 On Debian systems, the text of the GNU General Public License can be found in /usr/share/common-licenses/GPL-2. </p>
<h2>SEE ALSO</h2>
<p> btrace (8), blktrace (8), verify_blkparse (1), blkrawverify (1), btt (1) </p>
<h2>Index</h2>
