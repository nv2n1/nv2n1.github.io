---
title: "fedfs-map-nfs4(8)"
name: "fedfs-map-nfs4"
section: "8"
letter: "f"
url: "/docs/linux/man/8-fedfs-map-nfs4/"
description: "fedfs-map-nfs4 – generate automounter program map entries for FedFS"
---

<p>fedfs-map-nfs4 &#8211; generate automounter program map entries for FedFS</p>
<h2>Synopsis</h2>
<p><code>fedfs-map-nfs4</code> <i>domainname</i></p>
<h2>Introduction</h2>
<p>RFC 5716 introduces the Federated File System (FedFS, for short). FedFS is an extensible standardized mechanism by which system administrators construct a coherent namespace across multiple file servers using <i>file system referrals</i>. For further details, see <code><a href="/docs/linux/man/7-fedfs/">fedfs</a></code>(7).</p>
<h2>Description</h2>
<p>The <code><a href="/docs/linux/man/8-fedfs-map-nfs4/">fedfs-map-nfs4</a></code>(8) command provides a FedFS program map for the local system&#8217;s automounter. Although it is typically intended to be invoked by the automounter, it is also safe to invoke directly for scripting or debugging purposes. See <code><a href="/docs/linux/man/5-autofs/">autofs</a></code>(5) for information about how program maps work.</p>
<h3>Operation</h3>
<p>The <code><a href="/docs/linux/man/8-fedfs-map-nfs4/">fedfs-map-nfs4</a></code>(8) command locates FedFS domains by looking for DNS SRV records that advertise file servers exporting FedFS domain root replicas. The <i>domainname</i> argument determines what FedFS domain is to be mounted. </p>
<p> It retrieves and sorts the domain root replica records according to SRV record sorting rules outlined in RFC 2782. It then generates a sun format map entry on <i>stdout</i> representing the set of servers contained in the SRV record, a standard export path to the domain root, and appropriate NFS mount options. Error messages are output on <i>stderr</i>.</p>
<h3>Globally useful names</h3>
<p>Across all FedFS-enabled file system clients, a unique file object in a FedFS domain is always accessed via the same pathname. Such pathnames are referred to as <i>globally useful names</i>. See <code><a href="/docs/linux/man/7-fedfs/">fedfs</a></code>(7) for a full discussion. </p>
<p> The top-level directory of a globally useful name is always the networked file system type (NFS version 4, CIFS, and so on). A <code><a href="/docs/linux/man/8-fedfs-map-nfs4/">fedfs-map-nfs4</a></code>(8) program map entry is used with the NFS version 4 top-level directory to provide globally useful names via the NFS version 4 protocol.</p>
<h2>Examples</h2>
<p>Typically, a <code><a href="/docs/linux/man/8-fedfs-map-nfs4/">fedfs-map-nfs4</a></code>(8) entry in <i>/etc/auto.master</i> looks like this:</p>
<dl>
<dd>/nfs4 /usr/sbin/fedfs-map-nfs4 </p>
</dl>
<p> Under the /nfs4 directory on the local system, the automounter uses <code><a href="/docs/linux/man/8-fedfs-map-nfs4/">fedfs-map-nfs4</a></code>(8) to convert a FedFS domain name to a set of servers and an export path, which are then passed to <code><a href="/docs/linux/man/8-mount-nfs/">mount.nfs</a></code>(8). The automounter mounts this FedFS domain on the directory <i>/nfs4/domainname</i>. </p>
<p> After configuring and restarting <code>autofs</code>, to access files in the <i>example.net</i> FedFS domain, for instance, you can start with:</p>
<dl>
<dd>$ cd /nfs4/example.net </p>
</dl>
<p> The automounter uses the <code><a href="/docs/linux/man/8-fedfs-map-nfs4/">fedfs-map-nfs4</a></code>(8) command to look up the file servers that provide the domain root for the <i>example.net</i> domain. It then mounts one of these servers on <i>/nfs4/example.net</i>. </p>
<p> If the <code><a href="/docs/linux/man/8-fedfs-map-nfs4/">fedfs-map-nfs4</a></code>(8) command cannot find the requested domain, no local directory is created and no mount operation is performed. Applications receive an ENOENT error in this case. </p>
<p> While these mounted domains remain active on the local system, the mounted-on directories remain visible. After a period of inactivity, the automounter automatically unmounts a FedFS domain. </p>
<p> Local applications browsing the top-level directory do not see all available FedFS domains. They see only the ones that are mounted and active.</p>
<h3>Mount option inheritance</h3>
<p>The Linux NFS client treats an NFS referral as a server-initiated mount request. The referring fileserver provides only a list of server names and export paths. The mount options for this new mount are inherited from the new mount point&#8217;s parent directory on the client. </p>
<p> As applications proceed deeper into a domain&#8217;s namespace, they can encounter both file sets to which they have read-only access, and file sets to which they have read-write access. To allow applications proper access to both types of file sets, typically file-access clients mount domain root directories in read-write mode. All submounts of the domain root are then mounted read-write as well. Write access is controlled by fileservers. </p>
<p> For example, a domain root may contain an NFS version 4 referral to an export containing user home directories. The domain root may be exported read-only so file-access clients cannot update it, but user home directories would not be very useful if they could not be written to by their owners. The fileserver continues to employ user credentials to limit access as appropriate. </p>
<p> Network file system clients follow file system referrals as applications encounter them, which is similar to how an automounter works. Consider the initial mount of the domain root as if you are mounting a single whole file system, even though underneath, additional NFS mounts come and go as needed.</p>
<h2>Files</h2>
<dl>
<dt><i>/etc/auto.master</i></p>
<dd>master automounter map</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-fedfs/">fedfs</a></code>(7), <code><a href="/docs/linux/man/5-nfs/">nfs</a></code>(5), <code><a href="/docs/linux/man/5-autofs/">autofs</a></code>(5), </p>
<p> RFC 2782 for a discussion of DNS SRV records </p>
<p> RFC 5716 for FedFS requirements and overview</p>
<h2>Colophon</h2>
<p>This page is part of the fedfs-utils package. A description of the project and information about reporting bugs can be found at <i><a rel="nofollow" href="http://wiki.linux-nfs.org/wiki/index.php/FedFsUtilsProject">http://wiki.linux-nfs.org/wiki/index.php/FedFsUtilsProject</a></i>.</p>
<h2>Author</h2>
<p>Chuck Lever &lt;chuck.lever [at] oracle.com&gt;</p>
