---
title: "blktrace(8)"
name: "blktrace"
section: "8"
letter: "b"
url: "/docs/linux/man/8-blktrace/"
description: "blktrace – generate traces of the i/o traffic on block devices"
---

<p>blktrace &#8211; generate traces of the i/o traffic on block devices </p>
<h2>Synopsis</h2>
<p><code>blktrace -d </code><i>dev</i> [ -r <i>debugfs_path</i> ] [ -o <i>output</i> ] [ -w <i>time</i> ] [ -a <i>action</i> ] [ -A <i>action_mask</i> ] [ -v ] </p>
<h2>Description</h2>
<p>blktrace is a block layer IO tracing mechanism which provides detailed information about request queue operations up to user space. There are three major components: a kernel component, a utility to record the i/o trace information for the kernel to user space, and utilities to analyse and view the trace information. This man page describes blktrace, which records the i/o event trace information for a specific block device to a file. The <code>blktrace</code> utility extracts event traces from the kernel (via the relaying through the debug file system). Some background details concerning the run-time behaviour of blktrace will help to understand some of the more arcane command line options:</p>
<dl>
<dt>&#8211;</p>
<dd>blktrace receives data from the kernel in buffers passed up through the debug file system (relay). Each device being traced has a file created in the mounted directory for the debugfs, which defaults to <i>/sys/kernel/debug</i> &#8212; this can be overridden with the <code>-r</code> command line argument.</p>
<dt>&#8211;</p>
<dd>blktrace defaults to collecting all events that can be traced. To limit the events being captured, you can specify one or more filter masks via the <code>-a</code> option. Alternatively, one may specify the entire mask utilising a hexadecimal value that is version-specific. (Requires understanding of the internal representation of the filter mask.)</p>
<dt>&#8211;</p>
<dd>As noted above, the events are passed up via a series of buffers stored into debugfs files. The size and number of buffers can be specified via the <code>-b</code> and <code>-n</code> arguments respectively.</p>
<dt>&#8211;</p>
<dd>blktrace stores the extracted data into files stored in the local directory. The format of the file names is (by default) <code>device</code>.<code>blktrace</code>.<code>cpu</code>, where <code>device</code> is the base device name (e.g, if we are tracing /dev/sda, the base device name would be <code>sda</code>); and <code>cpu</code> identifies a CPU for the event stream. The <code>device</code> portion of the event file name can be changed via the <code>-o</code> option.</p>
<dt>&#8211;</p>
<dd>blktrace may also be run concurrently with blkparse to produce <code>live</code> output &#8212; to do this specify <code>-o &#8211;</code> for blktrace.</p>
<dt>&#8211;</p>
<dd>The default behaviour for blktrace is to run forever until explicitly killed by the user (via a control-C, or sending SIGINT signal to the process via invocation the kill (1) utility). Also you can specify a run-time duration for blktrace via the <code>-w</code> option &#8212; then blktrace will run for the specified number of seconds, and then halt. </p>
<h2>Options</h2>
<p>-A <i>hex-mask</i><br />
 &#8211;set-mask=<i>hex-mask</i></p>
<dl>
<dd>Set filter mask to <i>hex-mask</i> (see below for masks)</dl>
<p> -a <i>mask</i><br />
 &#8211;act-mask=<i>mask</i></p>
<dl>
<dd>Add <i>mask</i> to current filter (see below for masks)</dl>
<p> -b <i>size</i><br />
 &#8211;buffer-size=<i>size</i></p>
<dl>
<dd>Specifies buffer size for event extraction (scaled by 1024). The default buffer size is 512KiB.</dl>
<p> -d <i>dev</i><br />
 &#8211;dev=<i>dev</i></p>
<dl>
<dd>Adds <i>dev</i> as a device to trace</dl>
<p> -I <i>file</i><br />
 &#8211;input-devs=<i>file</i></p>
<dl>
<dd>Adds the devices found in <i>file</i> as devices to trace</dl>
<p> -n <i>num-sub</i><br />
 &#8211;num-sub-buffers=<i>num-sub</i></p>
<dl>
<dd>Specifies number of buffers to use. blktrace defaults to 4 sub buffers.</dl>
<p> -l<br />
 &#8211;listen</p>
<dl>
<dd>Run in network listen mode (blktrace server)</dl>
<p> -h <i>hostname</i><br />
 &#8211;host=<i>hostname</i></p>
<dl>
<dd>Run in network client mode, connecting to the given host</dl>
<p> -p <i>number</i><br />
 &#8211;port=<i>number</i></p>
<dl>
<dd>Network port to use (default 8462)</dl>
<p> -s<br />
 &#8211;no-sendfile</p>
<dl>
<dd>Make the network client NOT use sendfile() to transfer data</dl>
<p> -o <i>basename</i><br />
 &#8211;output=<i>basename</i></p>
