---
title: "pmdasimple(1)"
name: "pmdasimple"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmdasimple/"
description: "pmdasimple – simple performance metrics domain agent (PMDA)"
---

<h2>NAME</h2>
<p> <code>pmdasimple</code> &#8211; simple performance metrics domain agent (PMDA)</p>
<h2>SYNOPSIS</h2>
<p> <code>$PCP_PMDAS_DIR/simple/pmdasimple</code> [<code>-d</code> <i>domain</i>] [<code>-i</code> <i>port</i>] [<code>-l</code> <i>logfile</i>] [<code>-p</code>] [<code>-u</code> <i>socket</i>] [<code>-U</code> <i>username</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>pmdasimple</code> is a simple Performance Metrics Domain Agent (PMDA) which exports a small number of synthetic performance metrics. </p>
<p> The simple PMDA is shipped as source code and is designed to be an aid for PMDA developers. In terms of code size and features, it is more complex than the trivial PMDA, about the same as the txmon PMDA and less complex than the sample PMDA. The source for the simple PMDA is a good template from which production, customized PMDAs can be developed. </p>
<p> A brief description of the <code>pmdasimple</code> command line options follows:</p>
<dl>
<dt><code>-d</code></p>
<dd> It is absolutely crucial that the performance metrics <i>domain</i> number specified here is unique and consistent. That is, <i>domain</i> should be different for every PMDA on the one host, and the same <i>domain</i> number should be used for the same PMDA on all hosts.</p>
<dt><code>-i</code></p>
<dd> Expect PMCD to connect to <code>pmdasimple</code> on the specified TCP/IP port. <i>port</i> may be a port number or port name.</p>
<dt><code>-l</code></p>
<dd> Location of the log file. By default, a log file named <i>simple.log</i> is written in the current directory of <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) when <code>pmdasimple</code> is started, i.e. <code>$PCP_LOG_DIR/pmcd</code>. If the log file cannot be created or is not writable, output is written to the standard error instead.</p>
<dt><code>-p</code></p>
<dd> Expect PMCD to create a pipe and the connection to <code>pmdasimple</code> is via standard input and standard output. This is the default connection mode.</p>
<dt><code>-u</code></p>
<dd> Expect PMCD to connect to <code>pmdasimple</code> on the Unix domain socket named <i>socket</i>.</p>
<dt><code>-U</code></p>
<dd> User account under which to run the agent. The default is the unprivileged &quot;pcp&quot; account in current versions of PCP, but in older versions the superuser account (&quot;root&quot;) was used by default.</dl>
<p> At most one of the options <code>-i</code>, <code>-p</code> and <code>-u</code> may be specified.</p>
<h2>INSTALLATION</h2>
<p> If you want access the names, help text and values for the simple performance metrics, do the following as root: </p>
<pre>
# cd $PCP_PMDAS_DIR/simple
# ./Install
</pre>
<p> If you want to undo the installation, do the following as root: </p>
<pre>
# cd $PCP_PMDAS_DIR/simple
# ./Remove
</pre>
<p> <code>pmdasimple</code> is launched by <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) and should never be executed directly. The Install and Remove scripts notify <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) when the agent is installed or removed.</p>
<h2>FILES</h2>
<dl>
<dt><code>$PCP_PMCDCONF_PATH</code></p>
<dd> command line options used to launch <code>pmdasimple</code></p>
<dt><code>$PCP_PMDAS_DIR/simple/help</code></p>
<dd> default help text file for the simple metrics</p>
<dt><code>$PCP_PMDAS_DIR/simple/Install</code></p>
<dd> installation script for the <code>pmdasimple</code> agent</p>
<dt><code>$PCP_PMDAS_DIR/simple/Remove</code></p>
<dd> undo installation script for the <code>pmdasimple</code> agent</p>
<dt><code>$PCP_PMDAS_DIR/simple/simple.conf</code></p>
<dd> configuration file for the dynamic instance domain that underlies the <code>simple.now</code> performance metric. For a description, refer to the help text file, or run the command </p>
<p> $ pminfo -T simple.now </p>
<dt><code>$PCP_PMDAS_DIR/simple/*.pmda_simple.so</code></p>
<dd> The DSO version of the PMDA. The same source is used to create both the DSO and the daemon versions of the simple PMDA, and one or the other may be installed as part of the dialog in the <code>Install</code> script.</p>
<dt><code>$PCP_LOG_DIR/pmcd/simple.log</code></p>
<dd> default log file for error messages and other information from <code>pmdasimple</code></dl>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <code>/etc/pcp.conf</code> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1), <code><a href="/docs/linux/man/1-pmdasample/">pmdasample</a></code>(1), <code><a href="/docs/linux/man/1-pmdatrivial/">pmdatrivial</a></code>(1), <code><a href="/docs/linux/man/1-pmdatxmon/">pmdatxmon</a></code>(1), <code><a href="/docs/linux/man/3-pmda/">PMDA</a></code>(3), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5) and <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5). </p>
<h2>Index</h2>
