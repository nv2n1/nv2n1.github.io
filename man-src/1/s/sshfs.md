---
title: "sshfs(1)"
name: "sshfs"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sshfs/"
description: "SSHFS – filesystem client based on ssh"
---

<h2 class="name">NAME</h2>
<p> SSHFS &#8211; filesystem client based on ssh </p>
<h2>SYNOPSIS</h2>
<h3>mounting</h3>
<dl>
<dt><code>sshfs</code> [<i>user</i>@]<code>host</code>:[<i>dir</i>] <code>mountpoint</code> [<i>options</i>]</p>
<dd></dl>
<h3>unmounting</h3>
<dl>
<dt><code> mountpoint</code></p>
<dd></dl>
<h2>DESCRIPTION</h2>
<p> SSHFS (Secure SHell FileSystem) is a file system for Linux (and other operating systems with a FUSE implementation, such as Mac OS X or FreeBSD) capable of operating on files on a remote computer using just a secure shell login on the remote computer. On the local computer where the SSHFS is mounted, the implementation makes use of the FUSE (Filesystem in Userspace) kernel module. The practical effect of this is that the end user can seamlessly interact with remote files being securely served over SSH just as if they were local files on his/her computer. On the remote computer the SFTP subsystem of SSH is used. </p>
<p> If <i>host</i> is a numeric IPv6 address, it needs to be enclosed in square brackets.</p>
<h2>OPTIONS</h2>
<h3>general options:</h3>
<dl>
<dt><code>-o</code> opt,[opt&#8230;]</p>
<dd> mount options</p>
<dt><code>-h</code> <code>&#8211;help</code></p>
<dd> print help</p>
<dt><code>-V</code> <code>&#8211;version</code></p>
<dd> print version</dl>
<h3>SSHFS options:</h3>
<dl>
<dt><code>-p</code> PORT</p>
<dd> equivalent to &#8216;-o port=PORT&#8217;</p>
<dt><code>-C</code></p>
<dd> equivalent to &#8216;-o compression=yes&#8217;</p>
<dt><code>-F</code> ssh_configfile</p>
<dd> specifies alternative ssh configuration file</p>
<dt><code>-1</code></p>
<dd> equivalent to &#8216;-o ssh_protocol=1&#8217;</p>
<dt><code>-o</code> reconnect</p>
<dd> reconnect to server</p>
<dt><code>-o</code> delay_connect</p>
<dd> delay connection to server</p>
<dt><code>-o</code> sshfs_sync</p>
<dd> synchronous writes</p>
<dt><code>-o</code> no_readahead</p>
<dd> synchronous reads (no speculative readahead)</p>
<dt><code>-o</code> sync_readdir</p>
<dd> synchronous readdir</p>
<dt><code>-o</code> sshfs_debug</p>
<dd> print some debugging information</p>
<dt><code>-o</code> cache=BOOL</p>
<dd> enable caching {yes,no} (default: yes)</p>
<dt><code>-o</code> cache_timeout=N</p>
<dd> sets timeout for caches in seconds (default: 20)</p>
<dt><code>-o</code> cache_X_timeout=N</p>
<dd> sets timeout for {stat,dir,link} cache</p>
<dt><code>-o</code> workaround=LIST</p>
<dd> colon separated list of workarounds</p>
<dl>
<dt>
<dd>
<dl>
<dt>none</p>
<dd> no workarounds enabled</p>
<dt>all</p>
<dd> all workarounds enabled</p>
<dt>[no]rename</p>
<dd> fix renaming to existing file (default: off)</p>
<dt>[no]nodelaysrv</p>
<dd> set nodelay tcp flag in ssh (default: off)</p>
<dt>[no]truncate</p>
<dd> fix truncate for old servers (default: off)</p>
<dt>[no]buflimit</p>
<dd> fix buffer fillup bug in server (default: on)</dl>
</dl>
<dt><code>-o</code> idmap=TYPE</p>
<dd> user/group ID mapping (default: &quot;none&quot;)</p>
<dl>
<dt>
<dd>
<dl>
<dt>none</p>
<dd> no translation of the ID space</p>
<dt>user</p>
<dd> only translate UID/GID of connecting user</p>
<dt>file</p>
<dd> translate UIDs/GIDs based upon the contents of <code>uidfile </code> and <code>gidfile</code></dl>
</dl>
<dt><code>-o</code> uidfile=FILE</p>
<dd> file containing username:uid mappings for <code>idmap=file</code></p>
<dt><code>-o</code> gidfile=FILE</p>
<dd> file containing groupname:gid mappings for <code>idmap=file</code></p>
<dt><code>-o</code> nomap=TYPE</p>
<dd> with idmap=file, how to handle missing mappings</p>
<dl>
<dt>
<dd>
<dl>
<dt>ignore</p>
<dd> don&#8217;t do any re-mapping</p>
<dt>error</p>
<dd> return an error (default)</dl>
</dl>
<dt><code>-o</code> ssh_command=CMD</p>
<dd> execute CMD instead of &#8216;ssh&#8217;</p>
<dt><code>-o</code> ssh_protocol=N</p>
<dd> ssh protocol to use (default: 2)</p>
<dt><code>-o</code> sftp_server=SERV</p>
<dd> path to sftp server or subsystem (default: sftp)</p>
<dt><code>-o</code> directport=PORT</p>
<dd> directly connect to PORT bypassing ssh</p>
<dt><code>-o</code> slave</p>
<dd> communicate over stdin and stdout bypassing network</p>
<dt><code>-o</code> disable_hardlink</p>
<dd> <a href="/docs/linux/man/2-link/">link</a>(2) will return with errno set to ENOSYS. Hard links don&#8217;t currently work perfectly on sshfs, and this confuses some programs. If that happens try disabling hard links with this option.</p>
<dt><code>-o</code> transform_symlinks</p>
<dd> transform absolute symlinks to relative</p>
<dt><code>-o</code> follow_symlinks</p>
<dd> follow symlinks on the server</p>
<dt><code>-o</code> no_check_root</p>
<dd> don&#8217;t check for existence of &#8216;dir&#8217; on server</p>
<dt><code>-o</code> password_stdin</p>
<dd> read password from stdin (only for pam_mount!)</p>
<dt><code>-o</code> SSHOPT=VAL</p>
<dd> ssh options (see man ssh_config)</dl>
<h3>FUSE options:</h3>
<dl>
<dt><code>-d</code> <code>-o</code> debug</p>
<dd> enable debug output (implies <code>-f</code>)</p>
<dt><code>-f</code></p>
<dd> foreground operation</p>
<dt><code>-s</code></p>
<dd> disable multi-threaded operation</p>
<dt><code>-o</code> allow_other</p>
<dd> allow access to other users</p>
<dt><code>-o</code> allow_root</p>
<dd> allow access to root</p>
<dt><code>-o</code> nonempty</p>
<dd> allow mounts over non-empty file/dir</p>
<dt> <code>-o</code> default_permissions</p>
<dd>enable permission checking by kernel</p>
<dt><code>-o</code> fsname=NAME</p>
<dd> set filesystem name</p>
<dt><code>-o</code> subtype=NAME</p>
<dd> set filesystem type</p>
<dt><code>-o</code> large_read</p>
<dd> issue large read requests (2.4 only)</p>
<dt><code>-o</code> max_read=N</p>
<dd> set maximum size of read requests</p>
<dt><code>-o</code> hard_remove</p>
<dd> immediate removal (don&#8217;t hide files)</p>
<dt><code>-o</code> use_ino</p>
<dd> let filesystem set inode numbers</p>
<dt><code>-o</code> readdir_ino</p>
<dd> try to fill in d_ino in readdir</p>
<dt><code>-o</code> direct_io</p>
<dd> use direct I/O</p>
<dt><code>-o</code> kernel_cache</p>
<dd> cache files in kernel</p>
<dt><code>-o</code> [no]auto_cache</p>
<dd> enable caching based on modification times</p>
<dt><code>-o</code> umask=M</p>
<dd> set file permissions (octal)</p>
<dt><code>-o</code> uid=N</p>
<dd> set file owner (number)</p>
<dt><code>-o</code> gid=N</p>
<dd> set file group (number)</p>
<dt><code>-o</code> entry_timeout=T</p>
<dd> cache timeout for names (1.0s)</p>
<dt><code>-o</code> negative_timeout=T</p>
<dd> cache timeout for deleted names (0.0s)</p>
<dt><code>-o</code> attr_timeout=T</p>
<dd> cache timeout for attributes (1.0s)</p>
<dt><code>-o</code> ac_attr_timeout=T</p>
<dd> auto cache timeout for attributes (attr_timeout)</p>
<dt><code>-o</code> intr</p>
<dd> allow requests to be interrupted</p>
<dt><code>-o</code> intr_signal=NUM</p>
<dd> signal to send on interrupt (10)</p>
<dt><code>-o</code> modules=M1[:M2&#8230;]</p>
<dd> names of modules to push onto filesystem stack</p>
<dt><code>-o</code> max_write=N</p>
<dd> set maximum size of write requests</p>
<dt><code>-o</code> max_readahead=N</p>
<dd> set maximum readahead</p>
<dt><code>-o</code> async_read</p>
<dd> perform reads asynchronously (default)</p>
<dt><code>-o</code> sync_read</p>
<dd> perform reads synchronously</dl>
<h3>Module options:</h3>
<dl>
<dt>[subdir]</p>
<dd>
<dt><code>-o</code> subdir=DIR</p>
<dd> prepend this directory to all paths (mandatory)</p>
<dt><code>-o</code> [no]rellinks</p>
<dd> transform absolute symlinks to relative</p>
<dt>[iconv]</p>
<dd>
<dt><code>-o</code> from_code=CHARSET</p>
<dd> original encoding of file names (default: UTF-8)</p>
<dt><code>-o</code> to_code=CHARSET</p>
<dd> new encoding of the file names (default: ISO-8859-2)</dl>
<h2>AUTHORS</h2>
<p> SSHFS has been written by Miklos Szeredi &lt;miklos [at] szeredi.hu&gt;. </p>
<p> This man page was written by Bartosz Fenski &lt;fenio [at] debian.org&gt; for the Debian GNU/Linux distribution (but it may be used by others). </p>
<h2>Index</h2>
