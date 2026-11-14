---
title: "pcp(1)"
name: "pcp"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pcp/"
description: "pcp, pcp-summary – run a command or summarize an installation"
---

<h2>NAME</h2>
<p> <code>pcp</code>, <code>pcp-summary</code> &#8211; run a command or summarize an installation</p>
<h2>SYNOPSIS</h2>
<p> <code> pcp</code> [pcp options&#8230;] pcp-<i>command</i> [command options&#8230;]<br />
 <code>pcp</code> [<code>-P</code>] [<code>-a</code> <i>archive</i>] [<code>-h</code> <i>host</i>] [<code>-n</code> <i>pmnsfile</i>]</p>
<h2>DESCRIPTION</h2>
<p> The <code>pcp</code> command is used in one of two modes. By default, it summarizes the Performance Co-Pilot (PCP) installation on the local host. This mode can also be used to summarize the installation from a remote <i>host</i>, or a historical installation from a set of PCP <i>archives</i>. This mode indirectly invokes the <code>pcp-summary</code> <i>command</i> (in the absence of any other requested command). </p>
<p> Alternatively, a <i>command</i> can be passed to <code>pcp</code> to run, again possibly in the context of a remote <i>host</i> or set of historical <i>archives</i>.</p>
<h2>COMMAND MODE</h2>
<p> When <code>pcp</code> is invoked with a command to run, it will search for the named <i>command</i> in <code>$PCP_BINADM_DIR</code> and also <code>$HOME/.pcp/bin</code> (these are usually scripts, and are installed with a &quot;pcp-&quot; prefix). This mode of operation allows system performance tools to be implemented using <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3) services, while still preserving all of their usual command line options. These options are thus (indirectly) augmented with the standard PCP option set, as described in <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1). </p>
<p> This provides a convenient mechanism for obtaining retrospective or remote monitoring capabilities while preserving the behaviour of the system tools. </p>
<p> For example, the <code><a href="/docs/linux/man/1-pcp-free/">pcp-free</a></code>(1) utility can be invoked as follows, for recorded data from host <i>munch</i>: </p>
<pre>
$ pcp -a $PCP_LOG_DIR/pmlogger/<i>munch</i>/20140317 -O 11:35:50am <code>free -m</code>
             total       used       free     shared    buffers     cached
Mem:         23960      14554       9406          0        176       2137
-/+ buffers/cache:      12240      11720
Swap         12047          0      12047
</pre>
<p> A complete list of the available and installed tools is provided along with the <code><a href="/docs/linux/man/1-pcp/">pcp</a></code>(1) usage message, but some examples include: <code><a href="/docs/linux/man/1-pcp-free/">pcp-free</a></code>(1), <code><a href="/docs/linux/man/1-pcp-uptime/">pcp-uptime</a></code>(1) and <code><a href="/docs/linux/man/1-pcp-numastat/">pcp-numastat</a></code>(1).</p>
<h2>SUMMARY MODE</h2>
<p> The summary report includes: the OS version, a summary of the hardware inventory, the local timezone, the PCP software version, the state of the <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) process and associated Performance Metrics Domain Agents (PMDAs), as well as information about any PCP archive loggers (<code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1)) and PCP inference engines (<code><a href="/docs/linux/man/1-pmie/">pmie</a></code>(1)) that are running. </p>
<p> With no arguments, <code>pcp</code> reports on the local host, however the following options are accepted:</p>
<dl>
<dt><code>-a</code> <i>archive</i></p>
<dd> Report the PCP configuration as described in the set of PCP archive logs, <i>archive</i>, which is a comma-separated list of names, each of which may be the base name of an archive or the name of a directory containing one or more archives.</p>
<dt><code>-h</code> <i>host</i></p>
<dd> Report the PCP configuration on <i>host</i> rather than the local host.</p>
<dt><code>-n</code> <i>pmnsfile</i></p>
<dd> Load an alternative Performance Metrics Name Space (<code><a href="/docs/linux/man/5-pmns/">pmns</a></code>(5)) from the file <i>pmnsfile</i>.</p>
<dt><code>-P</code></p>
<dd> Display <code>pmie</code> performance information &#8211; counts of rules evaluating to true, false, or indeterminate, as well as the expected rate of rule calculation, for each <code>pmie</code> process running on the default host. Refer to the individual metric help text for full details on these values.</dl>
<p> All of the displayed values are performance <i>metric</i> values and further information for each can be obtained using the command: </p>
<pre>
$ pminfo -dtT <i>metric</i>
</pre>
<p> The complete set of <i>metric</i>s required by <code>pcp</code> to produce its output is contained in <code>$PCP_VAR_DIR/config/pmlogconf/tools/pcp-summary</code>.</p>
<h2>FILES</h2>
<dl>
<dt><code>$HOME/.pcp/bin</code></p>
<dd> Per-user location for <i>command</i> scripts.</p>
<dt><code>$PCP_BINADM_DIR</code></p>
<dd> System location for installed <i>command</i> scripts.</p>
<dt><code>$PCP_VAR_DIR/config/pmlogconf/tools/pcp-summary</code></p>
<dd> <code><a href="/docs/linux/man/1-pmlogconf/">pmlogconf</a></code>(1) configuration file for collecting all of the metrics required by <code>pcp</code>.</dl>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <code>/etc/pcp.conf</code> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), <code><a href="/docs/linux/man/1-pcp-free/">pcp-free</a></code>(1), <code><a href="/docs/linux/man/1-pcp-numastat/">pcp-numastat</a></code>(1), <code><a href="/docs/linux/man/1-pcp-python/">pcp-python</a></code>(1), <code><a href="/docs/linux/man/1-pcp-uptime/">pcp-uptime</a></code>(1), <code><a href="/docs/linux/man/1-pcp-verify/">pcp-verify</a></code>(1), <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1), <code><a href="/docs/linux/man/1-pmie/">pmie</a></code>(1), <code><a href="/docs/linux/man/1-pmlogconf/">pmlogconf</a></code>(1), <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5) and <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5).</p>
<h2>DIAGNOSTICS</h2>
<p> <code>pcp </code> will terminate with an exit status of <code>1</code> if <code>pmcd</code> on the target host could not be reached or the set of archives could not be opened, or <code>2</code> for any other error. </p>
<h2>Index</h2>
