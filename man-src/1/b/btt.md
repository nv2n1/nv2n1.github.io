---
title: "btt(1)"
name: "btt"
section: "1"
letter: "b"
url: "/docs/linux/man/1-btt/"
description: "btt – analyse block i/o traces produces by blktrace"
---

<h2 class="name">NAME</h2>
<p> btt &#8211; analyse block i/o traces produces by blktrace </p>
<h2>SYNOPSIS</h2>
<p> <code>btt </code><br />
 [ -a | &#8211;seek-absolute ]<br />
 [ -A | &#8211;all-data ]<br />
 [ -B &lt;<i>output name</i>&gt; | &#8211;dump-blocknos=&lt;<i>output name</i>&gt; ]<br />
 [ -d &lt;<i>seconds</i>&gt; | &#8211;range-delta=&lt;<i>seconds</i>&gt; ]<br />
 [ -D &lt;<i>dev;&#8230;</i>&gt; | &#8211;devices=&lt;<i>dev;&#8230;</i>&gt; ]<br />
 [ -e &lt;<i>exe,&#8230;</i>&gt; | &#8211;exes=&lt;<i>exe,&#8230;</i>&gt; ]<br />
 [ -h | &#8211;help ]<br />
 [ -i &lt;<i>input name</i>&gt; | &#8211;input-file=&lt;<i>input name</i>&gt; ]<br />
 [ -I &lt;<i>output name</i>&gt; | &#8211;iostat=&lt;<i>output name</i>&gt; ]<br />
 [ -l &lt;<i>output name</i>&gt; | &#8211;d2c-latencies=&lt;<i>output name</i>&gt; ]<br />
 [ -L &lt;<i>freq</i>&gt; | &#8211;periodic-latencies=&lt;<i>freq</i>&gt; ]<br />
 [ -m &lt;<i>output name</i>&gt; | &#8211;seeks-per-second=&lt;<i>output name</i>&gt; ]<br />
 [ -M &lt;<i>dev map</i>&gt; | &#8211;dev-maps=&lt;<i>dev map</i>&gt;<br />
 [ -o &lt;<i>output name</i>&gt; | &#8211;output-file=&lt;<i>output name</i>&gt; ]<br />
 [ -p &lt;<i>output name</i>&gt; | &#8211;per-io-dump=&lt;<i>output name</i>&gt; ]<br />
 [ -P &lt;<i>output name</i>&gt; | &#8211;per-io-trees=&lt;<i>output name</i>&gt; ]<br />
 [ -q &lt;<i>output name</i>&gt; | &#8211;q2c-latencies=&lt;<i>output name</i>&gt; ]<br />
 [ -Q &lt;<i>output name</i>&gt; | &#8211;active-queue-depth=&lt;<i>output name</i>&gt; ]<br />
 [ -r | &#8211;no-remaps ]<br />
 [ -s &lt;<i>output name</i>&gt; | &#8211;seeks=&lt;<i>output name</i>&gt; ]<br />
 [ -S &lt;<i>interval</i>&gt; | &#8211;iostat-interval=&lt;<i>interval</i>&gt; ]<br />
 [ -t &lt;<i>sec</i>&gt; | &#8211;time-start=&lt;<i>sec</i>&gt; ]<br />
 [ -T &lt;<i>sec</i>&gt; | &#8211;time-end=&lt;<i>sec</i>&gt; ]<br />
 [ -u &lt;<i>output name</i>&gt; | &#8211;unplug-hist=&lt;<i>output name</i>&gt; ]<br />
 [ -v | &#8211;verbose ]<br />
 [ -V | &#8211;version ]<br />
 [ -X | &#8211;easy-parse-avgs ]<br />
 [ -z &lt;<i>output name</i>&gt; | &#8211;q2d-latencies=&lt;<i>output name</i>&gt; ]<br />
 [ -Z | &#8211;do-active ] </p>
<h2>DESCRIPTION</h2>
<p> btt is a post-processing tool for the block layer IO tracing tool called <a href="/docs/linux/man/8-blktrace/">blktrace</a>(8). As noted in its documentation, blktrace is a block layer IO tracing mechanism which provides detailed information about request queue operations up to user space. </p>
<p> btt will take in binary dump data from blkparse, and analyse the events, producing a series of output from the analysis. It will also build .dat files containing &quot;range data&quot; &#8212; showing things like Q activity (periods of time while Q events are being produced), C activity (likewise for command completions), and etc. </p>
<p> Included with the distribution is a simple 3D plotting utility, <i>bno_plot</i>, which can plot the block numbers btt outputs if the <i>-B</i> option is specified. The display will display each IO generated, with the time (seconds) along the X-axis, the block number (start) along the Y-axis and the number of blocks transferred in the IO represented along the Z-axis. </p>
<h2>OPTIONS</h2>
<p> <code>-a</code><br />
 <code>&#8211;seek-absolute</code></p>
<dl>
<dt>
<dd> When specified on the command line, this directs btt to calculate seek distances based solely upon the ending block address of one IO, and the start of the next. By default <code>btt</code> uses the concept of the closeness to either the beginning or end of the previous IO. See the Users Manual for more details about seek distances.</dl>
<p> <code>-A</code><br />
 <code>&#8211;all-data</code></p>
<dl>
<dt>
<dd> Normally <code>btt</code> will not print out verbose information concerning per-process and per-device data. If you desire that level of detail you can specify this option.</dl>
<p> <code>-B &lt;</code><i>output name</i>&gt;<br />
 <code>&#8211;dump-blocknos=&lt;</code><i>output name</i>&gt;</p>
<dl>
<dt>
<dd> This option will output absolute block numbers to three files prefixed by the specified output name:</p>
<dl>
<dt> <i>prefix_device_r.dat</i></p>
<dd>
<dd>All read block numbers are output, first column is time (seconds), second is the block number, and the third column is the ending block number.</p>
<dt> <i>prefix_device_w.dat</i></p>
<dd>
<dd>All write block numbers are output, first column is time (seconds), second is the block number, and the third column is the ending block number.</p>
<dt> <i>prefix_device_c.dat</i></p>
<dd>
<dd>All block numbers (read and write) are output, first column is time (seconds), second is the block number, and the third column is the ending block number.</dl>
</dl>
<p> <code>-d &lt;</code><i>seconds</i>&gt;<br />
 <code>&#8211;range-delta=&lt;</code><i>seconds</i>&gt;</p>
<dl>
<dt>
<dd> <code>btt</code> outputs a file containing Q and C activity, the notion of active traces simply means that there are Q or C traces occurring within a certain period of each other. The default values is 0.1 seconds; with this option allowing one to change that granularity. The smaller the value, the more data points provided.</dl>
<p> <code>-D &lt;</code><i>dev;&#8230;</i>&gt;<br />
 <code>&#8211;devices=&lt;</code><i>dev;&#8230;</i>&gt;</p>
<dl>
<dt>
<dd> Normally, <code>btt</code> will produce data for all devices detected in the traces parsed. With this option, one can reduce the analysis to one or more devices provided in the string passed to this option. The device identifiers are the major and minor number of each device, and each device identifier is separated by a colon (:). A valid specifier for devices 8,0 and 8,8 would then be: <i>8,0:8,8</i>.</dl>
<p> <code>-e &lt;</code><i>exe,&#8230;</i>&gt;<br />
 <code>&#8211;exes=&lt;</code><i>exe,&#8230;</i>&gt;</p>
<dl>
<dt>
<dd> The -e option supplies the list of executables that will have I/Os analysed.</dl>
<p> <code>-h</code><br />
 <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Shows a short summary of possible command line option</dl>
<p> <code>-i &lt;</code><i>input name</i>&gt;<br />
 <code>&#8211;input-file &lt;</code><i>input file</i>&gt;</p>
<dl>
<dt>
<dd> Specifies the input file to analyse. This should be a trace file produced by <i>blktrace</i> (8).</dl>
<p> <code>-I &lt;</code><i>output name</i>&gt;<br />
 <code>&#8211;iostat=&lt;</code><i>output name</i>&gt;</p>
<dl>
<dt>
<dd> The -I option directs btt to output iostat-like data to the specified file. Refer to the iostat (sysstat) documentation for details on the data columns.</dl>
<p> <code>-l &lt;</code><i>output name</i>&gt;<br />
 <code>&#8211;d2c-latencies=&lt;</code><i>output name</i>&gt;</p>
<dl>
<dt>
<dd> The -l option allows one to output per-IO D2C latencies respectively. The supplied argument provides the basis for the output name for each device.</dl>
<p> <code>-L &lt;</code><i>freq</i>&gt;<br />
 <code>&#8211;periodic-latencies=&lt;</code><i>freq</i>&gt;</p>
<dl>
<dt>
<dd> The -L option allows one to output periodic latency information for both Q2C and D2C latencies. The frequency specified will regulate how often an average latency is output &#8212; a floating point value expressing seconds.</dl>
<p> <code>-m &lt;</code><i>output name</i>&gt;<br />
 <code>&#8211;seeks-per-second=&lt;</code><i>output name</i>&gt;</p>
<dl>
<dt>
<dd> Trigger btt to output seeks-per-second information. The first column will contain a time value (seconds), and the second column will indicate the number of seeks per second at that point.</dl>
<p> <code>-M &lt;</code><i>dev map</i>&gt;<br />
 <code>&#8211;dev-maps=&lt;</code><i>dev map</i>&gt;</p>
<dl>
<dt>
<dd> The -M option takes in a file generated by the provided script (gen_disk_info.py), and allows for better output of device names.</dl>
<p> <code>-o &lt;</code><i>output name</i>&gt;<br />
 <code>&#8211;output-file=&lt;</code><i>output name</i>&gt;</p>
<dl>
<dt>
<dd> Specifies the output file name.</dl>
<p> <code>-p &lt;</code><i>output name</i>&gt;<br />
 <code>&#8211;per-io-dump=&lt;</code><i>output name</i>&gt;</p>
<dl>
<dt>
<dd> The -p option will generate a file that contains a list of all IO &quot;sequences&quot; &#8211; showing the parts of each IO (Q, A, I/M, D, &amp; C).</dl>
<p> <code>-P &lt;</code><i>output name</i>&gt;<br />
 <code>&#8211;per-io-trees=&lt;</code><i>output name</i>&gt;</p>
<dl>
<dt>
<dd> The -P option will generate a file that contains a list of all IO &quot;sequences&quot; &#8211; showing only the Q, D &amp; C operation times. The D &amp; C time values are separated from the Q time values with a vertical bar.</dl>
<p> <code>-q &lt;</code><i>output name</i>&gt;<br />
 <code>&#8211;q2c-latencies=&lt;</code><i>output name</i>&gt;</p>
<dl>
<dt>
<dd> The -q option allows one to output per-IO Q2C latencies respectively. The supplied argument provides the basis for the output name for each device.</dl>
<p> <code>-Q &lt;</code><i>output name</i>&gt;<br />
 <code>&#8211;active-queue-depth=&lt;</code><i>output name</i>&gt;</p>
<dl>
<dt>
<dd> The -Q option allows one to output data files showing the time stamp and the depth of active commands (those issued but not completed).</dl>
<p> <code>-r</code><br />
 <code>&#8211;no-remaps</code></p>
<dl>
<dt>
<dd> Ignore remap traces; older kernels did not implement the full remap PDU.</dl>
<p> <code>-s &lt;</code><i>output name</i>&gt;<br />
 <code>&#8211;seeks=&lt;</code><i>output name</i>&gt;</p>
<dl>
<dt>
<dd> The -s option instructs btt to output seek data, the argument provided is the basis for file names output. There are two files per device, read seeks and write seeks.</dl>
<p> <code>-S &lt;</code><i>interval</i>&gt;<br />
 <code>&#8211;iostat-interval=&lt;</code><i>interval</i>&gt;</p>
<dl>
<dt>
<dd> The -S option specifies the interval to use between data output, it defaults to once per second.</dl>
<p> <code>-t &lt;</code><i>sec</i>&gt;<br />
 <code>&#8211;time-start=&lt;</code><i>sec</i>&gt;<br />
 <code>-T &lt;</code><i>sec</i>&gt;<br />
 <code>&#8211;time-end=&lt;</code><i>sec</i>&gt;</p>
<dl>
<dt>
<dd> The -t/-T options allow one to set a start and/or end time for analysing &#8211; analysing will only be done for traces after -t&#8217;s argument and before -T&#8217;s argument. (-t and -T are optional, so if you specify just -t, analysis will occur for all traces after the time specified. Similarly, if only -T is specified, analysis stops after -T&#8217;s seconds.)</dl>
<p> <code>-u &lt;</code><i>output name</i>&gt;<br />
 <code>&#8211;unplug-hist=&lt;</code><i>output name</i>&gt;</p>
<dl>
<dt>
<dd> This option instructs <code>btt</code> to generate a data file containing histogram information for unplug traces on a per device basis. It shows how many times an unplug was hit with a specified number of IOs released. There are 21 output values into the file, as follows: </p>
<dl>
<dt>
<dd> a value of 0 represents 0..4 counts<br />
 a value of 1 represents 5..9 counts<br />
 a value of 2 represents 10..14 counts<br />
 etc, until<br />
 a value of 20 represents 100+ counts
</dl>
<p> The file name(s) generated use the text string passed as an argument for the prefix, followed by the device identifier in <i>major,minor</i> form, with a <i>.dat</i> extension. For example, with <i>-u up_hist</i> specified on the command line: <i>up_hist_008,032.dat</i>.</dl>
<p> <code>-V</code><br />
 <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Shows the version of btt.</dl>
<p> <code>-v</code><br />
 <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Requests a more verbose output.</dl>
<p> <code>-X</code><br />
 <code>&#8211;easy-parse-avgs</code></p>
<dl>
<dt>
<dd> Provide data in an easy-to-parse form and write it to a file with .avg exentsion</dl>
<p> <code>-z &lt;</code><i>output name</i>&gt;<br />
 <code>&#8211;q2d-latencies=&lt;</code><i>output name</i>&gt;</p>
<dl>
<dt>
<dd> The -z option allows one to output per-IO Q2D latencies respectively. The supplied argument provides the basis for the output name for each device.</dl>
<p> <code>-Z</code><br />
 <code>&#8211;do-active</code></p>
<dl>
<dt>
<dd> The -Z will output files containing data which can be plotted showing per-device (and total system) I/O activity.</dl>
<h2>AUTHORS</h2>
<p> <i>btt</i> was written by Alan D. Brunelle. This man page was created from the <i>blktrace</i> documentation by Bas Zoetekouw. </p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;linux-btrace [at] vger.kernel.org&gt; </p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2006 Jens Axboe, Alan D. Brunelle and Nathan Scott.<br />
 This is free software. You may redistribute copies of it under the terms of the GNU General Public License &lt;<a rel="nofollow" href="http://www.gnu.org/licenses/gpl.html">http://www.gnu.org/licenses/gpl.html</a>&gt;. There is NO WARRANTY, to the extent permitted by law.<br />
 This manual page was created for Debian by Bas Zoetekouw. It was derived from the documentation provided by the authors and it may be used, distributed and modified under the terms of the GNU General Public License, version 2.<br />
 On Debian systems, the text of the GNU General Public License can be found in /usr/share/common-licenses/GPL-2. </p>
<h2>SEE ALSO</h2>
<p> The btt Users Guide, which can be found in /usr/share/doc/blktrace/btt.pdf<br />
 bno_plot (1), blktrace (8), blkparse (1), verify_blkparse (1), blkrawverify (1), btt (1) </p>
<h2>Index</h2>
