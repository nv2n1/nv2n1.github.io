---
title: "pmdasystemd(1)"
name: "pmdasystemd"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmdasystemd/"
description: "pmdasystemd – systemd performance metrics domain agent (PMDA)"
---

<h2>NAME</h2>
<p> <code>pmdasystemd</code> &#8211; systemd performance metrics domain agent (PMDA)</p>
<h2>SYNOPSIS</h2>
<p> <code>$PCP_PMDAS_DIR/systemd/pmdasystemd</code> [<code>-f</code>] [<code>-d</code> <i>domain</i>] [<code>-l</code> <i>logfile</i>] [<code>-m</code> <i>memory</i>] [<code>-s</code> <i>interval</i>] [<code>-U</code> <i>username</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>pmdasystemd</code> is a systemd log file monitoring Performance Metrics Domain Agent (PMDA). It can be seen as analagous to the <code>-f</code> option to <code><a href="/docs/linux/man/1-journalctl/">journalctl</a></code>(1) and converts each new log line into a performance event, suitable for consumption by <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3) client tools like <code><a href="/docs/linux/man/1-pmevent/">pmevent</a></code>(1). </p>
<p> The <code>systemd</code> PMDA exports both event-style metrics reflecting timestamped event records for messages logged to the system logs, as well as the more orthodox sample-style metrics such as message counts and throughput size values. </p>
<p> A brief description of the <code>pmdasystemd</code> command line options follows:</p>
<dl>
<dt><code>-d</code></p>
<dd> It is absolutely crucial that the performance metrics <i>domain</i> number specified here is unique and consistent. That is, <i>domain</i> should be different for every PMDA on the one host, and the same <i>domain</i> number should be used for the same PMDA on all hosts.</p>
<dt><code>-f</code></p>
<dd> Disables per-uid/gid record filtering. By default the user and group credentials will be used to filter log records returned to the client tool, preventing information exposure to arbitrary users. This option disables that, so use only with extreme caution.</p>
<dt><code>-l</code></p>
<dd> Location of the log file. By default, a log file named <i>systemd.log</i> is written in the current directory of <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) when <code>pmdasystemd</code> is started, i.e. <code>$PCP_LOG_DIR/pmcd</code>. If the log file cannot be created or is not writable, output is written to the standard error instead.</p>
<dt><code>-m</code></p>
<dd> Limit the physical memory used by the PMDA to buffer event records to <i>maxsize</i> bytes. As log events arrive at the PMDA, they must be buffered until individual client tools request the next batch since their previous batch of events. The default maximum is 2 megabytes.</p>
<dt><code>-s</code></p>
<dd> Sets the polling interval for detecting newly arrived log lines. Mirrors the same option from the <code><a href="/docs/linux/man/1-tail/">tail</a></code>(1) command.</p>
<dt><code>-U</code></p>
<dd> User account under which to run the agent. The default is the &quot;adm&quot; user account.</dl>
<h2>INSTALLATION</h2>
<p> If you want access to the names, help text and values for the systemd performance metrics, do the following as root: </p>
<pre>
# cd $PCP_PMDAS_DIR/systemd
# ./Install
</pre>
<p> If you want to undo the installation, do the following as root: </p>
<pre>
# cd $PCP_PMDAS_DIR/systemd
# ./Remove
</pre>
<p> <code>pmdasystemd</code> is launched by <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) and should never be executed directly. The Install and Remove scripts notify <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) when the agent is installed or removed.</p>
<h2>FILES</h2>
<dl>
<dt><code>$PCP_PMCDCONF_PATH</code></p>
<dd> command line options used to launch <code>pmdasystemd</code></p>
<dt><code>$PCP_PMDAS_DIR/systemd/help</code></p>
<dd> default help text file for the systemd metrics</p>
<dt><code>$PCP_PMDAS_DIR/systemd/Install</code></p>
<dd> installation script for the <code>pmdasystemd</code> agent</p>
<dt><code>$PCP_PMDAS_DIR/systemd/Remove</code></p>
<dd> undo installation script for the <code>pmdasystemd</code> agent</p>
<dt><code>$PCP_LOG_DIR/pmcd/systemd.log</code></p>
<dd> default log file for error messages and other information from <code>pmdasystemd</code></dl>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1), <code><a href="/docs/linux/man/1-pmevent/">pmevent</a></code>(1), <code><a href="/docs/linux/man/1-journalctl/">journalctl</a></code>(1), <code><a href="/docs/linux/man/1-tail/">tail</a></code>(1), <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5) and <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5). </p>
<h2>Index</h2>
