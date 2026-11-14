---
title: "vfs_acl_tdb(8)"
name: "vfs_acl_tdb"
section: "8"
letter: "v"
url: "/docs/linux/man/8-vfs_acl_tdb/"
description: "vfs_acl_tdb – Save NTFS-ACLs in a tdb file"
---

<p>vfs_acl_tdb &#8211; Save NTFS-ACLs in a tdb file</p>
<h2>Synopsis</h2>
<dl>
<dd>vfs objects = acl_tdb</dl>
<h2>Description</h2>
<p>This VFS module is part of the <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7) suite. </p>
<p> The vfs_acl_tdb VFS module stores NTFS Access Control Lists (ACLs) in a tdb file. This enables the full mapping of Windows ACLs on Samba servers. </p>
<p> The ACL settings are stored in $LOCKDIR/file_ntacls.tdb. </p>
<p> This module forces the following parameters: </p>
<dl>
<dd>&bull; inherit acls = true</dl>
<dl>
<dd>&bull; dos filemode = true</dl>
<dl>
<dd>&bull; force unknown acl user = true</dl>
<p> This module is stackable.</p>
<h2>Options</h2>
<p>acl_tdb:ignore system acls = [yes|no]</p>
<dl>
<dd>When set to <i>yes</i>, a best effort mapping from/to the POSIX ACL layer will <i>not</i> be done by this module. The default is <i>no</i>, which means that Samba keeps setting and evaluating both the system ACLs and the NT ACLs. This is better if you need your system ACLs be set for local or NFS file access, too. If you only access the data via Samba you might set this to yes to achieve better NT ACL compatibility. </p>
<p> If <i>acl_tdb:ignore system acls</i> is set to <i>yes</i>, the following additional settings will be enforced: </p>
<dl>
<dd>&bull; create mask = 0666</dl>
<dl>
<dd>&bull; directory mask = 0777</dl>
<dl>
<dd>&bull; map archive = no</dl>
<dl>
<dd>&bull; map hidden = no</dl>
<dl>
<dd>&bull; map readonly = no</dl>
<dl>
<dd>&bull; map system = no</dl>
<dl>
<dd>&bull; store dos attributes = yes</dl>
</dl>
<p> acl_tdb:default acl style = [posix|windows]</p>
<dl>
<dd>This parameter determines the type of ACL that is synthesized in case a file or directory lacks an <i>security.NTACL</i> xattr. </p>
<p> When set to <i>posix</i>, an ACL will be synthesized based on the POSIX mode permissions for user, group and others, with an additional ACE for <i>NT Authority\SYSTEM</i> will full rights. </p>
<p> When set to <i>windows</i>, an ACL is synthesized the same way Windows does it, only including permissions for the owner and <i>NT Authority\SYSTEM</i>. </p>
<p> The default for this option is <i>posix</i>.</dl>
<h2>Author</h2>
<p>The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed.</p>
