---
title: "ocf_heartbeat_exportfs(7)"
name: "ocf_heartbeat_exportfs"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_heartbeat_exportfs/"
description: "ocf_heartbeat_exportfs – Manages NFS exports"
---

<p>ocf_heartbeat_exportfs &#8211; Manages NFS exports</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>exportfs</code> [start | stop | monitor | meta-data | validate-all]</dl>
<h2>Description</h2>
<dd>Exportfs uses the exportfs command to add/remove nfs exports. It does NOT manage the nfs server daemon. It depends on Linux specific NFS implementation details, so is considered not portable to other platforms yet.</p>
<h2>Supported Parameters</h2>
<p><code>clientspec</code></p>
<dl>
<dd>The client specification allowing remote machines to mount the directory over NFS. </p>
<p> (required, string, no default)</dl>
<p> <code>options</code></p>
<dl>
<dd>The options to pass to exportfs for the exported directory. </p>
<p> (optional, string, no default)</dl>
<p> <code>directory</code></p>
<dl>
<dd>The directory which you wish to export using NFS. </p>
<p> (required, string, no default)</dl>
<p> <code>fsid</code></p>
<dl>
<dd>The fsid option to pass to exportfs. This can be a unique positive integer, a UUID, or the special string &quot;root&quot; which is functionally identical to numeric fsid of 0. 0 (root) identifies the export as the root of an NFSv4 pseudofilesystem &#8212; avoid this setting unless you understand its special status. This value will override any fsid provided via the options parameter. </p>
<p> (unique, required, string, no default)</dl>
<p> <code>unlock_on_stop</code></p>
<dl>
<dd>Relinquish NFS locks associated with this filesystem when the resource stops. Enabling this parameter is highly recommended unless the path exported by this exportfs resource is also exported by a different resource. </p>
<p> Note: Unlocking is only possible on Linux systems where /proc/fs/nfsd/unlock_filesystem exists and is writable. If your system does not fulfill this requirement (on account of having an nonrecent kernel, for example), you may set this parameter to 0 to silence the associated warning. </p>
<p> (optional, boolean, default 0)</dl>
<p> <code>wait_for_leasetime_on_stop</code></p>
<dl>
<dd>When stopping (unexporting), wait out the NFSv4 lease time. Only after all leases have expired does the NFS kernel server relinquish all server-side handles on the exported filesystem. If this exportfs resource manages an export that resides on a mount point designed to fail over along with the NFS export itself, then enabling this parameter will ensure such failover is working properly. Note that when this parameter is set, your stop timeout MUST accommodate for the wait period. This parameter is safe to disable if none of your NFS clients are using NFS version 4 or later. </p>
<p> (optional, boolean, default 0)</dl>
<p> <code>rmtab_backup</code></p>
<dl>
<dd>Back up those entries from the NFS rmtab that apply to the exported directory, to the specified backup file. The filename is interpreted as relative to the exported directory. This backup is required if clients are connecting to the export via NFSv3 over TCP. Note that a configured monitor operation is required for this functionality. </p>
<p> To disable rmtab backups, set this parameter to the special string &quot;none&quot;. </p>
<p> (optional, string, default &quot;.rmtab&quot;)</dl>
<h2>Supported Actions</h2>
<p>This resource agent supports the following actions (operations): </p>
<p> <code>start</code></p>
<dl>
<dd>Starts the resource. Suggested minimum timeout: 40.</dl>
<p> <code>stop</code></p>
<dl>
<dd>Stops the resource. Suggested minimum timeout: 120.</dl>
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
<p>The following is an example configuration for a exportfs resource using the <code><a href="/docs/linux/man/8-crm/">crm</a></code>(8) shell: </p>
<dl>
<dd>
<pre>primitive p_exportfs ocf:heartbeat:exportfs \
 params \
 clientspec=<i>string</i> \
 directory=<i>string</i> \
 fsid=<i>string</i> \
 op monitor depth=&quot;0&quot; timeout=&quot;20&quot; interval=&quot;10&quot; </pre>
</dl>
<h2>Example Pcs</h2>
<p>The following is an example configuration for a exportfs resource using <code><a href="/docs/linux/man/8-pcs/">pcs</a></code>(8) </p>
<dl>
<dd>
<pre>pcs resource create p_exportfs ocf:heartbeat:exportfs \
 clientspec=<i>string</i> \
 directory=<i>string</i> \
 fsid=<i>string</i> \
 op monitor depth=&quot;0&quot; timeout=&quot;20&quot; interval=&quot;10&quot; </pre>
</dl>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.linux-ha.org/wiki/exportfs_(resource_agent)">http://www.linux-ha.org/wiki/exportfs_(resource_agent)</a></code>m[]</p>
<h2>Author</h2>
<p><code>Linux-HA contributors (see the resource agent source for information about individual authors)</code></p>
