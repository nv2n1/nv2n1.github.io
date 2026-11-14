---
title: "fedfs(7)"
name: "fedfs"
section: "7"
letter: "f"
url: "/docs/linux/man/7-fedfs/"
description: "fedfs – The Linux Federated File System implementation"
---

<p>fedfs &#8211; The Linux Federated File System implementation</p>
<h2>Description</h2>
<p>RFC 5716 introduces the Federated File System (FedFS, for short). FedFS is an extensible standardized mechanism by which system administrators construct a coherent namespace across multiple fileservers using <i>file system referrals</i>. </p>
<p> A file system referral is like a symbolic link to another file system share, but it is not visible to applications. It behaves like an automounted directory where a mount operation is performed when an application first accesses that directory. </p>
<p> Today, file system referral mechanisms exist in several standard network file system protocols. Because FedFS uses a mechanism already built in to standard network protocols, using it does not require any change to file system protocols or file-access client implementations. </p>
<p> A sideband protocol, such as NIS, is also unnecessary. File-access clients automatically share a common view of the network file system namespace with no need for individual configuration on each client. </p>
<p> Currently, the Linux FedFS implementation supports only NFS version 4 referrals. More on NFS version 4 referrals can be found in RFC 5661. FedFS may support other network file system protocols in the future.</p>
<h2>Fedfs Domain Operation</h2>
<p>A file system referral whose target is managed by FedFS is called a <i>FedFS junction</i>. Junctions join separate fileserver shares into a single coherent FedFS namespace. On FedFS-enabled Linux fileservers, the <code><a href="/docs/linux/man/8-rpc-fedfsd/">rpc.fedfsd</a></code>(8) daemon and the <code><a href="/docs/linux/man/5-nfsref/">nfsref</a></code>(5) command create and remove FedFS junctions. </p>
<p> An independently administered FedFS namespace is referred to as a <i>FedFS domain</i>. FedFS domains are file namespaces only. They do not represent authentication or ID-mapping realms, for example. FedFS-enabled file-access clients and fileservers are not members of a particular FedFS domain and do not have <i>a priori</i> knowledge of what FedFS domains exist. </p>
<p> The top-level directory of a FedFS domain is referred to as its <i>domain root</i>. Domain roots typically contain nothing but FedFS junctions and a few other directories. Useful data is contained in other shares which file-access clients discover by following FedFS junctions in the domain root directory. </p>
<p> Although FedFS junctions are stored on fileservers, they are lightweight objects that contain little actual data. The bulk of FedFS junction information in a FedFS domain is stored on an LDAP server. LDAP servers that store FedFS information are known as <i>namespace databases</i>, or NSDBs, for short. Any standard LDAP server can become an NSDB if it knows the FedFS schema (the definitions of FedFS record types).</p>
<h3>Filesets</h3>
<p>FedFS groups a set of directories in a server&#8217;s physical file system namespace into a single administrative unit called a <i>fileset</i>. For NFS, a whole share might be considered a fileset. A FedFS domain consists of one or more filesets, a domain root, and junction information stored on an NSDB node. </p>
<p> To function as a FedFS fileset, a set of directories must have a name unique in a FedFS domain, and a set of locations where the file data is stored. </p>
<p> A FedFS <i>fileset name</i> is a UUID and an NSDB domainname and port. This information is also maintained in an LDAP record on the NSDB node. </p>
<p> A FedFS <i>fileset location</i> is an LDAP record that describes the location (the fileserver where it resides, and its export path) of a copy of a fileset&#8217;s data. These records are children of the fileset name record for this fileset. </p>
<p> A fileset can have multiple replicas. Such a fileset has one FedFS fileset name, and each replica of the fileset has an individual FedFS fileset location record. </p>
<p> A FedFS junction contains only a FedFS fileset name. A fileserver resolves a FedFS junction by performing an LDAP query on the NSDB node named in the junction, using the UUID named in the junction. The NSDB node returns location information stored in FedFS fileset location records for that FedFS fileset name. The fileserver returns this location information to file-access clients it servers via a file system referral. </p>
<p> On Linux NFS fileservers, <code><a href="/docs/linux/man/8-rpc-mountd/">rpc.mountd</a></code>(8) is the gateway through which the in-kernel NFS server performs FedFS junction resolution.</p>
<h3>Discovering domain roots</h3>
<p>As with other FedFS filesets, copies of a domain root can exist on multiple fileservers. These copies are known as <i>domain root replicas</i>. </p>
<p> Rather than using junctions and information in an NSDB node, FedFS-enabled file-access clients locate a domain&#8217;s root by looking for DNS SRV records that advertise fileservers exporting domain root replicas. </p>
<p> Such clients typically mount FedFS domain roots in a standard place so that files residing in a FedFS domain appear at the same location in the file namespace on all file-access clients. By convention, the top of the global FedFS namespace looks like this:</p>
<dl>
<dd>/<i>fstype</i>/<i>domainname</i> </p>
</dl>
<p> where <i>fstype</i> specifies a network file system protocol to use, and <i>domainname</i> specifies a FedFS domain. Currently, the Linux FedFS implementation recognizes only <code>nfs4</code> as a valid fstype.</p>
<h3>Globally Useful Names</h3>
<p>On FedFS-enabled Linux file-access clients, the automounter (via a program map) or the <code><a href="/docs/linux/man/8-mount-fedfs/">mount.fedfs</a></code>(8) command find and mount the root of a FedFS domain. </p>
<p> Typically, file-access clients mount the FedFS namespace so that FedFS pathnames appear the same on all clients. Such pathnames are referred to as <i>globally useful names</i>, since a globally useful name refers to exactly the same file object on every file-access client in a FedFS domain. </p>
<p> For example, the FedFS globally useful name <i>/nfs4/example.net</i> would be mounted on a local directory called <i>/nfs4/example.net</i> on all file-access clients, so that applications have the same view of the <i>example.net</i> domain namespace on all FedFS-enabled file-access clients. </p>
<p> The Linux <code><a href="/docs/linux/man/8-mount-fedfs/">mount.fedfs</a></code>(8) command can attach anywhere in a file-access client&#8217;s local file namespace any directory in the FedFS namespace that client has permission to access. This can be useful to ensure local namespace compatibility in some cases, or hide parts of the FedFS namespace for security purposes. </p>
<p> However, it breaks cross-platform application interoperability by presenting applications with multiple pathnames to the same file object. Therefore it should be avoided.</p>
<h2>Security</h2>
<p>Each host in a FedFS domain plays one or more of the following roles, each of which have different security requirements.</p>
<dl>
<dt><i>NSDB node</i></p>
<dd>LDAP server that contains FedFS domain information</p>
<dt><i>FedFS fileserver</i></p>
<dd>stores data accessible via a FedFS domain name space</p>
<dt><i>FedFS file-access client</i></p>
<dd>accesses data in FedFS domain name spaces</p>
<dt><i>FedFS admin client</i></p>
<dd>manages FedFS domain information</dl>
<p> The Linux FedFS implementation provides administrative tools to manage FedFS fileset name and location records on an NSDB node. Junction resolution uses anonymous LDAP search requests, and administration takes place via authenticated LDAP modification requests. </p>
<p> Fileservers and administrative clients use plaintext or TLS-secured transports to perform junction lookups and administrative requests. The Linux FedFS implementation provides tools for managing x.509 certificates required for LDAP over TLS. </p>
<p> FedFS junction objects are created on fileservers by a side-band RPC protocol called the <i>FedFS ADMIN protocol</i>. This protocol is separate from network file system protocols. This allows FedFS to operate without modification to network file system protocols. The protocol uses RPCSEC GSS to secure administrative requests. </p>
<p> Since two separate protocols are involved when administering junctions and filesets, junctions are created on fileservers and registered with the domain&#8217;s NSDB node in two separate steps.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-nsdb-parameters/">nsdb-parameters</a></code>(7), <code><a href="/docs/linux/man/8-nsdbparams/">nsdbparams</a></code>(8), <code><a href="/docs/linux/man/8-fedfs-map-nfs4/">fedfs-map-nfs4</a></code>(8), <code><a href="/docs/linux/man/8-mount-fedfs/">mount.fedfs</a></code>(8), <code><a href="/docs/linux/man/8-rpc-fedfsd/">rpc.fedfsd</a></code>(8), <code><a href="/docs/linux/man/8-rpc-mountd/">rpc.mountd</a></code>(8), <code><a href="/docs/linux/man/8-fedfs-create-junction/">fedfs-create-junction</a></code>(8), <code><a href="/docs/linux/man/8-fedfs-create-replication/">fedfs-create-replication</a></code>(8), <code><a href="/docs/linux/man/8-fedfs-delete-junction/">fedfs-delete-junction</a></code>(8), <code><a href="/docs/linux/man/8-fedfs-delete-replication/">fedfs-delete-replication</a></code>(8), <code><a href="/docs/linux/man/8-fedfs-get-limited-nsdb-params/">fedfs-get-limited-nsdb-params</a></code>(8), <code><a href="/docs/linux/man/8-fedfs-get-nsdb-params/">fedfs-get-nsdb-params</a></code>(8), <code><a href="/docs/linux/man/8-fedfs-lookup-junction/">fedfs-lookup-junction</a></code>(8), <code><a href="/docs/linux/man/8-fedfs-lookup-replication/">fedfs-lookup-replication</a></code>(8), <code><a href="/docs/linux/man/8-fedfs-null/">fedfs-null</a></code>(8), <code><a href="/docs/linux/man/8-fedfs-set-nsdb-params/">fedfs-set-nsdb-params</a></code>(8), <code><a href="/docs/linux/man/8-nsdb-simple-nce/">nsdb-simple-nce</a></code>(8), <code><a href="/docs/linux/man/8-nsdb-annotate/">nsdb-annotate</a></code>(8), <code><a href="/docs/linux/man/8-nsdb-create-fsl/">nsdb-create-fsl</a></code>(8), <code><a href="/docs/linux/man/8-nsdb-create-fsn/">nsdb-create-fsn</a></code>(8), <code><a href="/docs/linux/man/8-nsdb-update-nci/">nsdb-update-nci</a></code>(8), <code><a href="/docs/linux/man/8-nsdb-delete-fsl/">nsdb-delete-fsl</a></code>(8), <code><a href="/docs/linux/man/8-nsdb-delete-fsn/">nsdb-delete-fsn</a></code>(8), <code><a href="/docs/linux/man/8-nsdb-remove-nci/">nsdb-remove-nci</a></code>(8), <code><a href="/docs/linux/man/8-nsdb-describe/">nsdb-describe</a></code>(8), <code><a href="/docs/linux/man/8-nsdb-list/">nsdb-list</a></code>(8), <code><a href="/docs/linux/man/8-nsdb-nces/">nsdb-nces</a></code>(8), <code><a href="/docs/linux/man/8-nsdb-resolve-fsn/">nsdb-resolve-fsn</a></code>(8), <code><a href="/docs/linux/man/8-nsdb-update-fsl/">nsdb-update-fsl</a></code>(8) </p>
<p> RFC 4510 for an introduction to LDAP </p>
<p> RFC 5661 for a description of NFS version 4 referrals </p>
<p> RFC 5716 for FedFS requirements and overview</p>
<h2>Colophon</h2>
<p>This page is part of the fedfs-utils package. A description of the project and information about reporting bugs can be found at <i><a rel="nofollow" href="http://wiki.linux-nfs.org/wiki/index.php/FedFsUtilsProject">http://wiki.linux-nfs.org/wiki/index.php/FedFsUtilsProject</a></i>.</p>
<h2>Author</h2>
<p>Chuck Lever &lt;chuck.lever [at] oracle.com&gt;</p>
