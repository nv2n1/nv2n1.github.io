---

title: "sshfs(1)"
name: "sshfs"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sshfs/"
description: "SSHFS – filesystem client based on ssh"
---

<h3>mounting</h3>
<dl>
<dt><code>sshfs</code> [<i>user</i>@]<code>host</code>:[<i>dir</i>] <code>mountpoint</code> [<i>options</i>]</dt>
<dd></dd></dl>
<h3>unmounting</h3>
<dl>
<dt><code> mountpoint</code></dt>
<dd></dd></dl>
<p> SSHFS (Secure SHell FileSystem) is a file system for Linux (and other operating systems with a FUSE implementation, such as Mac OS X or FreeBSD) capable of operating on files on a remote computer using just a secure shell login on the remote computer. On the local computer where the SSHFS is mounted, the implementation makes use of the FUSE (Filesystem in Userspace) kernel module. The practical effect of this is that the end user can seamlessly interact with remote files being securely served over SSH just as if they were local files on his/her computer. On the remote computer the SFTP subsystem of SSH is used. </p>
<p> If <i>host</i> is a numeric IPv6 address, it needs to be enclosed in square brackets.</p>
<h2>OPTIONS</h2>
<h3>general options:</h3>
<dl>
<dt><code>-o</code> opt,[opt&#8230;]</dt>
<dd> mount options</dd>
<dt><code>-h</code> <code>&#8211;help</code></dt>
<dd> print help</dd>
<dt><code>-V</code> <code>&#8211;version</code></dt>
<dd> print version</dd></dl>
<h3>SSHFS options:</h3>
<dl>
<dt><code>-p</code> PORT</dt>
<dd> equivalent to &#8216;-o port=PORT&#8217;</dd>
<dt><code>-C</code></dt>
<dd> equivalent to &#8216;-o compression=yes&#8217;</dd>
<dt><code>-F</code> ssh_configfile</dt>
<dd> specifies alternative ssh configuration file</dd>
<dt><code>-1</code></dt>
<dd> equivalent to &#8216;-o ssh_protocol=1&#8217;</dd>
<dt><code>-o</code> reconnect</dt>
<dd> reconnect to server</dd>
<dt><code>-o</code> delay_connect</dt>
<dd> delay connection to server</dd>
<dt><code>-o</code> sshfs_sync</dt>
<dd> synchronous writes</dd>
<dt><code>-o</code> no_readahead</dt>
<dd> synchronous reads (no speculative readahead)</dd>
<dt><code>-o</code> sync_readdir</dt>
<dd> synchronous readdir</dd>
<dt><code>-o</code> sshfs_debug</dt>
<dd> print some debugging information</dd>
<dt><code>-o</code> cache=BOOL</dt>
<dd> enable caching {yes,no} (default: yes)</dd>
<dt><code>-o</code> cache_timeout=N</dt>
<dd> sets timeout for caches in seconds (default: 20)</dd>
<dt><code>-o</code> cache_X_timeout=N</dt>
<dd> sets timeout for {stat,dir,link} cache</dd>
<dt><code>-o</code> workaround=LIST</dt>
<dd> colon separated list of workarounds</dd>
<dl>
<dl>
<dt>none</dt>
<dd> no workarounds enabled</dd>
<dt>all</dt>
<dd> all workarounds enabled</dd>
<dt>[no]rename</dt>
<dd> fix renaming to existing file (default: off)</dd>
<dt>[no]nodelaysrv</dt>
<dd> set nodelay tcp flag in ssh (default: off)</dd>
<dt>[no]truncate</dt>
<dd> fix truncate for old servers (default: off)</dd>
<dt>[no]buflimit</dt>
<dd> fix buffer fillup bug in server (default: on)</dd></dl>
</dl>
<dt><code>-o</code> idmap=TYPE</dt>
<dd> user/group ID mapping (default: &quot;none&quot;)</dd>
<dl>
<dl>
<dt>none</dt>
<dd> no translation of the ID space</dd>
<dt>user</dt>
<dd> only translate UID/GID of connecting user</dd>
<dt>file</dt>
<dd> translate UIDs/GIDs based upon the contents of <code>uidfile </code> and <code>gidfile</code></dd></dl>
</dl>
<dt><code>-o</code> uidfile=FILE</dt>
<dd> file containing username:uid mappings for <code>idmap=file</code></dd>
<dt><code>-o</code> gidfile=FILE</dt>
<dd> file containing groupname:gid mappings for <code>idmap=file</code></dd>
<dt><code>-o</code> nomap=TYPE</dt>
<dd> with idmap=file, how to handle missing mappings</dd>
<dl>
<dl>
<dt>ignore</dt>
<dd> don&#8217;t do any re-mapping</dd>
<dt>error</dt>
<dd> return an error (default)</dd></dl>
</dl>
<dt><code>-o</code> ssh_command=CMD</dt>
<dd> execute CMD instead of &#8216;ssh&#8217;</dd>
<dt><code>-o</code> ssh_protocol=N</dt>
<dd> ssh protocol to use (default: 2)</dd>
<dt><code>-o</code> sftp_server=SERV</dt>
<dd> path to sftp server or subsystem (default: sftp)</dd>
<dt><code>-o</code> directport=PORT</dt>
<dd> directly connect to PORT bypassing ssh</dd>
<dt><code>-o</code> slave</dt>
<dd> communicate over stdin and stdout bypassing network</dd>
<dt><code>-o</code> disable_hardlink</dt>
<dd> <a href="/docs/linux/man/2-link/">link</a>(2) will return with errno set to ENOSYS. Hard links don&#8217;t currently work perfectly on sshfs, and this confuses some programs. If that happens try disabling hard links with this option.</dd>
<dt><code>-o</code> transform_symlinks</dt>
<dd> transform absolute symlinks to relative</dd>
<dt><code>-o</code> follow_symlinks</dt>
<dd> follow symlinks on the server</dd>
<dt><code>-o</code> no_check_root</dt>
<dd> don&#8217;t check for existence of &#8216;dir&#8217; on server</dd>
<dt><code>-o</code> password_stdin</dt>
<dd> read password from stdin (only for pam_mount!)</dd>
<dt><code>-o</code> SSHOPT=VAL</dt>
<dd> ssh options (see man ssh_config)</dd></dl>
<h3>FUSE options:</h3>
<dl>
<dt><code>-d</code> <code>-o</code> debug</dt>
<dd> enable debug output (implies <code>-f</code>)</dd>
<dt><code>-f</code></dt>
<dd> foreground operation</dd>
<dt><code>-s</code></dt>
<dd> disable multi-threaded operation</dd>
<dt><code>-o</code> allow_other</dt>
<dd> allow access to other users</dd>
<dt><code>-o</code> allow_root</dt>
<dd> allow access to root</dd>
<dt><code>-o</code> nonempty</dt>
<dd> allow mounts over non-empty file/dir</dd>
<dt> <code>-o</code> default_permissions</dt>
<dd>enable permission checking by kernel</dd>
<dt><code>-o</code> fsname=NAME</dt>
<dd> set filesystem name</dd>
<dt><code>-o</code> subtype=NAME</dt>
<dd> set filesystem type</dd>
<dt><code>-o</code> large_read</dt>
<dd> issue large read requests (2.4 only)</dd>
<dt><code>-o</code> max_read=N</dt>
<dd> set maximum size of read requests</dd>
<dt><code>-o</code> hard_remove</dt>
<dd> immediate removal (don&#8217;t hide files)</dd>
<dt><code>-o</code> use_ino</dt>
<dd> let filesystem set inode numbers</dd>
<dt><code>-o</code> readdir_ino</dt>
<dd> try to fill in d_ino in readdir</dd>
<dt><code>-o</code> direct_io</dt>
<dd> use direct I/O</dd>
<dt><code>-o</code> kernel_cache</dt>
<dd> cache files in kernel</dd>
<dt><code>-o</code> [no]auto_cache</dt>
<dd> enable caching based on modification times</dd>
<dt><code>-o</code> umask=M</dt>
<dd> set file permissions (octal)</dd>
<dt><code>-o</code> uid=N</dt>
<dd> set file owner (number)</dd>
<dt><code>-o</code> gid=N</dt>
<dd> set file group (number)</dd>
<dt><code>-o</code> entry_timeout=T</dt>
<dd> cache timeout for names (1.0s)</dd>
<dt><code>-o</code> negative_timeout=T</dt>
<dd> cache timeout for deleted names (0.0s)</dd>
<dt><code>-o</code> attr_timeout=T</dt>
<dd> cache timeout for attributes (1.0s)</dd>
<dt><code>-o</code> ac_attr_timeout=T</dt>
<dd> auto cache timeout for attributes (attr_timeout)</dd>
<dt><code>-o</code> intr</dt>
<dd> allow requests to be interrupted</dd>
<dt><code>-o</code> intr_signal=NUM</dt>
<dd> signal to send on interrupt (10)</dd>
<dt><code>-o</code> modules=M1[:M2&#8230;]</dt>
<dd> names of modules to push onto filesystem stack</dd>
<dt><code>-o</code> max_write=N</dt>
<dd> set maximum size of write requests</dd>
<dt><code>-o</code> max_readahead=N</dt>
<dd> set maximum readahead</dd>
<dt><code>-o</code> async_read</dt>
<dd> perform reads asynchronously (default)</dd>
<dt><code>-o</code> sync_read</dt>
<dd> perform reads synchronously</dd></dl>
<h3>Module options:</h3>
<dl>
<dt>[subdir]</dt>
<dd>
</dd><dt><code>-o</code> subdir=DIR</dt>
<dd> prepend this directory to all paths (mandatory)</dd>
<dt><code>-o</code> [no]rellinks</dt>
<dd> transform absolute symlinks to relative</dd>
<dt>[iconv]</dt>
<dd>
</dd><dt><code>-o</code> from_code=CHARSET</dt>
<dd> original encoding of file names (default: UTF-8)</dd>
<dt><code>-o</code> to_code=CHARSET</dt>
<dd> new encoding of the file names (default: ISO-8859-2)</dd></dl>
<h2>AUTHORS</h2>
<p> SSHFS has been written by Miklos Szeredi &lt;miklos [at] szeredi.hu&gt;. </p>
<p> This man page was written by Bartosz Fenski &lt;fenio [at] debian.org&gt; for the Debian GNU/Linux distribution (but it may be used by others). </p>
