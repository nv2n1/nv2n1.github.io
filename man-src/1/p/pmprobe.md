---
title: "pmprobe(1)"
name: "pmprobe"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmprobe/"
description: "pmprobe – lightweight probe for performance metrics"
---

<h2>NAME</h2>
<p> <code>pmprobe</code> &#8211; lightweight probe for performance metrics</p>
<h2>SYNOPSIS</h2>
<p> <code>pmprobe</code> [<code>-fIiLVvz</code>] [<code>-a</code> <i>archive</i>] [<code>-h</code> <i>hostname</i>] [<code>-K</code> <i>spec</i>] [<code>-n</code> <i>pmnsfile</i>] [<code>-O</code> <i>time</i>] [<code>-Z</code> <i>timezone</i>] [<i>metricname</i> &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>pmprobe</code> determines the availability of performance metrics exported through the facilities of the Performance Co-Pilot (PCP). </p>
<p> The metrics of interest are named in the <i>metricname</i> arguments. If <i>metricname</i> is a non-leaf node in the Performance Metrics Name Space (<code><a href="/docs/linux/man/5-pmns/">pmns</a></code>(5)), then <code>pmprobe</code> will recursively descend the PMNS and report on all leaf nodes. If no <i>metricname</i> argument is given, the root of the namespace is used. </p>
<p> The output format is spartan and intended for use in wrapper scripts creating configuration files for other PCP tools. By default, there is one line of output per metric, with the metric name followed by a count of the number of available values. Error conditions are encoded as a negative value count (as per the <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3) protocols, but may be decoded using <code><a href="/docs/linux/man/1-pmerr/">pmerr</a></code>(1)) and followed by a textual description of the error. </p>
<p> Unless directed to another host by the <code>-h</code> option, <code>pmprobe</code> will contact the Performance Metrics Collector Daemon (PMCD) on the local host. </p>
<p> The <code>-a</code> option causes <code>pmprobe</code> to use the specified set of archives rather than connecting to a PMCD. The argument is a comma-separated list of names, each of which may be the base name of an archive or the name of a directory containing one or more archives. The <code>-a</code> and <code>-h</code> options are mutually exclusive. </p>
<p> The <code>-L</code> option causes <code>pmprobe</code> to use a local context to collect metrics from PMDAs on the local host without PMCD. Only some metrics are available in this mode. The <code>-a</code>,<code>-h</code> and <code>-L</code> options are mutually exclusive. </p>
<p> Normally <code>pmprobe</code> operates on the distributed Performance Metrics Name Space (PMNS), however, if the <code>-n</code> option is specified an alternative local PMNS file is loaded from the file <i>pmnsfile</i>. </p>
<p> Other options control the output of additional information when one or more values is available.</p>
<dl>
<dt><code>-f</code></p>
<dd> When used with <code>-i</code> or <code>-I</code> the set of instances reported will be all of those known at the source of the performance data. By default the set of reported instances are those for which values are currently available, which may be smaller than the set reported with <code>-f</code>.</p>
<dt><code>-I</code></p>
<dd> Report the external identifiers for each instance. The literal string <code>PM_IN_NULL</code> is reported for singular metrics.</p>
<dt><code>-i</code></p>
<dd> Report the internal identifiers for each instance. The values are in decimal and prefixed by &#8220;?&#8221;. As a special case, the literal string <code>PM_IN_NULL</code> is reported for singular metrics.</p>
<dt><code>-K</code></p>
<dd> When using the <code>-L</code> option to fetch metrics from a local context, the <code>-K</code> option may be used to control the DSO PMDAs that should be made accessible. The <i>spec</i> argument conforms to the syntax described in <code><a href="/docs/linux/man/3-__pmspeclocalpmda/">__pmSpecLocalPMDA</a></code>(3). More than one <code>-K</code> option may be used.</p>
<dt><code>-O</code></p>
<dd> When used in conjunction with an archive source of metrics and the <code>-v</code> option the <i>time</i> argument defines a time origin at which the metrics should be fetched from the archive(s). Refer to <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1) for a complete description of this option, and the syntax for the <i>time</i> argument.</p>
<dt><code>-v</code></p>
<dd> Report the value for each instance, as per the formatting rules of <code><a href="/docs/linux/man/3-pmprintvalue/">pmPrintValue</a></code>(3). When fetching from a set of archives, only those instances present in the first archive record for a metric will be displayed; see also the <code>-O</code> option.</dl>
<p> The <code>-v</code> option is mutually exclusive with either the <code>-I</code> or <code>-i</code> options. </p>
<p> The <code>-V</code> option provides a cryptic summary of the number of messages sent and received across the PMAPI interface.</p>
<h2>EXAMPLES</h2>
<pre>
$ pmprobe disk.dev
disk.dev.read 2
disk.dev.write 2
disk.dev.total 2
disk.dev.blkread 2
disk.dev.blkwrite 2
disk.dev.blktotal 2
disk.dev.active 2
disk.dev.response 2
$ pmprobe -I disk.dev.read disk.dev.write disk.all.total
disk.dev.read 2 &quot;dks0d1&quot; &quot;dks0d2&quot;
disk.dev.write 2 &quot;dks0d1&quot; &quot;dks0d2&quot;
disk.all.total 1 PM_IN_NULL
$ pmprobe -v pmcd.numagents pmcd.version pmcd.control.timeout
pmcd.numagents 1 9
pmcd.version 1 &quot;2.0 beta-1&quot;
pmcd.control.timeout 1 5
$ pmprobe -v disk.dev.total disk.all.total
disk.dev.total -1012 Unknown metric name
disk.all.total 1 4992466
</pre>
<h2>FILES</h2>
<dl>
<dt><code>$PCP_VAR_DIR/pmns/</code><i>*</i></p>
<dd> default PMNS specification files</dl>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1), <code><a href="/docs/linux/man/1-pmdumplog/">pmdumplog</a></code>(1), <code><a href="/docs/linux/man/1-pminfo/">pminfo</a></code>(1), <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmerrstr/">pmErrStr</a></code>(3), <code><a href="/docs/linux/man/3-__pmspeclocalpmda/">__pmSpecLocalPMDA</a></code>(3), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5), <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5) and <code><a href="/docs/linux/man/5-pmns/">pmns</a></code>(5). </p>
<h2>Index</h2>
