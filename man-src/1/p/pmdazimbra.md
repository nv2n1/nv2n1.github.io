---
title: "pmdazimbra(1)"
name: "pmdazimbra"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmdazimbra/"
description: "pmdazimbra – Zimbra Collaboration Suite (ZCS) PMDA"
---

<h2>NAME</h2>
<p> <code>pmdazimbra</code> &#8211; Zimbra Collaboration Suite (ZCS) PMDA</p>
<h2>DESCRIPTION</h2>
<p> <code>pmdazimbra</code> is a Performance Metrics Domain Agent (<font SIZE="-1">PMDA</font>) which exports metric values from several subsystems of the Zimbra Suite. Further details on Zimbra can be found at <a rel="nofollow" href="http://www.zimbra.com/.">http://www.zimbra.com/.</a></p>
<h2>INSTALLATION</h2>
<p> Install the zimbra PMDA by using the Install script as root: </p>
<p>#&nbsp;<wbr>cd&nbsp;<wbr>$PCP_PMDAS_DIR/zimbra </p>
<p>#&nbsp;<wbr>./Install </p>
<p> To uninstall, do the following as root: </p>
<p>#&nbsp;<wbr>cd&nbsp;<wbr>$PCP_PMDAS_DIR/zimbra </p>
<p>#&nbsp;<wbr>./Remove </p>
<p> <code>pmdazimbra</code> is launched by <i><a href="/docs/linux/man/1-pmcd/">pmcd</a></i>(1) and should never be executed directly. The Install and Remove scripts notify <i><a href="/docs/linux/man/1-pmcd/">pmcd</a></i>(1) when the agent is installed or removed.</p>
<h2>FILES</h2>
<dl>
<dt><code>/opt/zimbra/zmstat/*</code></p>
<dd> comma-separated value files containing Zimbra performance data</p>
<dt><code>$PCP_PMDAS_DIR/zimbra/Install</code></p>
<dd> installation script for the <code>pmdazimbra</code> agent</p>
<dt><code>$PCP_PMDAS_DIR/zimbra/Remove</code></p>
<dd> undo installation script for the <code>pmdazimbra</code> agent</p>
<dt><code>$PCP_LOG_DIR/pmcd/zimbra.log</code></p>
<dd> default log file for error messages from <code>pmdazimbra</code></dl>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by <code>PCP</code>. On each installation, the file <code>/etc/pcp.conf</code> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <i><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></i>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) and <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1). </p>
<h2>Index</h2>
