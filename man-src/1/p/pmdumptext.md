---
title: "pmdumptext(1)"
name: "pmdumptext"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmdumptext/"
description: "pmdumptext – dump performance metrics to an ASCII table"
---

<h2>NAME</h2>
<p> <code>pmdumptext</code> &#8211; dump performance metrics to an ASCII table</p>
<h2>SYNOPSIS</h2>
<p> <code>pmdumptext</code> [<code>-CFGHilmMNoruXz</code>] [<code>-A</code> <i>align</i>] [<code>-a</code> <i>archive</i>[<code>,</code><i>archive</i><code>,</code>&#8230;]] [<code>-c</code> <i>config</i>] [<code>-d</code> <i>delimiter</i>] [<code>-f</code> <i>format</i>] [<code>-h</code> <i>host</i>] [<code>-n</code> <i>pmnsfile</i>] [<code>-O</code> <i>offset</i>] [<code>-P</code> <i>precision</i>] [<code>-R</code> <i>lines</i>] [<code>-s</code> <i>sample</i>] [<code>-S</code> <i>starttime</i>] [<code>-t</code> <i>interval</i>] [<code>-T</code> <i>endtime</i>] [<code>-U</code> <i>string</i>] [<code>-w</code> <i>width</i>] [<code>-Z</code> <i>timezone</i>] [<i>metric </i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>pmdumptext</code> outputs the values of performance metrics collected live or from a set of Performance Co-Pilot (PCP) archives. By default, the metric values are displayed in tab separated columns, prefixed by a timestamp. </p>
<p> Unless directed to another host by the <code>-h</code> option, or to one or more sets of archives by the <code>-a</code> option, <code>pmdumptext</code> will contact <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) on the local host to obtain the required information. </p>
<p> <code>pmdumptext</code> may be run in interactive mode with the <code>-i</code> option which displays the values in equal width columns. Without this option, no attempt is made to line up any values allowing the output to be easily parsed by other applications. </p>
<p> The format of the output can be further controlled by changing the precision of the values with <code>-P</code>, the width of the columns with <code>-w</code>, and the format of the values with the <code>-G</code> and <code>-F</code> options for the shortest of scientific or fixed digits, and a fixed width format, respectively. </p>
<p> The <i>metrics</i> to be dumped can be listed on the command line, in a <i>config</i> file, or piped to <code>pmdumptext</code> on <i>stdin</i>. A metric consists of an optional source (host or archive), the metric name, and an optional instance list immediately after the name. A colon is used to separate a host name from the metric, and a forward slash (&#8220;/&#8221;) to separate an archive name from the metric. Instances are enclosed in square brackets and a comma is used between each instance if more than one is stated. For example, some legal metrics are: </p>
<pre><code>
kernel.all.cpu.idle
        myhost : kernel.all.cpu.idle[cpu0, cpu3] /
    path / to / myarchive / kernel.all.cpu.idle[cpu1]
</code></pre>
<p> The format of a metric is further described in <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1). A normalization value may optionally follow a metric name in a <i>config</i> file or on <i>stdin</i>. The metric value will be scaled by this value. For example, if the file system &#8220;/dev/root&#8221; has a capacity of 1965437 bytes, then the percentage of the file system that is used could be dumped with this <i>config</i>: </p>
<pre>
filesys.used[/dev/root] 19654.37
</pre>
<p> A normalization value may not be used with <i>metrics</i> specified as command line arguments. </p>
<p> A metric name is not required to be a leaf node in the Performance Metrics Name Space (PMNS), except when one or more instances are specified. For example, to dump all file system metrics, only <i>filesys</i> is required to dump <i>filesys.capacity</i>, <i>filesys.used</i>, <i>filesys.free</i> etc.</p>
<h2>COMMAND LINE OPTIONS</h2>
<p> The command line options <code>-A</code>, <code>-O</code>, <code>-S</code> and <code>-T</code> control the alignment, offset, start and end time when visualizing metrics from archives. These options are common to most Performance Co-Pilot tools and are fully described in <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1). </p>
<p> The other available options are: </p>
<dl>
<dt><code>-a</code></p>
<dd> Specify a set of <i>archive</i> from which metrics can be obtained for a particular host. <i>archive</i> is the name of a directory containing archives, or the basename of an archive, previously created by <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1). Multiple sets of archives (separated by commas or in different <code>-a</code> options) from different hosts may be given, but only one set of archives per host is permitted. Any metrics that are not associated with a specific host or archive will use the first archive as their source.</p>
<dt><code>-C</code></p>
<dd> Exit before dumping any values, but after parsing the metrics. Metrics, instances, normals and units are listed if <code>-m</code>, <code>-l</code>, <code>-N</code> and/or <code>-u</code> are specified.</p>
<dt><code>-c</code></p>
<dd> If no <i>metrics</i> are listed on the command line, a <i>config</i> file can be used to specify the <i>metrics</i> to be dumped. Unlike the command line <i>metrics</i>, each metric may be followed by a normalization value. Empty lines and lines that begin with &#8220;#&#8221; are ignored.</p>
<dt><code>-d</code></p>
<dd> Specify the <i>delimiter</i> that separates each column of output. The <i>delimiter</i> may only be a single character.</p>
<dt><code>-f</code></p>
<dd> Use the <i>format</i> string for formatting the timestamp with each set of values. The syntax of this string is the same as that described in <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3). An empty <i>format</i> string (eg. &#8221;) will remove the timestamps from the output.</p>
<dt><code>-F</code></p>
<dd> Output the values in a fixed width format of 6 characters. Positive numbers are represented as <i>dd</i>.<i>dd</i><code>u</code> and negative numbers as <code>[</code>&#8211;<code>]</code><i>d</i>.<i>dd</i><code>u</code>. The postfix multiplier may have the values <code>K</code>(10^3), <code>M</code>(10^6), <code>G</code>(10^9) and <code>T</code>(10^12). For example, 4567 would be displayed as 4.57K, even if the units of the metric are bytes.</p>
<dt><code>-G</code></p>
<dd> Output the values using the shortest of a scientific format or a decimal notation.</p>
<dt><code>-h</code></p>
<dd> Fetch performance metrics from <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) on <i>host</i>, rather than the default localhost.</p>
<dt><code>-H</code></p>
<dd> Show all headers before dumping any metric values. This is equivalent to <code>-lmNu</code>.</p>
<dt><code>-i</code></p>
<dd> Output the data in fixed width columns using fixed width values (see <code>-F</code>) so that it is human-readable. This option may not be used with <code>-P</code> as fixed point values are not fixed width. This option will also affect the output of <code>-m</code> and <code>-u</code> options as the metric, instance and unit names will be truncated.</p>
<dt><code>-l</code></p>
<dd> Show the source of the metrics. In interactive mode, the host of the metrics is shown. In non-interactive mode, this option shows the source of the metrics with the metric name even if <code>-m</code> is not specified.</p>
<dt><code>-m</code></p>
<dd> Output the metric names before the metric values. The source and units of the metrics may also be dumped with the <code>-l</code> and <code>-u</code> options respectively. If in interactive mode, the metrics names may be truncated, and the instance names, where relevant, are also truncated on the follow line.</p>
<dt><code>-M</code></p>
<dd> Output the column number and complete metric names before dumping any values. If the <code>-l</code> flag is also specified, the source of the metrics is also shown.</p>
<dt><code>-n</code></p>
<dd> Load an alternative local PMNS from the file <i>pmnsfile.</i></p>
<dt><code>-o</code></p>
<dd> When a timestamp is being reported (ie. unless an empty format string is given with the <code>-f </code> option), the timestamp is prefixed with the offset in seconds from the start of the set of archives or the beginning of the execution of <code>pmdumptext</code>.</p>
<dt><code>-N</code></p>
<dd> Output the normalization factors before the metric values.</p>
<dt><code>-P</code></p>
<dd> Set the <i>precision</i> of the values. This option may not be used with <code>-F</code> as the precision is constant. The default precision is 3.</p>
<dt><code>-r</code></p>
<dd> Output the raw metric values, do not convert counters to rates. This option also causes <code>pmdumptext</code> to ignore the normalization values for each metric.</p>
<dt><code>-R</code></p>
<dd> Repeat the header every <i>lines</i> of output. This option is useful in interactive mode when using a graphical window to avoid the header scrolling beyond the window&#8217;s buffer, and to realign the header if the window is resized.</p>
<dt><code>-s</code></p>
<dd> <code>pmdumptext</code> will terminate after this many samples.</p>
<dt><code>-t</code></p>
<dd> The <i>interval</i> argument follows the syntax described in <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), and in the simplest form may be an unsigned integer (the implied units in this case are seconds). The default interval is 1.0 seconds.</p>
<dt><code>-u</code></p>
<dd> Output the units of the metrics before the first values, but after the metric names if <code>-m</code> is also specified.</p>
<dt><code>-U</code></p>
<dd> Change the output when values are unavailable to <i>string</i>. The default string is &#8220;?&#8221;.</p>
<dt><code>-w</code></p>
<dd> Set the column width of the output. Strings will be truncated to this width, and maybe postfixed by &#8220;&#8230;&#8221; if the <i>width</i> is greater than 5.</p>
<dt><code>-X</code></p>
<dd> Output the column number and complete metric names, one-per-line, both before dumping the first set of values and again each time the header is repeated.</p>
<dt><code>-z</code></p>
<dd> Use the local timezone of the host that is the source of the performance metrics, as identified by either the <code>-h</code> or the first <code>-a</code> options. The default is to use the timezone of the local host.</p>
<dt><code>-Z</code></p>
<dd> Use <i>timezone</i> when displaying the date and time. <i>Timezone</i> is in the format of the environment variable <code>TZ</code> as described in <code><a href="/docs/linux/man/7-environ/">environ</a></code>(7).</dl>
<h2>MULTIPLE SOURCES</h2>
<p> <code>pmdumptext</code> supports the dumping of metrics from multiple hosts or set of archives. The metrics listed on the command line or in the <i>config</i> file may have no specific source or come from different sources. </p>
<p> However, restrictions apply when archives are specified on the command line (<code>-a</code>) and/or in the configuration file. Firstly, there may be only one set of archives for any one host. Secondly, the hosts of any metrics with host sources must correspond to the host of a set of archives, either on the command line or previously as the source of another metric. </p>
<p> The options <code>-a</code> and <code>-h</code> may not be used together.</p>
<h2>UNIT CONVERSION</h2>
<p> All metrics that have the semantics of counters are automatically converted to rates over the sample time interval. In interactive mode, <code>pmdumptext</code> will also change the units of some metrics so that they are easier to comprehend:</p>
<dl>
<dt>o</p>
<dd> All metrics with space units (bytes to terabytes) are scaled to bytes. Note that 1024 bytes with be represented as 1.02K, not 1.00K.</p>
<dt>o</p>
<dd> Metrics that are counters with time units (nanoseconds to hours) represent time utilization over the sample interval. The unit strings of such metrics is changed to &#8220;Time Utilization&#8221; or abbreviated to &#8220;util&#8221; and the values are normalized to the range zero to one.</dl>
<h2>EXAMPLES</h2>
<p> o To examine the load on two hosts foo and bar, simultaneously: </p>
<pre><code>
$ pmdumptext - il 'foo:kernel.all.load[1]' 'bar:kernel.all.load[1]' Source foo bar
                   Wed Jul 30 11 : 37 : 53 0.309 0.409 Wed Jul 30 11 : 37 : 54 0.309 0.409 Wed Jul 30 11 : 37 : 55 0.309 0.409
