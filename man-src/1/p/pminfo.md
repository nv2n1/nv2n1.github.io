---
title: "pminfo(1)"
name: "pminfo"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pminfo/"
description: "pminfo – display information about performance metrics"
---

<h2>NAME</h2>
<p> <code>pminfo</code> &#8211; display information about performance metrics</p>
<h2>SYNOPSIS</h2>
<p> <code>pminfo</code> [<code>-dfFLmMtTvxz</code>] [<code>-a</code> <i>archive</i>] [<code>-b</code> <i>batchsize</i>] [<code>-c</code> <i>dmfile</i>] [<code>-h</code> <i>hostname</i>] [<code>-K</code> <i>spec</i>] [<code>&#8211;</code>[<code>n</code>|<code>N</code>] <i>pmnsfile</i>] [<code>-O</code> <i>time</i>] [<code>-Z</code> <i>timezone</i>] [<i>metricname</i> &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>pminfo</code> displays various types of information about performance metrics available through the facilities of the Performance Co-Pilot (PCP). </p>
<p> Normally <code>pminfo</code> operates on the distributed Performance Metrics Name Space (PMNS), however if the <code>-n</code> option is specified an alternative local PMNS is loaded from the file <i>pmnsfile.</i> The <code>-N</code> option supports the same function as <code>-n</code>, except for the handling of duplicate names for the same Performance Metric Identifier (PMID) in <i>pmnsfile</i> &#8211; duplicate names are allowed with <code>-n</code> they are not allowed with <code>-N</code>. </p>
<p> The metrics of interest are named in the <i>metricname</i> arguments. If <i>metricname</i> is a non-leaf node in the PMNS, then <code>pminfo</code> will recursively descend the PMNS and report on all leaf nodes. If no <i>metricname</i> argument is given, the root of the PMNS is used. </p>
<p> Unless directed to another host by the <code>-h</code> option, by default <code>pminfo</code> will contact the Performance Metrics Collector Daemon (PMCD) on the local host. The connection to a PMCD is only required if <code>pminfo</code> requires distributed PMNS information, and/or meta-data describing metrics, and/or metric values, and/or help text. </p>
<p> The <code>-a</code> option causes <code>pminfo</code> to use the specified set of archives rather than connecting to a PMCD. The argument to <code>-a</code> is a comma-separated list of names, each of which may be the base name of an archive or the name of a directory containing one or more archives. The <code>-a , -h</code> and <code>-L</code> options are mutually exclusive. </p>
<p> The <code>-L</code> option causes <code>pminfo</code> to use a local context to collect metrics from PMDAs on the local host without PMCD. Only some metrics are available in this mode. The <code>-a</code>,<code>-h</code> and <code>-L</code> options are mutually exclusive. </p>
<p> The <code>-b</code> option may be used to define the maximum size of the group of metrics to be fetched in a single request for the <code>-f</code> and <code>-v</code> options. The default value for <i>batchsize</i> is 20. </p>
<p> Other options control the specific information to be reported.</p>
<dl>
<dt><code>-c</code></p>
<dd> The <i>dmfile</i> argument specifies a file that contains derived metric definitions in the format described for <code><a href="/docs/linux/man/3-pmloadderivedconfig/">pmLoadDerivedConfig</a></code>(3). The <code>-c</code> option provides a way to load derived metric definitions that is an alternative to the more generic use of the <code>PCP_DERIVED_CONFIG</code> environment variable as described in <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1). Using the <code>-c</code> option and the <code>PCP_DERIVED_CONFIG</code> environment variable to specify the <code>same</code> configuration is a bad idea, so choose one or the other method.</p>
<dt><code>-d</code></p>
<dd> Metric descriptions detailing the PMID, data type, data semantics, units, scale and associated instance domain.</p>
<dt><code>-f</code></p>
<dd> Fetch and print values for all instances. When fetching from a set if archives, only those instances present in the first archive record for a metric will be displayed; see also the <code>-O</code> option, else use <code><a href="/docs/linux/man/1-pmdumplog/">pmdumplog</a></code>(1) which may be a better tool for examining archives.</p>
<dt><code>-F</code></p>
<dd> Same as <code>-f</code> but try harder to fetch instances for metrics which have non-enumerable instance domains (e.g. metrics in the &#8220;proc&#8221; subtree of the default PMNS).</p>
<dt><code>-K</code></p>
<dd> When using the <code>-L</code> option to fetch metrics from a local context, the <code>-K</code> option may be used to control the DSO PMDAs that should be made accessible. The <i>spec</i> argument conforms to the syntax described in <code><a href="/docs/linux/man/3-__pmspeclocalpmda/">__pmSpecLocalPMDA</a></code>(3). More than one <code>-K</code> option may be used.</p>
<dt><code>-m</code></p>
<dd> Print the PMID in terse mode.</p>
<dt><code>-M</code></p>
<dd> Print the PMID in verbose mode.</p>
<dt><code>-O</code></p>
<dd> When used in conjunction with an archive source of metrics and the options <code>-f</code> or <code>-F</code>, the <i>time</i> argument defines a time origin at which the metrics should be fetched from the set of archives. Refer to <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1) for a complete description of this option, and the syntax for the <i>time</i> argument.</p>
<dt><code>-t</code></p>
<dd> Print the &#8220;one line&#8221; help summary, if available.</p>
<dt><code>-T</code></p>
<dd> Print the help text, if available.</p>
<dt><code>-v</code></p>
<dd> Verify mode in which descriptions and values are retrieved, but only error conditions are reported. This option silently disables any output from the options <code>-f</code>, <code>-M</code>, <code>-m</code>, <code>-t</code> and <code>-T</code>.</p>
<dt><code>-x</code></p>
<dd> Like the <code>-f</code> option, but with the additional functionality that if a value is processed that is of type PM_TYPE_EVENT, then the event records will be unpacked and the details of each event record reported.</dl>
<h2>FILES</h2>
<dl>
<dt><code>$PCP_VAR_DIR/pmns/</code><i>*</i></p>
<dd> default local PMNS specification files</dl>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1), <code><a href="/docs/linux/man/1-pmchart/">pmchart</a></code>(1), <code><a href="/docs/linux/man/1-pmdumplog/">pmdumplog</a></code>(1), <code><a href="/docs/linux/man/1-pmdumptext/">pmdumptext</a></code>(1), <code><a href="/docs/linux/man/1-pmprobe/">pmprobe</a></code>(1), <code><a href="/docs/linux/man/1-pmrep/">pmrep</a></code>(1), <code><a href="/docs/linux/man/1-pmval/">pmval</a></code>(1), <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmloadderivedconfig/">pmLoadDerivedConfig</a></code>(3), <code><a href="/docs/linux/man/3-__pmspeclocalpmda/">__pmSpecLocalPMDA</a></code>(3), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5), <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5) and <code><a href="/docs/linux/man/5-pmns/">pmns</a></code>(5). </p>
<h2>Index</h2>
