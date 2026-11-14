---
title: "vfs_full_audit(8)"
name: "vfs_full_audit"
section: "8"
letter: "v"
url: "/docs/linux/man/8-vfs_full_audit/"
description: "vfs_full_audit – record Samba VFS operations in the system log"
---

<p>vfs_full_audit &#8211; record Samba VFS operations in the system log</p>
<h2>Synopsis</h2>
<dl>
<dd>vfs objects = full_audit</dl>
<h2>Description</h2>
<p>This VFS module is part of the <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7) suite. </p>
<p> The vfs_full_audit VFS module records selected client operations to the system log using <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3). </p>
<p> vfs_full_audit is able to record the complete set of Samba VFS operations:</p>
<dl>
<dd>chdir</dl>
<dl>
<dd>chflags</dl>
<dl>
<dd>chmod</dl>
<dl>
<dd>chmod_acl</dl>
<dl>
<dd>chown</dl>
<dl>
<dd>close</dl>
<dl>
<dd>closedir</dl>
<dl>
<dd>connect</dl>
<dl>
<dd>copy_chunk_send</dl>
<dl>
<dd>copy_chunk_recv</dl>
<dl>
<dd>disconnect</dl>
<dl>
<dd>disk_free</dl>
<dl>
<dd>fchmod</dl>
<dl>
<dd>fchmod_acl</dl>
<dl>
<dd>fchown</dl>
<dl>
<dd>fget_nt_acl</dl>
<dl>
<dd>fgetxattr</dl>
<dl>
<dd>flistxattr</dl>
<dl>
<dd>fremovexattr</dl>
<dl>
<dd>fset_nt_acl</dl>
<dl>
<dd>fsetxattr</dl>
<dl>
<dd>fstat</dl>
<dl>
<dd>fsync</dl>
<dl>
<dd>ftruncate</dl>
<dl>
<dd>get_compression</dl>
<dl>
<dd>get_nt_acl</dl>
<dl>
<dd>get_quota</dl>
<dl>
<dd>get_shadow_copy_data</dl>
<dl>
<dd>getlock</dl>
<dl>
<dd>getwd</dl>
<dl>
<dd>getxattr</dl>
<dl>
<dd>kernel_flock</dl>
<dl>
<dd>link</dl>
<dl>
<dd>linux_setlease</dl>
<dl>
<dd>listxattr</dl>
<dl>
<dd>lock</dl>
<dl>
<dd>lseek</dl>
<dl>
<dd>lstat</dl>
<dl>
<dd>mkdir</dl>
<dl>
<dd>mknod</dl>
<dl>
<dd>open</dl>
<dl>
<dd>opendir</dl>
<dl>
<dd>pread</dl>
<dl>
<dd>pwrite</dl>
<dl>
<dd>read</dl>
<dl>
<dd>readdir</dl>
<dl>
<dd>readlink</dl>
<dl>
<dd>realpath</dl>
<dl>
<dd>removexattr</dl>
<dl>
<dd>rename</dl>
<dl>
<dd>rewinddir</dl>
<dl>
<dd>rmdir</dl>
<dl>
<dd>seekdir</dl>
<dl>
<dd>sendfile</dl>
<dl>
<dd>set_compression</dl>
<dl>
<dd>set_nt_acl</dl>
<dl>
<dd>set_quota</dl>
<dl>
<dd>setxattr</dl>
<dl>
<dd>snap_check_path</dl>
<dl>
<dd>snap_create</dl>
<dl>
<dd>snap_delete</dl>
<dl>
<dd>stat</dl>
<dl>
<dd>statvfs</dl>
<dl>
<dd>symlink</dl>
<dl>
<dd>sys_acl_delete_def_file</dl>
<dl>
<dd>sys_acl_get_fd</dl>
<dl>
<dd>sys_acl_get_file</dl>
<dl>
<dd>sys_acl_set_fd</dl>
<dl>
<dd>sys_acl_set_file</dl>
<dl>
<dd>telldir</dl>
<dl>
<dd>unlink</dl>
<dl>
<dd>utime</dl>
<dl>
<dd>write</dl>
<p> In addition to these operations, vfs_full_audit recognizes the special operation names &quot;all&quot; and &quot;none &quot;, which refer to all the VFS operations and none of the VFS operations respectively. </p>
<p> vfs_full_audit records operations in fixed format consisting of fields separated by &#8216;|&#8217; characters. The format is: </p>
<dl>
<dd>
<pre> smbd_audit: PREFIX|OPERATION|RESULT|FILE</pre>
</dl>
<p> The record fields are: </p>
<dl>
<dd>&bull; PREFIX &#8211; the result of the full_audit:prefix string after variable substitutions</dl>
<dl>
<dd>&bull; OPERATION &#8211; the name of the VFS operation</dl>
<dl>
<dd>&bull; RESULT &#8211; whether the operation succeeded or failed</dl>
<dl>
<dd>&bull; FILE &#8211; the name of the file or directory the operation was performed on</dl>
<p> This module is stackable.</p>
<h2>Options</h2>
<p>full_audit:prefix = STRING</p>
<dl>
<dd>Prepend audit messages with STRING. STRING is processed for standard substitution variables listed in <code><a href="/docs/linux/man/5-smb-conf/">smb.conf</a></code>(5). The default prefix is &quot;%u|%I&quot;.</dl>
<p> full_audit:success = LIST</p>
<dl>
<dd>LIST is a list of VFS operations that should be recorded if they succeed. Operations are specified using the names listed above. Operations can be unset by prefixing the names with &quot;!&quot;. The default is all operations.</dl>
<p> full_audit:failure = LIST</p>
<dl>
<dd>LIST is a list of VFS operations that should be recorded if they failed. Operations are specified using the names listed above. Operations can be unset by prefixing the names with &quot;!&quot;. The default is all operations.</dl>
<p> full_audit:facility = FACILITY</p>
<dl>
<dd>Log messages to the named <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3) facility.</dl>
<p> full_audit:priority = PRIORITY</p>
<dl>
<dd>Log messages with the named <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3) priority.</dl>
<p> full_audit:syslog = true/false</p>
<dl>
<dd>Log messages to syslog (default) or as a debug level 1 message.</dl>
<p> full_audit:log_secdesc = true/false</p>
<dl>
<dd>Log an sddl form of the security descriptor coming in when a client sets an acl. Defaults to false.</dl>
<h2>Examples</h2>
<p>Log file and directory open operations on the [records] share using the LOCAL7 facility and ALERT priority, including the username and IP address. Logging excludes the open VFS function on failures: </p>
<dl>
<dd>
<pre> <i>[records]</i>
 m[blue]<code>path = /data/records</code>m[]
 m[blue]<code>vfs objects = full_audit</code>m[]
 m[blue]<code>full_audit:prefix = %u|%I</code>m[]
 m[blue]<code>full_audit:success = open opendir</code>m[]
 m[blue]<code>full_audit:failure = all !open</code>m[]
 m[blue]<code>full_audit:facility = LOCAL7</code>m[]
 m[blue]<code>full_audit:priority = ALERT</code>m[]</pre>
</dl>
<h2>Version</h2>
<p>This man page is correct for version 3.0.25 of the Samba suite.</p>
<h2>Author</h2>
<p>The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed.</p>
