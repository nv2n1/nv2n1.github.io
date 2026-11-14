---
title: "pmclient(1)"
name: "pmclient"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmclient/"
description: "pmclient, pmclient_fg – a simple performance metrics client"
---

<h2>NAME</h2>
<p> <code>pmclient</code>, <code>pmclient_fg</code> &#8211; a simple performance metrics client</p>
<h2>SYNOPSIS</h2>
<p> <code>pmclient</code> [<code>-a</code> <i>archive</i>] [<code>-h</code> <i>host</i>] [<code>-n</code> <i>pmnsfile</i>] [<code>-P</code>] [<code>-S</code> <i>numsec</i>] [<code>-s</code> <i>samples</i>] [<code>-t</code> <i>interval</i>] [<code>-Z</code> <i>timezone</i>] [<code>-z</code>]</p>
<h2>DESCRIPTION</h2>
<p> <code>pmclient</code> and <code>pmclient_fg</code> are simple clients that use the Performance Metrics Application Programming Interface (PMAPI) to report some high-level system performance metrics. </p>
<p> The real value of these tools is as sample clients using the <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), interfaces and to this end the source code is included with the Performance Co-Pilot (PCP) package (see <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1)), and is typically installed in <i>/usr/share/pcp/demos/pmclient</i>. </p>
<p> The <code>pmclient_fg</code> program differs to <code>pmclient</code> in that it uses the fetchgroup API extension to the PMAPI, see <code><a href="/docs/linux/man/3-pmfetchgroup/">pmFetchGroup</a></code>(3). </p>
<p> Normally <code>pmclient</code> operates on the distributed Performance Metrics Name Space (PMNS), however if the <code>-n</code> option is specified an alternative local PMNS is loaded from the file <i>pmnsfile</i>. </p>
<p> Unless directed to another host by the <code>-h</code> option, or to an archive by the <code>-a</code> option, <code>pmclient</code> will contact the Performance Metrics Collector Daemon (PMCD) on the local host to obtain the required information. The argument to <code>-a</code> is a comma-separated list of names, each of which may be the base name of an archive or the name of a directory containing one or more archives. The <code>-a</code> and <code>-h</code> options are mutually exclusive. </p>
<p> By default, <code>pmclient</code> reports the time of day according to the local timezone on the system where <code>pmclient</code> is run. The <code>-Z</code> option changes the timezone to <i>timezone</i> in the format of the environment variable <code>TZ</code> as described in <code><a href="/docs/linux/man/7-environ/">environ</a></code>(7). The <code>-z</code> option changes the timezone to the local timezone at the host that is the source of the performance metrics, as identified via either the <code>-h</code> or <code>-a</code> options. </p>
<p> Other options control the specific information to be reported.</p>
<dl>
<dt><code>-P</code></p>
<dd> The default behavior for replaying a set of archives, is to replay at full speed. The <code>-P</code> option may be used in conjunction with a set of archives, to request that the prevailing real-time delay be applied between samples (see <code>-t</code>) to effect a pause.</p>
<dt><code>-S</code> <i>numsec</i></p>
<dd> The <code>-S</code> option may be used in conjunction with a set of archives to request that display start at the time <i>numsec</i> seconds from the start of the set of archives.</p>
<dt><code>-s</code> <i>samples</i></p>
<dd> The argument <i>samples</i> defines the number of samples to be retrieved and reported. If samples is 0 or <code>-s</code> is not specified, <code>pmclient</code> will sample and report continuously (in real time mode) or until the end of the set of PCP archives (in archive mode).</p>
<dt><code>-t</code> <i>interval</i></p>
<dd> The default update <i>interval</i> may be set to something other than the default 5 seconds. The <i>interval</i> argument follows the syntax described in <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), and in the simplest form may be an unsigned integer (the implied units in this case are seconds).</dl>
<p> The output from <code>pmclient</code> is directed to standard output, and lists</p>
<dl>
<dt>+</p>
<dd> Aggregate CPU utilization, in the range 0 to 1.</p>
<dt>+</p>
<dd> If the system has more than 1 CPU, the ordinal number of the busiest CPU, in the range 0 to &#8230;</p>
<dt>+</p>
<dd> If the system has more than 1 CPU, the CPU utilization for the busiest CPU.</p>
<dt>+</p>
<dd> Real free memory in Mbytes.</p>
<dt>+</p>
<dd> Aggregate physical disk I/O operations per second (IOPS).</p>
<dt>+</p>
<dd> Load average over the last 1 minute and over the last 15 minutes.</dl>
<h2>FILES</h2>
<dl>
<dt><code>$PCP_DEMOS_DIR/pmclient</code></p>
<dd> source code, documentation, configuration files and Makefile when the PCP development package is installed</dl>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1), <code><a href="/docs/linux/man/1-pmchart/">pmchart</a></code>(1), <code><a href="/docs/linux/man/1-pmdumptext/">pmdumptext</a></code>(1), <code><a href="/docs/linux/man/1-pmgenmap/">pmgenmap</a></code>(1), <code><a href="/docs/linux/man/1-pminfo/">pminfo</a></code>(1), <code><a href="/docs/linux/man/1-pmrep/">pmrep</a></code>(1), <code><a href="/docs/linux/man/1-pmstat/">pmstat</a></code>(1), <code><a href="/docs/linux/man/1-pmval/">pmval</a></code>(1), <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmfetchgroup/">pmFetchGroup</a></code>(3), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5) and <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5).</p>
<h2>DIAGNOSTICS</h2>
<p> All are generated on standard error, and are intended to be self-explanatory. </p>
<h2>Index</h2>
