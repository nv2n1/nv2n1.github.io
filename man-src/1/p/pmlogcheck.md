---
title: "pmlogcheck(1)"
name: "pmlogcheck"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmlogcheck/"
description: "pmlogcheck – checks for invalid data in a PCP archive"
---

<h2>NAME</h2>
<p> <code>pmlogcheck</code> &#8211; checks for invalid data in a PCP archive</p>
<h2>SYNOPSIS</h2>
<p> <code>pmlogcheck</code> [<code>-lz</code>] [<code>-n</code> <i>pmnsfile</i>] [<code>-S</code> <i>start</i>] [<code>-T</code> <i>finish</i>] [<code>-Z</code> <i>timezone</i>] <i>archive</i></p>
<h2>DESCRIPTION</h2>
<p> <code>pmlogcheck</code> prints information about the nature of any invalid data which it detects in the files of a PCP archive. </p>
<p> The archive has the base name <i>archive</i> and must have been previously created using <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1). </p>
<p> Normally <code>pmlogcheck</code> operates on the default Performance Metrics Name Space (<code><a href="/docs/linux/man/5-pmns/">pmns</a></code>(5)), however if the <code>-n</code> option is specified an alternative namespace is loaded from the file <i>pmnsfile</i>. </p>
<p> The command line options <code>-S</code> and <code>-T</code> can be used to specify a time window over which metrics should be checked in Pass 3 (see below). These options are common to many Performance Co-Pilot tools and are fully described in <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1). </p>
<p> The <code>-l</code> option prints the archive label, showing the log format version, the time and date for the start and (current) end of the archive, and the host from which the performance metrics values were collected. </p>
<p> By default, <code>pmlogcheck</code> reports the time of day according to the local timezone on the system where <code>pmlogcheck</code> is run. The <code>-Z</code> option changes the timezone to <i>timezone</i> in the format of the environment variable <code>TZ</code> as described in <code><a href="/docs/linux/man/7-environ/">environ</a></code>(7). The <code>-z</code> option changes the timezone to the local timezone at the host that is the source of the performance metrics, as specified in the label record of the archive log. </p>
<p> The checking proceeds in a number of passes, each designed to validate progressively more complex semantic relationships between the information in a PCP archive.</p>
<h2>Pass 0</h2>
<p> Each physical file of the PCP archive is processed to ensure the label records are valid and consistent, and that each file contains an integral number of physical records with correct header and trailer fields. </p>
<p> Any errors at this stage are usually fatal. The PCP archive is probably damaged beyond repair, and no more passes of <code>pmlogcheck</code> are attempted.</p>
<h2>Pass 1</h2>
<p> Validates the integrity of the temporal index, usually <i>archive</i><code>.index</code>. </p>
<p> As the temporal index is (strictly speaking) optional, errors at this stage are handled by marking the index as bad and ignoring it for the remainder of the <code>pmlogcheck</code> passes. </p>
<p> Permanent repair can be achieved by removing the temporal index file and then making a copy of the PCP archive using <code><a href="/docs/linux/man/1-pmlogrewrite/">pmlogrewrite</a></code>(1) or <code><a href="/docs/linux/man/1-pmlogextract/">pmlogextract</a></code>(1). This will create a new temporal index for the copied archive as a side-effect.</p>
<h2>Pass 2</h2>
<p> Validates the integrity of the metadata file, usually <i>archive</i><code>.meta</code>.</p>
<h2>Pass 3</h2>
<p> Validates the integrity of each of the log volumes of the PCP archive, usually <i>archive</i><code>.0</code>, <i>archive</i><code>.1</code>, etc. </p>
<p> There is some basic integrity checks to ensure the encoding of values for each metric remains consistent and the values are well formed across all the observations in the archive. </p>
<p> Also the timestamps for the observations are expected to be monotonically increasing as the archive is tranversed. </p>
<p> Additional attention is given to counter metrics (<i>type</i> from <code><a href="/docs/linux/man/3-pmlookupdesc/">pmLookupDesc</a></code>(3) is <code>PM_SEM_COUNTER</code>) which are expected to have monotonically increasing values. If the values are not monotonic increasing this may suggest a counter wrap has happened or there has been some interruption or reset to the underlying source of the performance data that is no captured in the archive. </p>
<p> For each counter metric which has been detected as having wrapped at some point in the archive, <code>pmlogcheck</code> produces output describing the metric name (with instance identifiers where appropriate), the internal storage type for the metric, the value of the metric before the counter wrap (with its associated timestamp), and the value of the metric after the wrap (also with a timestamp). </p>
<p> <code>pmlogcheck</code> produces two different timestamp formats, depending on the interval over which it is run. For an interval greater than 24 hours, the date is displayed in addition to the time at which the counter wrap occurred. If the extent of the data being checked is less than 24 hours, a more precise format is used (time is displayed with millisecond precision, but without the date). </p>
<h2>FILES</h2>
<dl>
<dt><code>$PCP_VAR_DIR/pmns/</code><i>*</i></p>
<dd> default PMNS specification files</p>
<dt><code>$PCP_LOG_DIR/pmlogger/</code><i>hostname</i></p>
<dd> default directory for PCP archives containing performance data collected from the host <i>hostname</i>.</dl>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), <code><a href="/docs/linux/man/1-pmdumplog/">pmdumplog</a></code>(1), <code><a href="/docs/linux/man/1-pmlogextract/">pmlogextract</a></code>(1), <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1), <code><a href="/docs/linux/man/1-pmlogrewrite/">pmlogrewrite</a></code>(1), <code><a href="/docs/linux/man/1-pmlogsummary/">pmlogsummary</a></code>(1), <code><a href="/docs/linux/man/1-pmval/">pmval</a></code>(1), <code><a href="/docs/linux/man/3-pmlookupdesc/">pmLookupDesc</a></code>(3), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5), <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5) and <code><a href="/docs/linux/man/5-pmns/">pmns</a></code>(5).</p>
<h2>DIAGNOSTICS</h2>
<p> All are generated on standard error and are intended to be self- explanatory. </p>
<h2>Index</h2>
