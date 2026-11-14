---
title: "btrecord(8)"
name: "btrecord"
section: "8"
letter: "b"
url: "/docs/linux/man/8-btrecord/"
description: "btrecord – recreate IO loads recorded by blktrace"
---

<p>btrecord &#8211; recreate IO loads recorded by blktrace </p>
<h2>Synopsis</h2>
<p><code>Usage: </code> btrecord [ <i>options</i> ] &lt;<i>dev</i>&#8230;&gt; </p>
<h2>Description</h2>
<p>The <i>btrecord</i> and <i>btreplay</i> tools provide the ability to record and replay IOs captured by the <i>blktrace</i> utility. Attempts are made to maintain ordering, CPU mappings and time-separation of IOs. The <i>blktrace</i> utility provides the ability to collect detailed traces from the kernel for each IO processed by the block IO layer. The traces provide a complete timeline for each IO processed, including detailed information concerning when an IO was first received by the block IO layer &#8212; indicating the device, CPU number, time stamp, IO direction, sector number and IO size (number of sectors). Using this information, one is able to <code>replay</code> the IO again on the same machine or another set up entirely. The basic operating work-flow to replay IOs would be something like:</p>
<dl>
<dt>&#8211;</p>
<dd>&nbsp;<wbr>&nbsp;<wbr>Run&nbsp;<wbr><i>blktrace</i>&nbsp;<wbr>to collect traces. Here you specify the<br />
&nbsp;<wbr>&nbsp;<wbr>device or devices that you wish to trace and later replay IOs upon. Note:<br />
&nbsp;<wbr>&nbsp;<wbr>the only traces you are interested in are&nbsp;<wbr><code>QUEUE</code>&nbsp;<wbr>requests &#8212;<br />
&nbsp;<wbr>&nbsp;<wbr>thus, to save system resources&nbsp;<wbr>(including storage for traces), one could<br />
&nbsp;<wbr>&nbsp;<wbr>specify the&nbsp;<wbr><i>-a queue</i>&nbsp;<wbr>command line option to&nbsp;<wbr><i>blktrace</i>.</p>
<dt>&#8211;</p>
<dd>&nbsp;<wbr>&nbsp;<wbr>While&nbsp;<wbr><i>blktrace</i>&nbsp;<wbr>is running, you run the workload that you<br />
&nbsp;<wbr>&nbsp;<wbr>are interested in.&nbsp;<wbr></p>
<dt>&#8211;</p>
<dd>&nbsp;<wbr>&nbsp;<wbr>When the work load has completed, you stop the&nbsp;<wbr><i>blktrace</i><br />
&nbsp;<wbr>&nbsp;<wbr>utility&nbsp;<wbr>(thus saving all traces over the complete workload).&nbsp;<wbr></p>
<dt>&#8211;</p>
<dd>&nbsp;<wbr>&nbsp;<wbr>You extract the pertinent IO information from the traces saved by<br />
&nbsp;<wbr>&nbsp;<wbr><i>blktrace</i>&nbsp;<wbr>using the&nbsp;<wbr><i>btrecord</i>&nbsp;<wbr>utility. This will parse<br />
&nbsp;<wbr>&nbsp;<wbr>each trace file created by&nbsp;<wbr><i>blktrace</i>, and crafty IO descriptions<br />
&nbsp;<wbr>&nbsp;<wbr>to be used in the next phase of the workload processing.</p>
<dt>&#8211;</p>
<dd>&nbsp;<wbr>&nbsp;<wbr>Once&nbsp;<wbr><i>btrecord</i>&nbsp;<wbr>has successfully created a series of data<br />
&nbsp;<wbr>&nbsp;<wbr>files to be processed, you can run the&nbsp;<wbr><i>btreplay</i>&nbsp;<wbr>utility which<br />
&nbsp;<wbr>&nbsp;<wbr>attempts to generate the same IOs seen during the sample workload phase. </p>
<h2>Options</h2>
<p>-d &lt;<i>dir</i>&gt;<br />
 &#8211;input-directory=&lt;<i>dir</i>&gt;</p>
<dl>
<dd>Set input directory. This option requires a single parameter providing the directory name for where input files are to be found. The default directory is the current directory (<i>.</i>).</dl>
<p> -D &lt;<i>dir</i>&gt;<br />
 &#8211;output-directory=&lt;<i>dir</i>&gt;</p>
<dl>
<dd>Set output directory. This option requires a single parameter providing the directory name for where output files are to be found. The default directory is the current directory (<i>.</i>).</dl>
<p> -F<br />
 &#8211;find-traces</p>
