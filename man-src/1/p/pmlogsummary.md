---
title: "pmlogsummary(1)"
name: "pmlogsummary"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmlogsummary/"
description: "pmlogsummary – calculate averages of metrics stored in a set of PCP archives"
---

<h2>NAME</h2>
<p> <code>pmlogsummary</code> &#8211; calculate averages of metrics stored in a set of PCP archives</p>
<h2>SYNOPSIS</h2>
<p> <code>pmlogsummary</code> [<code>-abfFHiIlmMNsvxyz</code>] [<code>-B</code> <i>nbins</i>] [<code>-n</code> <i>pmnsfile</i>] [<code>-p</code> <i>precision</i>] [<code>-S</code> <i>starttime</i>] [<code>-T</code> <i>endtime</i>] [<code>-Z</code> <i>timezone</i>] <i>archive</i> [<i>metricname</i> &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>pmlogsummary</code> prints statistical information about metrics of numeric type contained within the files of a set of Performance Co-Pilot (PCP) archive logs. The default output prints time averages for both counter and non-counter metrics. The set of archive logs is identified by <i>archive</i>, which is a comma-separated list of names, each of which may be the base name of an archive or the name of a directory containing one or more archives. The archive logs are typically created using <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1). </p>
<p> The metrics of interest are named in the <i>metricname</i> arguments. If <i>metricname</i> is a non-leaf node in the Performance Metrics Name Space (<code><a href="/docs/linux/man/5-pmns/">pmns</a></code>(5)), then <code>pmlogsummary</code> will recursively descend the PMNS and report on all leaf nodes. If no <i>metricname</i> argument is given, the root of the namespace is used. </p>
<p> Normally <code>pmlogsummary</code> operates on the default <code><a href="/docs/linux/man/5-pmns/">pmns</a></code>(5), however if the <code>-n</code> option is specified an alternative namespace is loaded from the file <i>pmnsfile</i>. </p>
<p> The command line options <code>-S</code> and <code>-T</code> can be used to specify a time window over which metrics should be summarized. These options are common to most Performance Co-Pilot tools and are fully described in <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1). </p>
<p> The remaining options control the specific information to be reported. Metrics with counter semantics are converted to rates before being evaluated.</p>
<dl>
<dt><code>-a</code></p>
<dd> Print all information. This is equivalent to <code>-blmMy</code>.</p>
<dt><code>-b</code></p>
<dd> Print both forms of averaging, that is both stochastic and time averaging.</p>
<dt><code>-B</code></p>
<dd> Print the approximate distribution of values, using histogram bins such that the value range (minimum &#8211; maximum) for each metric is divided equally into <i>nbins</i> bins, and each bin accumulates the frequency of observed values in the corresponding range. Refer to the &#8220;OUTPUT FORMAT&#8221; section below for a description of how the distribution of values is reported).</p>
<dt><code>-f</code></p>
<dd> Spreadsheet format &#8211; the tab character is used to delimit each field printed. This option is intended to allow <code>pmlogsummary</code> output to be imported directly into common spreadsheet applications.</p>
<dt><code>-F</code></p>
<dd> Spreadsheet format &#8211; the comma character is used to delimit each field printed. This option is intended to allow <code>pmlogsummary</code> output to be imported directly into common spreadsheet applications which support the Comma Separated Value (.csv) format.</p>
<dt><code>-H</code></p>
<dd> Print a one-line header at the start showing what each field represents.</p>
<dt><code>-l</code></p>
<dd> Also print the archive label, showing the log format version, the time and date for the start and end of the archive time window, and the host from which the performance metrics values were collected.</p>
<dt><code>-i</code></p>
<dd> Also print the time at which the minimum value was logged. The format of this timestamp is described in the &#8220;OUTPUT FORMAT&#8221; section below.</p>
<dt><code>-I</code></p>
<dd> Also print the time at which the maximum value was logged. The format of this timestamp is described in the &#8220;OUTPUT FORMAT&#8221; section below.</p>
<dt><code>-m</code></p>
<dd> Also print the minimum logged value for each metric.</p>
<dt><code>-M</code></p>
<dd> Also print the maximum logged value for each metric.</p>
<dt><code>-s</code></p>
<dd> Print (only) the sum of all logged values for each metric.</p>
<dt><code>-N</code></p>
<dd> Suppress any warnings resulting from individual archive fetches (default).</p>
<dt><code>-p</code></p>
<dd> Print all floating point numbers with <i>precision</i> digits after the decimal place.</p>
<dt><code>-v</code></p>
<dd> Report (verbosely) on warnings resulting from individual archive fetches.</p>
<dt><code>-x</code></p>
<dd> Print stochastic averages instead of the default (time averages).</p>
<dt><code>-y</code></p>
<dd> Also print the number of samples encountered in the set of archives for each metric.</dl>
<p> By default, <code>pmlogsummary</code> reports the time of day according to the local timezone on the system where <code>pmlogsummary</code> is run. The <code>-Z</code> option changes the timezone to <i>timezone</i> in the format of the environment variable <code>TZ</code> as described in <code><a href="/docs/linux/man/7-environ/">environ</a></code>(7). The <code>-z</code> option changes the timezone to the local timezone at the host that is the source of the performance metrics, as specified in the label record of the archive log.</p>
<h2>OUTPUT FORMAT</h2>
<p> The <code>pmlogsummary</code> output format is spartan as it is intended to be post-processed with standard tools. This means that there is no annotation associated with each output field which would make processing harder. The intention is that <code>pmlogsummary</code> output be massaged into a format which can be used by a spreadsheet program, is suitable for inclusion in a web page, or whatever. </p>
<p> For each metric, <code>pmlogsummary</code> produces a single output line as follows: </p>
<pre>
<i>metricname</i>  <i>value(s)</i> <i>units</i>
</pre>
<p> For metrics with multiple instances, <code>pmlogsummary</code> produces multiple lines of output as follows: </p>
<pre><code>
metricname["instance 1"] value(s) units
    metricname["instance 2"] value(s) units
    metricname["instance N"] value(s) units
</code></pre>
<p> The printed <i>value(s)</i> for each metric always follow this order: stochastic average, time average, minimum, minimum timestamp, maximum, maximum timestamp, count, [bin 1 range], bin 1 count, &#8230; [bin <i>nbins</i> range], bin <i>nbins</i> count. The individual values for each metric are space-separated (unless the <code>-f</code> option is used). </p>
<p> All counter metrics which are measured in units of time will be converted to seconds before being rate converted and used in the <code>pmlogsummary</code> calculations. The values calculated for these metrics are also printed in seconds. </p>
<p> The units will be displayed in the format described by <code><a href="/docs/linux/man/3-pmunitsstr/">pmUnitsStr</a></code>(3). </p>
<p> Given either of the <code>-i</code> or <code>-I</code> options, <code>pmlogsummary</code> produces two different timestamp formats, depending on the interval over which it is run. For an interval greater than 24 hours, the date is displayed in addition to the time at which the maxima and/or minima occurred. If the extent of the data being checked is less than 24 hours, a more precise format is used (time is displayed with millisecond precision, but without the date). </p>
<h2>NOTES</h2>
<p> The average for an individual metric is calculated as follows: </p>
<p> Non-counter metrics are averaged using stochastic averaging &#8211; each observation has an equal weighting towards the calculation of the average (the sum of all values divided by the total number of values, for each metric). </p>
<p> Counter metrics are averaged using time averaging (by default), but the <code>-x</code> option can be used to specify that counters be averaged using the stochastic method instead. When calculating a time average, the sum of the product of each sample value multiplied by the time difference between each sample, is divided by the total time over which that metric was logged. </p>
<p> Counter metrics whose measurements do not span 90% of the set of archives will be printed with the metric name prefixed by an asterisk (*). </p>
<h2>EXAMPLE</h2>
<pre><code>
$ pmlogsummary - aN - p 1 - B 3 surf network.interface.out.bytes Log Label(Log Format Version 1) Performance metrics from host www.sgi.com commencing Tue Jan 14 20 : 50 : 50.317 1997 ending Wed Jan 29 10 : 13 : 07.387 1997 network.interface.out.bytes["xpi0"] 202831.3 202062.5 20618.7 1235067.7 971 [&lt;= 425435.0] 912 [&lt;= 830251.4] 42 [&lt;= 1235067.7] 17 byte / sec network.interface.out.bytes["xpi1"] 0.0 0.0 0.0 0.0 1033 [&lt;= 0.0] 1033 [] 0 [] 0 byte / sec network.interface.out.bytes["et0"] 0.0 0.0 0.0 0.0 1033 [&lt;= 0.0] 1033 [] 0 [] 0 byte / sec network.interface.out.bytes["lo0"] 899.0 895.2 142.6 9583.1 1031 [&lt;= 3289.4] 1027 [&lt;= 6436.2] 3 [&lt;= 9583.1] 1 byte / sec
</code></pre>
<p> A description of each field in the first line of statistical output, which describes one instance of the network.interface.out.bytes metric, follows: <center></p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center>Field</td>
<td ALIGN=center>Meaning
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>[&quot;xpi0&quot;]</td>
<td>instance name
</td>
</tr>
<tr VALIGN=top>
<td>202831.3</td>
<td>stochastic average
</td>
</tr>
<tr VALIGN=top>
<td>202062.5</td>
<td>time average
</td>
</tr>
<tr VALIGN=top>
<td>20618.7</td>
<td>minimum value
</td>
</tr>
<tr VALIGN=top>
<td>1235067.7</td>
<td>maximum value
</td>
</tr>
<tr VALIGN=top>
<td>971</td>
<td>total number of values for this instance
</td>
</tr>
<tr VALIGN=top>
<td>[&lt;=425435.0]</td>
<td>range for first bin (20618.7-425435.0)
</td>
</tr>
<tr VALIGN=top>
<td>912</td>
<td>number of values in first bin
</td>
</tr>
<tr VALIGN=top>
<td>[&lt;=830251.4]</td>
<td>range for second bin (425435.0-830251.4)
</td>
</tr>
<tr VALIGN=top>
<td>42</td>
<td>number of values in second bin
</td>
</tr>
<tr VALIGN=top>
<td>[&lt;=1235067.7]</td>
<td>range for third bin (830251.4-1235067.7)
</td>
</tr>
<tr VALIGN=top>
<td>17</td>
<td>number of values in third bin
</td>
</tr>
<tr VALIGN=top>
<td>byte / sec</td>
<td>base units for this metric
</td>
</tr>
</table>
</table>
<p></center></p>
<h2>FILES</h2>
<dl>
<dt><code>$PCP_VAR_DIR/pmns/</code><i>*</i></p>
<dd> default PMNS specification files</p>
<dt><code>$PCP_LOG_DIR/pmlogger/</code><i>hostname</i></p>
<dd> Default directory for PCP archives containing performance metric values collected from the host <i>hostname</i>.</dl>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), <code><a href="/docs/linux/man/1-pmchart/">pmchart</a></code>(1), <code><a href="/docs/linux/man/1-pmdumptext/">pmdumptext</a></code>(1), <code><a href="/docs/linux/man/1-pmlogextract/">pmlogextract</a></code>(1), <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1), <code><a href="/docs/linux/man/1-pmrep/">pmrep</a></code>(1), <code><a href="/docs/linux/man/1-pmval/">pmval</a></code>(1), <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmunitsstr/">pmUnitsStr</a></code>(3) and <code><a href="/docs/linux/man/5-pmns/">pmns</a></code>(5).</p>
<h2>DIAGNOSTICS</h2>
<p> All are generated on standard error and are intended to be self- explanatory. </p>
<h2>Index</h2>
