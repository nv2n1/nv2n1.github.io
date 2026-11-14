---
title: "pmdaxfs(1)"
name: "pmdaxfs"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmdaxfs/"
description: "pmdaxfs – XFS filesystem performance metrics domain agent (PMDA)"
---

<h2>NAME</h2>
<p> <code>pmdaxfs</code> &#8211; XFS filesystem performance metrics domain agent (PMDA)</p>
<h2>SYNOPSIS</h2>
<p> <code>$PCP_PMDAS_DIR/xfs/pmdaxfs</code> [<code>-d</code> <i>domain</i>] [<code>-l</code> <i>logfile</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>pmdaxfs</code> is a Performance Metrics Domain Agent (PMDA) which extracts performance metrics describing the state of the XFS filesystem from the Linux kernel. </p>
<p> The <code>xfs</code> PMDA exports metrics that measure information about metadata buffer usage, the journal, btree operations, inode operations, extended attributes, directories, quotas, read and write operation counts and of course throughput. </p>
<p> The PMDA provides a facility to reset the values of all counters to zero using <code><a href="/docs/linux/man/1-pmstore/">pmstore</a></code>(1) with the xfs.control.reset metric. </p>
<p> A brief description of the <code>pmdaxfs</code> command line options follows:</p>
<dl>
<dt><code>-d</code></p>
<dd> It is absolutely crucial that the performance metrics <i>domain</i> number specified here is unique and consistent. That is, <i>domain</i> should be different for every PMDA on the one host, and the same <i>domain</i> number should be used for the same PMDA on all hosts.</p>
<dt><code>-l</code></p>
<dd> Location of the log file. By default, a log file named <i>xfs.log</i> is written in the current directory of <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) when <code>pmdaxfs</code> is started, i.e. <code>$PCP_LOG_DIR/pmcd</code>. If the log file cannot be created or is not writable, output is written to the standard error instead.</dl>
<h2>INSTALLATION</h2>
<p> The <code>xfs</code> PMDA is installed and available by default on Linux. If you want to undo the installation, do the following as root: </p>
<pre>
# cd $PCP_PMDAS_DIR/xfs
# ./Remove
</pre>
<p> If you want to establish access to the names, help text and values for the XFS performance metrics once more, after removal, do the following as root: </p>
<pre>
# cd $PCP_PMDAS_DIR/xfs
# ./Install
</pre>
<p> <code>pmdaxfs</code> is launched by <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) and should never be executed directly. The Install and Remove scripts notify <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) when the agent is installed or removed.</p>
<h2>FILES</h2>
<dl>
<dt><code>$PCP_PMCDCONF_PATH</code></p>
<dd> command line options used to launch <code>pmdaxfs</code></p>
<dt><code>$PCP_PMDAS_DIR/xfs/help</code></p>
<dd> default help text file for the xfs metrics</p>
<dt><code>$PCP_PMDAS_DIR/xfs/Install</code></p>
<dd> installation script for the <code>pmdaxfs</code> agent</p>
<dt><code>$PCP_PMDAS_DIR/xfs/Remove</code></p>
<dd> undo installation script for the <code>pmdaxfs</code> agent</p>
<dt><code>$PCP_LOG_DIR/pmcd/xfs.log</code></p>
<dd> default log file for error messages and other information from <code>pmdaxfs</code></dl>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1), <code><a href="/docs/linux/man/1-pmstore/">pmstore</a></code>(1), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5) and <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5). </p>
<h2>Index</h2>
