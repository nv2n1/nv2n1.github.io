---
title: "ocf_heartbeat_filesystem(7)"
name: "ocf_heartbeat_filesystem"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_heartbeat_filesystem/"
description: "ocf_heartbeat_Filesystem – Manages filesystem mounts"
---

<p>ocf_heartbeat_Filesystem &#8211; Manages filesystem mounts</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>Filesystem</code> [start | stop | monitor | meta-data | validate-all]</dl>
<h2>Description</h2>
<dd>Resource script for Filesystem. It manages a Filesystem on a shared storage medium. </p>
<p> The standard monitor operation of depth 0 (also known as probe) checks if the filesystem is mounted. If you want deeper tests, set OCF_CHECK_LEVEL to one of the following values: </p>
<p> 10: read first 16 blocks of the device (raw read) </p>
<p> This doesn&#8217;t exercise the filesystem at all, but the device on which the filesystem lives. This is noop for non-block devices such as NFS, SMBFS, or bind mounts. </p>
<p> 20: test if a status file can be written and read </p>
<p> The status file must be writable by root. This is not always the case with an NFS mount, as NFS exports usually have the &quot;root_squash&quot; option set. In such a setup, you must either use read-only monitoring (depth=10), export with &quot;no_root_squash&quot; on your NFS server, or grant world write permissions on the directory where the status file is to be placed.</p>
<h2>Supported Parameters</h2>
<p><code>device</code></p>
<dl>
<dd>The name of block device for the filesystem, or -U, -L options for mount, or NFS mount specification. </p>
<p> (required, string, no default)</dl>
<p> <code>directory</code></p>
<dl>
<dd>The mount point for the filesystem. </p>
<p> (required, string, no default)</dl>
<p> <code>fstype</code></p>
<dl>
<dd>The type of filesystem to be mounted. </p>
<p> (required, string, no default)</dl>
<p> <code>options</code></p>
<dl>
<dd>Any extra options to be given as -o options to mount. </p>
<p> For bind mounts, add &quot;bind&quot; here and set fstype to &quot;none&quot;. We will do the right thing for options such as &quot;bind,ro&quot;. </p>
<p> (optional, string, no default)</dl>
<p> <code>statusfile_prefix</code></p>
<dl>
<dd>The prefix to be used for a status file for resource monitoring with depth 20. If you don&#8217;t specify this parameter, all status files will be created in a separate directory. </p>
<p> (optional, string, default &quot;.Filesystem_status/&quot;)</dl>
<p> <code>run_fsck</code></p>
<dl>
<dd>Specify how to decide whether to run fsck or not. </p>
<p> &quot;auto&quot; : decide to run fsck depending on the fstype(default) &quot;force&quot; : always run fsck regardless of the fstype &quot;no&quot; : do not run fsck ever. </p>
<p> (optional, string, default &quot;auto&quot;)</dl>
<p> <code>fast_stop</code></p>
<dl>
<dd>Normally, we expect no users of the filesystem and the stop operation to finish quickly. If you cannot control the filesystem users easily and want to prevent the stop action from failing, then set this parameter to &quot;no&quot; and add an appropriate timeout for the stop operation. </p>
<p> (optional, boolean, default yes)</dl>
<p> <code>force_clones</code></p>
<dl>
<dd>The use of a clone setup for local filesystems is forbidden by default. For special setups like glusterfs, cloning a mount of a local device with a filesystem like ext4 or xfs independently on several nodes is a valid use case. </p>
<p> Only set this to &quot;true&quot; if you know what you are doing! </p>
<p> (optional, boolean, default false)</dl>
<p> <code>force_unmount</code></p>
<dl>
<dd>This option allows specifying how to handle processes that are currently accessing the mount directory. </p>
<p> &quot;true&quot; : Default value, kill processes accessing mount point &quot;safe&quot; : Kill processes accessing mount point using methods that avoid functions that could potentially block during process detection &quot;false&quot; : Do not kill any processes. </p>
<p> The &#8216;safe&#8217; option uses shell logic to walk the /procs/ directory for pids using the mount point while the default option uses the fuser cli tool. fuser is known to perform operations that can potentially block if unresponsive nfs mounts are in use on the system. </p>
<p> (optional, boolean, default true)</dl>
<h2>Supported Actions</h2>
<p>This resource agent supports the following actions (operations): </p>
<p> <code>start</code></p>
<dl>
<dd>Starts the resource. Suggested minimum timeout: 60.</dl>
<p> <code>stop</code></p>
<dl>
<dd>Stops the resource. Suggested minimum timeout: 60.</dl>
<p> <code>notify</code></p>
<dl>
<dd>Suggested minimum timeout: 60.</dl>
<p> <code>monitor</code></p>
<dl>
<dd>Performs a detailed status check. Suggested minimum timeout: 40. Suggested interval: 20.</dl>
<p> <code>validate-all</code></p>
<dl>
<dd>Performs a validation of the resource configuration. Suggested minimum timeout: 5.</dl>
<p> <code>meta-data</code></p>
<dl>
<dd>Retrieves resource agent metadata (internal use only). Suggested minimum timeout: 5.</dl>
<h2>Example Crm Shell</h2>
<p>The following is an example configuration for a Filesystem resource using the <code><a href="/docs/linux/man/8-crm/">crm</a></code>(8) shell: </p>
<dl>
<dd>
<pre>primitive p_Filesystem ocf:heartbeat:Filesystem \
 params \
 device=<i>string</i> \
 directory=<i>string</i> \
 fstype=<i>string</i> \
 op monitor depth=&quot;0&quot; timeout=&quot;40&quot; interval=&quot;20&quot; </pre>
</dl>
<h2>Example Pcs</h2>
<p>The following is an example configuration for a Filesystem resource using <code><a href="/docs/linux/man/8-pcs/">pcs</a></code>(8) </p>
<dl>
<dd>
<pre>pcs resource create p_Filesystem ocf:heartbeat:Filesystem \
 device=<i>string</i> \
 directory=<i>string</i> \
 fstype=<i>string</i> \
 op monitor depth=&quot;0&quot; timeout=&quot;40&quot; interval=&quot;20&quot; </pre>
</dl>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.linux-ha.org/wiki/Filesystem_(resource_agent)">http://www.linux-ha.org/wiki/Filesystem_(resource_agent)</a></code>m[]</p>
<h2>Author</h2>
<p><code>Linux-HA contributors (see the resource agent source for information about individual authors)</code></p>
