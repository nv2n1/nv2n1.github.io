---
title: "pmdalogger(1)"
name: "pmdalogger"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmdalogger/"
description: "pmdalogger – log file performance metrics domain agent (PMDA)"
---

<h2>NAME</h2>
<p> <code>pmdalogger</code> &#8211; log file performance metrics domain agent (PMDA)</p>
<h2>SYNOPSIS</h2>
<p> <code>$PCP_PMDAS_DIR/logger/pmdalogger</code> [<code>-d</code> <i>domain</i>] [<code>-l</code> <i>logfile</i>] [<code>-m</code> <i>memory</i>] [<code>-s</code> <i>interval</i>] [<code>-U</code> <i>username</i>] [<i>configfile</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>pmdalogger</code> is a configurable log file monitoring Performance Metrics Domain Agent (PMDA). It can be seen as analogous to the <code>-f</code> option to <code><a href="/docs/linux/man/1-tail/">tail</a></code>(1) and converts each new log line into a performance event. It was the first PMDA to make extensive use of event metrics, which can be consumed by client tools like <code><a href="/docs/linux/man/1-pmevent/">pmevent</a></code>(1). </p>
<p> The <code>logger</code> PMDA exports both event-style metrics reflecting timestamped event records for text logged to a file (or set of files or output from a process), as well as the more orthodox sample-style metrics such as event counts and throughput size values. </p>
<p> The PMDA is configured via a <i>configfile</i> which contains one line for each source of events (file or process). This file is setup by the Install script described in the later section on &#8220;INSTALLATION&#8221; of the PMDA. </p>
<p> A brief description of the <code>pmdalogger</code> command line options follows:</p>
<dl>
<dt><code>-d</code></p>
<dd> It is absolutely crucial that the performance metrics <i>domain</i> number specified here is unique and consistent. That is, <i>domain</i> should be different for every PMDA on the one host, and the same <i>domain</i> number should be used for the same PMDA on all hosts.</p>
<dt><code>-l</code></p>
<dd> Location of the log file. By default, a log file named <i>logger.log</i> is written in the current directory of <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) when <code>pmdalogger</code> is started, i.e. <code>$PCP_LOG_DIR/pmcd</code>. If the log file cannot be created or is not writable, output is written to the standard error instead.</p>
<dt><code>-m</code></p>
<dd> Limit the physical memory used by the PMDA to buffer event records to <i>maxsize</i> bytes. As log events arrive at the PMDA, they must be buffered until individual client tools request the next batch since their previous batch of events. The default maximum is 2 megabytes.</p>
<dt><code>-s</code></p>
<dd> Sets the polling interval for detecting newly arrived log lines. Mirrors the same option from the <code><a href="/docs/linux/man/1-tail/">tail</a></code>(1) command.</p>
<dt><code>-U</code></p>
<dd> User account under which to run the agent. The default is the unprivileged &quot;pcp&quot; account in current versions of PCP, but in older versions the superuser account (&quot;root&quot;) was used by default.</dl>
<h2>INSTALLATION</h2>
<p> If you want access to the names, help text and values for the logger performance metrics, do the following as root: </p>
<pre>
# cd $PCP_PMDAS_DIR/logger
# ./Install
</pre>
<p> This is an interactive installation process which prompts for each log file path to be monitored (or command to be run), a metric instance name to identify it, and whether access should be restricted (refer to the <code>-x</code> option to <code><a href="/docs/linux/man/1-pmevent/">pmevent</a></code>(1) for further details). </p>
<p> If you want to undo the installation, do the following as root: </p>
<pre>
# cd $PCP_PMDAS_DIR/logger
# ./Remove
</pre>
<p> <code>pmdalogger</code> is launched by <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) and should never be executed directly. The Install and Remove scripts notify <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) when the agent is installed or removed.</p>
<h2>FILES</h2>
<dl>
<dt><code>$PCP_PMCDCONF_PATH</code></p>
<dd> command line options used to launch <code>pmdalogger</code></p>
<dt><code>$PCP_PMDAS_DIR/logger/logger.conf</code></p>
<dd> default configuration file for the logger metrics</p>
<dt><code>$PCP_PMDAS_DIR/logger/help</code></p>
<dd> default help text file for the logger metrics</p>
<dt><code>$PCP_PMDAS_DIR/logger/Install</code></p>
<dd> installation script for the <code>pmdalogger</code> agent</p>
<dt><code>$PCP_PMDAS_DIR/logger/Remove</code></p>
<dd> undo installation script for the <code>pmdalogger</code> agent</p>
<dt><code>$PCP_LOG_DIR/pmcd/logger.log</code></p>
<dd> default log file for error messages and other information from <code>pmdalogger</code></dl>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), <code><a href="/docs/linux/man/1-pmevent/">pmevent</a></code>(1), <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1), <code><a href="/docs/linux/man/1-tail/">tail</a></code>(1), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5) and <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5). </p>
<h2>Index</h2>
