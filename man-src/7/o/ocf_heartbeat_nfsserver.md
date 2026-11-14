---
title: "ocf_heartbeat_nfsserver(7)"
name: "ocf_heartbeat_nfsserver"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_heartbeat_nfsserver/"
description: "ocf_heartbeat_nfsserver – Manages an NFS server"
---

<p>ocf_heartbeat_nfsserver &#8211; Manages an NFS server</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>nfsserver</code> [start | stop | monitor | meta-data | validate-all]</dl>
<h2>Description</h2>
<dd>Nfsserver helps to manage the Linux nfs server as a failover-able resource in Linux-HA. It depends on Linux specific NFS implementation details, so is considered not portable to other platforms yet.</p>
<h2>Supported Parameters</h2>
<p><code>nfs_init_script</code></p>
<dl>
<dd>The default init script shipped with the Linux distro. The nfsserver resource agent offloads the start/stop/monitor work to the init script because the procedure to start/stop/monitor nfsserver varies on different Linux distro. In the event that this option is not set, this agent will attempt to use an init script at this location, /etc/init.d/nfs, or detect a systemd unit-file to use in the event that no init script is detected. </p>
<p> (optional, string, default &quot;auto detected&quot;)</dl>
<p> <code>nfs_no_notify</code></p>
<dl>
<dd>Do not send reboot notifications to NFSv3 clients during server startup. </p>
<p> (optional, boolean, default false)</dl>
<p> <code>nfs_notify_foreground</code></p>
<dl>
<dd>Keeps the sm-notify attached to its controlling terminal and running in the foreground. </p>
<p> (optional, boolean, default false)</dl>
<p> <code>nfs_smnotify_retry_time</code></p>
<dl>
<dd>Specifies the length of sm-notify retry time, in minutes, to continue retrying notifications to unresponsive hosts. If this option is not specified, sm-notify attempts to send notifications for 15 minutes. Specifying a value of 0 causes sm-notify to continue sending notifications to unresponsive peers until it is manually killed. </p>
<p> (optional, integer, no default)</dl>
<p> <code>nfs_ip</code></p>
<dl>
<dd>Comma separated list of floating IP addresses used to access the nfs service </p>
<p> (optional, string, no default)</dl>
<p> <code>nfsd_args</code></p>
<dl>
<dd>Specifies what arguments to pass to the nfs daemon on startup. View the rpc.nfsd man page for information on what arguments are available. Note that setting this value will override all settings placed in the local /etc/sysconfig/nfs file. </p>
<p> (optional, string, no default)</dl>
<p> <code>lockd_udp_port</code></p>
<dl>
<dd>The udp port lockd should listen on. Note that setting this value will override all settings placed in the local /etc/sysconfig/nfs file. </p>
<p> (optional, integer, no default)</dl>
<p> <code>lockd_tcp_port</code></p>
<dl>
<dd>The tcp port lockd should listen on. Note that setting this value will override all settings placed in the local /etc/sysconfig/nfs file. </p>
<p> (optional, integer, no default)</dl>
<p> <code>statd_outgoing_port</code></p>
<dl>
<dd>The source port number sm-notify uses when sending reboot notifications. Note that setting this value will override all settings placed in the local /etc/sysconfig/nfs file. </p>
<p> (optional, integer, no default)</dl>
<p> <code>statd_port</code></p>
<dl>
<dd>The port number used for RPC listener sockets. Note that setting this value will override all settings placed in the local /etc/sysconfig/nfs file. </p>
<p> (optional, integer, no default)</dl>
<p> <code>mountd_port</code></p>
<dl>
<dd>The port number used for rpc.mountd listener sockets. Note that setting this value will override all settings placed in the local /etc/sysconfig/nfs file. </p>
<p> (optional, integer, no default)</dl>
<p> <code>rquotad_port</code></p>
<dl>
<dd>The port number used for rpc.rquotad. Note that setting this value will override all settings placed in the local /etc/sysconfig/nfs file. </p>
<p> (optional, integer, no default)</dl>
<p> <code>nfs_shared_infodir</code></p>
<dl>
<dd>The nfsserver resource agent will save nfs related information in this specific directory. And this directory must be able to fail-over before nfsserver itself. </p>
<p> (optional, string, no default)</dl>
<p> <code>rpcpipefs_dir</code></p>
<dl>
<dd>The mount point for the sunrpc file system. Default is /var/lib/nfs/rpc_pipefs. This script will mount (bind) nfs_shared_infodir on /var/lib/nfs/ (cannot be changed), and this script will mount the sunrpc file system on /var/lib/nfs/rpc_pipefs (default, can be changed by this parameter). If you want to move only rpc_pipefs/ (e.g. to keep rpc_pipefs/ local) from default, please set this value. </p>
<p> (optional, string, default &quot;/var/lib/nfs/rpc_pipefs&quot;)</dl>
<h2>Supported Actions</h2>
<p>This resource agent supports the following actions (operations): </p>
<p> <code>start</code></p>
<dl>
<dd>Starts the resource. Suggested minimum timeout: 40.</dl>
<p> <code>stop</code></p>
<dl>
<dd>Stops the resource. Suggested minimum timeout: 20s.</dl>
<p> <code>monitor</code></p>
<dl>
<dd>Performs a detailed status check. Suggested minimum timeout: 20s. Suggested interval: 10.</dl>
<p> <code>meta-data</code></p>
<dl>
<dd>Retrieves resource agent metadata (internal use only). Suggested minimum timeout: 5.</dl>
<p> <code>validate-all</code></p>
<dl>
<dd>Performs a validation of the resource configuration. Suggested minimum timeout: 30.</dl>
<h2>Example Crm Shell</h2>
<p>The following is an example configuration for a nfsserver resource using the <code><a href="/docs/linux/man/8-crm/">crm</a></code>(8) shell: </p>
<dl>
<dd>
<pre>primitive p_nfsserver ocf:heartbeat:nfsserver \
 op monitor depth=&quot;0&quot; timeout=&quot;20s&quot; interval=&quot;10&quot; </pre>
</dl>
<h2>Example Pcs</h2>
<p>The following is an example configuration for a nfsserver resource using <code><a href="/docs/linux/man/8-pcs/">pcs</a></code>(8) </p>
<dl>
<dd>
<pre>pcs resource create p_nfsserver ocf:heartbeat:nfsserver \
 op monitor depth=&quot;0&quot; timeout=&quot;20s&quot; interval=&quot;10&quot; </pre>
</dl>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.linux-ha.org/wiki/nfsserver_(resource_agent)">http://www.linux-ha.org/wiki/nfsserver_(resource_agent)</a></code>m[]</p>
<h2>Author</h2>
<p><code>Linux-HA contributors (see the resource agent source for information about individual authors)</code></p>
