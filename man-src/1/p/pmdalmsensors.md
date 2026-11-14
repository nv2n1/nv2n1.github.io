---
title: "pmdalmsensors(1)"
name: "pmdalmsensors"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmdalmsensors/"
description: "pmdalmsensors – Linux hardware monitoring performance metrics domain agent (PMDA)"
---

<h2>NAME</h2>
<p> <code>pmdalmsensors</code> &#8211; Linux hardware monitoring performance metrics domain agent (PMDA)</p>
<h2>SYNOPSIS</h2>
<p> <code>$PCP_PMDAS_DIR/lmsensors/pmdalmsensors</code> [<code>-d</code> <i>domain</i>] [<code>-l</code> <i>logfile</i>] [<code>-U</code> <i>username</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>pmdalmsensors</code> is a Performance Metrics Domain Agent (PMDA) which extracts performance metrics describing the state of hardware using the lm-sensors on compatible motherboards. </p>
<p> The <code>lmsensors</code> PMDA exports metrics that measure fan speeds, core temperatures and voltage levels. </p>
<p> A brief description of the <code>pmdalmsensors</code> command line options follows:</p>
<dl>
<dt><code>-d</code></p>
<dd> It is absolutely crucial that the performance metrics <i>domain</i> number specified here is unique and consistent. That is, <i>domain</i> should be different for every PMDA on the one host, and the same <i>domain</i> number should be used for the same PMDA on all hosts.</p>
<dt><code>-l</code></p>
<dd> Location of the log file. By default, a log file named <i>lmsensors.log</i> is written in the current directory of <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) when <code>pmdalmsensors</code> is started, i.e. <code>$PCP_LOG_DIR/pmcd .</code> If the log file cannot be created or is not writable, output is written to the standard error instead.</p>
<dt><code>-U</code></p>
<dd> User account under which to run the agent. The default is the unprivileged &quot;pcp&quot; account in current versions of PCP, but in older versions the superuser account (&quot;root&quot;) was used by default.</dl>
<h2>INSTALLATION</h2>
<p> If you want access to the names, help text and values for the lmsensors performance metrics, do the following as root: </p>
<pre>
# cd $PCP_PMDAS_DIR/lmsensors
# ./Install
</pre>
<p> If you want to undo the installation, do the following as root: </p>
<pre>
# cd $PCP_PMDAS_DIR/lmsensors
# ./Remove
</pre>
<p> <code>pmdalmsensors</code> is launched by <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) and should never be executed directly. The Install and Remove scripts notify <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) when the agent is installed or removed.</p>
<h2>FILES</h2>
<dl>
<dt><code>$PCP_PMCDCONF_PATH</code></p>
<dd> command line options used to launch <code>pmdalmsensors</code></p>
<dt><code>$PCP_PMDAS_DIR/lmsensors/help</code></p>
<dd> default help text file for the lmsensors metrics</p>
<dt><code>$PCP_PMDAS_DIR/lmsensors/Install</code></p>
<dd> installation script for the <code>pmdalmsensors</code> agent</p>
<dt><code>$PCP_PMDAS_DIR/lmsensors/Remove</code></p>
<dd> undo installation script for the <code>pmdalmsensors</code> agent</p>
<dt><code>$PCP_LOG_DIR/pmcd/lmsensors.log</code></p>
<dd> default log file for error messages and other information from <code>pmdalmsensors</code></dl>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5) and <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5). </p>
<h2>Index</h2>
