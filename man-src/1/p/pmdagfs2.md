---
title: "pmdagfs2(1)"
name: "pmdagfs2"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmdagfs2/"
description: "pmdagfs2 – Global Filesystem v2 (GFS2) PMDA"
---

<h2>NAME</h2>
<p> <code>pmdagfs2</code> &#8211; Global Filesystem v2 (GFS2) PMDA</p>
<h2>DESCRIPTION</h2>
<p> <code>pmdagfs2</code> is a Performance Metrics Domain Agent (PMDA) which exports metric values about mounted GFS2 filesystems from the debugfs filesystem. This PMDA requires debugfs along with at least one mounted GFS2 filesystem to be mounted in order to be able to provide metric data. </p>
<p> This PMDA can be used with GFS2 filesystems which are both mounted as local filesystems and filesystems which are mounted as shared storage within a clustered environment. However there are some metrics which specifically require GFS2 to be setup in a clustered environment to be able to provide metric data. This is due to them expecting locking messages to be passed via the distributed lock manager (DLM) between nodes of a cluster in order to generate their output. </p>
<p> These cluster-environment-only metrics can be distinguished by the inclusion of their corresponding control metrics so that they can be optionally enabled or disabled on systems where they are not desired to be monitored or not supported. </p>
<p> <code><a href="/docs/linux/man/3-pmstore/">pmstore</a></code>(3) can be used to assign values to these control metrics in order to enable (1) or disable (0) them. This mechanism is also useful on distributions that do not currently have full support for the GFS2 trace-points or provide older versions of the GFS2 driver. </p>
<p> Further details on clustering and GFS2 can be found at <a rel="nofollow" href="http://redhat.com">http://redhat.com</a></p>
<h2>INSTALLATION</h2>
<p> Install the GFS2 PMDA by using the Install script as root: </p>
<p>#&nbsp;<wbr>cd&nbsp;<wbr>$PCP_PMDAS_DIR/gfs2 </p>
<p>#&nbsp;<wbr>./Install </p>
<p> To uninstall, do the following as root: </p>
<p>#&nbsp;<wbr>cd&nbsp;<wbr>$PCP_PMDAS_DIR/gfs2 </p>
<p>#&nbsp;<wbr>./Remove </p>
<p> <code>pmdagfs2</code> is launched by <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) and should never be executed directly. The Install and Remove scripts notify <code>pmcd</code> when the agent is installed or removed.</p>
<h2>FILES</h2>
<dl>
<dt><code>$PCP_PMDAS_DIR/gfs2/help</code></p>
<dd> default help text file for the GFS2 metrics</p>
<dt><code>$PCP_PMDAS_DIR/gfs2/Install</code></p>
<dd> installation script for the <code>pmdagfs2</code> agent</p>
<dt><code>$PCP_PMDAS_DIR/gfs2/Remove</code></p>
<dd> undo installation script for the <code>pmdagfs2</code> agent</p>
<dt><code>$PCP_LOG_DIR/pmcd/gfs2.log</code></p>
<dd> default log file for error messages from <code>pmdagfs2</code></dl>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by <code>PCP</code>. On each installation, the file <code>/etc/pcp.conf</code> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <i><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></i>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1), <code><a href="/docs/linux/man/1-pmstore/">pmstore</a></code>(1), and <code><a href="/docs/linux/man/5-gfs2/">gfs2</a></code>(5). </p>
<h2>Index</h2>