<dl>
<dd>Find trace files automatically This option instructs <i>btreplay</i> to go find all the trace files in the directory specified (either via the <i>-d</i> option, or in the default directory (<i>.</i>).</dl>
<p> -h<br />
 &#8211;help</p>
<dl>
<dd>Show help and exit.</dl>
<p> -V<br />
 &#8211;version</p>
<dl>
<dd>Show version number and exit.</dl>
<p> -m &lt;<i>nanoseconds</i>&gt;<br />
 &#8211;max-bunch-time=&lt;<i>nanoseconds</i>&gt;</p>
<dl>
<dd>The <i>-m</i> option requires a single parameter which specifies an amount of time (in nanoseconds) to include in any one bunch of IOs that are to be processed. The smaller the value, the smaller the number of IOs processed at one time &#8212; perhaps yielding in more realistic replay. However, after a certain point the amount of overhead per bunch may result in additional real replay time, thus yielding less accurate replay times. </p>
<p> The default value is 10,000,000 nanoseconds (10 milliseconds).</dl>
<p> -M &lt;<i>num</i>&gt;<br />
 &#8211;max-pkts=&lt;<i>num</i>&gt;</p>
<dl>
<dd>Set maximum number of packets per bunch. The <i>-M</i> option requires a single parameter which specifies the maximum number of IOs to store in a single bunch. As with the <i>-m</i> option, smaller values may or may not yield more accurate replay times. </p>
<p> The default value is 8, with a maximum value of up to 512 being supported.</dl>
<p> -o &lt;<i>basename</i>&gt;<br />
 &#8211;output-base=&lt;<i>basename</i>&gt;</p>
<dl>
<dd>Set base name for output files. Each output file has 3 fields:</p>
<dl>
<dt>1.</p>
<dd>&nbsp;<wbr>Device identifier&nbsp;<wbr>(taken directly from the device name of the<br />
&nbsp;<wbr><i>blktrace</i>&nbsp;<wbr>output file).</p>
<dt>2.</p>
<dd>&nbsp;<wbr><i>btrecord</i>&nbsp;<wbr>base name &#8212; by default&nbsp;<wbr>&#8220;replay&#8221;.</p>
<dt>3.</p>
<dd>&nbsp;<wbr>The CPU number&nbsp;<wbr>(again, taken directly from the<br />
&nbsp;<wbr><i>blktrace</i>&nbsp;<wbr>output file name).</dl>
<p> This option requires a single parameter that will override the default name (replay), and replace it with the specified value.</dl>
<p> -v<br />
 &#8211;verbose</p>
<dl>
<dd>Enable verbose output. This option will output some simple statistics at the end of a successful run. Example output is: </p>
<pre>sdab:0: 580661 pkts (tot), 126030 pkts (replay), 89809 bunches, 1.4 pkts/bunch
sdab:1: 2559775 pkts (tot), 430172 pkts (replay), 293029 bunches, 1.5 pkts/bunch
sdab:2: 653559 pkts (tot), 136522 pkts (replay), 102288 bunches, 1.3 pkts/bunch
sdab:3: 474773 pkts (tot), 117849 pkts (replay), 69572 bunches, 1.7 pkts/bunch</pre>
<p>The meaning of the columns is:</p>
<dl>
<dt>1.</p>
<dd>&nbsp;<wbr>&nbsp;<wbr>The first field contains the device name and CPU identifier. Thus:<br />
&nbsp;<wbr>&nbsp;<wbr><i>sdab:0:</i>&nbsp;<wbr>means the device&nbsp;<wbr><i>sdab</i>&nbsp;<wbr>and traces on CPU 0.&nbsp;<wbr></p>
<dt>2.</p>
<dd>&nbsp;<wbr>&nbsp;<wbr>The second field contains the total number of packets processed for each<br />
&nbsp;<wbr>&nbsp;<wbr>device file.&nbsp;<wbr></p>
<dt>3.</p>
<dd>&nbsp;<wbr>&nbsp;<wbr>The next field shows the number of packets eligible for replay.&nbsp;<wbr></p>
<dt>4.</p>
<dd>&nbsp;<wbr>&nbsp;<wbr>The fourth field contains the total number of IO bunches.&nbsp;<wbr></p>
<dt>5.</p>
<dd>&nbsp;<wbr>&nbsp;<wbr>The last field shows the average number of IOs per bunch recorded.</dl>
</dl>
<h2>Authors</h2>
<p><i>btrecord</i> was written by Alan D. Brunelle. This man page was created from the <i>btreplay</i> documentation by Bas Zoetekouw.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;linux-btrace [at] vger.kernel.org&gt;</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2007 Alan D. Brunelle, Alan D. Brunelle and Nathan Scott.<br />
 This is free software. You may redistribute copies of it under the terms of the GNU General Public License &lt;<a rel="nofollow" href="http://www.gnu.org/licenses/gpl.html">http://www.gnu.org/licenses/gpl.html</a>&gt;. There is NO WARRANTY, to the extent permitted by law.<br />
 This manual page was created for Debian by Bas Zoetekouw. It was derived from the documentation provided by the authors and it may be used, distributed and modified under the terms of the GNU General Public License, version 2.<br />
 On Debian systems, the text of the GNU General Public License can be found in /usr/share/common-licenses/GPL-2.</p>
<h2>See Also</h2>
<p>The full documentation for btreplay can be found in /usr/share/doc/blktrace on Debian systems.<br />
 blktrace (8), blkparse (1), btreplay (8) </p>
