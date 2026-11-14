---
title: "btreplay(8)"
name: "btreplay"
section: "8"
letter: "b"
url: "/docs/linux/man/8-btreplay/"
description: "btreplay – recreate IO loads recorded by blktrace"
---

<p>btreplay &#8211; recreate IO loads recorded by blktrace </p>
<h2>Synopsis</h2>
<p><code>btreplay [ </code><i>options</i> ] &lt;<i>dev</i>&#8230;&gt; </p>
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
<p>-c &lt;<i>num</i>&gt;<br />
 &#8211;cpus=&lt;<i>num</i>&gt;</p>
<dl>
<dd>Set number of CPUs to use.</dl>
<p> -d &lt;<i>dir</i>&gt;<br />
 &#8211;input-directory=&lt;<i>dir</i>&gt;</p>
<dl>
<dd>Set input directory. This option requires a single parameter providing the directory name for where input files are to be found. The default directory is the current directory (<i>.</i>).</dl>
<p> -F<br />
 &#8211;find-records</p>
<dl>
<dd>Find record files automatically This option instructs <i>btreplay</i> to go find all the record files in the directory specified (either via the <i>-d</i> option, or in the default directory (<i>.</i>).</dl>
<p> -h<br />
 &#8211;help</p>
<dl>
<dd>Show help and exit.</dl>
<p> -i &lt;<i>basename</i>&gt;<br />
 &#8211;input-base=&lt;<i>basename</i>&gt;</p>
<dl>
<dd>Set base name for input files. Each input file has 3 fields:</p>
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
<p> -I &lt;<i>num</i>&gt;<br />
 &#8211;iterations=&lt;<i>num</i>&gt;</p>
<dl>
<dd>Set number of iterations to run. This option requires a single parameter which specifies the number of times to run through the input files. The default value is 1</dl>
<p> -M &lt;<i>filename</i>&gt;<br />
 &#8211;map-devs=&lt;<i>filename</i>&gt;</p>
<dl>
<dd>Specify device mappings. This option requires a single parameter which specifies the name of a file contain device mappings. The file must be very simply managed, with just two pieces of data per line: </p>
<dl>
<dt>&#8211;</p>
<dd>&nbsp;<wbr>&nbsp;<wbr>The device name on the recorded system&nbsp;<wbr>(with the&nbsp;<wbr>&#8216;<i>/dev/</i>&#8216;<br />
&nbsp;<wbr>&nbsp;<wbr>removed). Example:&nbsp;<wbr><i>/dev/sda</i>&nbsp;<wbr>would just be&nbsp;<wbr><i>sda</i>. </p>
<dt>&#8211;</p>
<dd>&nbsp;<wbr>&nbsp;<wbr>The device name on the replay system to use&nbsp;<wbr>(again, without the<br />
&nbsp;<wbr>&nbsp;<wbr>&#8216;<i>/dev/</i>&#8216;&nbsp;<wbr>path prepended). </p>
</dl>
<p> An example file for when one would map devices <i>/dev/sda</i> and <i>/dev/sdb</i> on the recorded system to <i>dev/sdg</i> and <i>sdh</i> on the replay system would be: </p>
<pre><dl><dt><dd>sda sdg
sdb sdh</pre>
</dl>
<p> The only entries in the file that are allowed are these two element lines &#8212; we do not (yet?) support the notion of blank lines, or comment lines, or the like. </p>
<p> The utility allows for multiple <i>-M</i> options to be supplied on the command line.</dl>
<p> -N<br />
 &#8211;no-stalls</p>
<dl>
<dd>Disable pre-bunch stalls. When specified on the command line, all pre-bunch stall indicators will be ignored. IOs will be replayed without inter-bunch delays.</dl>
<p> -x &lt;<i>factor</i>&gt;<br />
 &#8211;acc-factor=&lt;<i>factor</i>&gt;</p>
<dl>
<dd>Specify acceleration factor. Default value is 1 (no acceleration).</dl>
<p> -v<br />
 &#8211;verbose</p>
<dl>
<dd>Enable verbose output. When specified on the command line, this option instructs <i>btreplay</i> to store information concerning each <code>stall</code> and IO operation performed by <i>btreplay</i>. The name of each file so created will be the input file name used with an extension of <i>.rep</i> appended onto it. Thus, an input file of the name <i>sdab.replay.3</i> would generate a verbose output file with the name <i>sdab.replay.3.rep</i> in the directory specified for input files. </p>
<p> In addition, <i>btreplay</i> will also output to <i>stderr</i> the names of the input files being processed.</dl>
<p> -V<br />
 &#8211;version</p>
<dl>
<dd>Show version number and exit.</dl>
<p> -W<br />
 &#8211;write-enable</p>
<dl>
<dd>Enable writing during replay. As a precautionary measure, by default <i>btreplay</i> will not process <code>write</code> requests. In order to enable <i>btreplay</i> to actually <code>write</code> to devices one must explicitly specify the <i>-W</i> option.</dl>
<h2>Authors</h2>
<p><i>btreplay</i> was written by Alan D. Brunelle. This man page was created from the <i>btreplay</i> documentation by Bas Zoetekouw.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;linux-btrace [at] vger.kernel.org&gt;</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2007 Alan D. Brunelle, Alan D. Brunelle and Nathan Scott.<br />
 This is free software. You may redistribute copies of it under the terms of the GNU General Public License &lt;<a rel="nofollow" href="http://www.gnu.org/licenses/gpl.html">http://www.gnu.org/licenses/gpl.html</a>&gt;. There is NO WARRANTY, to the extent permitted by law.<br />
 This manual page was created for Debian by Bas Zoetekouw. It was derived from the documentation provided by the authors and it may be used, distributed and modified under the terms of the GNU General Public License, version 2.<br />
 On Debian systems, the text of the GNU General Public License can be found in /usr/share/common-licenses/GPL-2.</p>
<h2>See Also</h2>
<p>The full documentation for btreplay can be found in /usr/share/doc/blktrace on Debian systems.<br />
 blktrace (8), blkparse (1), btrecord (8) </p>
