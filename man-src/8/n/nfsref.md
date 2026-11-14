---
title: "nfsref(8)"
name: "nfsref"
section: "8"
letter: "n"
url: "/docs/linux/man/8-nfsref/"
description: "nfsref – manage NFS referrals"
---

<p>nfsref &#8211; manage NFS referrals</p>
<h2>Synopsis</h2>
<p><code>nfsref</code> [<code>-?d</code>] [<code>-t</code> <i>type</i><code>]</code> <code>add</code> <i>pathname server export</i> [<i> server</i> <i>export</i> &#8230; ] </p>
<p> <code>nfsref</code> [<code>-?d</code>] [<code>-t</code> <i>type</i><code>]</code> <code>remove</code> <i>pathname</i> </p>
<p> <code>nfsref</code> [<code>-?d</code>] [<code>-t</code> <i>type</i><code>]</code> <code>lookup</code> <i>pathname</i></p>
<h2>Introduction</h2>
<p>NFS version 4 introduces the concept of <i>file system referrals</i> to NFS. A file system referral is like a symbolic link on a file server to another file system share, possibly on another file server. On an NFS client, a referral behaves like an automounted directory. The client, under the server&#8217;s direction, mounts a new NFS export automatically when an application first accesses that directory. </p>
<p> Referrals are typically used to construct a single file name space across multiple file servers. Because file servers control the shape of the name space, no client configuration is required, and all clients see the same referral information. </p>
<p> The Linux NFS server supports NFS version 4 referrals. Administrators can specify the <code>refer=</code> export option in <i>/etc/exports</i> to configure a list of exports from which the client can choose. See <code><a href="/docs/linux/man/5-exports/">exports</a></code>(5) for details. </p>
<p> The <code><a href="/docs/linux/man/8-nfsref/">nfsref</a></code>(8) command provides an alternate way to configure NFS referrals. This command stores referral information as metadata within a leaf directory in an exported file system. The metadata it stores can contain one of two types of information:</p>
<dl>
<dt><i>A list of Fileset Locations</i></p>
<dd>A set of server name and export path pairs which are returned verbatim to clients during an NFS referral event. This is known as an <i>NFS basic junction</i>.</p>
<dt><i>A Fileset Name</i></p>
<dd>The name of an LDAP record which contains information to return to clients during an NFS referral event. This is known as a <i>FedFS junction</i>.</dl>
<p> A directory can hold either an NFS basic junction or a FedFS junction, but not both. When a directory acts as a junction, its regular contents remain, but are no longer visible to NFS clients. </p>
<p> By storing the location information in an LDAP directory, FedFS junctions on multiple file servers can refer to the same copy of location information. This common locations metadata can be updated via a single administrative operation, altering the file name space consistently across all servers. The <code><a href="/docs/linux/man/7-fedfs/">fedfs</a></code>(7) man page has more information.</p>
<h2>Description</h2>
<p>The <code><a href="/docs/linux/man/8-nfsref/">nfsref</a></code>(8) command is a simple way to get started managing junction metadata. Other administrative commands provide richer access to junction information.</p>
<h3>Subcommands</h3>
<p>Valid <code><a href="/docs/linux/man/8-nfsref/">nfsref</a></code>(8) subcommands are:</p>
<dl>
<dt><code>add</code></p>
<dd>Adds junction information to the directory named by <i>pathname</i>. The named directory must already exist, and must not already contain junction information. Regular directory contents are obscured to NFS clients by this operation.</p>
<dd>A list of one or more file server and export path pairs is also specified on the command line. When creating an NFS basic junction, this list is stored in an extended attribute of the directory.</p>
<dd>When creating a FedFS junction, FedFS records containing the file server and export path pairs are created on an LDAP server, and a pointer to the new FedFS records is stored in an extended attribute of the directory. Fresh FSN and FSL UUIDs are generated during this operation.</p>
<dd>If junction creation is successful, the <code><a href="/docs/linux/man/8-nfsref/">nfsref</a></code>(8) command flushes the kernel&#8217;s export cache to remove previously cached junction information.</p>
<dt><code>remove</code></p>
<dd>Removes junction information from the directory named by <i>pathname</i>. The named directory must exist, and must contain junction information. Regular directory contents are made visible to NFS clients again by this operation.</p>
<dd>When removing a FedFS junction, the <code><a href="/docs/linux/man/8-nfsref/">nfsref</a></code>(8) command also removes FSN and FSL records referred to in the junction.</p>
<dd>If junction deletion is successful, the <code><a href="/docs/linux/man/8-nfsref/">nfsref</a></code>(8) command flushes the kernel&#8217;s export cache to remove previously cached junction information.</p>
<dt><code>lookup</code></p>
<dd>Displays junction information stored in the directory named by <i>pathname</i>. The named directory must exist, and must contain junction information.</p>
<dd>When looking up an NFS basic junction, the junction information in the directory is listed on <i>stdout</i>. When looking up a FedFS junction, junction information is retrieved from the LDAP server listed in the junction and listed on <i>stdout</i>.</dl>
<p> When creating a new FedFS junction, the <code><a href="/docs/linux/man/8-nfsref/">nfsref</a></code>(8) command reads the following environment variables:</p>
<dl>
<dt><code>FEDFS_NSDB_HOST</code></p>
<dd>Specifies the hostname of the LDAP server where new FedFS records should reside. If this variable is not set, the <code><a href="/docs/linux/man/8-nfsref/">nfsref</a></code>(8) command fails. The LDAP server specified by this variable must be registered with the local NSDB connection parameter database before the <code><a href="/docs/linux/man/8-nfsref/">nfsref</a></code>(8) command can communicate with it. See <code><a href="/docs/linux/man/8-nsdbparams/">nsdbparams</a></code>(8) for more information.</p>
<dt><code>FEDFS_NSDB_PORT</code></p>
<dd>Specifies the IP port of the LDAP server where new FedFS records should reside. The default value if this variable is not set is 389.</p>
<dt><code>FEDFS_NSDB_NCE</code></p>
<dd>Specifies the distinguished name of the NSDB Container Entry under which new FedFS records should reside. If this variable is not set, the local NSDB connection parameter database is searched for a default NCE for the hostname specified by <code>FEDFS_NSDB_HOST</code>. If neither of these is specified, the <code><a href="/docs/linux/man/8-nfsref/">nfsref</a></code>(8) command fails.</p>
<dt><code>FEDFS_NSDB_ADMIN</code></p>
<dd>Specifies a distinguished name of an entity used to bind to the LDAP server where new FedFS records should reside. If this variable is not set, the local NSDB connection parameter database is searched for a default bind DN for the hostname specified by <code>FEDFS_NSDB_HOST</code>. If neither of these is specified, or if this entity does not have permission to modify the LDAP server&#8217;s DIT, the <code><a href="/docs/linux/man/8-nfsref/">nfsref</a></code>(8) command fails.</dl>
<h3>Command line options</h3>
<dl>
<dt><code>-d, &#8211;debug</p>
<dd>Enables debugging messages during operation.</p>
<dt>-t, &#8211;type=</code><i>junction-type</i></p>
<dd>Specifies the junction type for the operation. Valid values for <i>junction-type</i> are <code>nfs-basic</code> or <code>nfs-fedfs</code>.</p>
<dd>For the <code>add</code> subcommand, the default value if this option is not specified is <code>nfs-basic</code>. For the <code>remove</code> and <code>lookup</code> subcommands, the <code>&#8211;type</code> option is not required. The <code><a href="/docs/linux/man/8-nfsref/">nfsref</a></code>(8) command operates on whatever junction contents are available.</dl>
<h2>Examples</h2>
<p>Suppose you have two file servers, <i>top.example.net</i> and <i>home.example.net</i>. You want all your clients to mount <i>top.example.net:/</i> and then see the files under <i>home.example.net:/</i> automatically in <i>top:/home</i>. On <i>top.example.net</i>, you might issue this command as root:</p>
<dl>
<dd># mkdir /home<br />
 # nfsref &#8211;type=nfs-basic add /home home.example.net /<br />
 Created junction /home. </p>
<h2>Files</h2>
<dl>
<dt><i>/etc/exports</i></p>
<dd>NFS server export table</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-fedfs/">fedfs</a></code>(7), <code><a href="/docs/linux/man/8-nsdbparams/">nsdbparams</a></code>(8), <code><a href="/docs/linux/man/5-exports/">exports</a></code>(5) </p>
<p> RFC 5661 for a description of NFS version 4 referrals </p>
<p> RFC 5716 for FedFS requirements and overview</p>
<h2>Colophon</h2>
<p>This page is part of the fedfs-utils package. A description of the project and information about reporting bugs can be found at <i><a rel="nofollow" href="http://wiki.linux-nfs.org/wiki/index.php/FedFsUtilsProject">http://wiki.linux-nfs.org/wiki/index.php/FedFsUtilsProject</a></i>.</p>
<h2>Author</h2>
<p>Chuck Lever &lt;chuck.lever [at] oracle.com&gt;</p>
