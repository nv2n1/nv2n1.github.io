---
title: "pmlogextract(1)"
name: "pmlogextract"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmlogextract/"
description: "pmlogextract – reduce, extract, concatenate and merge Performance Co-Pilot archives"
---

<h2>NAME</h2>
<p> <code>pmlogextract</code> &#8211; reduce, extract, concatenate and merge Performance Co-Pilot archives</p>
<h2>SYNOPSIS</h2>
<p> <code>pmlogextract</code> [<code>-dfwz</code>] [<code>-c</code> <i>configfile</i>] [<code>-S</code> <i>starttime</i>] [<code>-s</code> <i>samples</i>] [<code>-T</code> <i>endtime</i>] [<code>-v</code> <i>volsamples</i>] [<code>-Z</code> <i>timezone</i>] <i>input</i> [&#8230;] <i>output</i></p>
<h2>DESCRIPTION</h2>
<p> <code>pmlogextract</code> reads one or more Performance Co-Pilot (PCP) archive logs identified by <i>input</i> and creates a temporally merged and/or reduced PCP archive log in <i>output</i>. <i>input</i> is a comma-separated list of names, each of which may be the base name of an archive or the name of a directory containing one or more archives. The nature of merging is controlled by the number of input archive logs, while the nature of data reduction is controlled by the command line arguments. The input(s) must be sets of PCP archive logs created by <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1) with performance data collected from the <code>same</code> host, but usually over different time periods and possibly (although not usually) with different performance metrics being logged. </p>
<p> If only one <i>input</i> is specified, then the default behavior simply copies the input set of PCP archive logs, into the output PCP archive log. When two or more sets of PCP archive logs are specified as <i>input</i>, the sets of logs are merged (or concatenated) and written to <i>output</i>. </p>
<p> In the output archive log a <i>&lt;mark&gt;</i> record will be inserted at a time just past the end of each of the input archive logs to indicate a possible temporal discontinuity between the end of one input archive log and the start of the next input archive log. See the <code>MARK RECORDS</code> section below for more information. There is no <i>&lt;mark&gt;</i> record after the end of the <i>last</i> (in temporal order) of the input archive logs.</p>
<h2>COMMAND LINE OPTIONS</h2>
<p> The command line options for <code>pmlogextract</code> are as follows: </p>
<dl>
<dt><code>-c</code><i> configfile</i></p>
<dd> Extract only the metrics specified in <i>configfile</i> from the <i>input</i> PCP archive log(s). The <i>configfile</i> syntax accepted by <code>pmlogextract</code> is explained in more detail in the <code>Configuration File Syntax</code> section.</dl>
<dl>
<dt><code>-d</code></p>
<dd> Desperate mode. Normally if a fatal error occurs, all trace of the partially written PCP archive <i>output</i> is removed. With the <code>-d</code> option, the <i>output</i> archive log is not removed.</dl>
<dl>
<dt><code>-f</code></p>
<dd> For most common uses, all of the input archive logs will have been collected in the same timezone. But if this is not the case, then <code>pmlogextract</code> must choose one of the timezones from the input archive logs to be used as the timezone for the output archive log. The default is to use the timezone from the <i>last</i> input archive log. The <code>-f</code> option forces the timezone from the <i>first</i> input archive log to be used.</p>
<dt><code>-S</code><i> starttime</i></p>
<dd> Define the start of a time window to restrict the samples retrieved or specify a &#8220;natural&#8221; alignment of the output sample times; refer to <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1). See also the <code>-w</code> option.</dl>
<dl>
<dt><code>-s</code><i> samples</i></p>
<dd> The argument <i>samples</i> defines the number of samples to be written to <i>output</i>. If <i>samples</i> is 0 or <code>-s</code> is not specified, <code>pmlogextract</code> will sample until the end of the PCP archive log, or the end of the time window as specified by <code>-T</code>, whichever comes first. The <code>-s</code> option will override the <code>-T</code> option if it occurs sooner.</dl>
<dl>
<dt><code>-T</code><i> endtime</i></p>
<dd> Define the termination of a time window to restrict the samples retrieved or specify a &#8220;natural&#8221; alignment of the output sample times; refer to <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1). See also the <code>-w</code> option.</dl>
<dl>
<dt><code>-v</code><i> volsamples</i></p>
<dd> The <i>output</i> archive log is potentially a multi-volume data set, and the <code>-v</code> option causes <code>pmlogextract</code> to start a new volume after <i>volsamples</i> log records have been written to the archive log.</p>
<dl>
<dt>
<dd>
<p> Independent of any <code>-v</code> option, each volume of an archive is limited to no more than 2^31 bytes, so <i>pmlogextract</i> will automatically create a new volume for the archive before this limit is reached.</dl>
</dl>
<dl>
<dt><code>-w</code></p>
<dd> Where <code>-S</code> and <code>-T</code> specify a time window within the same day, the <code>-w</code> flag will cause the data within the time window to be extracted, for every day in the archive log. For example, the options <code>-w -S @11:00 -T @15:00</code> specify that <code>pmlogextract</code> should include archive log records only for the periods from 11am to 3pm on each day. When <code>-w</code> is used, the <i>output</i> archive log will contain <i>&lt;mark&gt;</i> records to indicate the temporal discontinuity between the end of one time window and the start of the next.</dl>
<dl>
<dt><code>-Z</code><i> timezone</i></p>
<dd> Use <i>timezone</i> when displaying the date and time. <i>Timezone</i> is in the format of the environment variable <code>TZ</code> as described in <code><a href="/docs/linux/man/7-environ/">environ</a></code>(7).</dl>
<dl>
<dt><code>-z</code></p>
<dd> Use the local timezone of the host from the input archive logs. The default is to initially use the timezone of the local host.</dl>
<h2>CONFIGURATION FILE SYNTAX</h2>
<p> The <i>configfile</i> contains metrics of interest &#8211; only those metrics (or instances) mentioned explicitly or implicitly in the configuration file will be included in the <i>output</i> archive. Each specifications must begin on a new line, and may span multiple lines in the configuration file. Instances may also be specified, but they are optional. The format for each specification is </p>
<p>&nbsp;<wbr>&nbsp;<wbr>metric&nbsp;<wbr>[[instance[,instance&#8230;]]] </p>
<p> where <i>metric</i> may be a leaf or a non-leaf name in the Performance Metrics Name Space (PMNS, see <code><a href="/docs/linux/man/5-pmns/">pmns</a></code>(5)). If a metric refers to a non-leaf node in the PMNS, <code>pmlogextract</code> will recursively descend the PMNS and include all metrics corresponding to descendent leaf nodes. </p>
<p> Instances are optional, and may be specified as a list of one or more space (or comma) separated names, numbers or strings (enclosed in single or double quotes). Elements in the list that are numbers are assumed to be internal instance identifiers &#8211; see <code><a href="/docs/linux/man/3-pmgetindom/">pmGetInDom</a></code>(3) for more information. If no instances are given, then <code>all</code> instances of the associated metric(s) will be extracted. </p>
<p> Any additional white space is ignored and comments may be added with a `#&#8217; prefix.</p>
<h2>CONFIGURATION FILE EXAMPLE</h2>
<p> This is an example of a valid <i>configfile</i>: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>#<br />
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>config file for pmlogextract<br />
&nbsp;<wbr>&nbsp;<wbr># </p>
<p>&nbsp;<wbr>&nbsp;<wbr>kernel.all.cpu<br />
&nbsp;<wbr>&nbsp;<wbr>kernel.percpu.cpu.sys&nbsp;<wbr>[&quot;cpu0&quot;,&quot;cpu1&quot;]<br />
&nbsp;<wbr>&nbsp;<wbr>disk.dev&nbsp;<wbr>[&quot;dks0d1&quot;]</p>
<h2>MARK RECORDS</h2>
<p> When more than one input archive log contributes performance data to the output archive log, then <i>&lt;mark&gt;</i> records are inserted to indicate a possible discontinuity in the performance data. </p>
<p> A <i>&lt;mark&gt;</i> record contains a timestamp and no performance data and is used to indicate that there is a time period in the PCP archive log where we do not know the values of <code>any</code> performance metrics, because there was no <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1) collecting performance data during this period. Since these periods are often associated with the restart of a service or <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) or a system, there may be considerable doubt as to the continuity of performance data across this time period. </p>
<p> The rationale behind <i>&lt;mark&gt;</i> records may be demonstrated with an example. Consider one input archive log that starts at 00:10 and ends at 09:15 on the same day, and another input archive log that starts at 09:20 on the same day and ends at 00:10 the following morning. This would be a very common case for archives managed and rotated by <code><a href="/docs/linux/man/1-pmlogger_check/">pmlogger_check</a></code>(1) and <code><a href="/docs/linux/man/1-pmlogger_daily/">pmlogger_daily</a></code>(1). </p>
<p> The output archive log created by <code>pmlogextract</code> would contain:<br />
 00:10.000<tt>&nbsp;<wbr>&nbsp;<wbr></tt>first record from first input archive log</p>
<p> &#8230;<br />
 09:15.000<tt>&nbsp;<wbr>&nbsp;<wbr></tt>last record from first input archive log</p>
<p> 09:15.001<tt>&nbsp;<wbr>&nbsp;<wbr></tt>&lt;mark&gt; record</p>
<p> 09:20.000<tt>&nbsp;<wbr>&nbsp;<wbr></tt>first record from second input archive log</p>
<p> &#8230;<br />
 01:10.000<tt>&nbsp;<wbr>&nbsp;<wbr></tt>last record from second input archive log</p>
<p> The time period where the performance data is missing starts just after 09:15 and ends just before 09:20. When the output archive log is processed with any of the PCP reporting tools, the <i>&lt;mark&gt;</i> record is used to indicate a period of missing data. For example using the output archive above, imagine one was reporting the average I/O rate at 30 minute intervals aligned on the hour and half-hour. The I/O count metric is a counter, so the average I/O rate requires two valid values from consecutive sample times. There would be values for all the intervals ending at 09:00, then no values at 09:30 because of the <i>&lt;mark&gt;</i> record, then no values at 10:00 because the &#8220;prior&#8221; value at 09:30 is not available, then the rate would be reported again at 10:30 and continue every 30 minutes until the last reported value at 01:00. </p>
<p> The presence of <i>&lt;mark&gt;</i> records in a PCP archive log can be established using <code><a href="/docs/linux/man/1-pmdumplog/">pmdumplog</a></code>(1) where a timestamp and the annotation <code>&lt;mark&gt;</code> is used to indicate a <i>&lt;mark&gt;</i> record.</p>
<h2>METADATA CHECKS</h2>
<p> When more than one <i>input</i> archive set is specified, <code>pmlogextract</code> performs a number of checks to ensure the metadata is consistent for metrics appearing in more than one of the <i>input</i> archive sets. These checks include:</p>
<dl>
<dt>*</p>
<dd> metric data type is the same</p>
<dt>*</p>
<dd> metric semantics are the same</p>
<dt>*</p>
<dd> metric units are the same</p>
<dt>*</p>
<dd> metric is either always singular or always has the same instance domain</p>
<dt>*</p>
<dd> metrics with the same name have the same PMID</p>
<dt>*</p>
<dd> metrics with the same PMID have the same name</dl>
<p> If any of these checks fail, <code>pmlogextract</code> reports the details and aborts without creating the <i>output</i> archive. </p>
<p> To address these semantic issues, use <code><a href="/docs/linux/man/1-pmlogrewrite/">pmlogrewrite</a></code>(1) to translate the <i>input</i> archives into equivalent archives with consistent metdadata before using <code>pmlogextract</code>.</p>
<h2>FILES</h2>
<p> For each of the <i>input</i> and <i>output</i> archive logs, several physical files are used.</p>
<dl>
<dt><i>archive</i><code>.meta</p>
<dd> metadata (metric descriptions, instance domains, etc.) for the archive log</p>
<dt></code><i>archive</i><code>.0</p>
<dd> initial volume of metrics values (subsequent volumes have suffixes 1</code>, <code>2</code>, &#8230;) &#8211; for <i>input</i> these files may have been previously compressed with <code><a href="/docs/linux/man/1-bzip2/">bzip2</a></code>(1) or <code><a href="/docs/linux/man/1-gzip/">gzip</a></code>(1) and thus may have an additional <code>.bz2</code> or <code>.gz</code> suffix.</p>
<dt><i>archive</i><code>.index</p>
<dd> temporal index to support rapid random access to the other files in the archive log.</dl>
<p> </code></p>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), <code><a href="/docs/linux/man/1-pmdumplog/">pmdumplog</a></code>(1), <code><a href="/docs/linux/man/1-pmlc/">pmlc</a></code>(1), <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1), <code><a href="/docs/linux/man/1-pmlogreduce/">pmlogreduce</a></code>(1), <code><a href="/docs/linux/man/1-pmlogrewrite/">pmlogrewrite</a></code>(1), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5) and <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5).</p>
<h2>DIAGNOSTICS</h2>
<p> All error conditions detected by <code>pmlogextract</code> are reported on <i>stderr</i> with textual (if sometimes terse) explanation. </p>
<p> Should one of the input archive logs be corrupted (this can happen if the <code>pmlogger</code> instance writing the log suddenly dies), then <code>pmlogextract</code> will detect and report the position of the corruption in the file, and any subsequent information from that archive log will not be processed. </p>
<p> If any error is detected, <code>pmlogextract</code> will exit with a non-zero status.</p>
<h2>CAVEATS</h2>
<p> The preamble metrics (pmcd.pmlogger.archive, pmcd.pmlogger.host, and pmcd.pmlogger.port), which are automatically recorded by <code>pmlogger</code> at the start of the archive, may not be present in the archive output by <code>pmlogextract</code>. These metrics are only relevant while the archive is being created, and have no significance once recording has finished. </p>
<h2>Index</h2>
