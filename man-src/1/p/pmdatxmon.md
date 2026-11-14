---
title: "pmdatxmon(1)"
name: "pmdatxmon"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmdatxmon/"
description: "pmdatxmon – txmon performance metrics domain agent (PMDA)"
---

<h2>NAME</h2>
<p> <code>pmdatxmon</code> &#8211; txmon performance metrics domain agent (PMDA)</p>
<h2>SYNOPSIS</h2>
<p> <code>$PCP_PMDAS_DIR/txmon/pmdatxmon</code> [<code>-d</code> <i>domain</i>] [<code>-l</code> <i>logfile</i>] [<code>-U</code> <i>username</i>] <i>tx_type</i> &#8230;<br />
 <code>$PCP_PMDAS_DIR/txmon/txrecord</code> [<code>-l</code>]<br />
 <code>$PCP_PMDAS_DIR/txmon/txrecord</code> <i>tx_type servtime</i> [<i>tx_type servtime</i> &#8230; ]<br />
 <code>$PCP_PMDAS_DIR/txmon/genload</code></p>
<h2>DESCRIPTION</h2>
<p> <code>pmdatxmon</code> is an example Performance Metrics Domain Agent (PMDA) which exports a small number of performance metrics from a simulated transaction monitor. </p>
<p> The txmon PMDA is shipped as both binary and source code and is designed to be an aid for PMDA developers; the txmon PMDA demonstrates how performance data can be exported from an application (in this case <code>txrecord</code>) to the PCP infrastructure via a shared memory segment. As a matter of convenience, <code>pmdatxmon</code> creates (and destroys on exit) the shared memory segment. </p>
<p> The <i>tx_type</i> arguments are arbitrary unique tags used to identify different transaction types. </p>
<p> The <code>txrecord</code> application simulates the processing of one or more transactions identified by <i>tx_type</i> and with an observed service time of <i>servtime .</i> </p>
<p> With the <code>-l</code> option, <code>txrecord</code> displays the current summary of the transaction activity from the shared memory segment. </p>
<p> <code>genload</code> is a shell and <code><a href="/docs/linux/man/1-awk/">awk</a></code>(1) script that acts as a front-end to <code>txrecord</code> to generate a constant load of simulated transaction activity. </p>
<p> A brief description of the <code>pmdatxmon</code> command line options follows:</p>
<dl>
<dt><code>-d</code></p>
<dd> It is absolutely crucial that the performance metrics <i>domain</i> number specified here is unique and consistent. That is, <i>domain</i> should be different for every PMDA on the one host, and the same <i>domain</i> number should be used for the same PMDA on all hosts.</p>
<dt><code>-l</code></p>
<dd> Location of the log file. By default, a log file named <i>txmon.log</i> is written in the current directory of <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) when <code>pmdatxmon</code> is started, i.e. <code>$PCP_LOG_DIR/pmcd</code>. If the log file cannot be created or is not writable, output is written to the standard error instead.</p>
<dt><code>-U</code></p>
<dd> User account under which to run the agent. The default is the unprivileged &quot;pcp&quot; account in current versions of PCP, but in older versions the superuser account (&quot;root&quot;) was used by default.</dl>
<h2>INSTALLATION</h2>
<p> If you want access to the names, help text and values for the txmon performance metrics, do the following as root: </p>
<pre>
# cd $PCP_PMDAS_DIR/txmon
# ./Install
</pre>
<p> You will be prompted for the <i>tx_type</i> tags. </p>
<p> If you want to undo the installation, do the following as root: </p>
<pre>
# cd $PCP_PMDAS_DIR/txmon
# ./Remove
</pre>
<p> <code>pmdatxmon</code> is launched by <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) and should never be executed directly. The Install and Remove scripts notify <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) when the agent is installed or removed.</p>
<h2>FILES</h2>
<dl>
<dt><code>$PCP_PMCDCONF_PATH</code></p>
<dd> command line options used to launch <code>pmdatxmon</code></p>
<dt><code>$PCP_PMDAS_DIR/txmon/help</code></p>
<dd> default help text file for the txmon metrics</p>
<dt><code>$PCP_PMDAS_DIR/txmon/Install</code></p>
<dd> installation script for the <code>pmdatxmon</code> agent</p>
<dt><code>$PCP_PMDAS_DIR/txmon/Remove</code></p>
<dd> undo installation script for the <code>pmdatxmon</code> agent</p>
<dt><code>$PCP_LOG_DIR/pmcd/txmon.log</code></p>
<dd> default log file for error messages and other information from <code>pmdatxmon</code></dl>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <code>/etc/pcp.conf</code> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1), <code><a href="/docs/linux/man/1-pmdasample/">pmdasample</a></code>(1), <code><a href="/docs/linux/man/1-pmdatrivial/">pmdatrivial</a></code>(1), <code><a href="/docs/linux/man/1-txmonvis/">txmonvis</a></code>(1) and <code><a href="/docs/linux/man/3-pmda/">PMDA</a></code>(3). </p>
<h2>Index</h2>
