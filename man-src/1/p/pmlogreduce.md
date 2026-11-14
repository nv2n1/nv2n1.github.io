---
title: "pmlogreduce(1)"
name: "pmlogreduce"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmlogreduce/"
description: "pmlogreduce – temporal reduction of Performance Co-Pilot archives"
---

<h2>NAME</h2>
<p> <code>pmlogreduce</code> &#8211; temporal reduction of Performance Co-Pilot archives</p>
<h2>SYNOPSIS</h2>
<p> <code>$PCP_BINADM_DIR/pmlogreduce</code> [<code>-z</code>] [<code>-A</code> <i>align</i>] [<code>-S</code> <i>starttime</i>] [<code>-s</code> <i>samples</i>] [<code>-T</code> <i>endtime</i>] [<code>-t</code> <i>interval</i>] [<code>-v</code> <i>volsamples</i>] [<code>-Z</code> <i>timezone</i>] <i>input</i> <i>output</i></p>
<h2>DESCRIPTION</h2>
<p> <code>pmlogreduce</code> reads one set of Performance Co-Pilot (PCP) archives identified by <i>input</i> and creates a temporally reduced PCP archive in <i>output</i>. <i>input</i> is a comma-separated list of names, each of which may be the base name of an archive or the name of a directory containing one or more archives. The data reduction involves statistical and temporal reduction of samples with an output sampling interval defined by the <code>-t</code> option in the <i>output</i> archive (independent of the sampling intervals in the <i>input</i> archives), and is further controlled by other command line arguments. </p>
<p> For some metrics, temporal data reduction is not going to be helpful, so for metrics with types <code>PM_TYPE_AGGREGATE</code> or <code>PM_TYPE_EVENT</code>, a warning is issued if these metrics are found in <i>input</i> and they will be skipped and not appear in the <i>output</i> archive.</p>
<h2>COMMAND LINE OPTIONS</h2>
<p> The command line options for <code>pmlogreduce</code> are as follows: </p>
<dl>
<dt><code>-A</code><i> align</i></p>
<dd> Specify a &#8220;natural&#8221; alignment of the output sample times; refer to <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1).</dl>
<dl>
<dt><code>-S</code><i> starttime</i></p>
<dd> Define the start of a time window to restrict the samples retrieved from the <i>input</i> archives; refer to <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1).</dl>
<dl>
<dt><code>-s</code><i> samples</i></p>
<dd> The argument <i>samples</i> defines the number of samples to be written to <i>output</i>. If <i>samples</i> is 0 or <code>-s</code> is not specified, <code>pmlogreduce</code> will sample until the end of the set of PCP archives, or the end of the time window as specified by <code>-T</code>, whichever comes first. The <code>-s</code> option will override the <code>-T</code> option if it occurs sooner.</dl>
<dl>
<dt><code>-T</code><i> endtime</i></p>
<dd> Define the termination of a time window to restrict the samples retrieved from the <i>input</i> archives; refer to <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1).</dl>
<dl>
<dt><code>-v</code><i> volsamples</i></p>
<dd> The <i>output</i> archive is potentially a multi-volume data set, and the <code>-v</code> option causes <code>pmlogreduce</code> to start a new volume after <i>volsamples</i> log records have been written to the <i>output</i> archive.</p>
<dl>
<dt>
<dd>
<p> Independent of any <code>-v</code> option, each volume of an archive is limited to no more than 2^31 bytes, so <i>pmlogreduce</i> will automatically create a new volume for the archive before this limit is reached.</dl>
</dl>
<dl>
<dt><code>-t</code><i> interval</i></p>
<dd> Consecutive samples in the <i>output</i> archive will appear with a time delta defined by <i>interval</i>; refer to <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1). Note the default value is 600 (seconds, i.e. 10 minutes).</dl>
<dl>
<dt><code>-Z</code><i> timezone</i></p>
<dd> Use <i>timezone</i> when displaying the date and time, or interpreting the <code>-S</code> and <code>-T</code> options. <i>Timezone</i> is in the format of the environment variable <code>TZ</code> as described in <code><a href="/docs/linux/man/7-environ/">environ</a></code>(7).</dl>
<dl>
<dt><code>-z</code></p>
<dd> Use the local timezone of the host from the <i>input</i> archives when displaying the date and time, or interpreting the <code>-S</code> and <code>-T</code> options. The default is to initially use the timezone of the local host.</dl>
<h2>DATA REDUCTION</h2>
<p> The statistical and temporal reduction follows the following rules:</p>
<dl>
<dt>1.</p>
<dd> Consecutive records from <i>input</i> are read without interpolation, and at most one output record is written for each <i>interval</i>, summarizing the performance data over that period.</p>
<dt>2.</p>
<dd> If the semantics of a metric indicates it is <code>instantaneous</code> or <code>discrete</code> then <i>output</i> value is computed as the arithmetic mean of the observations (if any) over each <i>interval</i>.</p>
<dt>3.</p>
<dd> If the semantics of a metric indicates it is a <code>counter</code> then the following transformations are applied:</p>
<dl>
<dt>
<dd>
<dl>
<dt>a)</p>
<dd> Metrics with 32-bit precision are promoted to 64-bit precision.</p>
<dt>b)</p>
<dd> Any counter wrap (overflow) is noted, and appropriate adjustment made in the value of the metric over each <i>interval</i>. This will be correct in the case of a single counter wrap, but will silently <code>underestimate</code> in the case where more than one counter wrap occurs between consecutive observations in the <i>input</i> archives, and silently <code>overestimate</code> in the case where a counter is reset occurs between consecutive observations in the <i>input</i> archives; unfortunately these situations cannot be detected, but are believed to be rare events for the sort of production monitoring environments where <code>pmlogreduce</code> is most likely to be deployed.</dl>
</dl>
<dt>4.</p>
<dd> Any changes in instance domains, and indeed all metadata, is preserved.</p>
<dt>5.</p>
<dd> Any &#8220;mark&#8221; records in the <i>input</i> archives (as created by <code><a href="/docs/linux/man/1-pmlogextract/">pmlogextract</a></code>(1)) will be preserved in the <i>output</i> archive, so periods where no data is available are maintained, and data interpolation will <code>not</code> occur across these periods when the <i>output</i> archive is subsequently processed with PCP applications.</dl>
<h2>FILES</h2>
<p> For each of the <i>input</i> and <i>output</i> archives, several physical files are used.</p>
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
<p> <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), <code><a href="/docs/linux/man/1-pmdumplog/">pmdumplog</a></code>(1), <code><a href="/docs/linux/man/1-pmlc/">pmlc</a></code>(1), <code><a href="/docs/linux/man/1-pmlogextract/">pmlogextract</a></code>(1), <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5) and <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5).</p>
<h2>DIAGNOSTICS</h2>
<p> All error conditions detected by <code>pmlogreduce</code> are reported on <i>stderr</i> with textual (if sometimes terse) explanation. </p>
<p> Should the <i>input</i> archives be corrupted (this can happen if the <code>pmlogger</code> instance writing the archive suddenly dies), then <code>pmlogreduce</code> will detect and report the position of the corruption in the file, and any subsequent information from the <i>input</i> archives will not be processed. </p>
<p> If any error is detected, <code>pmlogreduce</code> will exit with a non-zero status.</p>
<h2>CAVEATS</h2>
<p> The preamble metrics (pmcd.pmlogger.archive, pmcd.pmlogger.host, and pmcd.pmlogger.port), which are automatically recorded by <code>pmlogger</code> at the start of the archive, may not be present in the archive output by <code>pmlogreduce</code>. These metrics are only relevant while the archive is being created, and have no significance once recording has finished. </p>
<h2>Index</h2>
