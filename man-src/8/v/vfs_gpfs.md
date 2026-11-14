---
title: "vfs_gpfs(8)"
name: "vfs_gpfs"
section: "8"
letter: "v"
url: "/docs/linux/man/8-vfs_gpfs/"
description: "vfs_gpfs – gpfs specific samba extensions like acls and prealloc"
---

<p>vfs_gpfs &#8211; gpfs specific samba extensions like acls and prealloc</p>
<h2>Synopsis</h2>
<dl>
<dd>vfs objects = gpfs</dl>
<h2>Description</h2>
<p>This VFS module is part of the <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7) suite. </p>
<p> The gpfs VFS module is the home for all gpfs extensions that Samba requires for proper integration with GPFS. It uses the GPL library interfaces provided by GPFS. </p>
<p> Currently the gpfs vfs module provides extensions in following areas : </p>
<dl>
<dd>&bull; NFSv4 ACL Interfaces with configurable options for GPFS</dl>
<dl>
<dd>&bull; Kernel oplock support on GPFS</dl>
<dl>
<dd>&bull; Lease support on GPFS</dl>
<p> NOTE: This module follows the posix-acl behaviour and hence allows permission stealing via chown. Samba might allow at a later point in time, to restrict the chown via this module as such restrictions are the responsibility of the underlying filesystem than of Samba. </p>
<p> This module makes use of the smb.conf parameter m[blue]<code>acl map full control</code>m[]. When set to yes (the default), this parameter will add in the FILE_DELETE_CHILD bit on a returned ACE entry for a file (not a directory) that already contains all file permissions except for FILE_DELETE and FILE_DELETE_CHILD. This can prevent Windows applications that request GENERIC_ALL access from getting ACCESS_DENIED errors when running against a filesystem with NFSv4 compatible ACLs. </p>
<p> This module is stackable. </p>
<p> Since Samba 4.0 all options are per share options.</p>
<h2>Options</h2>
<p>gpfs:sharemodes = [ yes | no ]</p>
<dl>
<dd>Enable/Disable cross node sharemode handling for GPFS. </p>
<dl>
<dd>&bull; yes(default) &#8211; propagate sharemodes across all GPFS nodes.</dl>
<dl>
<dd>&bull; no &#8211; do not propagate sharemodes across all GPFS nodes. This should only be used if the GPFS file system is exclusively exported by Samba. Access by local unix application or NFS exports could lead to corrupted files.</dl>
</dl>
<p> gpfs:leases = [ yes | no ]</p>
<dl>
<dd>Enable/Disable cross node leases (oplocks) for GPFS. You should also set the oplocks and kernel oplocks options to the same value. </p>
<dl>
<dd>&bull; yes(default) &#8211; propagate leases across all GPFS nodes.</dl>
<dl>
<dd>&bull; no &#8211; do not propagate leases across all GPFS nodes. This should only be used if the GPFS file system is exclusively exported by Samba. Access by local unix application or NFS exports could lead to corrupted files.</dl>
</dl>
<p> gpfs:hsm = [ yes | no ]</p>
<dl>
<dd>Enable/Disable announcing if this FS has HSM enabled. </p>
<dl>
<dd>&bull; no(default) &#8211; Do not announce HSM.</dl>
<dl>
<dd>&bull; yes &#8211; Announce HSM.</dl>
</dl>
<p> gpfs:recalls = [ yes | no ]</p>
<dl>
<dd>When this option is set to no, an attempt to open an offline file will be rejected with access denied. This helps preventing recall storms triggered by careless applications like Finder and Explorer. </p>
<dl>
<dd>&bull; yes(default) &#8211; Open files that are offline. This will recall the files from HSM.</dl>
<dl>
<dd>&bull; no &#8211; Reject access to offline files with access denied. This will prevent recalls of files from HSM. Using this setting also requires gpfs:hsm to be set to yes.</dl>
</dl>
<p> gpfs:getrealfilename = [ yes | no ]</p>
<dl>
<dd>Enable/Disable usage of the gpfs_get_realfilename_path() function. This improves the casesensitive wildcard file name access. </p>
<dl>
<dd>&bull; yes(default) &#8211; use gpfs_get_realfilename_path().</dl>
<dl>
<dd>&bull; no &#8211; do not use gpfs_get_realfilename_path(). It seems that gpfs_get_realfilename_path() doesn&#8217;t work on AIX.</dl>
</dl>
<p> gpfs:winattr = [ yes | no ]</p>
<dl>
<dd>Enable/Disable usage of the windows attributes in GPFS. GPFS is able to store windows file attributes e.g. HIDDEN, READONLY, SYSTEM and others natively. That means Samba doesn&#8217;t need to map them to permission bits or extended attributes. </p>
<dl>
<dd>&bull; no(default) &#8211; do not use GPFS windows attributes.</dl>
<dl>
<dd>&bull; yes &#8211; use GPFS windows attributes.</dl>
</dl>
<p> gpfs:merge_writeappend = [ yes | no ]</p>
<dl>
<dd>GPFS ACLs doesn&#8217;t know about the &#8216;APPEND&#8217; right. This option lets Samba map the &#8216;APPEND&#8217; right to &#8216;WRITE&#8217;. </p>
<dl>
<dd>&bull; yes(default) &#8211; map &#8216;APPEND&#8217; to &#8216;WRITE&#8217;.</dl>
<dl>
<dd>&bull; no &#8211; do not map &#8216;APPEND&#8217; to &#8216;WRITE&#8217;.</dl>
</dl>
<p> gpfs:acl = [ yes | no ]</p>
<dl>
<dd>This option lets Samba use or ignore GPFS ACLs. </p>
<dl>
<dd>&bull; yes(default) &#8211; use GPFS ACLs.</dl>
<dl>
<dd>&bull; no &#8211; do not use GPFS ACLs and pass everything to the next SMB_VFS module.</dl>
</dl>
<p> gpfs:refuse_dacl_protected = [ yes | no ]</p>
<dl>
<dd>As GPFS does not support the ACE4_FLAG_NO_PROPAGATE NFSv4 flag (which would be the mapping for the DESC_DACL_PROTECTED flag), the status of this flag is currently silently ignored by Samba. That means that if you deselect the &quot;Allow inheritable permissions&#8230;&quot; checkbox in Windows&#8217; ACL dialog and then apply the ACL, the flag will be back immediately. </p>
<p> To make sure that automatic migration with e.g. robocopy does not lead to ACLs silently (and unintentionally) changed, you can set gpfs:refuse_dacl_protected = yes to enable an explicit check for this flag and if set, it will return NT_STATUS_NOT_SUPPORTED so errors are shown up on the Windows side and the Administrator is aware of the ACLs not being settable like intended </p>
<dl>
<dd>&bull; no(default) &#8211; ignore the DESC_DACL_PROTECTED flags.</dl>
<dl>
<dd>&bull; yes &#8211; reject ACLs with DESC_DACL_PROTECTED.</dl>
</dl>
<p> gpfs:dfreequota = [ yes | no ]</p>
<dl>
<dd>Adjust reporting of the size and free space of a share according to quotas. If this setting is &quot;yes&quot;, a request for size and free space will also evaluate the user quota of the user requesting the data and the group quota of the primary group of the user. Fileset quotas are not queried, since GPFS already provides the option &#8211;dfreequota to reflect the fileset quota in the free space query. Please use that option to include fileset quotas in the reported disk space. </p>
<p> If any of the soft or hard quota limits has been reached, the free space will be reported as 0. If a quota is in place, but the limits have not been reached, the free space will be reported according to the space left in the quota. If more than one quota applies the free space will be reported as the smallest space left in those quotas. The size of the share will be reported according to the quota usage. If more than one quota applies, the smallest size will be reported for the share size according to these quotas. </p>
<dl>
<dd>&bull; yes &#8211; include the quotas when reporting the share size and free space</dl>
<dl>
<dd>&bull; no(default) &#8211; do not include quotas, simply report the size and free space of the file system</dl>
</dl>
<p> gpfs:prealloc = [ yes | no ]</p>
<dl>
<dd>If set to yes the gpfs_prealloc function will be used in the fallocate callback when appropriate. If set to no gpfs_prealloc will not be used. In both cases the system and libc calls are avoided. </p>
<dl>
<dd>&bull; yes (default) &#8211; Use gpfs_prealloc for the fallocate callback.</dl>
<dl>
<dd>&bull; no &#8211; Do not use gpfs_prealloc for the fallocate callback.</dl>
</dl>
<p> gpfs:settimes = [ yes | no ]</p>
<dl>
<dd>Use the gpfs_set_times API when changing the timestamps of a file or directory. If the GPFS API is not available the old method of using utime and the GPFS winattr call will be used instead. </p>
<dl>
<dd>&bull; yes(default) &#8211; Use gpfs_set_times. Fall back to utime and winattr when it is not available.</dl>
<dl>
<dd>&bull; no &#8211; Do not use gpfs_set_times.</dl>
</dl>
<p> nfs4:mode = [ simple | special ]</p>
<dl>
<dd>Controls substitution of special IDs (OWNER@ and GROUP@) on GPFS. The use of mode simple is recommended. In this mode only non inheriting ACL entries for the file owner and group are mapped to special IDs. </p>
<p> The following MODEs are understood by the module: </p>
<dl>
<dd>&bull; simple(default) &#8211; use OWNER@ and GROUP@ special IDs for non inheriting ACEs only.</dl>
<dl>
<dd>&bull; special(deprecated) &#8211; use OWNER@ and GROUP@ special IDs in ACEs for all file owner and group ACEs.</dl>
</dl>
<p> nfs4:acedup = [dontcare|reject|ignore|merge]</p>
<dl>
<dd>This parameter configures how Samba handles duplicate ACEs encountered in GPFS ACLs. GPFS allows/creates duplicate ACE for different bits for same ID. </p>
<p> Following is the behaviour of Samba for different values : </p>
<dl>
<dd>&bull; dontcare (default) &#8211; copy the ACEs as they come</dl>
<dl>
<dd>&bull; reject &#8211; stop operation and exit with error on ACL set op</dl>
<dl>
<dd>&bull; ignore &#8211; don&#8217;t include the second matching ACE</dl>
<dl>
<dd>&bull; merge &#8211; bitwise OR the 2 ace.flag fields and 2 ace.mask fields of the 2 duplicate ACEs into 1 ACE</dl>
</dl>
<p> nfs4:chown = [yes|no]</p>
<dl>
<dd>This parameter allows enabling or disabling the chown supported by the underlying filesystem. This parameter should be enabled with care as it might leave your system insecure. </p>
<p> Some filesystems allow chown as a) giving b) stealing. It is the latter that is considered a risk. </p>
<p> Following is the behaviour of Samba for different values : </p>
<dl>
<dd>&bull; yes &#8211; Enable chown if as supported by the under filesystem</dl>
<dl>
<dd>&bull; no (default) &#8211; Disable chown</dl>
</dl>
<p> gpfs:syncio = [yes|no]</p>
<dl>
<dd>This parameter makes Samba open all files with O_SYNC. This triggers optimizations in GPFS for workloads that heavily share files. </p>
<p> Following is the behaviour of Samba for different values: </p>
<dl>
<dd>&bull; yes &#8211; Open files with O_SYNC</dl>
<dl>
<dd>&bull; no (default) &#8211; Open files as normal Samba would do</dl>
</dl>
<h2>Examples</h2>
<p>A GPFS mount can be exported via Samba as follows : </p>
<dl>
<dd>
<pre> <i>[samba_gpfs_share]</i>
 m[blue]<code>vfs objects = gpfs</code>m[]
 m[blue]<code>path = /test/gpfs_mount</code>m[]
 m[blue]<code>nfs4: mode = special</code>m[]
 m[blue]<code>nfs4: acedup = merge</code>m[]</pre>
</dl>
<h2>Caveats</h2>
<p>Depending on the version of gpfs, the libgpfs_gpl library or the libgpfs library is needed at runtime by the gpfs VFS module: Starting with gpfs 3.2.1 PTF8, the complete libgpfs is available as open source and libgpfs_gpl does no longer exist. With earlier versions of gpfs, only the libgpfs_gpl library was open source and could be used at run time. </p>
<p> At build time, only the header file gpfs_gpl.h is required, which is a symlink to gpfs.h in gpfs versions newer than 3.2.1 PTF8.</p>
<h2>Version</h2>
<p>This man page is correct for version 3.0.25 of the Samba suite.</p>
<h2>Author</h2>
<p>The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed. </p>
<p> The GPFS VFS module was created with contributions from Volker Lendecke and the developers at IBM. </p>
<p> This manpage was created by the IBM FSCC team</p>
