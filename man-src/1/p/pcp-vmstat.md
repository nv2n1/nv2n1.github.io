---
title: "pcp-vmstat(1)"
name: "pcp-vmstat"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pcp-vmstat/"
description: "pcp-vmstat, pmstat – high-level system performance overview"
---

<h2>NAME</h2>
<p> <code>pcp-vmstat</code>, <code>pmstat</code> &#8211; high-level system performance overview</p>
<h2>SYNOPSIS</h2>
<p> <code>pcp</code> [<i>pcp options</i>] <code>vmstat</code> [<i>interval</i> [<i>samples</i>]] </p>
<p> <code>pmstat</code> [<code>-gLlPxz</code>] [<code>-A</code> <i>align</i>] [<code>-a</code> <i>archive</i>] [<code>-h</code> <i>host</i>] [<code>-H</code> <i>file</i>] [<code>-n</code> <i>pmnsfile</i>] [<code>-O</code> <i>offset</i>] [<code>-p</code> <i>port</i>] [<code>-S</code> <i>starttime</i>] [<code>-s</code> <i>samples</i>] [<code>-T</code> <i>endtime</i>] [<code>-t</code> <i>interval</i>] [<code>-Z</code> <i>timezone</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>pmstat</code> provides a one line summary of system performance every <i>interval</i> unit of time (the default is 5 seconds). <code>pmstat</code> is intended to monitor system performance at the highest level, after which other tools may be used to examine subsystems in which potential performance problems may be observed in greater detail. </p>
<p> <code>pcp-vmstat</code> is a simple wrapper for use with the <code><a href="/docs/linux/man/1-pcp/">pcp</a></code>(1) command, providing a more familiar command line format for some users. It also enables the extended reporting option by default, see the <i>-x</i> option below. </p>
<p> Multiple hosts may be monitored by supplying more than one host with multiple <code>-h</code> flags (for live monitoring) or by providing a name of the hostlist file, where each line contain one host name, with <code>-H,</code> or multiple <code>-a</code> flags (for retrospective monitoring from sets of archives). </p>
<p> The <code>-t</code> option may be used to change the default reporting <i>interval</i>. The <i>interval</i> argument follows the syntax described in <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), and in the simplest form may be an unsigned integer (the implied units in this case are seconds). </p>
<p> By default, <code>pmstat</code> fetches metrics by connecting to the Performance Metrics Collector Daemon (PMCD) on the local host. If the <code>-L</code> option is specified, then <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) is bypassed, and metrics are fetched from PMDAs on the local host using the standalone <code>PM_CONTEXT_LOCAL</code> variant of <code><a href="/docs/linux/man/3-pmnewcontext/">pmNewContext</a></code>(3). When the <code>-h</code> option is specified, <code>pmstat</code> connects to the <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) on <i>host</i> and fetches metrics from there. As mentioned above, multiple hosts may be monitored by supplying multiple <code>-h</code> flags. </p>
<p> Alternatively, if the <code>-a</code> option is used, the metrics are retrieved from the Performance Co-Pilot archive log files identified by <i>archive</i>, which is a comma-separated list of names, each of which may be the base name of an archive or the name of a directory containing one or more archives. Multiple sets of archives may be replayed by supplying multiple <code>-a</code> flags. When the <code>-a</code> flag is used, the <code>-P</code> flag may also be used to pause the output after each interval. </p>
<p> Standalone mode can only connect to the local host, using a set of archives implies a host name, and nominating a host precludes using an archive, so the options <code>-L</code>, <code>-a </code> and <code>-h</code> are mutually exclusive. </p>
<p> Normally <code>pmstat</code> operates on the default Performance Metrics Name Space (PMNS), however if the <code>-n</code> option is specified an alternative namespace is loaded from the file <i>pmnsfile</i>. </p>
<p> If the <code>-s</code> the option is specified, <i>samples</i> defines the number of samples to be retrieved and reported. If <i>samples</i> is 0 or <code>-s</code> is not specified, <code>pmstat</code> will sample and report continuously &#8211; this is the default behavior. </p>
<p> When processing a set of archives, <code>pmstat</code> may relinquish its own timing control, and operate as a &#8220;slave&#8221; of a <code><a href="/docs/linux/man/1-pmtime/">pmtime</a></code>(1) process that uses a GUI dialog to provide timing control. In this case, either the <code>-g</code> option should be used to start <code>pmstat</code> as the sole slave of a new <code><a href="/docs/linux/man/1-pmtime/">pmtime</a></code>(1) instance, or <code>-p</code> should be used to attach <code>pmstat</code> to an existing <code><a href="/docs/linux/man/1-pmtime/">pmtime</a></code>(1) instance via the IPC channel identified by the port argument. </p>
<p> The <code>-S</code>, <code>-T</code>, <code>-O</code> and <code>-A</code> options may be used to define a time window to restrict the samples retrieved, set an initial origin within the time window, or specify a &#8220;natural&#8221; alignment of the sample times; refer to <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1) for a complete description of these options. </p>
<p> The <code>-l</code> option prints the last 7 characters of a hostname in summaries involving more than one host (when more than one <code>-h</code> option has been specified on the command line). </p>
<p> The <code>-x</code> option (extended CPU metrics) causes two additional CPU metrics to be reported, namely wait for I/O (&quot;wa&quot;) and virtualisation steal time (&quot;st&quot;). </p>
<p> The output from <code>pmstat</code> is directed to standard output, and the columns in the report are interpreted as follows: </p>
<dl>
<dt><code>loadavg</code></p>
<dd> The <i>1 minute</i> load average.</p>
<dt><code>memory</code></p>
<dd> The <code>swpd</code> column indicates average swap space used during the interval, in Kbytes. The <code>free</code> column indicates average free memory during the interval, in Kbytes. The <code>buff</code> column indicates average buffer memory in use during the interval, in Kbytes. The <code>cache</code> column indicates average cached memory in use during the interval, in Kbytes.</p>
<dl>
<dt>
<dd>
<p> If the values become large, they are reported as Mbytes (<code>m</code> suffix) or Gbytes (<code>g</code> suffix).</dl>
<dt><code>swap</code></p>
<dd> The metrics in this area of the kernel instrumentation are of varying value. We try to report the average number of <code>pages</code> that are paged in (<code>pi</code>) and out (<code>po</code>) per second during the interval. If the corresponding page swapping metrics are unavailable, we report the average rate per second of swap <code>operations</code> in (<code>si</code>) and out (<code>so</code>) during the interval. It is normal for the &#8220;in&#8221; values to be non-zero, but the system is suffering memory stress if the &#8220;out&#8221; values are non-zero over an extended period.</p>
<dl>
<dt>
<dd>
<p> If the values become large, they are reported as thousands of operations per second (<code>K</code> suffix) or millions of operations per second (<code>M</code> suffix).</dl>
<dt><code>io</code></p>
<dd> The <code>bi</code> and <code>bo</code> columns indicate the average rate per second of block input and block output operations (respectfully) during the interval. Unless all file systems have a 1 Kbyte block size, these rates do not directly indicate Kbytes transferred.</p>
<dl>
<dt>
<dd>
<p> If the values become large, they are reported as thousands of operations per second (<code>K</code> suffix) or millions of operations per second (<code>M</code> suffix).</dl>
<dt><code>system</code></p>
<dd> Interrupt rate (<code>in</code>) and context switch rate (<code>cs</code>). Rates are expressed as average operations per second during the interval. Note that the interrupt rate is normally at least <i>HZ</i> (the clock interrupt rate, usually 100) interrupts per second.</p>
<dl>
<dt>
<dd>
<p> If the values become large, they are reported as thousands of operations per second (<code>K</code> suffix) or millions of operations per second (<code>M</code> suffix).</dl>
<dt><code>cpu</code></p>
<dd> Percentage of CPU time spent executing user and &quot;nice user&quot; code (<code>us</code>), system and interrupt processing code (<code>sy</code>), idle loop (<code>id</code>).</dl>
<p> If any values for the associated performance metrics are unavailable, the value appears as &#8220;?&#8221; in the output. </p>
<p> By default, <code>pmstat</code> reports the time of day according to the local timezone on the system where <code>pmstat</code> is run. The <code>-Z</code> option changes the timezone to <i>timezone</i> in the format of the environment variable <code>TZ</code> as described in <code><a href="/docs/linux/man/7-environ/">environ</a></code>(7). The <code>-z</code> option changes the timezone to the local timezone at the host that is the source of the performance metrics, as identified via either the <code>-h</code> or <code>-a</code> options.</p>
<h2>FILES</h2>
<dl>
<dt><code>$PCP_VAR_DIR/pmns/</code><i>*</i></p>
<dd> default PMNS specification files</p>
<dt><code>$PCP_VAR_DIR/config/pmlogger/config.pmstat</code></p>
<dd> <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1) configuration for creating an archive suitable for replay with <code>pmstat</code></dl>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), <code><a href="/docs/linux/man/1-pmclient/">pmclient</a></code>(1), <code><a href="/docs/linux/man/1-pmtime/">pmtime</a></code>(1), <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmnewcontext/">pmNewContext</a></code>(3), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5) and <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5).</p>
<h2>DIAGNOSTICS</h2>
<p> All are generated on standard error, and are intended to be self-explanatory. </p>
<h2>Index</h2>
