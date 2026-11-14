---
title: "pmdacifs(1)"
name: "pmdacifs"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmdacifs/"
description: "pmdacifs – Common Internet Filesystem (CIFS) PMDA"
---

<h2>NAME</h2>
<p> <code>pmdacifs</code> &#8211; Common Internet Filesystem (CIFS) PMDA</p>
<h2>DESCRIPTION</h2>
<p> <code>pmdacifs</code> is a Performance Metrics Domain Agent (PMDA) which exports metric values about mounted CIFS shares from the /proc/fs/cifs directory. This PMDA requires at least the CIFS kernel module to be loaded to return some metric values and at least one mounted CIFS share in order to provide data for all metrics. </p>
<p> Further details on CIFS can be found at <a rel="nofollow" href="http://redhat.com">http://redhat.com</a></p>
<h2>INSTALLATION</h2>
<p> Install the CIFS PMDA by using the Install script as root: </p>
<p>#&nbsp;<wbr>cd&nbsp;<wbr>$PCP_PMDAS_DIR/cifs </p>
<p>#&nbsp;<wbr>./Install </p>
<p> To uninstall, do the following as root: </p>
<p>#&nbsp;<wbr>cd&nbsp;<wbr>$PCP_PMDAS_DIR/cifs </p>
<p>#&nbsp;<wbr>./Remove </p>
<p> <code>pmdacifs</code> is launched by <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) and should never be executed directly. The Install and Remove scripts notify <code>pmcd</code> when the agent is installed or removed.</p>
<h2>FILES</h2>
<dl>
<dt><code>$PCP_PMDAS_DIR/cifs/help</code></p>
<dd> default help text file for the CIFS metrics</p>
<dt><code>$PCP_PMDAS_DIR/cifs/Install</code></p>
<dd> installation script for the <code>pmdacifs</code> agent</p>
<dt><code>$PCP_PMDAS_DIR/cifs/Remove</code></p>
<dd> undo installation script for the <code>pmdacifs</code> agent</p>
<dt><code>$PCP_LOG_DIR/pmcd/cifs.log</code></p>
<dd> default log file for error messages from <code>pmdacifs</code></dl>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by <code>PCP</code>. On each installation, the file <code>/etc/pcp.conf</code> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <i><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></i>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1), <code><a href="/docs/linux/man/1-pmstore/">pmstore</a></code>(1), and <code><a href="/docs/linux/man/8-mount-cifs/">mount.cifs</a></code>(8). </p>
<h2>Index</h2>
