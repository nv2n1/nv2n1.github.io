---
title: "pmdumplog(1)"
name: "pmdumplog"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmdumplog/"
description: "pmdumplog – dump internal details of a performance metrics archive log"
---

<h2>NAME</h2>
<p> <code>pmdumplog</code> &#8211; dump internal details of a performance metrics archive log</p>
<h2>SYNOPSIS</h2>
<p> <code>pmdumplog</code> [<code>-adilLmMrstxz</code>] [<code>-n</code> <i>pmnsfile</i>] [<code>-S</code> <i>starttime</i>] [<code>-T</code> <i>endtime</i>] [<code>-Z</code> <i>timezone</i>] <i>archive</i> [<i>metricname</i> &#8230;]<br />
 <code>pmdumplog</code> [<code>-v</code> <i>file</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>pmdumplog</code> dumps assorted control, metadata, index and state information from the files of a Performance Co-Pilot (PCP) archive log. The archive log has the base name <i>archive</i> and must have been previously created using <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1). </p>
<p> Normally <code>pmdumplog</code> operates on the distributed Performance Metrics Name Space (PMNS), however if the <code>-n</code> option is specified an alternative local PMNS is loaded from the file <i>pmnsfile.</i> </p>
<p> If any <i>metricname</i> arguments appear, the report will be restricted to information relevant to the named performance metrics. If <i>metricname</i> is a non-leaf node in the namespace (see <code><a href="/docs/linux/man/5-pmns/">pmns</a></code>(5)), then <code>pmdumplog</code> will recursively descend the archive&#8217;s namespace and report on all leaf nodes. </p>
<p> The options control the specific information to be reported.</p>
<dl>
<dt><code>-a</code></p>
<dd> Report everything, i.e. the flags <code>-d</code>, <code>-i</code>, <code>-l</code>, <code>-m</code>, <code>-s</code> and <code>-t</code>.</p>
<dt><code>-d</code></p>
<dd> Display the metadata and descriptions for those performance metrics that appear at least once in the archive: see <code><a href="/docs/linux/man/3-pmlookupdesc/">pmLookupDesc</a></code>(3) for more details on the metadata describing metrics.</p>
<dt><code>-i</code></p>
<dd> Display the instance domains, and any variations in their instance members over the duration of the archive: see <code><a href="/docs/linux/man/3-pmgetindom/">pmGetInDom</a></code>(3) for more details on instance domains.</p>
<dt><code>-l</code></p>
<dd> Dump the archive label, showing the log format version, the time and date for the start and (current) end of the archive, and the host from which the performance metrics values were collected.</p>
<dt><code>-L</code></p>
<dd> Like <code>-l</code>, just a little more verbose.</p>
<dt><code>-m</code></p>
<dd> Print the values for the performance metrics from the archive. This is the default display option.</p>
<dl>
<dt>
<dd>
<p> Metrics without an instance domain are reported as: </p>
<p> &nbsp;<wbr>&nbsp;<wbr> [<i>timestamp</i>] <i>metric-id</i> (<i>metric-name</i>): <code>value1</code> <i>value2</i> </p>
<p> Metrics with an instance domain are reported as: </p>
<p> &nbsp;<wbr>&nbsp;<wbr> [<i>timestamp</i>] <i>metric-id</i> (<i>metric-name</i>): </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> <code>inst</code> [<i>internal-id</i> <code>or</code> &quot;<i>external-id</i>&quot;] <code>value1</code> <i>value2</i> </p>
<p> The <i>timestamp</i> is only reported for the first metric in a group of metrics sharing the same timestamp.</dl>
<dt><code>-M</code></p>
<dd> If no <i>metricname</i> is specified then <i>&lt;mark&gt; </i> records are reported when they are found in the <i>archive</i>. If <i>metricname</i> arguments are specified, then <i>&lt;mark&gt;</i> records are not reported by default. The <code>-M</code> option forces <i>&lt;mark&gt;</i> records to be reported, even when <i>metricname</i> arguments are specified.</p>
<dl>
<dt>
<dd>
<p> <i>&lt;mark&gt;</i> records are inserted into a PCP archive log by <code><a href="/docs/linux/man/1-pmlogextract/">pmlogextract</a></code>(1) to indicate a temporal discontinuity in the time-series of metric values.</dl>
<dt><code>-r</code></p>
<dd> Process the archive in reverse order, from most recent to oldest recorded metric values.</p>
<dt><code>-S</code></p>
<dd> When using the <code>-m</code> option, the report will be restricted to those records logged at or after <i>starttime</i>. Refer to <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1) for a complete description of the syntax for <i>starttime</i>.</p>
<dt><code>-s</code></p>
<dd> Report the size in bytes of each physical record in the archive.</p>
<dt><code>-T</code></p>
<dd> When using the <code>-m</code> option, the report will be restricted to those records logged before or at <i>endtime</i>. Refer to <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1) for a complete description of the syntax for <i>endtime</i>.</p>
<dt><code>-t</code></p>
<dd> Dump the temporal index that is used to provide accelerated access to large archive files.</p>
<dl>
<dt>
<dd>
<p> The integrity of the index will also be checked. If the index is found to be corrupted, the &#8220;*.index&#8221; file can be renamed or removed and the archive will still be accessible, however retrievals may take longer without the index. Note however that a corrupted temporal index is usually indicative of a deeper malaise that may infect all files in a PCP archive.</dl>
<dt><code>-v</code></p>
<dd> Verbose mode. Dump the records from a physical archive file in hexadecimal format. In this case <i>file</i> is the name of a single file, usually a basename (as would otherwise appear as the <i>archive</i> command line argument), concatenated with &#8220;.&#8221; followed by one of <code>meta</code> (the metadata), <code>index</code> (the temporal index), or a digit (one of the volumes of metric values). </p>
<p> Use of <code>-v</code> precludes the use of all other options and arguments.</p>
<dt><code>-x</code></p>
<dd> Extended timestamp reporting format that includes the day of the week, day of the month, month and year in addition to the (default) hours, minutes and seconds time. This is useful for archives that span multiple days.</p>
<dl>
<dt>
<dd>
<p> A second -x option will also report the timestamp as an offset from the start of the archive in units of seconds. This is useful in conjunction with debug diagnostics from the archive handling routines in <i>libpcp</i>.</dl>
</dl>
<p> By default, <code>pmdumplog</code> reports the time of day according to the local timezone on the system where <code>pmdumplog</code> is run. The <code>-Z</code> option changes the timezone to <i>timezone</i> in the format of the environment variable <code>TZ</code> as described in <code><a href="/docs/linux/man/7-environ/">environ</a></code>(7). The <code>-z</code> option changes the timezone to the local timezone at the host that is the source of the performance metrics, as specified in the label record of the archive log.</p>
<h2>FILES</h2>
<dl>
<dt><code>$PCP_VAR_DIR/pmns/</code><i>*</i></p>
<dd> default local PMNS specification files</p>
<dt><code>$PCP_LOG_DIR/pmlogger/</code><i>hostname</i></p>
<dd> Default directory for PCP archives containing performance metric values collected from the host <i>hostname</i>.</dl>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), <code><a href="/docs/linux/man/1-pmlogcheck/">pmlogcheck</a></code>(1), <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1), <code><a href="/docs/linux/man/1-pmlogger_check/">pmlogger_check</a></code>(1), <code><a href="/docs/linux/man/1-pmlogger_daily/">pmlogger_daily</a></code>(1), <code><a href="/docs/linux/man/1-pmloglabel/">pmloglabel</a></code>(1), <code><a href="/docs/linux/man/1-pmlogextract/">pmlogextract</a></code>(1), <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmgetindom/">pmGetInDom</a></code>(3), <code><a href="/docs/linux/man/3-pmlookupdesc/">pmLookupDesc</a></code>(3), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5), <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5) and <code><a href="/docs/linux/man/5-pmns/">pmns</a></code>(5). </p>
<h2>Index</h2>