<dl>
<dd>Specifies base name for input files. Default is device.blktrace.cpu. Specifying -o &#8211; runs in live mode with blkparse (writing data to standard out).</dl>
<p> -D <i>dir</i><br />
 &#8211;output-dir=<i>dir</i></p>
<dl>
<dd>Prepend <i>file</i> to output file name(s) </p>
<p> This only works when supplying a single device, or when piping the output via &quot;-o -&quot; with multiple devices.</dl>
<p> -r <i>rel-path</i><br />
 &#8211;relay=<i>rel-path</i></p>
<dl>
<dd>Specifies debugfs mount point</dl>
<p> -v<br />
 &#8211;version</p>
<dl>
<dd>Outputs version</dl>
<p> -V<br />
 &#8211;version</p>
<dl>
<dd>Outputs version</dl>
<p> -w <i>seconds</i><br />
 &#8211;stopwatch=<i>seconds</i></p>
<dl>
<dd>Sets run time to the number of seconds specified</dl>
<h2>Filter Masks</h2>
<p>The following masks may be passed with the <i>-a</i> command line option, multiple filters may be combined via multiple <i>-a</i> command line options. </p>
<dl>
<dd><i>barrier</i>: barrier attribute<br />
 <i>complete</i>: completed by driver<br />
 <i>fs</i>: requests<br />
 <i>issue</i>: issued to driver<br />
 <i>pc</i>: packet command events<br />
 <i>queue</i>: queue operations<br />
 <i>read</i>: read traces<br />
 <i>requeue</i>: requeue operations<br />
 <i>sync</i>: synchronous attribute<br />
 <i>write</i>: write traces<br />
 <i>notify</i>: trace messages<br />
 <i>drv_data</i>: additional driver specific trace</dl>
<h2>Request Types</h2>
<p>blktrace distinguishes between two types of block layer requests, file system and SCSI commands. The former are dubbed <code>fs</code> requests, the latter <code>pc</code> requests. File system requests are normal read/write operations, i.e. any type of read or write from a specific disk location at a given size. These requests typically originate from a user process, but they may also be initiated by the vm flushing dirty data to disk or the file system syncing a super or journal block to disk. <code>pc</code> requests are SCSI commands. blktrace sends the command data block as a payload so that blkparse can decode it.</p>
<h2>Examples</h2>
<p>To trace the i/o on the device <i>/dev/hda</i> and parse the output to human readable form, use the following command:<br />
&nbsp;<wbr>%&nbsp;<wbr>blktrace -d&nbsp;<wbr>/dev/sda -o &#8211; | blkparse -i &#8211; This same behaviour can be achieve with the convenience script <i>btrace</i>. The command<br />
&nbsp;<wbr>%&nbsp;<wbr>btrace&nbsp;<wbr>/dev/sda has exactly the same effect as the previous command. See <i>btrace</i> (8) for more information. To trace the i/o on a device and save the output for later processing with <i>blkparse</i>, use <i>blktrace</i> like this:<br />
&nbsp;<wbr>%&nbsp;<wbr>blktrace&nbsp;<wbr>/dev/sda&nbsp;<wbr>/dev/sdb This will trace i/o on the devices <i>/dev/sda</i> and <i>/dev/sdb</i> and save the recorded information in the files <i>sda</i> and <i>sdb</i> in the current directory, for the two different devices, respectively. This trace information can later be parsed by the <i>blkparse</i> utility:<br />
&nbsp;<wbr>%&nbsp;<wbr>blkparse sda sdb which will output the previously recorded tracing information in human readable form to stdout. See <i>blkparse</i> (1) for more information. </p>
<h2>Authors</h2>
<p>blktrace was written by Jens Axboe, Alan D. Brunelle and Nathan Scott. This man page was created from the blktrace documentation by Bas Zoetekouw.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;linux-btrace [at] vger.kernel.org&gt;</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2006 Jens Axboe, Alan D. Brunelle and Nathan Scott.<br />
 This is free software. You may redistribute copies of it under the terms of the GNU General Public License &lt;<a rel="nofollow" href="http://www.gnu.org/licenses/gpl.html">http://www.gnu.org/licenses/gpl.html</a>&gt;. There is NO WARRANTY, to the extent permitted by law.<br />
 This manual page was created for Debian by Bas Zoetekouw. It was derived from the documentation provided by the authors and it may be used, distributed and modified under the terms of the GNU General Public License, version 2.<br />
 On Debian systems, the text of the GNU General Public License can be found in /usr/share/common-licenses/GPL-2.</p>
<h2>See Also</h2>
<p>btrace (8), blkparse (1), verify_blkparse (1), blkrawverify (1), btt (1) </p>
