---
title: "pmdagluster(1)"
name: "pmdagluster"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmdagluster/"
description: "pmdagluster – Gluster Filesystem PMDA"
---

<h2>NAME</h2>
<p> <code>pmdagluster</code> &#8211; Gluster Filesystem PMDA</p>
<h2>DESCRIPTION</h2>
<p> <code>pmdagluster</code> is a Performance Metrics Domain Agent (PMDA) which exports metric values about mounted gluster filesystems using the <code><a href="/docs/linux/man/8-gluster/">gluster</a></code>(8) command. This PMDA exports metrics about volumes and bricks both local and remote to the node where pmdagluster is running. </p>
<p> The gluster filesystem supports fine-grained control over enabling statistics on individual volumes, so that the values are optionally enabled or disabled on systems where they are not desired to be monitored. </p>
<p> The <code><a href="/docs/linux/man/1-pmstore/">pmstore</a></code>(1) command can be used to enable and disable profiling of volumes. Using the individual instances of the gluster.volume.profile metric, one can set their values (and associated profiling) either on (1) or off (0). Additionally, <code><a href="/docs/linux/man/1-pminfo/">pminfo</a></code>(1) can report on the current status of profiling of each volume. </p>
<pre><code>
#pminfo - f gluster.volume.profile
gluster.volume.profile
    inst[0 or "gv0"] value 0 inst[1 or "gv1"] value 1
#pmstore - i "gv0" gluster.volume.profile 1
    gluster.volume.profile inst[0 or "gv0"] old value = 0 new value = 1
</code></pre>
<p> Further details on the gluster filesystem can be found at <a rel="nofollow" href="http://www.gluster.org">http://www.gluster.org</a></p>
<h2>INSTALLATION</h2>
<p> Install the gluster PMDA by using the Install script as root: </p>
<p>#&nbsp;<wbr>cd&nbsp;<wbr>$PCP_PMDAS_DIR/gluster </p>
<p>#&nbsp;<wbr>./Install </p>
<p> To uninstall, do the following as root: </p>
<p>#&nbsp;<wbr>cd&nbsp;<wbr>$PCP_PMDAS_DIR/gluster </p>
<p>#&nbsp;<wbr>./Remove </p>
<p> <code>pmdagluster</code> is launched by <i><a href="/docs/linux/man/1-pmcd/">pmcd</a></i>(1) and should never be executed directly. The Install and Remove scripts notify <i><a href="/docs/linux/man/1-pmcd/">pmcd</a></i>(1) when the agent is installed or removed.</p>
<h2>FILES</h2>
<dl>
<dt><code>$PCP_PMDAS_DIR/gluster/Install</code></p>
<dd> installation script for the <code>pmdagluster</code> agent</p>
<dt><code>$PCP_PMDAS_DIR/gluster/Remove</code></p>
<dd> undo installation script for the <code>pmdagluster</code> agent</p>
<dt><code>$PCP_LOG_DIR/pmcd/gluster.log</code></p>
<dd> default log file for error messages from <code>pmdagluster</code></dl>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by <code>PCP</code>. On each installation, the file <code>/etc/pcp.conf</code> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <i><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></i>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1), <code><a href="/docs/linux/man/1-pminfo/">pminfo</a></code>(1), <code><a href="/docs/linux/man/1-pmstore/">pmstore</a></code>(1), and <code><a href="/docs/linux/man/8-gluster/">gluster</a></code>(8) </p>
<h2>Index</h2>
