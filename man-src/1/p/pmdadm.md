---
title: "pmdadm(1)"
name: "pmdadm"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmdadm/"
description: "pmdadm – Device Mapper PMDA"
---

<h2>NAME</h2>
<p> <code>pmdadm</code> &#8211; Device Mapper PMDA</p>
<h2>DESCRIPTION</h2>
<p> <code>pmdadm</code> is a Performance Metrics Domain Agent (PMDA) which exports metric values for Devic Mapper on the local system. </p>
<p> This PMDA collects its data through the <code><a href="/docs/linux/man/8-dmsetup/">dmsetup</a></code>(8) utility and requires that the program is installed in order to function. </p>
<p> Further details on device mapper can be found at <a rel="nofollow" href="http://redhat.com">http://redhat.com</a></p>
<h2>INSTALLATION</h2>
<p> Install the DM PMDA by using the Install script as root: </p>
<p>#&nbsp;<wbr>cd&nbsp;<wbr>$PCP_PMDAS_DIR/dm </p>
<p>#&nbsp;<wbr>./Install </p>
<p> To uninstall, do the following as root: </p>
<p>#&nbsp;<wbr>cd&nbsp;<wbr>$PCP_PMDAS_DIR/dm </p>
<p>#&nbsp;<wbr>./Remove </p>
<p> <code>pmdadm</code> is launched by <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) and should never be executed directly. The Install and Remove scripts notify <code>pmcd</code> when the agent is installed or removed.</p>
<h2>FILES</h2>
<dl>
<dt><code>$PCP_PMDAS_DIR/dm/help</code></p>
<dd> default help text file for the dm metrics</p>
<dt><code>$PCP_PMDAS_DIR/dm/Install</code></p>
<dd> installation script for the <code>pmdadm</code> agent</p>
<dt><code>$PCP_PMDAS_DIR/dm/Remove</code></p>
<dd> undo installation script for the <code>pmdadm</code> agent</p>
<dt><code>$PCP_LOG_DIR/pmcd/dm.log</code></p>
<dd> default log file for error messages from <code>pmdadm</code></dl>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by <code>PCP</code>. On each installation, the file <code>/etc/pcp.conf</code> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <i><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></i>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1), <code><a href="/docs/linux/man/1-pmstore/">pmstore</a></code>(1), and <code><a href="/docs/linux/man/8-dmsetup/">dmsetup</a></code>(8). </p>
<h2>Index</h2>
