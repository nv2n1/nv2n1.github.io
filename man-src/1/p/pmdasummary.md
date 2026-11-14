---
title: "pmdasummary(1)"
name: "pmdasummary"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmdasummary/"
description: "pmdasummary – summary performance metrics domain agent (PMDA)"
---

<h2>NAME</h2>
<p> <code>pmdasummary</code> &#8211; summary performance metrics domain agent (PMDA)</p>
<h2>SYNOPSIS</h2>
<p> <code>$PCP_PMDAS_DIR/summary/pmdasummary</code> [<code>-d</code> <i>domain</i>] [<code>-h</code> <i>helpfile</i>] [<code>-l</code> <i>logfile</i>] [<code>-U</code> <i>username</i>] <i>pmie-command-line</i></p>
<h2>DESCRIPTION</h2>
<p> <code>pmdasummary</code> is a Performance Metrics Domain Agent (PMDA) which derives performance metrics values from values made available by other PMDAs. <code>pmdasummary</code> consists of two processes:</p>
<dl>
<dt><code>pmie process</code></p>
<dd> The inference engine for performance values <code><a href="/docs/linux/man/1-pmie/">pmie</a></code>(1) is used to periodically sample values for the base metrics and compute the derived values. This process is launched with the given <i>pmie-command-line</i> arguments by the main process, described below.</p>
<dt><code>main process</code></p>
<dd> The main process reads and buffers the values computed by <code><a href="/docs/linux/man/1-pmie/">pmie</a></code>(1) and makes them available to the performance metrics collector daemon <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1).</dl>
<p> A brief description of the <code>pmdasummary</code> command line options follows:</p>
<dl>
<dt><code>-d</code></p>
<dd> It is absolutely crucial that the performance metrics <i>domain</i> number specified here is unique and consistent. That is, <i>domain</i> should be different for every PMDA on the one host, and the same <i>domain</i> number should be used for the same PMDA on all hosts.</p>
<dt><code>-h</code></p>
<dd> This option specifies an alternative help text file <i>helpfile</i> for describing the metrics that <code>pmdasummary</code> represents.</p>
<dt><code>-l</code></p>
<dd> Location of the log file. By default, a log file named <i>summary.log</i> is written in the current directory of <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) when <code>pmdasummary</code> is started, i.e. <code>$PCP_LOG_DIR/pmcd</code>. If the log file cannot be created or is not writable, output is written to the standard error instead.</p>
<dt><code>-U</code></p>
<dd> User account under which to run the agent. The default is the unprivileged &quot;pcp&quot; account in current versions of PCP, but in older versions the superuser account (&quot;root&quot;) was used by default.</dl>
<h2>INSTALLATION</h2>
<p> If you want access to the names, help text and values for the summary performance metrics, do the following as root: </p>
<pre>
# cd $PCP_PMDAS_DIR/summary
# ./Install
</pre>
<p> If you want to undo the installation, do the following as root: </p>
<pre>
# cd $PCP_PMDAS_DIR/summary
# ./Remove
</pre>
<p> <code>pmdasummary</code> is launched by <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) and should never be executed directly. The Install and Remove scripts notify <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) when the agent is installed or removed.</p>
<h2>FILES</h2>
<dl>
<dt><code>$PCP_PMCDCONF_PATH</code></p>
<dd> command line options used to launch <code>pmdasummary</code></p>
<dt><code>$PCP_PMDAS_DIR/summary/expr.pmie</code></p>
<dd> default <code><a href="/docs/linux/man/1-pmie/">pmie</a></code>(1) expressions defining the summary metrics</p>
<dt><code>$PCP_PMDAS_DIR/summary/help</code></p>
<dd> default help text for the summary metrics</p>
<dt><code>$PCP_PMDAS_DIR/summary/Install</code></p>
<dd> installation script for the <code>pmdasummary</code> agent</p>
<dt><code>$PCP_PMDAS_DIR/summary/Remove</code></p>
<dd> undo installation script for the <code>pmdasummary</code> agent</p>
<dt><code>$PCP_LOG_DIR/pmcd/summary.log</code></p>
<dd> default log file for error messages and other information from <code>pmdasummary</code></dl>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <code>/etc/pcp.conf</code> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) and <code><a href="/docs/linux/man/1-pmie/">pmie</a></code>(1). </p>
<h2>Index</h2>
