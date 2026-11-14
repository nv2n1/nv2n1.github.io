---
title: "pmdanetfilter(1)"
name: "pmdanetfilter"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmdanetfilter/"
description: "pmdanetfilter – Linux netfilter IP connection tracking performance metrics domain agent (PMDA)"
---

<h2>NAME</h2>
<p> <code>pmdanetfilter</code> &#8211; Linux netfilter IP connection tracking performance metrics domain agent (PMDA)</p>
<h2>DESCRIPTION</h2>
<p> <code>pmdanetfilter</code> is a Performance Metrics Domain Agent (<font SIZE="-1">PMDA</font>) which exports metric values from the <font SIZE="-1">IP</font> connection tracking module in the Linux kernel.</p>
<h2>INSTALLATION</h2>
<p> Install the netfilter PMDA by using the Install script as root: </p>
<p>#&nbsp;<wbr>cd&nbsp;<wbr>$PCP_PMDAS_DIR/netfilter </p>
<p>#&nbsp;<wbr>./Install </p>
<p> To uninstall, do the following as root: </p>
<p>#&nbsp;<wbr>cd&nbsp;<wbr>$PCP_PMDAS_DIR/netfilter </p>
<p>#&nbsp;<wbr>./Remove </p>
<p> <code>pmdanetfilter</code> is launched by <i><a href="/docs/linux/man/1-pmcd/">pmcd</a></i>(1) and should never be executed directly. The Install and Remove scripts notify <i><a href="/docs/linux/man/1-pmcd/">pmcd</a></i>(1) when the agent is installed or removed.</p>
<h2>FILES</h2>
<dl>
<dt><code>$PCP_PMDAS_DIR/netfilter/Install</code></p>
<dd> installation script for the <code>pmdanetfilter</code> agent</p>
<dt><code>$PCP_PMDAS_DIR/netfilter/Remove</code></p>
<dd> undo installation script for the <code>pmdanetfilter</code> agent</p>
<dt><code>$PCP_LOG_DIR/pmcd/netfilter.log</code></p>
<dd> default log file for error messages from <code>pmdanetfilter</code></dl>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by <code>PCP</code>. On each installation, the file <code>/etc/pcp.conf</code> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <i><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></i>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1) and <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1). </p>
<h2>Index</h2>
