---
title: "blkiomon(8)"
name: "blkiomon"
section: "8"
letter: "b"
url: "/docs/linux/man/8-blkiomon/"
description: "blkiomon – monitor block device I/O based o blktrace data"
---

<p>blkiomon &#8211; monitor block device I/O based o blktrace data </p>
<h2>Synopsis</h2>
<p><code>blkiomon -I </code><i>interval</i> [ -h <i>file</i> ] [ -b <i>file</i> ] [ -d <i>file</i> ] [ -D <i>file</i> ] [ -Q <i>path_name</i> -q <i>msg_queue_id</i> -m <i>msg_id</i> ] [ -V ] </p>
<h2>Description</h2>
<p>blkiomon is a block device I/O monitor. It periodically generates per-device request size and request latency statistics from blktrace data. It provides histograms as well as data that can be used to calculate min, max, average and variance. For this purpose, it consumes D and C traces read from stdin. Note, that this doesn&#8217;t work for logical volumes, as high-level drivers don&#8217;t see the completion of the events (C). There are options for binary output and human-readable output to files and stdout. Output to a message queue is supported as well. There is no need to use blkparse with blkiomon. blkiomon is capable of consuming binary output written to stdout by blktrace. </p>
<h2>Options</h2>
<p>-I <i>interval</i><br />
 &#8211;interval=<i>interval</i></p>
<dl>
<dd>Set sample interval</dl>
<p> -h <i>file</i><br />
 &#8211;human-readable=<i>file</i></p>
<dl>
<dd>Human-readable output file. Use &#8216;-&#8216; for stdout.</dl>
<p> -b <i>file</i><br />
 &#8211;binary=<i>file</i></p>
<dl>
<dd>Binary output file. Use &#8216;-&#8216; for stdout.</dl>
<p> -d <i>file</i><br />
 &#8211;dump-lldd=<i>file</i></p>
<dl>
<dd>Output file for data emitted by low level device driver.</dl>
<p> -D <i>file</i><br />
 &#8211;debug=<i>file</i></p>
<dl>
<dd>Output file for debugging data. Use &#8216;-&#8216; for stdout.</dl>
<p> -Q <i>path_name</i><br />
 &#8211;msg-queue=<i>path_name</i></p>
<dl>
<dd>Sets <i>path_name</i> as path name for existing message queue to be used for binary output.</dl>
<p> -q <i>msg_queue_id</i><br />
 &#8211;msg-queue-id=<i>msg_queue_id</i></p>
<dl>
<dd>Sets <i>msg_queue_id</i> as ID for an existing message queue to be used for binary output.</dl>
<p> -m <i>msg_id</i><br />
 &#8211;msg-id=<i>msg_id</i></p>
<dl>
<dd>Sets <i>msg_id</i> as message identifier to be used for binary output messages written to an existing message queue.</dl>
<p> -V<br />
 &#8211;version</p>
<dl>
<dd>Print program version.</dl>
<h2>Examples</h2>
<p>To get I/O statistics for /dev/sdw every 10 seconds for a period of one hour, use the following command:<br />
&nbsp;<wbr>%&nbsp;<wbr>blktrace&nbsp;<wbr>/dev/sdw -a issue -a complete -w 3600 -o &#8211; | blkiomon -I 10 -h &#8211; </p>
<h2>Authors</h2>
<p>blkiomon and this man page were written by Martin Peschke.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;linux-btrace [at] vger.kernel.org&gt;</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2008 IBM Corp.<br />
 This is free software. You may redistribute copies of it under the terms of the GNU General Public License &lt;<a rel="nofollow" href="http://www.gnu.org/licenses/gpl.html">http://www.gnu.org/licenses/gpl.html</a>&gt;. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>See Also</h2>
<p>btrace (8), blktrace (8), blkparse (1), verify_blkparse (1), blkrawverify (1), btt (1) </p>
