---
title: "pmdasendmail(1)"
name: "pmdasendmail"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmdasendmail/"
description: "pmdasendmail – sendmail performance metrics domain agent (PMDA)"
---

<h2>NAME</h2>
<p> <code>pmdasendmail</code> &#8211; sendmail performance metrics domain agent (PMDA)</p>
<h2>SYNOPSIS</h2>
<p> <code>$PCP_PMDAS_DIR/sendmail/pmdasendmail</code> [<code>-d</code> <i>domain</i>] [<code>-l</code> <i>logfile</i>] [<code>-U</code> <i>username</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>pmdasendmail</code> is a sendmail Performance Metrics Domain Agent (PMDA) which exports mail traffic statistics as collected by <code><a href="/docs/linux/man/1-sendmail/">sendmail</a></code>(1). </p>
<p> Before the sendmail PMDA can export any metrics, <code><a href="/docs/linux/man/1-sendmail/">sendmail</a></code>(1) must have statistics collection enabled. This involves checking the name of the statistics file, as given by the <code>OS</code> or <code>O StatusFile</code> control lines in <code>/etc/sendmail.cf</code>, and then creating this file if it does not already exist. Removing the file will terminate statistics collection by <code><a href="/docs/linux/man/1-sendmail/">sendmail</a></code>(1) and hence the sendmail PMDA. </p>
<p> A brief description of the <code>pmdasendmail</code> command line options follows:</p>
<dl>
<dt><code>-d</code></p>
<dd> It is absolutely crucial that the performance metrics <i>domain</i> number specified here is unique and consistent. That is, <i>domain</i> should be different for every PMDA on the one host, and the same <i>domain</i> number should be used for the same PMDA on all hosts.</p>
<dt><code>-l</code></p>
<dd> Location of the log file. By default, a log file named <i>sendmail.log</i> is written in the current directory of <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) when <code>pmdasendmail</code> is started, i.e. <code>$PCP_LOG_DIR/pmcd</code>. If the log file cannot be created or is not writable, output is written to the standard error instead.</p>
<dt><code>-U</code></p>
<dd> User account under which to run the agent. The default is the unprivileged &quot;pcp&quot; account in current versions of PCP, but in older versions the superuser account (&quot;root&quot;) was used by default.</dl>
<p> There are no communication options, as the <i>Install</i> script ensures the sendmail PMDA will be connected to PMCD by a pipe.</p>
<h2>INSTALLATION</h2>
<p> If you want access to the names, help text and values for the sendmail performance metrics, do the following as root: </p>
<pre>
# cd $PCP_PMDAS_DIR/sendmail
# ./Install
</pre>
<p> If you want to undo the installation, do the following as root: </p>
<pre>
# cd $PCP_PMDAS_DIR/sendmail
# ./Remove
</pre>
<p> <code>pmdasendmail</code> is launched by <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) and should never be executed directly. The Install and Remove scripts notify <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) when the agent is installed or removed.</p>
<h2>FILES</h2>
<dl>
<dt><code>$PCP_PMCDCONF_PATH</code></p>
<dd> command line options used to launch <code>pmdasendmail</code></p>
<dt><code>$PCP_PMDAS_DIR/sendmail/help</code></p>
<dd> default help text file for the sendmail metrics</p>
<dt><code>$PCP_PMDAS_DIR/sendmail/Install</code></p>
<dd> installation script for the <code>pmdasendmail</code> agent</p>
<dt><code>$PCP_PMDAS_DIR/sendmail/Remove</code></p>
<dd> undo installation script for the <code>pmdasendmail</code> agent</p>
<dt><code>$PCP_LOG_DIR/pmcd/sendmail.log</code></p>
<dd> default log file for error messages and other information from <code>pmdasendmail</code></p>
<dt><code>/etc/sendmail.cf</code></p>
<dd> <code>sendmail</code> configuration file to identify the name of the statistics file</dl>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <code>/etc/pcp.conf</code> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) and <code><a href="/docs/linux/man/1-sendmail/">sendmail</a></code>(1). </p>
<h2>Index</h2>
