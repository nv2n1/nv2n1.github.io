---
title: "pmdajbd2(1)"
name: "pmdajbd2"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmdajbd2/"
description: "pmdajbd2 – journal block device (JBD) performance metrics domain agent (PMDA)"
---

<h2>NAME</h2>
<p> <code>pmdajbd2</code> &#8211; journal block device (JBD) performance metrics domain agent (PMDA)</p>
<h2>SYNOPSIS</h2>
<p> <code>$PCP_PMDAS_DIR/jbd2/pmdajbd2</code> [<code>-d</code> <i>domain</i>] [<code>-l</code> <i>logfile</i>] [<code>-j</code> <i>path</i>] [<code>-U</code> <i>username</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>pmdajbd2</code> is a Performance Metrics Domain Agent (PMDA) which extracts performance metrics from the Journal Block Device subsystem (version 2) in the Linux kernel. These metrics are exported by the kernel in procfs files, one file per block device. The JBD2 subsystem is used by several filesystems including ext3, ext4 and ocfs2. </p>
<p> The <code>jbd2</code> PMDA exports metrics that measure detailed journal transaction information, such as time spent waiting and locked, request rates, blocks used and so on. </p>
<p> A brief description of the <code>pmdajbd2</code> command line options follows (these are only relevant when running the PMDA as a daemon, and not as a shared library):</p>
<dl>
<dt><code>-d</code></p>
<dd> It is absolutely crucial that the performance metrics <i>domain</i> number specified here is unique and consistent. That is, <i>domain</i> should be different for every PMDA on the one host, and the same <i>domain</i> number should be used for the same PMDA on all hosts.</p>
<dt><code>-l</code></p>
<dd> Location of the log file. By default, when running as a daemon a log file named <i>jbd2.log</i> is written in the current directory of when <code>pmdajbd2</code> is started, i.e. <code>$PCP_LOG_DIR/pmcd</code>. If the log file cannot be created or is not writable, output is written to the standard error instead. When running in shared library mode, and diagnostic information will be written into the <code>pmcd</code> log file, namely <code>$PCP_LOG_DIR/pmcd/pmcd.log</code>.</p>
<dt><code>-j</code></p>
<dd> Allows an alternate path to the jbd2 statistics files to be specified. The default path is <i>/proc/fs/jbd2</i>.</p>
<dt><code>-U</code></p>
<dd> User account under which to run the agent. The default is the unprivileged &quot;pcp&quot; account in current versions of PCP, but in older versions the superuser account (&quot;root&quot;) was used by default.</dl>
<h2>INSTALLATION</h2>
<p> This PMDA is installed by default and in the shared library mode (rather than as a separate daemon to <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1)). Thus, the names, help text and values for the jbd2 performance metrics should always be available. </p>
<p> If you do not use these metrics you can remove this PMDA, do the following as root: </p>
<pre>
# cd $PCP_PMDAS_DIR/jbd2
# ./Remove
</pre>
<p> If you want to enable the installation again, do the following as root: </p>
<pre>
# cd $PCP_PMDAS_DIR/jbd2
# ./Install
</pre>
<p> <code>pmdajbd2</code> is launched by <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) and should never be executed directly. The Install and Remove scripts notify <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) when the agent is installed or removed.</p>
<h2>FILES</h2>
<dl>
<dt><code>$PCP_PMCDCONF_PATH</code></p>
<dd> command line options used to launch <code>pmdajbd2</code></p>
<dt><code>$PCP_PMDAS_DIR/jbd2/help</code></p>
<dd> default help text file for the jbd2 metrics</p>
<dt><code>$PCP_PMDAS_DIR/jbd2/Install</code></p>
<dd> installation script for the <code>pmdajbd2</code> agent</p>
<dt><code>$PCP_PMDAS_DIR/jbd2/Remove</code></p>
<dd> undo installation script for the <code>pmdajbd2</code> agent</p>
<dt><code>$PCP_LOG_DIR/pmcd/jbd2.log</code></p>
<dd> default log file for error messages and other information from <code>pmdajbd2</code></dl>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5) and <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5). </p>
<h2>Index</h2>
