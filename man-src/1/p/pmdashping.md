---
title: "pmdashping(1)"
name: "pmdashping"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmdashping/"
description: "pmdashping – \"shell-ping\" performance metrics domain agent"
---

<h2>NAME</h2>
<p> <code>pmdashping</code> &#8211; &quot;shell-ping&quot; performance metrics domain agent</p>
<h2>SYNOPSIS</h2>
<p> <code>$PCP_PMDAS_DIR/shping/pmdashping</code> [<code>-C</code>] [<code>-d</code> <i>domain</i>] [<code>-l</code> <i>logfile</i>] [<code>-I</code> <i>interval</i>] [<code>-t</code> <i>timeout</i>] [<code>-U</code> <i>username</i>] <i>configfile</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>pmdashping</code> is a Performance Metrics Domain Agent (PMDA) which exports quality of service and response time measurements for arbitrary commands as might be run from a shell such as <code><a href="/docs/linux/man/1-sh/">sh</a></code>(1). </p>
<p> These measurements are intended to be used to quantify service quality and service availability for those services that are either mission critical or act as early indicators of adverse system performance. </p>
<p> The sample configuration monitors simple shell commands (<code>exit</code> and <code><a href="/docs/linux/man/1-date/">date</a></code>(1)), a short computationally intensive task using <code><a href="/docs/linux/man/1-sum/">sum</a></code>(1), a short C compilation, DNS lookup via <code><a href="/docs/linux/man/1-nslookup/">nslookup</a></code>(1), YP lookup via <code><a href="/docs/linux/man/1-ypcat/">ypcat</a></code>(1), bind/portmapper service using <code><a href="/docs/linux/man/1-rpcbind/">rpcbind</a></code>(1), SMTP by connecting to telnet port 25 and sending an &#8220;expn root&#8221; request, and NNTP by connecting to telnet port 119 and running a &#8220;listgroup&#8221; command. </p>
<p> It is expected that other commands would follow the examples in the sample configuration file, and most deployments of the <code>pmdashping</code> PMDA are expected to use a customized configuration file. </p>
<p> A brief description of the <code>pmdashping</code> command line options follows:</p>
<dl>
<dt><code>-C</code></p>
<dd> Parse <i>configfile</i>, reporting any errors and exiting with non-zero status if the file contains syntactical errors.</p>
<dt><code>-d</code></p>
<dd> It is absolutely crucial that the performance metrics <i>domain</i> number specified here is unique and consistent. That is, <i>domain</i> should be different for every PMDA on the one host, and the same <i>domain</i> number should be used for the same PMDA on all hosts.</p>
<dt><code>-l</code></p>
<dd> Location of the log file. By default, a log file named <i>shping.log</i> is written in the current directory of <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) when <code>pmdashping</code> is started, i.e. <code>$PCP_LOG_DIR/pmcd</code>. If the log file cannot be created or is not writable, output is written to the standard error instead.</p>
<dt><code>-I</code></p>
<dd> Amount of time (in seconds) between subsequent executions of the list of commands provided via the configuration file <i>configfile</i>. The default is 2 minutes.</p>
<dt><code>-t</code></p>
<dd> Amount of time (in seconds) to wait before timing out awaiting a response for a command from <i>configfile</i>. The default is 20 seconds.</p>
<dt><code>-U</code></p>
<dd> User account under which to run the agent and all commands. The default is the unprivileged &quot;pcp&quot; account in current versions of PCP, but in older versions the superuser account (&quot;root&quot;) was used by default.</dl>
<p> The required <i>configfile</i> specifies &#8220;tag&#8221; and &#8220;command&#8221; pairs, each on a separate line. All of the commands are run one after another, with the whole group rescheduled to be run once per <i>interval</i>. For each command that is run, <code>pmdashping</code> records information related to the success (or timeout), exit status, elapsed time and CPU time (system and user), and this information is exported by the PMDA. The tags are used to identify the individual commands amongst the values exported by the PMDA, and form the external instance domain identifiers for the <code>pmdashping</code> metrics which relate to each command. </p>
<h2>INSTALLATION</h2>
<p> In order for a host to export the names, help text and values for the shping performance metrics, do the following as root: </p>
<pre>
# cd $PCP_PMDAS_DIR/shping
# ./Install
</pre>
<p> The set of &#8220;tag&#8221; and &#8220;command&#8221; pairs may be specified from a default (sample) configuration file, a customized file or entered interactively as part of the <code>Install</code> script. </p>
<p> If you want to undo the installation, do the following as root: </p>
<pre>
# cd $PCP_PMDAS_DIR/shping
# ./Remove
</pre>
<p> <code>pmdashping</code> is launched by <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) and should never be executed directly. The Install and Remove scripts notify <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) when the agent is installed or removed.</p>
<h2>FILES</h2>
<dl>
<dt><code>$PCP_PMCDCONF_PATH</code></p>
<dd> command line options used to launch <code>pmdashping</code></p>
<dt><code>$PCP_PMDAS_DIR/shping/help</code></p>
<dd> default help text file for the shping metrics</p>
<dt><code>$PCP_PMDAS_DIR/shping/sample.conf</code></p>
<dd> example configuration file with a number of common commands</p>
<dt><code>$PCP_PMDAS_DIR/shping/Install</code></p>
<dd> installation script for the <code>pmdashping</code> agent</p>
<dt><code>$PCP_PMDAS_DIR/shping/Remove</code></p>
<dd> undo installation script for <code>pmdashping</code></p>
<dt><code>$PCP_LOG_DIR/pmcd/shping.log</code></p>
<dd> default log file for error messages and other information from <code>pmdashping</code></dl>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <code>/etc/pcp.conf</code> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) and <code><a href="/docs/linux/man/1-pcp-shping/">pcp-shping</a></code>(1). </p>
<h2>Index</h2>
