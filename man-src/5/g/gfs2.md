---
title: "gfs2(5)"
name: "gfs2"
section: "5"
letter: "g"
url: "/docs/linux/man/5-gfs2/"
description: "gfs2 – GFS2 reference guide"
---

<p>gfs2 &#8211; GFS2 reference guide</p>
<h2>Synopsis</h2>
<p>Overview of the GFS2 filesystem </p>
<h2>Description</h2>
<p>GFS2 is a clustered filesystem, designed for sharing data between multiple nodes connected to a common shared storage device. It can also be used as a local filesystem on a single node, however since the design is aimed at clusters, that will usually result in lower performance than using a filesystem designed specifically for single node use. GFS2 is a journaling filesystem and one journal is required for each node that will mount the filesystem. The one exception to that is spectator mounts which are equivalent to mounting a read-only block device and as such can neither recover a journal or write to the filesystem, so do not require a journal assigned to them. </p>
<h2>Mount Options</h2>
<dl>
<dt><code>lockproto=</code><i>LockProtoName</i></p>
<dd>This specifies which inter-node lock protocol is used by the GFS2 filesystem for this mount, overriding the default lock protocol name stored in the filesystem&#8217;s on-disk superblock. </p>
<p> The <i>LockProtoName</i> must be one of the supported locking protocols, currently these are <i>lock_nolock</i> and <i>lock_dlm</i>. </p>
<p> The default lock protocol name is written to disk initially when creating the filesystem with <code><a href="/docs/linux/man/8-mkfs-gfs2/">mkfs.gfs2</a></code>(8), -p option. It can be changed on-disk by using the <code><a href="/docs/linux/man/8-gfs2_tool/">gfs2_tool</a></code>(8) utility&#8217;s <code>sb proto</code> command. </p>
<p> The <code>lockproto</code> mount option should be used only under special circumstances in which you want to temporarily use a different lock protocol without changing the on-disk default. Using the incorrect lock protocol on a cluster filesystem mounted from more than one node will almost certainly result in filesystem corruption.</p>
<dt><code>locktable=</code><i>LockTableName</i></p>
<dd>This specifies the identity of the cluster and of the filesystem for this mount, overriding the default cluster/filesystem identify stored in the filesystem&#8217;s on-disk superblock. The cluster/filesystem name is recognized globally throughout the cluster, and establishes a unique namespace for the inter-node locking system, enabling the mounting of multiple GFS2 filesystems. </p>
<p> The format of <i>LockTableName</i> is lock-module-specific. For <i>lock_dlm</i>, the format is <i>clustername:fsname</i>. For <i>lock_nolock</i>, the field is ignored. </p>
<p> The default cluster/filesystem name is written to disk initially when creating the filesystem with <code><a href="/docs/linux/man/8-mkfs-gfs2/">mkfs.gfs2</a></code>(8), -t option. It can be changed on-disk by using the <code><a href="/docs/linux/man/8-gfs2_tool/">gfs2_tool</a></code>(8) utility&#8217;s <code>sb table</code> command. </p>
<p> The <code>locktable</code> mount option should be used only under special circumstances in which you want to mount the filesystem in a different cluster, or mount it as a different filesystem name, without changing the on-disk default.</p>
<dt><code>localflocks</code></p>
<dd>This flag tells GFS2 that it is running as a local (not clustered) filesystem, so it can allow the kernel VFS layer to do all flock and fcntl file locking. When running in cluster mode, these file locks require inter-node locks, and require the support of GFS2. When running locally, better performance is achieved by letting VFS handle the whole job. </p>
<p> This is turned on automatically by the lock_nolock module.</p>
<dt><code>errors=</code><i>[panic|withdraw]</i></p>
<dd>Setting errors=panic causes GFS2 to oops when encountering an error that would otherwise cause the mount to withdraw or print an assertion warning. The default setting is errors=withdraw. This option should not be used in a production system. It replaces the earlier <code>debug</code> option on kernel versions 2.6.31 and above.</p>
<dt><code>acl</code></p>
<dd>Enables POSIX Access Control List <code><a href="/docs/linux/man/5-acl/">acl</a></code>(5) support within GFS2.</p>
<dt><code>spectator</code></p>
<dd>Mount this filesystem using a special form of read-only mount. The mount does not use one of the filesystem&#8217;s journals. The node is unable to recover journals for other nodes.</p>
<dt><code>norecovery</code></p>
<dd>A synonym for spectator</p>
<dt><code>suiddir</code></p>
<dd>Sets owner of any newly created file or directory to be that of parent directory, if parent directory has S_ISUID permission attribute bit set. Sets S_ISUID in any new directory, if its parent directory&#8217;s S_ISUID is set. Strips all execution bits on a new file, if parent directory owner is different from owner of process creating the file. Set this option only if you know why you are setting it.</p>
<dt><code>quota=</code><i>[off/account/on]</i></p>
<dd>Turns quotas on or off for a filesystem. Setting the quotas to be in the &quot;account&quot; state causes the per UID/GID usage statistics to be correctly maintained by the filesystem, limit and warn values are ignored. The default value is &quot;off&quot;.</p>
<dt><code>discard</code></p>
<dd>Causes GFS2 to generate &quot;discard&quot; I/O requests for blocks which have been freed. These can be used by suitable hardware to implement thin-provisioning and similar schemes. This feature is supported in kernel version 2.6.30 and above.</p>
<dt><code>barrier</code></p>
<dd>This option, which defaults to on, causes GFS2 to send I/O barriers when flushing the journal. The option is automatically turned off if the underlying device does not support I/O barriers. We highly recommend the use of I/O barriers with GFS2 at all times unless the block device is designed so that it cannot lose its write cache content (e.g. its on a UPS, or it doesn&#8217;t have a write cache)</p>
<dt><code>commit=</code><i>secs</i></p>
<dd>This is similar to the ext3 <code>commit=</code> option in that it sets the maximum number of seconds between journal commits if there is dirty data in the journal. The default is 60 seconds. This option is only provided in kernel versions 2.6.31 and above.</p>
<dt><code>data=</code><i>[ordered|writeback]</i></p>
<dd>When data=ordered is set, the user data modified by a transaction is flushed to the disk before the transaction is committed to disk. This should prevent the user from seeing uninitialized blocks in a file after a crash. Data=writeback mode writes the user data to the disk at any time after it&#8217;s dirtied. This doesn&#8217;t provide the same consistency guarantee as ordered mode, but it should be slightly faster for some workloads. The default is ordered mode.</p>
<dt><code>meta</code></p>
<dd>This option results in selecting the meta filesystem root rather than the normal filesystem root. This option is normally only used by the GFS2 utility functions. Altering any file on the GFS2 meta filesystem may render the filesystem unusable, so only experts in the GFS2 on-disk layout should use this option.</p>
<dt><code>quota_quantum=</code><i>secs</i></p>
<dd>This sets the number of seconds for which a change in the quota information may sit on one node before being written to the quota file. This is the preferred way to set this parameter. The value is an integer number of seconds greater than zero. The default is 60 seconds. Shorter settings result in faster updates of the lazy quota information and less likelihood of someone exceeding their quota. Longer settings make filesystem operations involving quotas faster and more efficient.</p>
<dt><code>statfs_quantum=</code><i>secs</i></p>
<dd>Setting statfs_quantum to 0 is the preferred way to set the slow version of statfs. The default value is 30 secs which sets the maximum time period before statfs changes will be syned to the master statfs file. This can be adjusted to allow for faster, less accurate statfs values or slower more accurate values. When set to 0, statfs will always report the true values.</p>
<dt><code>statfs_percent=</code><i>value</i></p>
<dd>This setting provides a bound on the maximum percentage change in the statfs information on a local basis before it is synced back to the master statfs file, even if the time period has not expired. If the setting of statfs_quantum is 0, then this setting is ignored.</p>
<dt><code>rgrplvb</code></p>
<dd>This flag tells gfs2 to look for information about a resource group&#8217;s free space and unlinked inodes in its glock lock value block. This keeps gfs2 from having to read in the resource group data from disk, speeding up allocations in some cases. This option was added in the 3.6 Linux kernel. Prior to this kernel, no information was saved to the resource group lvb. <code>Note:</code> To safely turn on this option, all nodes mounting the filesystem must be running at least a 3.6 Linux kernel. If any nodes had previously mounted the filesystem using older kernels, the filesystem must be unmounted on all nodes before it can be mounted with this option enabled. This option does not need to be enabled on all nodes using a filesystem.</p>
<dt><code>loccookie</code></p>
<dd>This flag tells gfs2 to use location based readdir cookies, instead of its usual filename hash readdir cookies. The filename hash cookies are not guaranteed to be unique, and as the number of files in a directory increases, so does the likelihood of a collision. NFS requires readdir cookies to be unique, which can cause problems with very large directories (over 100,000 files). With this flag set, gfs2 will try to give out location based cookies. Since the cookie is 31 bits, gfs2 will eventually run out of unique cookies, and will fail back to using hash cookies. The maximum number of files that could have unique location cookies assuming perfectly even hashing and names of 8 or fewer characters is 1,073,741,824. An average directory should be able to give out well over half a billion location based cookies. This option was added in the 4.5 Linux kernel. Prior to this kernel, gfs2 did not add directory entries in a way that allowed it to use location based readdir cookies. <code>Note:</code> To safely turn on this option, all nodes mounting the filesystem must be running at least a 4.5 Linux kernel or RHEL 7.3. If this option is only enabled on some of the nodes mounting a filesystem, the cookies returned by nodes using this option will not be valid on nodes that are not using this option, and vice versa. Finally, when first enabling this option on a filesystem that had been previously mounted without it, you must make sure that there are no outstanding cookies being cached by other software, such as NFS. </p>
</dl>
<h2>Bugs</h2>
<p>GFS2 doesn&#8217;t support <code>errors=</code><i>remount-ro</i> or <code>data=</code><i>journal</i>. It is not possible to switch support for user and group quotas on and off independently of each other. Some of the error messages are rather cryptic, if you encounter one of these messages check firstly that gfs_controld is running and secondly that you have enough journals on the filesystem for the number of nodes in use. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-mount/">mount</a></code>(8) for general mount options, <code><a href="/docs/linux/man/1-chmod/">chmod</a></code>(1) and <code><a href="/docs/linux/man/2-chmod/">chmod</a></code>(2) for access permission flags, <code><a href="/docs/linux/man/5-acl/">acl</a></code>(5) for access control lists, <code><a href="/docs/linux/man/8-lvm/">lvm</a></code>(8) for volume management, <code><a href="/docs/linux/man/7-ccs/">ccs</a></code>(7) for cluster management, <code><a href="/docs/linux/man/8-umount/">umount</a></code>(8), <code><a href="/docs/linux/man/4-initrd/">initrd</a></code>(4). The GFS2 documentation has been split into a number of sections: <code><a href="/docs/linux/man/8-gfs2_edit/">gfs2_edit</a></code>(8) A GFS2 debug tool (use with caution) <code><a href="/docs/linux/man/8-fsck-gfs2/">fsck.gfs2</a></code>(8) The GFS2 file system checker <code><a href="/docs/linux/man/8-gfs2_grow/">gfs2_grow</a></code>(8) Growing a GFS2 file system <code><a href="/docs/linux/man/8-gfs2_jadd/">gfs2_jadd</a></code>(8) Adding a journal to a GFS2 file system <code><a href="/docs/linux/man/8-mkfs-gfs2/">mkfs.gfs2</a></code>(8) Make a GFS2 file system <code><a href="/docs/linux/man/8-gfs2_quota/">gfs2_quota</a></code>(8) Manipulate GFS2 disk quotas <code><a href="/docs/linux/man/8-gfs2_tool/">gfs2_tool</a></code>(8) Tool to manipulate a GFS2 file system (obsolete) <code><a href="/docs/linux/man/8-tunegfs2/">tunegfs2</a></code>(8) Tool to manipulate GFS2 superblocks </p>
<h2>Setup</h2>
<p>GFS2 clustering is driven by the dlm, which depends on dlm_controld to provide clustering from userspace. dlm_controld clustering is built on corosync cluster/group membership and messaging. </p>
<p> Follow these steps to manually configure and run gfs2/dlm/corosync. </p>
<p> <code>1. create /etc/corosync/corosync.conf and copy to all nodes</code> </p>
<p> In this sample, replace cluster_name and IP addresses, and add nodes as needed. If using only two nodes, uncomment the two_node line. See <a href="/docs/linux/man/5-corosync-conf/">corosync.conf</a>(5) for more information. </p>
<pre>totem {
 version: 2
 secauth: off
 cluster_name: abc
}
nodelist {
 node {
 ring0_addr: 10.10.10.1
 nodeid: 1
 }
 node {
 ring0_addr: 10.10.10.2
 nodeid: 2
 }
 node {
 ring0_addr: 10.10.10.3
 nodeid: 3
 }
}
quorum {
 provider: corosync_votequorum
# two_node: 1
}
logging {
 to_syslog: yes
}</pre>
<p><code>2. start corosync on all nodes</code> </p>
<pre>systemctl start corosync</pre>
<p>Run corosync-quorumtool to verify that all nodes are listed. </p>
<p> <code>3. create /etc/dlm/dlm.conf and copy to all nodes</code> </p>
<p> <code>*</code> To use no fencing, use this line: </p>
<pre>enable_fencing=0</pre>
<p><code>*</code> To use no fencing, but exercise fencing functions, use this line: </p>
<pre>fence_all /bin/true</pre>
<p>The &quot;true&quot; binary will be executed for all nodes and will succeed (exit 0) immediately. </p>
<p> <code>*</code> To use manual fencing, use this line: </p>
<pre>fence_all /bin/false</pre>
<p>The &quot;false&quot; binary will be executed for all nodes and will fail (exit 1) immediately. </p>
<p> When a node fails, manually run: dlm_tool fence_ack &lt;nodeid&gt; </p>
<p> <code>*</code> To use stonith/pacemaker for fencing, use this line: </p>
<pre>fence_all /usr/sbin/dlm_stonith</pre>
<p>The &quot;dlm_stonith&quot; binary will be executed for all nodes. If stonith/pacemaker systems are not available, dlm_stonith will fail and this config becomes the equivalent of the previous /bin/false config. </p>
<p> <code>*</code> To use an APC power switch, use these lines: </p>
<pre>device apc /usr/sbin/fence_apc ipaddr=1.1.1.1 login=admin password=pw
connect apc node=1 port=1
connect apc node=2 port=2
connect apc node=3 port=3</pre>
<p>Other network switch based agents are configured similarly. </p>
<p> <code>*</code> To use sanlock/watchdog fencing, use these lines: </p>
<pre>device wd /usr/sbin/fence_sanlock path=/dev/fence/leases
connect wd node=1 host_id=1
connect wd node=2 host_id=2
unfence wd</pre>
<p>See <a href="/docs/linux/man/8-fence_sanlock/">fence_sanlock</a>(8) for more information. </p>
<p> <code>*</code> For other fencing configurations see <a href="/docs/linux/man/5-dlm-conf/">dlm.conf</a>(5) man page. </p>
<p> <code>4. start dlm_controld on all nodes</code> </p>
<pre>systemctl start dlm</pre>
<p>Run &quot;dlm_tool status&quot; to verify that all nodes are listed. </p>
<p> <code>5. if using clvm, start clvmd on all nodes</code> </p>
<p> systemctl clvmd start </p>
<p> <code>6. make new gfs2 file systems</code> </p>
<p> mkfs.gfs2 -p lock_dlm -t cluster_name:fs_name -j num /path/to/storage </p>
<p> The cluster_name must match the name used in step 1 above. The fs_name must be a unique name in the cluster. The -j option is the number of journals to create, there must be one for each node that will mount the fs. </p>
<p> <code>7. mount gfs2 file systems</code> </p>
<p> mount /path/to/storage /mountpoint </p>
<p> Run &quot;dlm_tool ls&quot; to verify the nodes that have each fs mounted. </p>
<p> <code>8. shut down</code> </p>
<pre>umount -a -t gfs2
systemctl clvmd stop
systemctl dlm stop
systemctl corosync stop</pre>
<p><code>More setup information:</code><br />
 <code><a href="/docs/linux/man/8-dlm_controld/">dlm_controld</a></code>(8),<br />
 <code><a href="/docs/linux/man/8-dlm_tool/">dlm_tool</a></code>(8),<br />
 <code><a href="/docs/linux/man/5-dlm-conf/">dlm.conf</a></code>(5),<br />
 <code><a href="/docs/linux/man/8-corosync/">corosync</a></code>(8),<br />
 <code><a href="/docs/linux/man/5-corosync-conf/">corosync.conf</a></code>(5)</p>
