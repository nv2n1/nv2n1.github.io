---
title: "pmdaunbound(1)"
name: "pmdaunbound"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmdaunbound/"
description: "pmdaunbound – Unbound resolver PMDA"
---

<h2>NAME</h2>
<p> <code>pmdaunbound</code> &#8211; Unbound resolver PMDA</p>
<h2>DESCRIPTION</h2>
<p> <code>pmdaunbound</code> is a Performance Metrics Domain Agent (PMDA) which exports metric values about the Unbound DNS resolver using the <code><a href="/docs/linux/man/8-unbound-control/">unbound-control</a></code>(8) <code>stats_noreset</code> command. </p>
<p> This gives lots of insight into query types, response time, cache hits/misses, etc. Please see the <code><a href="/docs/linux/man/8-unbound-control/">unbound-control</a></code>(8) man page for explanation about each statistics counter. </p>
<p> Further details on the Unbound DNS resolver can be found at <a rel="nofollow" href="https://unbound.net/">https://unbound.net/</a></p>
<h2>INSTALLATION</h2>
<p> Install the Unbound PMDA by using the Install script as root: </p>
<p>#&nbsp;<wbr>cd&nbsp;<wbr>$PCP_PMDAS_DIR/unbound </p>
<p>#&nbsp;<wbr>./Install </p>
<p> To uninstall, do the following as root: </p>
<p>#&nbsp;<wbr>cd&nbsp;<wbr>$PCP_PMDAS_DIR/unbound </p>
<p>#&nbsp;<wbr>./Remove </p>
<p> <code>pmdaunbound</code> is launched by <i><a href="/docs/linux/man/1-pmcd/">pmcd</a></i>(1) and should never be executed directly. The Install and Remove scripts notify <i><a href="/docs/linux/man/1-pmcd/">pmcd</a></i>(1) when the agent is installed or removed.</p>
<h2>FILES</h2>
<dl>
<dt><code>$PCP_PMDAS_DIR/unbound/Install</code></p>
<dd> installation script for the <code>pmdaunbound</code> agent</p>
<dt><code>$PCP_PMDAS_DIR/unbound/Remove</code></p>
<dd> undo installation script for the <code>pmdaunbound</code> agent</p>
<dt><code>$PCP_LOG_DIR/pmcd/unbound.log</code></p>
<dd> default log file for error messages from <code>pmdaunbound</code></dl>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by <code>PCP</code>. On each installation, the file <code>/etc/pcp.conf</code> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <i><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></i>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1), <code><a href="/docs/linux/man/8-unbound-control/">unbound-control</a></code>(8), and <code><a href="/docs/linux/man/8-unbound/">unbound</a></code>(8) </p>
<h2>Index</h2>
