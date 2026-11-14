---
title: "mount-fedfs(8)"
name: "mount-fedfs"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mount-fedfs/"
description: "mount.fedfs – mount a FedFS domain root"
---

<p>mount.fedfs &#8211; mount a FedFS domain root</p>
<h2>Synopsis</h2>
<p><code>mount.fedfs</code> <i>remotedir localdir</i> [<code>-fhnrsvVw</code>] [<code>-o</code> <i>options</i>]</p>
<h2>Description</h2>
<p>RFC 5716 introduces the Federated File System (FedFS, for short). FedFS is an extensible standardized mechanism by which system administrators construct a coherent namespace across multiple file servers using <i>file system referrals</i>. For further details, see <code><a href="/docs/linux/man/7-fedfs/">fedfs</a></code>(7). </p>
<p> The <code><a href="/docs/linux/man/8-mount-fedfs/">mount.fedfs</a></code>(8) command locates FedFS domains by looking for DNS SRV records that advertise file servers exporting FedFS domain root replicas. The <i>remotedir</i> argument determines what FedFS domain is mounted and what network file system protocol is used. </p>
<p> The <code><a href="/docs/linux/man/8-mount-fedfs/">mount.fedfs</a></code>(8) command sorts the list of available domain root replicas according to the SRV record sorting rules outlined in RFC 2782. It attempts to contact each file server appearing in the SRV record list until a mount request succeeds or the end of the SRV record list is reached.</p>
<h3>Command line arguments</h3>
<p>The first argument, <i>remotedir</i>, is the <i>globally useful name</i> to mount. Globally useful names are discussed in more detail in <code><a href="/docs/linux/man/7-fedfs/">fedfs</a></code>(7). </p>
<p> The second argument, <i>localdir</i>, specifies the local directory on which to mount the requested FedFS globally useful name. As with other file systems, <i>localdir</i> must exist on the client for a mount request to succeed. </p>
<p> The <code><a href="/docs/linux/man/8-mount-fedfs/">mount.fedfs</a></code>(8) command converts the specified <i>remotedir</i> and <i>localdir</i> arguments, along with information obtained via DNS SRV queries, to arguments suitable for a local mount request. It then forks and execs the appropriate file system mount subcommand (such as the <code><a href="/docs/linux/man/8-mount-nfs/">mount.nfs</a></code>(8) subcommand) to mount the file server where the domain root resides. </p>
<p> Because an unmodified file system mount subcommand is used for the actual mount operation, the file system&#8217;s equivalent umount subcommand is all that is required to unmount this mount point when it is finished being used.</p>
<h3>Mount option inheritance</h3>
<p>The Linux NFS client treats an NFS referral as a server-initiated mount request. The referring fileserver provides only a list of server names and export paths. The mount options for this new mount are inherited from the new mount point&#8217;s parent directory on the client. </p>
<p> As applications proceed deeper into a domain&#8217;s namespace, they can encounter both file sets to which they have read-only access, and file sets to which they have read-write access. To allow applications proper access to both types of file sets, typically file-access clients mount domain root directories in read-write mode. All submounts of the domain root are then mounted read-write as well. Write access is then controlled by fileservers. </p>
<p> For example, a domain root may contain an NFS version 4 referral to an export containing user home directories. The domain root may be exported read-only so file-access clients cannot update it, but user home directories would not be very useful if they could not be written to by their owners. The fileserver continues to employ user credentials to limit access as appropriate. </p>
<p> Network file system clients follow file system referrals as applications encounter them, which is similar to how an automounter works. Consider the initial mount of the domain root as if you are mounting a single whole file system, even though underneath, additional NFS mounts come and go as needed.</p>
<h3>Options</h3>
<dl>
<dt><code>-f, &#8211;fake</p>
<dd>Fake mount. This option is ignored by <a href="/docs/linux/man/8-mount-fedfs/">mount.fedfs</a></code>(8) but is passed to the underlying file system mount subcommand.</p>
<dt><code>-h, &#8211;help</code></p>
<dd>Print the <code><a href="/docs/linux/man/8-mount-fedfs/">mount.fedfs</a></code>(8) usage message and exit.</p>
<dt><code>-n, &#8211;no-mtab</code></p>
<dd>Do not update <i>/etc/mtab</i>. This option is ignored by <code><a href="/docs/linux/man/8-mount-fedfs/">mount.fedfs</a></code>(8) but is passed to the underlying file system mount subcommand.</p>
<dt><code>-o, &#8211;options </code><i>options</i></p>
<dd>Specify mount options for this mount point and all submounts. These are ignored by <code><a href="/docs/linux/man/8-mount-fedfs/">mount.fedfs</a></code>(8) but are passed to the underlying file system mount subcommand. For further details, refer to <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8).</p>
<dt><code>-r, &#8211;ro, &#8211;read-only</code></p>
<dd>Mount the domain root and all submounts read-only.</p>
<dt><code>-s, &#8211;sloppy</code></p>
<dd>Tolerate unrecognized mount options. This is ignored by <code><a href="/docs/linux/man/8-mount-fedfs/">mount.fedfs</a></code>(8) but is passed to the underlying file system mount subcommand.</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd>Report more information during the mount process. This affects <code><a href="/docs/linux/man/8-mount-fedfs/">mount.fedfs</a></code>(8) and is also passed to the underlying file system mount subcommand.</p>
<dt><code>-V, &#8211;version</code></p>
<dd>Print version information for <code><a href="/docs/linux/man/8-mount-fedfs/">mount.fedfs</a>(8)</code> and exit.</p>
<dt><code>-w, &#8211;rw, &#8211;read-write</code></p>
<dd>Mount the domain root and all submounts read-write. This is the default behavior.</dl>
<h2>Examples</h2>
<p>To mount the domain root of the <i>example.net</i> FedFS domain via NFS version 4 automatically, you might add this to your <i>/etc/fstab</i>:</p>
<dl>
<dd>/nfs4/example.net /nfs4/example.net fedfs defaults 0 0 </p>
</dl>
<p> A FedFS domain root can also be mounted with a stand-alone invocation of <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8):</p>
<dl>
<dd># mount -t fedfs /nfs4/example.net /mnt/fedfs </p>
</dl>
<p> This mounts the FedFS domain root for the <i>example.net</i> domain on the client&#8217;s <i>/mnt/fedfs</i> directory. A simple</p>
<dl>
<dd># umount /mnt/fedfs </p>
</dl>
<p> unmounts it when you are finished with it.</p>
<h2>Files</h2>
<dl>
<dt><i>/etc/fstab</i></p>
<dd>filesystem table</p>
<dt><i>/etc/mtab</i></p>
<dd>table of mounted file systems</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-fedfs/">fedfs</a></code>(7), <code><a href="/docs/linux/man/5-nfs/">nfs</a></code>(5), <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8), <code><a href="/docs/linux/man/8-mount-nfs/">mount.nfs</a></code>(8) </p>
<p> RFC 2782 for a discussion of DNS SRV records </p>
<p> RFC 5661 for a description of NFS version 4 referrals </p>
<p> RFC 5716 for FedFS requirements and overview</p>
<h2>Colophon</h2>
<p>This page is part of the fedfs-utils package. A description of the project and information about reporting bugs can be found at <i><a rel="nofollow" href="http://wiki.linux-nfs.org/wiki/index.php/FedFsUtilsProject">http://wiki.linux-nfs.org/wiki/index.php/FedFsUtilsProject</a></i>.</p>
<h2>Author</h2>
<p>Chuck Lever &lt;chuck.lever [at] oracle.com&gt;</p>
