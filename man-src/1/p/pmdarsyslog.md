---
title: "pmdarsyslog(1)"
name: "pmdarsyslog"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmdarsyslog/"
description: "pmdarsyslog – rsyslog (reliable and extended syslog) PMDA"
---

<h2>NAME</h2>
<p> <code>pmdarsyslog</code> &#8211; rsyslog (reliable and extended syslog) PMDA</p>
<h2>DESCRIPTION</h2>
<p> <code>pmdarsyslog</code> is a Performance Metrics Domain Agent (<font SIZE="-1">PMDA</font>) which exports metric values from the <code><a href="/docs/linux/man/8-rsyslogd/">rsyslogd</a></code>(8) server. Further details about rsyslog can be found at <a rel="nofollow" href="http://www.rsyslog.com/.">http://www.rsyslog.com/.</a></p>
<h2>INSTALLATION</h2>
<p> If you want access to the names and values for the rsyslog performance metrics, do the following as root: </p>
<p>#&nbsp;<wbr>cd&nbsp;<wbr>$PCP_PMDAS_DIR/rsyslog </p>
<p>#&nbsp;<wbr>./Install </p>
<p> To uninstall, do the following as root: </p>
<p>#&nbsp;<wbr>cd&nbsp;<wbr>$PCP_PMDAS_DIR/rsyslog </p>
<p>#&nbsp;<wbr>./Remove </p>
<p> <code>pmdarsyslog</code> is launched by <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) and should never be executed directly. The Install and Remove scripts notify <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) when the agent is installed or removed. </p>
<p> In order to use this agent, rsyslog stats gathering must be enabled. This is done by adding the lines: </p>
<p>$ModLoad impstats </p>
<p>$PStatsInterval 5&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>log every 5 seconds </p>
<p>syslog.info&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|/var/log/pcp/rsyslog/stats </p>
<p> to your <i><a href="/docs/linux/man/5-rsyslog-conf/">rsyslog.conf</a></i>(5) configuration file after installing the <font SIZE="-1">PMDA</font>. Take care to ensure the syslog.info messages do not get logged in any other file, as this could unexpectedly fill your filesystem. Syntax useful for this is syslog.!=info for explicitly excluding these.</p>
<h2>FILES</h2>
<dl>
<dt><code>$PCP_LOG_DIR/rsyslog/stats</code></p>
<dd> named pipe containing statistics exported from rsyslog, usually created by the <font SIZE="-1">PMDA</font> Install script.</p>
<dt><code>$PCP_PMDAS_DIR/rsyslog/rsyslog.conf</code></p>
<dd> optional configuration file for <code>pmdarsyslog</code></p>
<dt><code>$PCP_PMDAS_DIR/rsyslog/Install</code></p>
<dd> installation script for the <code>pmdarsyslog</code> agent</p>
<dt><code>$PCP_PMDAS_DIR/rsyslog/Remove</code></p>
<dd> undo installation script for the <code>pmdarsyslog</code> agent</p>
<dt><code>$PCP_LOG_DIR/pmcd/rsyslog.log</code></p>
<dd> default log file for error messages from <code>pmdarsyslog</code></dl>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by <code>PCP</code>. On each installation, the file <code>/etc/pcp.conf</code> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <i><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></i>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) and <code><a href="/docs/linux/man/1-rsyslogd/">rsyslogd</a></code>(1). </p>
<h2>Index</h2>
