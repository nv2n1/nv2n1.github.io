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
<dd>vfs objects = full_audit</dd></dl>
<h2>Description</h2>
<p>This VFS module is part of the <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7) suite. </p>
<p> The vfs_full_audit VFS module records selected client operations to the system log using <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3). </p>
<p> vfs_full_audit is able to record the complete set of Samba VFS operations:</p>
<dl>
<dd>chdir</dd></dl>
<dl>
<dd>chflags</dd></dl>
<dl>
<dd>chmod</dd></dl>
<dl>
<dd>chmod_acl</dd></dl>
<dl>
<dd>chown</dd></dl>
<dl>
<dd>close</dd></dl>
<dl>
<dd>closedir</dd></dl>
<dl>
<dd>connect</dd></dl>
<dl>
<dd>copy_chunk_send</dd></dl>
<dl>
<dd>copy_chunk_recv</dd></dl>
<dl>
<dd>disconnect</dd></dl>
<dl>
<dd>disk_free</dd></dl>
<dl>
<dd>fchmod</dd></dl>
<dl>
<dd>fchmod_acl</dd></dl>
<dl>
<dd>fchown</dd></dl>
<dl>
<dd>fget_nt_acl</dd></dl>
<dl>
<dd>fgetxattr</dd></dl>
<dl>
<dd>flistxattr</dd></dl>
<dl>
<dd>fremovexattr</dd></dl>
<dl>
<dd>fset_nt_acl</dd></dl>
<dl>
<dd>fsetxattr</dd></dl>
<dl>
<dd>fstat</dd></dl>
<dl>
<dd>fsync</dd></dl>
<dl>
<dd>ftruncate</dd></dl>
<dl>
<dd>get_compression</dd></dl>
<dl>
<dd>get_nt_acl</dd></dl>
<dl>
<dd>get_quota</dd></dl>
<dl>
<dd>get_shadow_copy_data</dd></dl>
<dl>
<dd>getlock</dd></dl>
<dl>
<dd>getwd</dd></dl>
<dl>
<dd>getxattr</dd></dl>
<dl>
<dd>kernel_flock</dd></dl>
<dl>
<dd>link</dd></dl>
<dl>
<dd>linux_setlease</dd></dl>
<dl>
<dd>listxattr</dd></dl>
<dl>
<dd>lock</dd></dl>
<dl>
<dd>lseek</dd></dl>
<dl>
<dd>lstat</dd></dl>
<dl>
<dd>mkdir</dd></dl>
<dl>
<dd>mknod</dd></dl>
<dl>
<dd>open</dd></dl>
<dl>
<dd>opendir</dd></dl>
<dl>
<dd>pread</dd></dl>
<dl>
<dd>pwrite</dd></dl>
<dl>
<dd>read</dd></dl>
<dl>
<dd>readdir</dd></dl>
<dl>
<dd>readlink</dd></dl>
<dl>
<dd>realpath</dd></dl>
<dl>
<dd>removexattr</dd></dl>
<dl>
<dd>rename</dd></dl>
<dl>
<dd>rewinddir</dd></dl>
<dl>
<dd>rmdir</dd></dl>
<dl>
<dd>seekdir</dd></dl>
<dl>
<dd>sendfile</dd></dl>
<dl>
<dd>set_compression</dd></dl>
<dl>
<dd>set_nt_acl</dd></dl>
<dl>
<dd>set_quota</dd></dl>
<dl>
<dd>setxattr</dd></dl>
<dl>
<dd>snap_check_path</dd></dl>
<dl>
<dd>snap_create</dd></dl>
<dl>
<dd>snap_delete</dd></dl>
<dl>
<dd>stat</dd></dl>
<dl>
<dd>statvfs</dd></dl>
<dl>
<dd>symlink</dd></dl>
<dl>
<dd>sys_acl_delete_def_file</dd></dl>
<dl>
<dd>sys_acl_get_fd</dd></dl>
<dl>
<dd>sys_acl_get_file</dd></dl>
<dl>
<dd>sys_acl_set_fd</dd></dl>
<dl>
<dd>sys_acl_set_file</dd></dl>
<dl>
<dd>telldir</dd></dl>
<dl>
<dd>unlink</dd></dl>
<dl>
<dd>utime</dd></dl>
<dl>
<dd>write</dd></dl>
<p> In addition to these operations, vfs_full_audit recognizes the special operation names &quot;all&quot; and &quot;none &quot;, which refer to all the VFS operations and none of the VFS operations respectively. </p>
<p> vfs_full_audit records operations in fixed format consisting of fields separated by &#8216;|&#8217; characters. The format is: </p>
<dl>
<dd>
<pre> smbd_audit: PREFIX|OPERATION|RESULT|FILE</pre>
</dd></dl>
<p> The record fields are: </p>
<dl>
<dd>&bull; PREFIX &#8211; the result of the full_audit:prefix string after variable substitutions</dd></dl>
<dl>
<dd>&bull; OPERATION &#8211; the name of the VFS operation</dd></dl>
<dl>
<dd>&bull; RESULT &#8211; whether the operation succeeded or failed</dd></dl>
<dl>
<dd>&bull; FILE &#8211; the name of the file or directory the operation was performed on</dd></dl>
<p> This module is stackable.</p>
<h2>Options</h2>
<p>full_audit:prefix = STRING</p>
<dl>
<dd>Prepend audit messages with STRING. STRING is processed for standard substitution variables listed in <code><a href="/docs/linux/man/5-smb-conf/">smb.conf</a></code>(5). The default prefix is &quot;%u|%I&quot;.</dd></dl>
<p> full_audit:success = LIST</p>
<dl>
<dd>LIST is a list of VFS operations that should be recorded if they succeed. Operations are specified using the names listed above. Operations can be unset by prefixing the names with &quot;!&quot;. The default is all operations.</dd></dl>
<p> full_audit:failure = LIST</p>
<dl>
<dd>LIST is a list of VFS operations that should be recorded if they failed. Operations are specified using the names listed above. Operations can be unset by prefixing the names with &quot;!&quot;. The default is all operations.</dd></dl>
<p> full_audit:facility = FACILITY</p>
<dl>
<dd>Log messages to the named <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3) facility.</dd></dl>
<p> full_audit:priority = PRIORITY</p>
<dl>
<dd>Log messages with the named <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3) priority.</dd></dl>
<p> full_audit:syslog = true/false</p>
<dl>
<dd>Log messages to syslog (default) or as a debug level 1 message.</dd></dl>
<p> full_audit:log_secdesc = true/false</p>
<dl>
<dd>Log an sddl form of the security descriptor coming in when a client sets an acl. Defaults to false.</dd></dl>
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
</dd></dl>
<h2>Version</h2>
<p>This man page is correct for version 3.0.25 of the Samba suite.</p>
<h2>Author</h2>
<p>The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed.</p>
