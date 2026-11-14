---
title: "mount-cifs(8)"
name: "mount-cifs"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mount-cifs/"
description: "mount.cifs – mount using the Common Internet File System (CIFS)"
---

<p>mount.cifs &#8211; mount using the Common Internet File System (CIFS)</p>
<h2>Synopsis</h2>
<dl>
<dd>mount.cifs {service} {mount-point} [-o options]</dl>
<h2>Description</h2>
<p>This tool is part of the cifs-utils suite. </p>
<p> mount.cifs mounts a Linux CIFS filesystem. It is usually invoked indirectly by the <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8) command when using the &quot;-t cifs&quot; option. This command only works in Linux, and the kernel must support the cifs filesystem. The CIFS protocol is the successor to the SMB protocol and is supported by most Windows servers and many other commercial servers and Network Attached Storage appliances as well as by the popular Open Source server Samba. </p>
<p> The mount.cifs utility attaches the UNC name (exported network resource) specified as <i>service</i> (using //server/share syntax, where &quot;server&quot; is the server name or IP address and &quot;share&quot; is the name of the share) to the local directory <i>mount-point</i>. </p>
<p> Options to <i>mount.cifs</i> are specified as a comma-separated list of key=value pairs. It is possible to send options other than those listed here, assuming that the cifs filesystem kernel module (cifs.ko) supports them. Unrecognized cifs mount options passed to the cifs vfs kernel code will be logged to the kernel log. </p>
<p> <i>mount.cifs</i> causes the cifs vfs to launch a thread named cifsd. After mounting it keeps running until the mounted resource is unmounted (usually via the umount utility). </p>
<p> <i>mount.cifs -V</i> command displays the version of cifs mount helper. </p>
<p> <i>modinfo cifs</i> command displays the version of cifs module.</p>
<h2>Options</h2>
<p>username=<i>arg</i></p>
<dl>
<dd>specifies the username to connect as. If this is not given, then the environment variable <i>USER</i> is used. </p>
<p> Earlier versions of mount.cifs also allowed one to specify the username in a &quot;user%password&quot; or &quot;workgroup/user&quot; or &quot;workgroup/user%password&quot; to allow the password and workgroup to be specified as part of the username. Support for those alternate username formats is now deprecated and should no longer be used. Users should use the discrete &quot;password=&quot; and &quot;domain=&quot; to specify those values. While some versions of the cifs kernel module accept &quot;user=&quot; as an abbreviation for this option, its use can confuse the standard mount program into thinking that this is a non-superuser mount. It is therefore recommended to use the full &quot;username=&quot; option name.</dl>
<p> password=<i>arg</i></p>
<dl>
<dd>specifies the CIFS password. If this option is not given then the environment variable <i>PASSWD</i> is used. If the password is not specified directly or indirectly via an argument to mount, <i>mount.cifs</i> will prompt for a password, unless the guest option is specified. </p>
<p> Note that a password which contains the delimiter character (i.e. a comma &#8216;,&#8217;) will fail to be parsed correctly on the command line. However, the same password defined in the PASSWD environment variable or via a credentials file (see below) or entered at the password prompt will be read correctly.</dl>
<p> credentials=<i>filename</i></p>
<dl>
<dd>specifies a file that contains a username and/or password and optionally the name of the workgroup. The format of the file is: </p>
<dl>
<dd>
<pre> username=<i>value</i>
 password=<i>value</i>
 domain=<i>value</i></pre>
</dl>
<p> This is preferred over having passwords in plaintext in a shared file, such as /etc/fstab. Be sure to protect any credentials file properly.</dl>
<p> uid=<i>arg</i></p>
<dl>
<dd>sets the uid that will own all files or directories on the mounted filesystem when the server does not provide ownership information. It may be specified as either a username or a numeric uid. When not specified, the default is uid 0. The mount.cifs helper must be at version 1.10 or higher to support specifying the uid in non-numeric form. See the section on FILE AND DIRECTORY OWNERSHIP AND PERMISSIONS below for more information.</dl>
<p> forceuid</p>
<dl>
<dd>instructs the client to ignore any uid provided by the server for files and directories and to always assign the owner to be the value of the uid= option. See the section on FILE AND DIRECTORY OWNERSHIP AND PERMISSIONS below for more information.</dl>
<p> cruid=<i>arg</i></p>
<dl>
<dd>sets the uid of the owner of the credentials cache. This is primarily useful with sec=krb5. The default is the real uid of the process performing the mount. Setting this parameter directs the upcall to look for a credentials cache owned by that user.</dl>
<p> gid=<i>arg</i></p>
<dl>
<dd>sets the gid that will own all files or directories on the mounted filesystem when the server does not provide ownership information. It may be specified as either a groupname or a numeric gid. When not specified, the default is gid 0. The mount.cifs helper must be at version 1.10 or higher to support specifying the gid in non-numeric form. See the section on FILE AND DIRECTORY OWNERSHIP AND PERMISSIONS below for more information.</dl>
<p> forcegid</p>
<dl>
<dd>instructs the client to ignore any gid provided by the server for files and directories and to always assign the owner to be the value of the gid= option. See the section on FILE AND DIRECTORY OWNERSHIP AND PERMISSIONS below for more information.</dl>
<p> port=<i>arg</i></p>
<dl>
<dd>sets the port number on which the client will attempt to contact the CIFS server. If this value is specified, look for an existing connection with this port, and use that if one exists. If one doesn&#8217;t exist, try to create a new connection on that port. If that connection fails, return an error. If this value isn&#8217;t specified, look for an existing connection on port 445 or 139. If no such connection exists, try to connect on port 445 first and then port 139 if that fails. Return an error if both fail.</dl>
<p> servernetbiosname=<i>arg</i></p>
<dl>
<dd>Specify the server netbios name (RFC1001 name) to use when attempting to setup a session to the server. Although rarely needed for mounting to newer servers, this option is needed for mounting to some older servers (such as OS/2 or Windows 98 and Windows ME) since when connecting over port 139 they, unlike most newer servers, do not support a default server name. A server name can be up to 15 characters long and is usually uppercased.</dl>
<p> servern=<i>arg</i></p>
<dl>
<dd>Synonym for <i>servernetbiosname</i>.</dl>
<p> netbiosname=<i>arg</i></p>
<dl>
<dd>When mounting to servers via port 139, specifies the RFC1001 source name to use to represent the client netbios machine name when doing the RFC1001 netbios session initialize.</dl>
<p> file_mode=<i>arg</i></p>
<dl>
<dd>If the server does not support the CIFS Unix extensions this overrides the default file mode.</dl>
<p> dir_mode=<i>arg</i></p>
<dl>
<dd>If the server does not support the CIFS Unix extensions this overrides the default mode for directories.</dl>
<p> ip=<i>arg</i></p>
<dl>
<dd>sets the destination IP address. This option is set automatically if the server name portion of the requested UNC name can be resolved so rarely needs to be specified by the user.</dl>
<p> domain=<i>arg</i></p>
<dl>
<dd>sets the domain (workgroup) of the user</dl>
<p> guest</p>
<dl>
<dd>don&#8217;t prompt for a password</dl>
<p> iocharset</p>
<dl>
<dd>Charset used to convert local path names to and from Unicode. Unicode is used by default for network path names if the server supports it. If iocharset is not specified then the nls_default specified during the local client kernel build will be used. If server does not support Unicode, this parameter is unused.</dl>
<p> ro</p>
<dl>
<dd>mount read-only</dl>
<p> rw</p>
<dl>
<dd>mount read-write</dl>
<p> setuids</p>
<dl>
<dd>If the CIFS Unix extensions are negotiated with the server the client will attempt to set the effective uid and gid of the local process on newly created files, directories, and devices (create, mkdir, mknod). If the CIFS Unix Extensions are not negotiated, for newly created files and directories instead of using the default uid and gid specified on the the mount, cache the new file&#8217;s uid and gid locally which means that the uid for the file can change when the inode is reloaded (or the user remounts the share).</dl>
<p> nosetuids</p>
<dl>
<dd>The client will not attempt to set the uid and gid on on newly created files, directories, and devices (create, mkdir, mknod) which will result in the server setting the uid and gid to the default (usually the server uid of the user who mounted the share). Letting the server (rather than the client) set the uid and gid is the default.If the CIFS Unix Extensions are not negotiated then the uid and gid for new files will appear to be the uid (gid) of the mounter or the uid (gid) parameter specified on the mount.</dl>
<p> perm</p>
<dl>
<dd>Client does permission checks (vfs_permission check of uid and gid of the file against the mode and desired operation), Note that this is in addition to the normal ACL check on the target machine done by the server software. Client permission checking is enabled by default.</dl>
<p> noperm</p>
<dl>
<dd>Client does not do permission checks. This can expose files on this mount to access by other users on the local client system. It is typically only needed when the server supports the CIFS Unix Extensions but the UIDs/GIDs on the client and server system do not match closely enough to allow access by the user doing the mount. Note that this does not affect the normal ACL check on the target machine done by the server software (of the server ACL against the user name provided at mount time).</dl>
<p> dynperm</p>
<dl>
<dd>Instructs the server to maintain ownership and permissions in memory that can&#8217;t be stored on the server. This information can disappear at any time (whenever the inode is flushed from the cache), so while this may help make some applications work, it&#8217;s behavior is somewhat unreliable. See the section below on FILE AND DIRECTORY OWNERSHIP AND PERMISSIONS for more information.</dl>
<p> cache=</p>
<dl>
<dd>Cache mode. See the section below on CACHE COHERENCY for details. Allowed values are: </p>
<dl>
<dd>&bull; none: do not cache file data at all</dl>
<dl>
<dd>&bull; strict: follow the CIFS/SMB2 protocol strictly</dl>
<dl>
<dd>&bull; loose: allow loose caching semantics</dl>
<p> The default in kernels prior to 3.7 was &quot;loose&quot;. As of kernel 3.7 the default is &quot;strict&quot;.</dl>
<p> directio</p>
<dl>
<dd>Do not do inode data caching on files opened on this mount. This precludes mmaping files on this mount. In some cases with fast networks and little or no caching benefits on the client (e.g. when the application is doing large sequential reads bigger than page size without rereading the same data) this can provide better performance than the default behavior which caches reads (readahead) and writes (writebehind) through the local Linux client pagecache if oplock (caching token) is granted and held. Note that direct allows write operations larger than page size to be sent to the server. On some kernels this requires the cifs.ko module to be built with the CIFS_EXPERIMENTAL configure option. </p>
<p> This option is will be deprecated in 3.7. Users should use cache=none instead on more recent kernels.</dl>
<p> strictcache</p>
<dl>
<dd>Use for switching on strict cache mode. In this mode the client reads from the cache all the time it has Oplock Level II, otherwise &#8211; read from the server. As for write &#8211; the client stores a data in the cache in Exclusive Oplock case, otherwise &#8211; write directly to the server. </p>
<p> This option is will be deprecated in 3.7. Users should use cache=strict instead on more recent kernels.</dl>
<p> rwpidforward</p>
<dl>
<dd>Forward pid of a process who opened a file to any read or write operation on that file. This prevent applications like WINE from failing on read and write if we use mandatory brlock style.</dl>
<p> mapchars</p>
<dl>
<dd>Translate six of the seven reserved characters (not backslash, but including the colon, question mark, pipe, asterik, greater than and less than characters) to the remap range (above 0xF000), which also allows the CIFS client to recognize files created with such characters by Windows&#8217;s POSIX emulation. This can also be useful when mounting to most versions of Samba (which also forbids creating and opening files whose names contain any of these seven characters). This has no effect if the server does not support Unicode on the wire. Please note that the files created with mapchars mount option may not be accessible if the share is mounted without that option.</dl>
<p> nomapchars</p>
<dl>
<dd>Do not translate any of these seven characters (default)</dl>
<p> intr</p>
<dl>
<dd>currently unimplemented</dl>
<p> nointr</p>
<dl>
<dd>(default) currently unimplemented</dl>
<p> hard</p>
<dl>
<dd>The program accessing a file on the cifs mounted file system will hang when the server crashes.</dl>
<p> soft</p>
<dl>
<dd>(default) The program accessing a file on the cifs mounted file system will not hang when the server crashes and will return errors to the user application.</dl>
<p> noacl</p>
<dl>
<dd>Do not allow POSIX ACL operations even if server would support them. </p>
<p> The CIFS client can get and set POSIX ACLs (getfacl, setfacl) to Samba servers version 3.0.10 and later. Setting POSIX ACLs requires enabling both CIFS_XATTR and then CIFS_POSIX support in the CIFS configuration options when building the cifs module. POSIX ACL support can be disabled on a per mount basis by specifying &quot;noacl&quot; on mount.</dl>
<p> cifsacl</p>
<dl>
<dd>This option is used to map CIFS/NTFS ACLs to/from Linux permission bits, map SIDs to/from UIDs and GIDs, and get and set Security Descriptors. </p>
<p> See sections on <i>CIFS/NTFS ACL, SID/UID/GID MAPPING, SECURITY DESCRIPTORS</i> for more information.</dl>
<p> backupuid=<i>arg</i></p>
<dl>
<dd>File access by this user shall be done with the backup intent flag set. Either a name or an id must be provided as an argument, there are no default values. </p>
<p> See section <i>ACCESSING FILES WITH BACKUP INTENT</i> for more details</dl>
<p> backupgid=<i>arg</i></p>
<dl>
<dd>File access by users who are members of this group shall be done with the backup intent flag set. Either a name or an id must be provided as an argument, there are no default values. </p>
<p> See section <i>ACCESSING FILES WITH BACKUP INTENT</i> for more details</dl>
<p> nocase</p>
<dl>
<dd>Request case insensitive path name matching (case sensitive is the default if the server suports it).</dl>
<p> ignorecase</p>
<dl>
<dd>Synonym for <i>nocase</i>.</dl>
<p> sec=</p>
<dl>
<dd>Security mode. Allowed values are: </p>
<dl>
<dd>&bull; none &#8211; attempt to connection as a null user (no name)</dl>
<dl>
<dd>&bull; krb5 &#8211; Use Kerberos version 5 authentication</dl>
<dl>
<dd>&bull; krb5i &#8211; Use Kerberos authentication and forcibly enable packet signing</dl>
<dl>
<dd>&bull; ntlm &#8211; Use NTLM password hashing</dl>
<dl>
<dd>&bull; ntlmi &#8211; Use NTLM password hashing and force packet signing</dl>
<dl>
<dd>&bull; ntlmv2 &#8211; Use NTLMv2 password hashing</dl>
<dl>
<dd>&bull; ntlmv2i &#8211; Use NTLMv2 password hashing and force packet signing</dl>
<dl>
<dd>&bull; ntlmssp &#8211; Use NTLMv2 password hashing encapsulated in Raw NTLMSSP message</dl>
<dl>
<dd>&bull; ntlmsspi &#8211; Use NTLMv2 password hashing encapsulated in Raw NTLMSSP message, and force packet signing</dl>
<p> The default in mainline kernel versions prior to v3.8 was sec=ntlm. In v3.8, the default was changed to sec=ntlmssp. </p>
<p> If the server requires signing during protocol negotiation, then it may be enabled automatically. Packet signing may also be enabled automatically if it&#8217;s enabled in /proc/fs/cifs/SecurityFlags.</dl>
<p> nobrl</p>
<dl>
<dd>Do not send byte range lock requests to the server. This is necessary for certain applications that break with cifs style mandatory byte range locks (and most cifs servers do not yet support requesting advisory byte range locks).</dl>
<p> sfu</p>
<dl>
<dd>When the CIFS Unix Extensions are not negotiated, attempt to create device files and fifos in a format compatible with Services for Unix (SFU). In addition retrieve bits 10-12 of the mode via the SETFILEBITS extended attribute (as SFU does). In the future the bottom 9 bits of the mode mode also will be emulated using queries of the security descriptor (ACL). [NB: requires version 1.39 or later of the CIFS VFS. To recognize symlinks and be able to create symlinks in an SFU interoperable form requires version 1.40 or later of the CIFS VFS kernel module.</dl>
<p> mfsymlinks</p>
<dl>
<dd>Enable support for Minshall+French symlinks(see <a rel="nofollow" href="http://wiki.samba.org/index.php/UNIX_Extensions#Minshall.2BFrench_symlinks">http://wiki.samba.org/index.php/UNIX_Extensions#Minshall.2BFrench_symlinks</a>). This option is ignored when specified together with the &#8216;sfu&#8217; option. Minshall+French symlinks are used even if the server supports the CIFS Unix Extensions.</dl>
<p> serverino</p>
<dl>
<dd>Use inode numbers (unique persistent file identifiers) returned by the server instead of automatically generating temporary inode numbers on the client. Although server inode numbers make it easier to spot hardlinked files (as they will have the same inode numbers) and inode numbers may be persistent (which is userful for some sofware), the server does not guarantee that the inode numbers are unique if multiple server side mounts are exported under a single share (since inode numbers on the servers might not be unique if multiple filesystems are mounted under the same shared higher level directory). Note that not all servers support returning server inode numbers, although those that support the CIFS Unix Extensions, and Windows 2000 and later servers typically do support this (although not necessarily on every local server filesystem). Parameter has no effect if the server lacks support for returning inode numbers or equivalent. This behavior is enabled by default.</dl>
<p> noserverino</p>
<dl>
<dd>Client generates inode numbers itself rather than using the actual ones from the server. </p>
<p> See section <i>INODE NUMBERS</i> for more information.</dl>
<p> nounix</p>
<dl>
<dd>Disable the CIFS Unix Extensions for this mount. This can be useful in order to turn off multiple settings at once. This includes POSIX acls, POSIX locks, POSIX paths, symlink support and retrieving uids/gids/mode from the server. This can also be useful to work around a bug in a server that supports Unix Extensions. </p>
<p> See section <i>INODE NUMBERS</i> for more information.</dl>
<p> nouser_xattr</p>
<dl>
<dd>Do not allow getfattr/setfattr to get/set xattrs, even if server would support it otherwise. The default is for xattr support to be enabled.</dl>
<p> rsize=<i>bytes</i></p>
<dl>
<dd>Maximum amount of data that the kernel will request in a read request in bytes. Prior to kernel 3.2.0, the default was 16k, and the maximum size was limited by the CIFSMaxBufSize module parameter. As of kernel 3.2.0, the behavior varies according to whether POSIX extensions are enabled on the mount and the server supports large POSIX reads. If they are, then the default is 1M, and the maxmimum is 16M. If they are not supported by the server, then the default is 60k and the maximum is around 127k. The reason for the 60k is because it&#8217;s the maximum size read that windows servers can fill. Note that this value is a maximum, and the client may settle on a smaller size to accomodate what the server supports. In kernels prior to 3.2.0, no negotiation is performed.</dl>
<p> wsize=<i>bytes</i></p>
<dl>
<dd>Maximum amount of data that the kernel will send in a write request in bytes. Prior to kernel 3.0.0, the default and maximum was 57344 (14 * 4096 pages). As of 3.0.0, the default depends on whether the client and server negotiate large writes via POSIX extensions. If they do, then the default is 1M, and the maximum allowed is 16M. If they do not, then the default is 65536 and the maximum allowed is 131007. </p>
<p> Note that this value is just a starting point for negotiation in 3.0.0 and up. The client and server may negotiate this size downward according to the server&#8217;s capabilities. In kernels prior to 3.0.0, no negotiation is performed. It can end up with an existing superblock if this value isn&#8217;t specified or it&#8217;s greater or equal than the existing one.</dl>
<p> fsc</p>
<dl>
<dd>Enable local disk caching using FS-Cache for CIFS. This option could be useful to improve performance on a slow link, heavily loaded server and/or network where reading from the disk is faster than reading from the server (over the network). This could also impact the scalability positively as the number of calls to the server are reduced. But, be warned that local caching is not suitable for all workloads, for e.g., read-once type workloads. So, you need to consider carefully the situation/workload before using this option. Currently, local disk caching is enabled for CIFS files opened as read-only. </p>
<p> NOTE: This feature is available only in the recent kernels that have been built with the kernel config option CONFIG_CIFS_FSCACHE. You also need to have cachefilesd daemon installed and running to make the cache operational.</dl>
<p> multiuser</p>
<dl>
<dd>Map user accesses to individual credentials when accessing the server. By default, CIFS mounts only use a single set of user credentials (the mount credentials) when accessing a share. With this option, the client instead creates a new session with the server using the user&#8217;s credentials whenever a new user accesses the mount. Further accesses by that user will also use those credentials. Because the kernel cannot prompt for passwords, multiuser mounts are limited to mounts using sec= options that don&#8217;t require passwords. </p>
<p> With this change, it&#8217;s feasible for the server to handle permissions enforcement, so this option also implies &quot;noperm&quot;. Furthermore, when unix extensions aren&#8217;t in use and the administrator has not overriden ownership using the uid= or gid= options, ownership of files is presented as the current user accessing the share.</dl>
<p> actimeo=<i>arg</i></p>
<dl>
<dd>The time (in seconds) that the CIFS client caches attributes of a file or directory before it requests attribute information from a server. During this period the changes that occur on the server remain undetected until the client checks the server again. </p>
<p> By default, the attribute cache timeout is set to 1 second. This means more frequent on-the-wire calls to the server to check whether attributes have changed which could impact performance. With this option users can make a tradeoff between performance and cache metadata correctness, depending on workload needs. Shorter timeouts mean better cache coherency, but frequent increased number of calls to the server. Longer timeouts mean a reduced number of calls to the server but looser cache coherency. The actimeo value is a positive integer that can hold values between 0 and a maximum value of 2^30 * HZ (frequency of timer interrupt) setting.</dl>
<p> noposixpaths</p>
<dl>
<dd>If unix extensions are enabled on a share, then the client will typically allow filenames to include any character besides &#8216;/&#8217; in a pathname component, and will use forward slashes as a pathname delimiter. This option prevents the client from attempting to negotiate the use of posix-style pathnames to the server.</dl>
<p> posixpaths</p>
<dl>
<dd>Inverse of <i>noposixpaths</i>.</dl>
<p> prefixpath=</p>
<dl>
<dd>It&#8217;s possible to mount a subdirectory of a share. The preferred way to do this is to append the path to the UNC when mounting. However, it&#8217;s also possible to do the same by setting this option and providing the path there.</dl>
<p> vers=</p>
<dl>
<dd>SMB protocol version. Allowed values are: </p>
<dl>
<dd>&bull; 1.0 &#8211; The classic CIFS/SMBv1 protocol. This is the default.</dl>
<dl>
<dd>&bull; 2.0 &#8211; The SMBv2.002 protocol. This was initially introduced in Windows Vista Service Pack 1, and Windows Server 2008. Note that the initial release version of Windows Vista spoke a slightly different dialect (2.000) that is not supported.</dl>
<dl>
<dd>&bull; 2.1 &#8211; The SMBv2.1 protocol that was introduced in Microsoft Windows 7 and Windows Server 2008R2.</dl>
<dl>
<dd>&bull; 3.0 &#8211; The SMBv3.0 protocol that was introduced in Microsoft Windows 8 and Windows Server 2012.</dl>
<p> Note too that while this option governs the protocol version used, not all features of each version are available.</dl>
<p> &#8211;verbose</p>
<dl>
<dd>Print additional debugging information for the mount. Note that this parameter must be specified before the -o. For example: </p>
<p> mount -t cifs //server/share /mnt &#8211;verbose -o user=username</dl>
<h2>Service Formatting And Delimiters</h2>
<p>It&#8217;s generally preferred to use forward slashes (/) as a delimiter in service names. They are considered to be the &quot;universal delimiter&quot; since they are generally not allowed to be embedded within path components on Windows machines and the client can convert them to blackslashes (\) unconditionally. Conversely, backslash characters are allowed by POSIX to be part of a path component, and can&#8217;t be automatically converted in the same way. </p>
<p> mount.cifs will attempt to convert backslashes to forward slashes where it&#8217;s able to do so, but it cannot do so in any path component following the sharename.</p>
<h2>Inode Numbers</h2>
<p>When Unix Extensions are enabled, we use the actual inode number provided by the server in response to the POSIX calls as an inode number. </p>
<p> When Unix Extensions are disabled and &quot;serverino&quot; mount option is enabled there is no way to get the server inode number. The client typically maps the server-assigned &quot;UniqueID&quot; onto an inode number. </p>
<p> Note that the UniqueID is a different value from the server inode number. The UniqueID value is unique over the scope of the entire server and is often greater than 2 power 32. This value often makes programs that are not compiled with LFS (Large File Support), to trigger a glibc EOVERFLOW error as this won&#8217;t fit in the target structure field. It is strongly recommended to compile your programs with LFS support (i.e. with -D_FILE_OFFSET_BITS=64) to prevent this problem. You can also use &quot;noserverino&quot; mount option to generate inode numbers smaller than 2 power 32 on the client. But you may not be able to detect hardlinks properly.</p>
<h2>Cache Coherency</h2>
<p>With a network filesystem such as CIFS or NFS, the client must contend with the fact that activity on other clients or the server could change the contents or attributes of a file without the client being aware of it. One way to deal with such a problem is to mandate that all file accesses go to the server directly. This is performance prohibitive however, so most protocols have some mechanism to allow the client to cache data locally. </p>
<p> The CIFS protocol mandates (in effect) that the client should not cache file data unless it holds an opportunistic lock (aka oplock) or a lease. Both of these entities allow the client to guarantee certain types of exclusive access to a file so that it can access its contents without needing to continually interact with the server. The server will call back the client when it needs to revoke either of them and allow the client a certain amount of time to flush any cached data. </p>
<p> The cifs client uses the kernel&#8217;s pagecache to cache file data. Any I/O that&#8217;s done through the pagecache is generally page-aligned. This can be problematic when combined with byte-range locks as Windows&#8217; locking is mandatory and can block reads and writes from occurring. </p>
<p> cache=none means that the client never utilizes the cache for normal reads and writes. It always accesses the server directly to satisfy a read or write request. </p>
<p> cache=strict means that the client will attempt to follow the CIFS/SMB2 protocol strictly. That is, the cache is only trusted when the client holds an oplock. When the client does not hold an oplock, then the client bypasses the cache and accesses the server directly to satisfy a read or write request. By doing this, the client avoids problems with byte range locks. Additionally, byte range locks are cached on the client when it holds an oplock and are &quot;pushed&quot; to the server when that oplock is recalled. </p>
<p> cache=loose allows the client to use looser protocol semantics which can sometimes provide better performance at the expense of cache coherency. File access always involves the pagecache. When an oplock or lease is not held, then the client will attempt to flush the cache soon after a write to a file. Note that that flush does not necessarily occur before a write system call returns. </p>
<p> In the case of a read without holding an oplock, the client will attempt to periodically check the attributes of the file in order to ascertain whether it has changed and the cache might no longer be valid. This mechanism is much like the one that NFSv2/3 use for cache coherency, but it particularly problematic with CIFS. Windows is quite &quot;lazy&quot; with respect to updating the &quot;LastWriteTime&quot; field that the client uses to verify this. The effect is that cache=loose can cause data corruption when multiple readers and writers are working on the same files. </p>
<p> Because of this, when multiple clients are accessing the same set of files, then cache=strict is recommended. That helps eliminate problems with cache coherency by following the CIFS/SMB2 protocols more strictly. </p>
<p> Note too that no matter what caching model is used, the client will always use the pagecache to handle mmap&#8217;ed files. Writes to mmap&#8217;ed files are only guaranteed to be flushed to the server when msync() is called, or on close(). </p>
<p> The default in kernels prior to 3.7 was &quot;loose&quot;. As of 3.7, the default is &quot;strict&quot;.</p>
<h2>Cifs/Ntfs Acl, Sid/Uid/Gid Mapping, Security Descriptors</h2>
<p>This option is used to work with file objects which posses Security Descriptors and CIFS/NTFS ACL instead of UID, GID, file permission bits, and POSIX ACL as user authentication model. This is the most common authentication model for CIFS servers and is the one used by Windows. </p>
<p> Support for this requires both CIFS_XATTR and CIFS_ACL support in the CIFS configuration options when building the cifs module. </p>
<p> A CIFS/NTFS ACL is mapped to file permission bits using an algorithm specified in the following Microsoft TechNet document: </p>
<dl>
<dd>&bull; <a rel="nofollow" href="http://technet.microsoft.com/en-us/library/bb463216.aspx">http://technet.microsoft.com/en-us/library/bb463216.aspx</a></dl>
<p> In order to map SIDs to/from UIDs and GIDs, the following is required: </p>
<dl>
<dd>&bull; a kernel upcall to the cifs.idmap utility set up via <a href="/docs/linux/man/5-request-key-conf/">request-key.conf</a>(5)</dl>
<dl>
<dd>&bull; winbind support configured via <a href="/docs/linux/man/5-nsswitch-conf/">nsswitch.conf</a>(5) and <a href="/docs/linux/man/5-smb-conf/">smb.conf</a>(5) </p>
</dl>
<p> Please refer to the respective manpages of <a href="/docs/linux/man/8-cifs-idmap/">cifs.idmap</a>(8) and <a href="/docs/linux/man/8-winbindd/">winbindd</a>(8) for more information. </p>
<p> Security descriptors for a file object can be retrieved and set directly using extended attribute named system.cifs_acl. The security descriptors presented via this interface are &quot;raw&quot; blobs of data and need a userspace utility to either parse and format or to assemble it such as <code><a href="/docs/linux/man/1-getcifsacl/">getcifsacl</a></code>(1) and <code><a href="/docs/linux/man/1-setcifsacl/">setcifsacl</a></code>(1) respectively. </p>
<p> Some of the things to consider while using this mount option: </p>
<dl>
<dd>&bull; There may be an increased latency when handling metadata due to additional requests to get and set security descriptors.</dl>
<dl>
<dd>&bull; The mapping between a CIFS/NTFS ACL and POSIX file permission bits is imperfect and some ACL information may be lost in the translation.</dl>
<dl>
<dd>&bull; If either upcall to cifs.idmap is not setup correctly or winbind is not configured and running, ID mapping will fail. In that case uid and gid will default to either to those values of the share or to the values of uid and/or gid mount options if specified.</dl>
<h2>Accessing Files With Backup Intent</h2>
<p>For an user on the server, desired access to a file is determined by the permissions and rights associated with that file. This is typically accomplished using owenrship and ACL. For a user who does not have access rights to a file, it is still possible to access that file for a specific or a targeted purpose by granting special rights. One of the specific purposes is to access a file with the intent to either backup or restore i.e. backup intent. The right to access a file with the backup intent can typically be granted by making that user a part of the built-in group Backup Operators. Thus, when this user attempts to open a file with the backup intent, open request is sent by setting the bit FILE_OPEN_FOR_BACKUP_INTENT as one of the CreateOptions. </p>
<p> As an example, on a Windows server, a user named testuser, cannot open this file with such a security descriptor. </p>
<p> REVISION:0x1 </p>
<p> CONTROL:0x9404 </p>
<p> OWNER:Administrator </p>
<p> GROUP:Domain Users </p>
<p> ACL:Administrator:ALLOWED/0x0/FULL </p>
<p> But the user testuser, if it becomes part of the group Backup Operators, can open the file with the backup intent. </p>
<p> Any user on the client side who can authenticate as such a user on the server, can access the files with the backup intent. But it is desirable and preferable for security reasons amongst many, to restrict this special right. </p>
<p> The mount option backupuid is used to restrict this special right to a user which is specified by either a name or an id. The mount option backupgid is used to restrict this special right to the users in a group which is specified by either a name or an id. Only users maching either backupuid or backupgid shall attempt to access files with backup intent. These two mount options can be used together.</p>
<h2>File And Directory Ownership And Permissions</h2>
<p>The core CIFS protocol does not provide unix ownership information or mode for files and directories. Because of this, files and directories will generally appear to be owned by whatever values the uid= or gid= options are set, and will have permissions set to the default file_mode and dir_mode for the mount. Attempting to change these values via chmod/chown will return success but have no effect. </p>
<p> When the client and server negotiate unix extensions, files and directories will be assigned the uid, gid, and mode provided by the server. Because CIFS mounts are generally single-user, and the same credentials are used no matter what user accesses the mount, newly created files and directories will generally be given ownership corresponding to whatever credentials were used to mount the share. </p>
<p> If the uid&#8217;s and gid&#8217;s being used do not match on the client and server, the forceuid and forcegid options may be helpful. Note however, that there is no corresponding option to override the mode. Permissions assigned to a file when forceuid or forcegid are in effect may not reflect the the real permissions. </p>
<p> When unix extensions are not negotiated, it&#8217;s also possible to emulate them locally on the server using the &quot;dynperm&quot; mount option. When this mount option is in effect, newly created files and directories will receive what appear to be proper permissions. These permissions are not stored on the server however and can disappear at any time in the future (subject to the whims of the kernel flushing out the inode cache). In general, this mount option is discouraged. </p>
<p> It&#8217;s also possible to override permission checking on the client altogether via the noperm option. Server-side permission checks cannot be overriden. The permission checks done by the server will always correspond to the credentials used to mount the share, and not necessarily to the user who is accessing the share.</p>
<h2>Environment Variables</h2>
<p>The variable <i>USER</i> may contain the username of the person to be used to authenticate to the server. The variable can be used to set both username and password by using the format username%password. </p>
<p> The variable <i>PASSWD</i> may contain the password of the person using the client. </p>
<p> The variable <i>PASSWD_FILE</i> may contain the pathname of a file to read the password from. A single line of input is read and used as the password.</p>
<h2>Notes</h2>
<p>This command may be used only by root, unless installed setuid, in which case the noeexec and nosuid mount flags are enabled. When installed as a setuid program, the program follows the conventions set forth by the mount program for user mounts, with the added restriction that users must be able to chdir() into the mountpoint prior to the mount in order to be able to mount onto it. </p>
<p> Some samba client tools like <a href="/docs/linux/man/8-smbclient/">smbclient</a>(8) honour client-side configuration parameters present in smb.conf. Unlike those client tools, <i>mount.cifs</i> ignores smb.conf completely.</p>
<h2>Configuration</h2>
<p>The primary mechanism for making configuration changes and for reading debug information for the cifs vfs is via the Linux /proc filesystem. In the directory /proc/fs/cifs are various configuration files and pseudo files which can display debug information. There are additional startup options such as maximum buffer size and number of buffers which only may be set when the kernel cifs vfs (cifs.ko module) is loaded. These can be seen by running the modinfo utility against the file cifs.ko which will list the options that may be passed to cifs during module installation (device driver load). For more information see the kernel file fs/cifs/README.</p>
<h2>Bugs</h2>
<p>Mounting using the CIFS URL specification is currently not supported. </p>
<p> The credentials file does not handle usernames or passwords with leading space. </p>
<p> Note that the typical response to a bug report is a suggestion to try the latest version first. So please try doing that first, and always include which versions you use of relevant software when reporting bugs (minimum: mount.cifs (try mount.cifs -V), kernel (see /proc/version) and server type you are trying to contact.</p>
<h2>Version</h2>
<p>This man page is correct for version 1.74 of the cifs vfs filesystem (roughly Linux kernel 3.0).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-cifs-upcall/">cifs.upcall</a></code>(8), <code><a href="/docs/linux/man/1-getcifsacl/">getcifsacl</a></code>(1), <code><a href="/docs/linux/man/1-setcifsacl/">setcifsacl</a></code>(1) </p>
<p> Documentation/filesystems/cifs.txt and fs/cifs/README in the linux kernel source tree may contain additional options and information.</p>
<h2>Author</h2>
<p>Steve French </p>
<p> The syntax and manpage were loosely based on that of smbmount. It was converted to Docbook/XML by Jelmer Vernooij. </p>
<p> The maintainer of the Linux cifs vfs and the userspace tool <i>mount.cifs</i> is Steve French. The Linux CIFS Mailing list is the preferred place to ask questions regarding these programs.</p>
