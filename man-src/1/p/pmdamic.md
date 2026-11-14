---
title: "pmdamic(1)"
name: "pmdamic"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmdamic/"
description: "pmdamic – MIC card PMDA"
---

<h2>NAME</h2>
<p> <code>pmdamic</code> &#8211; MIC card PMDA</p>
<h2>DESCRIPTION</h2>
<p> <code>pmdamic</code> is a Performance Metrics Domain Agent (PMDA) which exports metric values about Intel MIC cards using the <code><a href="/docs/linux/man/7-libmicmgmt/">libmicmgmt</a></code>(7) python bindings. </p>
<p> This provides information on core, memory and power utilization </p>
<h2>INSTALLATION</h2>
<p> Install the MIC PMDA by using the Install script as root: </p>
<p>#&nbsp;<wbr>cd&nbsp;<wbr>$PCP_PMDAS_DIR/mic </p>
<p>#&nbsp;<wbr>./Install </p>
<p> To uninstall, do the following as root: </p>
<p>#&nbsp;<wbr>cd&nbsp;<wbr>$PCP_PMDAS_DIR/mic </p>
<p>#&nbsp;<wbr>./Remove </p>
<p> <code>pmdamic</code> is launched by <i><a href="/docs/linux/man/1-pmcd/">pmcd</a></i>(1) and should never be executed directly. The Install and Remove scripts notify <i><a href="/docs/linux/man/1-pmcd/">pmcd</a></i>(1) when the agent is installed or removed.</p>
<h2>FILES</h2>
<dl>
<dt><code>$PCP_PMDAS_DIR/mic/Install</code></p>
<dd> installation script for the <code>pmdamic</code> agent</p>
<dt><code>$PCP_PMDAS_DIR/mic/Remove</code></p>
<dd> undo installation script for the <code>pmdamic</code> agent</p>
<dt><code>$PCP_LOG_DIR/pmcd/mic.log</code></p>
<dd> default log file for error messages from <code>pmdamic</code></dl>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by <code>PCP</code>. On each installation, the file <code>/etc/pcp.conf</code> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <i><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></i>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1), and <code><a href="/docs/linux/man/7-libmicmgmt/">libmicmgmt</a></code>(7) </p>
<h2>Index</h2>
