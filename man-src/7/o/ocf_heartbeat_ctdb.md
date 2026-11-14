---
title: "ocf_heartbeat_ctdb(7)"
name: "ocf_heartbeat_ctdb"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_heartbeat_ctdb/"
description: "ocf_heartbeat_CTDB – CTDB Resource Agent"
---

<p>ocf_heartbeat_CTDB &#8211; CTDB Resource Agent</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>CTDB</code> [start | stop | monitor | meta-data | validate-all]</dl>
<h2>Description</h2>
<dd>This resource agent manages CTDB, allowing one to use Clustered Samba in a Linux-HA/Pacemaker cluster. You need a shared filesystem (e.g. OCFS2 or GFS2) on which the CTDB lock will be stored. Create /etc/ctdb/nodes containing a list of private IP addresses of each node in the cluster, then configure this RA as a clone. This agent expects the samba and windbind resources to be managed outside of CTDB&#8217;s control as a separate set of resources controlled by the cluster manager. The optional support for enabling CTDB management of these daemons will be depreciated. </p>
<p> For more information see <a rel="nofollow" href="http://linux-ha.org/wiki/CTDB_(resource_agent)">http://linux-ha.org/wiki/CTDB_(resource_agent)</a></p>
<h2>Supported Parameters</h2>
<p><code>ctdb_recovery_lock</code></p>
<dl>
<dd>The location of a shared lock file, common across all nodes. This must be on shared storage, e.g.: /shared-fs/samba/ctdb.lock </p>
<p> (unique, required, string, no default)</dl>
<p> <code>ctdb_manages_samba</code></p>
<dl>
<dd>Should CTDB manage starting/stopping the Samba service for you? This will be deprecated in future, in favor of configuring a separate Samba resource. </p>
<p> (optional, boolean, default no)</dl>
<p> <code>ctdb_manages_winbind</code></p>
<dl>
<dd>Should CTDB manage starting/stopping the Winbind service for you? This will be deprecated in future, in favor of configuring a separate Winbind resource. </p>
<p> (optional, boolean, default no)</dl>
<p> <code>ctdb_service_smb</code></p>
<dl>
<dd>Name of smb init script. Only necessary if CTDB is managing Samba directly. Will usually be auto-detected. </p>
<p> (optional, string, no default)</dl>
<p> <code>ctdb_service_nmb</code></p>
<dl>
<dd>Name of nmb init script. Only necessary if CTDB is managing Samba directly. Will usually be auto-detected. </p>
<p> (optional, string, no default)</dl>
<p> <code>ctdb_service_winbind</code></p>
<dl>
<dd>Name of winbind init script. Only necessary if CTDB is managing Winbind directly. Will usually be auto-detected. </p>
<p> (optional, string, no default)</dl>
<p> <code>ctdb_samba_skip_share_check</code></p>
<dl>
<dd>If there are very many shares it may not be feasible to check that all of them are available during each monitoring interval. In that case this check can be disabled. </p>
<p> (optional, boolean, default yes)</dl>
<p> <code>ctdb_monitor_free_memory</code></p>
<dl>
<dd>If the amount of free memory drops below this value the node will become unhealthy and ctdb and all managed services will be shutdown. Once this occurs, the administrator needs to find the reason for the OOM situation, rectify it and restart ctdb with &quot;service ctdb start&quot;. </p>
<p> (optional, integer, default 100)</dl>
<p> <code>ctdb_start_as_disabled</code></p>
<dl>
<dd>When set to yes, the CTDB node will start in DISABLED mode and not host any public ip addresses. </p>
<p> (optional, boolean, default no)</dl>
<p> <code>ctdb_config_dir</code></p>
<dl>
<dd>The directory containing various CTDB configuration files. The &quot;nodes&quot; and &quot;notify.sh&quot; scripts are expected to be in this directory, as is the &quot;events.d&quot; subdirectory. </p>
<p> (optional, string, default &quot;/etc/ctdb&quot;)</dl>
<p> <code>ctdb_binary</code></p>
<dl>
<dd>Full path to the CTDB binary. </p>
<p> (optional, string, default &quot;/usr/bin/ctdb&quot;)</dl>
<p> <code>ctdbd_binary</code></p>
<dl>
<dd>Full path to the CTDB cluster daemon binary. </p>
<p> (optional, string, default &quot;/usr/sbin/ctdbd&quot;)</dl>
<p> <code>ctdb_socket</code></p>
<dl>
<dd>Full path to the domain socket that ctdbd will create, used for local clients to attach and communicate with the ctdb daemon. </p>
<p> (unique, optional, string, default &quot;/run/ctdb/ctdbd.socket&quot;)</dl>
<p> <code>ctdb_dbdir</code></p>
<dl>
<dd>The directory to put the local CTDB database files in. Persistent database files will be put in ctdb_dbdir/persistent. </p>
<p> (unique, optional, string, default &quot;/var/run&quot;)</dl>
<p> <code>ctdb_logfile</code></p>
<dl>
<dd>Full path to log file. To log to syslog instead, use the value &quot;syslog&quot;. </p>
<p> (optional, string, default &quot;/var/log/ctdb/log.ctdb&quot;)</dl>
<p> <code>ctdb_rundir</code></p>
<dl>
<dd>Full path to ctdb runtime directory, used for storage of socket lock state. </p>
<p> (optional, string, default &quot;/run/ctdb&quot;)</dl>
<p> <code>ctdb_debuglevel</code></p>
<dl>
<dd>What debug level to run at (0-10). Higher means more verbose. </p>
<p> (optional, integer, default 2)</dl>
<p> <code>smb_conf</code></p>
<dl>
<dd>Path to default samba config file. Only necessary if CTDB is managing Samba. </p>
<p> (optional, string, default &quot;/etc/samba/smb.conf&quot;)</dl>
<p> <code>smb_private_dir</code></p>
<dl>
<dd>The directory for smbd to use for storing such files as smbpasswd and secrets.tdb. Old versions of CTBD (prior to 1.0.50) required this to be on shared storage. This parameter should not be set for current versions of CTDB, and only remains in the RA for backwards compatibility. </p>
<p> (unique, optional, string, no default)</dl>
<p> <code>smb_passdb_backend</code></p>
<dl>
<dd>Which backend to use for storing user and possibly group information. Only necessary if CTDB is managing Samba. </p>
<p> (optional, string, default &quot;tdbsam&quot;)</dl>
<p> <code>smb_idmap_backend</code></p>
<dl>
<dd>Which backend to use for SID/uid/gid mapping. Only necessary if CTDB is managing Samba. </p>
<p> (optional, string, default &quot;tdb2&quot;)</dl>
<p> <code>smb_fileid_algorithm</code></p>
<dl>
<dd>Which fileid:algorithm to use with vfs_fileid. The correct value depends on which clustered filesystem is in use, e.g.: for OCFS2, this should be set to &quot;fsid&quot;. Only necessary if CTDB is managing Samba. </p>
<p> (optional, string, no default)</dl>
<h2>Supported Actions</h2>
<p>This resource agent supports the following actions (operations): </p>
<p> <code>start</code></p>
<dl>
<dd>Starts the resource. Suggested minimum timeout: 90.</dl>
<p> <code>stop</code></p>
<dl>
<dd>Stops the resource. Suggested minimum timeout: 100.</dl>
<p> <code>monitor</code></p>
<dl>
<dd>Performs a detailed status check. Suggested minimum timeout: 20. Suggested interval: 10.</dl>
<p> <code>meta-data</code></p>
<dl>
<dd>Retrieves resource agent metadata (internal use only). Suggested minimum timeout: 5.</dl>
<p> <code>validate-all</code></p>
<dl>
<dd>Performs a validation of the resource configuration. Suggested minimum timeout: 30.</dl>
<h2>Example Crm Shell</h2>
<p>The following is an example configuration for a CTDB resource using the <code><a href="/docs/linux/man/8-crm/">crm</a></code>(8) shell: </p>
<dl>
<dd>
<pre>primitive p_CTDB ocf:heartbeat:CTDB \
 params \
 ctdb_recovery_lock=<i>string</i> \
 op monitor timeout=&quot;20&quot; interval=&quot;10&quot; depth=&quot;0&quot; </pre>
</dl>
<h2>Example Pcs</h2>
<p>The following is an example configuration for a CTDB resource using <code><a href="/docs/linux/man/8-pcs/">pcs</a></code>(8) </p>
<dl>
<dd>
<pre>pcs resource create p_CTDB ocf:heartbeat:CTDB \
 ctdb_recovery_lock=<i>string</i> \
 op monitor timeout=&quot;20&quot; interval=&quot;10&quot; depth=&quot;0&quot; </pre>
</dl>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.linux-ha.org/wiki/CTDB_(resource_agent)">http://www.linux-ha.org/wiki/CTDB_(resource_agent)</a></code>m[]</p>
<h2>Author</h2>
<p><code>Linux-HA contributors (see the resource agent source for information about individual authors)</code></p>