</code></pre>
<p> o To output the memory utilization on a remote host called bong with a simpler timestamp: </p>
<pre>
$ pmdumptext -imu -h bong -f '%H:%M:%S' mem.util
  Metric        kernel  fs_ctl  _dirty  _clean    free    user
   Units             b       b       b       b       b       b
09:32:28         8.98M   0.97M   0.00    3.90M   7.13M  46.13M
09:32:29         8.99M   0.98M   0.00    5.71M   5.39M  46.03M
09:32:30         8.99M   1.07M   0.00    5.81M   4.55M  46.69M
09:32:31         9.03M   1.16M   0.00    6.45M   3.48M  47.00M
09:32:32         9.09M   1.18M  20.48K   6.23M   3.29M  47.30M
</pre>
<p> o To dump all metrics collected in an archive at a 30 second interval to a file for processing by another tool: </p>
<pre>
$ pminfo -a archive | pmdumptext -t 30s -m -a archive &gt; outfile
</pre>
<h2>FILES</h2>
<dl>
<dt><code>$PCP_VAR_DIR/pmns/*</code></p>
<dd> default PMNS specification files</dl>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pmchart/">pmchart</a></code>(1), <code><a href="/docs/linux/man/1-pmtime/">pmtime</a></code>(1), <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1), <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1), <code><a href="/docs/linux/man/1-pmlogextract/">pmlogextract</a></code>(1), <code><a href="/docs/linux/man/1-pmrep/">pmrep</a></code>(1), <code><a href="/docs/linux/man/1-pmval/">pmval</a></code>(1), <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3) and <code><a href="/docs/linux/man/7-environ/">environ</a></code>(7). </p>
<h2>Index</h2>
