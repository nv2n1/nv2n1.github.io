---
title: "mount-davfs(8)"
name: "mount-davfs"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mount-davfs/"
description: "mount.davfs – Mount a WebDAV resource in a directory"
---

<p>mount.davfs &#8211; Mount a WebDAV resource in a directory </p>
<h2>Synopsis</h2>
<p><code>mount.davfs [-h | &#8211;help] [-V | &#8211;version]</code><br />
 <code>mount {</code><i>dir</i><code> | </code><i>webdavserver</i><code>}</code> </p>
<h2>SYNOPSIS (root only)</h2>
<p><code>mount -t davfs [-o </code><i>option</i><code>[,&#8230;]]</code><i> webdavserver dir</i><br />
 <code>mount.davfs [-o </code><i>option</i><code>[,&#8230;]]</code><i> webdavserver dir</i></p>
<h2>Description</h2>
<p><code>mount.davfs</code> allows you to mount the WebDAV resource identified by <i>webdavserver</i> into the local filesystem at <i>dir.</i> WebDAV is an extension to HTTP that allows remote, collaborative authoring of Web resources, defined in RFC 4918. <code>mount.davfs</code> is part of <code>davfs2</code>. <code>davfs2</code> allows documents on a remote Web server to be edited using standard applications. For example, a remote Web site could be updated in-place using the same development tools that initially created the site. Or you may use a WebDAV resource for documents you want to access and edited from different locations. <code>davfs2</code> supports <code>TLS/SSL</code> (if the neon library supports it) and proxies. <code>mount.davfs</code> runs as a daemon in userspace. It integrates into the virtual file system by either the coda or the fuse kernel files system. Currently CODA_KERNEL_VERSION 3 and FUSE_KERNEL_VERSION 7 are supported. <code>mount.davfs</code> is usually invoked by the <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8) command when using the <i>-t davfs</i> option. After mounting it runs as a daemon. To unmount the <code><a href="/docs/linux/man/8-umount/">umount</a></code>(8) command is used. <i>webdavserver</i> is the URL of the server. It must at least contain the host name. It may additionally contain the scheme, the port and the path. Missing components are set to sensible default values. The path component must <code>not</code> be %-encoded, but when entering the URL at the command line or in /etc/fstab the escaping rules of the shell or fstab must be obeyed. <i>dir</i> is the mountpoint where the WebDAV resource is mounted on. It may be an absolute or relative path. <i>fstab</i> may be used to define mounts and mount options as usual. In place of the device the url of the WebDAV server must be given. There must not be more than one entry in <i>fstab</i> for every mountpoint. </p>
<h2>Options</h2>
<dl>
<dt><code>-V &#8211;version</code></p>
<dd>Output version. </p>
<dt><code>-h &#8211;help</code></p>
<dd>Print a help message. </p>
<dt><code>-o</code></p>
<dd>A comma-separated list defines mount options to be used. Available options are: </p>
<dl>
<dd>
<dl>
<dt><code>[no]auto</code></p>
<dd>Can (not) be mounted with <code>mount -a</code>.<br />
 Default: <code>auto</code>. </p>
<dt><code>conf=</code><i>absolute path</i></p>
<dd>An alternative user configuration file. This option is intended for cases where the default user configuration file in the users home directory can not be used.<br />
 Default: <i>~/.davfs2/davfs2.conf</i> </p>
<dt><code>[no]dev</code></p>
<dd>(Do not) interpret character or block special devices on the file system. This option is only included for compatibility with the <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8) program. It will allways be set to <code>nodev</code> </p>
<dt><code>dir_mode=</code><i>mode</i></p>
<dd>The default mode bits for directories in the mounted file system. Value given in octal. s-bits for user and group are allways silently ignored.<br />
 Default: calculated from the umask of the mounting user; an x-bit is associated to every r-bit in u-g-o. </p>
<dt><code>[no]exec</code></p>
<dd>(Do not) allow execution of any binaries on the mounted file system.<br />
 Default: <code>exec</code>. (When mounting as an ordinary user, the <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8) program will set the default to <code>noexec</code>.) </p>
<dt><code>file_mode=</code><i>mode</i></p>
<dd>The default mode bits for files in the mounted file system. Value given in octal. s-bits for user and group are allways silently ignored.<br />
 Default: calculated from the umask of the mounting user; no x-bits are set for files. </p>
<dt><code>gid=</code><i>group</i></p>
<dd>The group the mounted file system belongs to. It may be a numeric ID or a group name. The mounting user, if not root, must be member of this group.<br />
 Default: the primary group of the mounting user. </p>
<dt><code>[no]_netdev</code></p>
<dd>The file system needs a (no) network connection for operation. This information allows the operating system to handle the file system properly at system start and when the network is shut down.<br />
 Default: <code>_netdev</code> </p>
<dt><code>ro</code></p>
<dd>Mount the file system read-only.<br />
 Default: <code>rw</code>. </p>
<dt><code>rw</code></p>
<dd>Mount the file system read-write.<br />
 Default: <code>rw</code>. </p>
<dt><code>[no]suid</code></p>
<dd>Do not allow set-user-identifier or set-group-identifier bits to take effect. This option is only included for compatibility with the mount program. It will allways be set to <code>nosuid</code>. </p>
<dt><code>[no]user</code></p>
<dd>(Do not) allow an ordinary user to mount the file system. The name of the mounting user is written to <i>mtab</i> so that he can unmount the file system again. Option <code>user</code> implies the options <code>noexec</code>, <code>nosuid</code> and <code>nodev</code> (unless overridden by subsequent options). This option makes only sense when set in <i>fstab</i>.<br />
 Default: ordinary users are not allowed to mount. </p>
<dt><code>users</code></p>
<dd>Like <code>user</code>, but <code>any</code> user is allowed to unmount the file system, not only the mounting user. This is generally not recomended. On systems with no <i>mtab</i> file with the <code>user</code> option unmounting by the mounting user will fail. In this case the <code>users</code> may be an appropriate work around.<br />
 Default: only the mounting user is allowed to unmount the file system. </p>
<dt><code>uid=</code><i>user</i></p>
<dd>The owner of the mounted file system. It may be a numeric ID or a user name. Only when mounted by root, this may be different from the mounting user.<br />
 Default: ID of the mounting user.</dl>
</dl>
<dt><code>username=</code><i>WebDAV_user</i></p>
<dd>Use this name to authenticate with the WebDAV server. This option is intended for use with pam_mount only. When this option is set the credentials in the secrets files will be ignored. The password will always be read from stdin, even when option <i>askauth</i> is set to 0. Do not use it in <i>fstab</i>. The username will be visible for everyone in the output of <i>ps</i>.<br />
 Default: no username.<br />
 <code>Experimental:</code> This option is experimental and might be removed. If you think it useful and successfully use it please send a short report. </p>
</dl>
<h2>Security Policy</h2>
<p><code>mount.davfs</code> needs root privileges for mounting. But running a daemon, that is connected to the internet, with root privileges is a security risk. So <code>mount.davfs</code> will change its uid and gid when entering daemon mode. </p>
<dl>
<dd>When invoked by root <code>mount.davfs</code> will run as user <code>davfs2</code> and group <code>davfs2</code>. This may be changed in <i>/etc/davfs2/davfs2.conf</i>. </p>
<p> When invoked by an ordinary user it will run with the id of this user and with group <code>davfs2</code>.</dl>
<p> As the file system may be mounted over an insecure internet connection, this increases the risk that malicious content may be included in the file system. So <code>mount.davfs</code> is slightly more restrictive than <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8). </p>
<dl>
<dd>Options <code>nosuid</code> and <code>nodev</code> will always be set; even root can not change this. </p>
<p> For ordinary users to be able to mount, they must be member of group <code>davfs2</code> and there must be an entry in <i>fstab</i>. </p>
<p> When the mount point given in <i>fstab</i> is a relative file name and the file system is mounted by an unprivileged user, the mount point must lie within the home directory of the mounting user. </p>
<p> If in <i>fstab</i> option <code>uid</code> and/or <code>gid</code> are given, an ordinary user can only mount, if her uid is the one given in option <code>uid</code> and he belongs to the group given in option <code>gid</code>.</dl>
<p> <code>WARNING:</code> If root allows an ordinary user to mount a file system (using <i>fstab</i>) this includes the permission to read the associated <code>credentials</code> from <i>/etc/davfs2/secrets</i> as well as the <code>private key</code> of the associated <code>client certificate</code> and the mounting user may get access to this information. You should only do this, if you might as well give this information to the user directly.</p>
<h2>Urls And Mount Points With Spaces</h2>
<p>Special characters like spaces in pathnames are a mess. They are interpreted differently by different programs and protocols, and there are different rules for escaping. </p>
<p> In <i>fstab</i> spaces must be replaced by a three digit octal escape sequence. Write <i><a rel="nofollow" href="http://foo.bar/path with spaces">http://foo.bar/path with spaces</a></i> instead of <i><a rel="nofollow" href="http://foo.bar/path">http://foo.bar/path</a> with spaces</i>. It might also be necessary to replace the &#8216;#&#8217;-character by #. </p>
<p> For the <i>davfs2.conf</i> and the <i>secrets</i> files please see the escape and quotation rules described in the <code><a href="/docs/linux/man/5-davfs2-conf/">davfs2.conf</a></code>(5) man page. </p>
<p> On <i>command line</i> you must obey the escaping rules of the shell.</p>
<h2>Caching</h2>
<p><code>mount.davfs</code> tries to reduce HTTP-trafic by caching and reusing data. Information about directories and files are held in memory, while downloaded files are cached on disk. </p>
<p> <code>mount.davfs</code> will consider cached information about directories and file attributes valid for a configurable time and look up this information on the server only after this time has expired (or there is other evidence that this information is stale). So if somebody else creates or deletes files on the server it may take some time before the local file system reflects this. </p>
<p> This will not affect the content of files and directory listings. Whenever a file is opened, the server is looked up for a newer version of the file. Please consult the manual <code><a href="/docs/linux/man/5-davfs2-conf/">davfs2.conf</a></code>(5) to see how can you configure this according your needs.</p>
<h2>Locks, Lost Update Problem And Backup Files</h2>
<p>WebDAV introduced locks and <code>mount.davfs</code> uses them by default. This will in most cases prevent two people from changing the same file in parallel. But not allways: </p>
<dl>
<dd>You might have disabled locks in <i>/etc/davfs2/davfs2.conf</i> or <i>~/.davfs2/davfs2.conf</i>. </p>
<p> The server might not support locks (they are not mandatory). </p>
<p> A bad connection might prevent <code>mount.davfs</code> from refreshing the lock in time. </p>
<p> Another WebDAV-client might use your lock (that is not too difficult and might even happen without intention).</dl>
<p> <code>mount.davfs</code> will therefore check if the file has been changed on the the server before it uploads a new version. If it finds it impossible to upload the locally changed file, it will store it in the local backup direcotry <i>lost+found</i>. You should check this directory from time to time and decide what to do with this files. </p>
<p> Sometimes locks held by some client on the server will not be released. Maybe the client crashes or the network connection fails. When <code>mount.davfs</code> finds a file locked on the server, it will check whether the lock is held by <code>mount.davfs</code> and the current user, and if so tries to reuse and release it. But this will not allways succeed. So servers should automatically release locks after some time, when they are not refreshed by the client. </p>
<p> WebDAV allows to lock files that don&#8217;t exist (to protect the name when a client intends to create a new file). This locks will be displayed as files with size 0 and last modified date of 1970-01-01. If this locks are not released properly <code>mount.davfs</code> may not be able to access this files. You can use <code><a href="/docs/linux/man/1-cadaver/">cadaver</a></code>(1) &lt;<i><a rel="nofollow" href="http://www.webdav.org/cadaver/">http://www.webdav.org/cadaver/</a></i>&gt; to remove this locks.</p>
<h2>File Owner And Permissions</h2>
<p><code>davfs2</code> implements Unix permissions for access control. But changing owner and permissions of a file is only <code>local</code>. It is intended as a means for the owner of the file system, to controll whether other local users may acces this file system. </p>
<p> The server does not know about this. From the servers point of view there is just one user (identified by the credentials) connected. Another WebDAV-client, connected to the same server, is not affected by this local changes. </p>
<p> There is one exeption: The <code>execute bit</code> on files is stored as a property on the sever. You may think of this property as an information about the type of file rather than a permission. Whether the file is executable on the local system is still controlled by mount options and local permissions. </p>
<p> When the file system is unmounted, attributes of cached files (including owner and permissions) are stored in cache, as well as the attributs of the direcotries they are in. But there is no information stored about directories that do not contain cached files.</p>
<h2>Files</h2>
<dl>
<dt><i>/etc/davfs2/davfs2.conf</i></p>
<dd>System wide configuration file. </p>
<dt><i>~/.davfs2/davfs2.conf</i></p>
<dd>Configuration file in the users home directory.The user configuration takes precedence over the system wide configuration. If it does not exist, <code>mount.davfs</code> will will create a template file. </p>
<dt><i>/etc/davfs2/secrets</i></p>
<dd>Holds the credentials for WebDAV servers and the proxy, as well as decryption passwords for client certificates. The file must be read-writable by root only. </p>
<dt><i>~/.davfs2/secrets</i></p>
<dd>Holds credentials for WebDAV servers and proxy, as well as decryption passwords for client certificates. The file must be read-writable by the owner only. Credentials are first looked up in the home directory of the mounting user. If not found there the system wide secrets file is consulted. If no creditentials and passwords are found they are asked from the user interactively (if not disabled). If the file does not exist, <code>mount.davfs</code> will will create a template file. </p>
<dt><i>/etc/davfs2/certs</i></p>
<dd>You may store trusted server certificates here, that can not be verified by use of the system wide CA-Certificates. This is useful when your server uses a selfmade certificate. You must configure the <code>servercert</code> option in <i>/etc/davfs2/davfs2.conf</i> or <i>~/.davfs2/davfs2.conf</i> to use it. Certificates must be in PEM format.<br />
 Be sure to verify the certificate. </p>
<dt><i>~/.davfs2/certs</i></p>
<dd>You may store trusted server certificates here, that can not be verified by use of the system wide CA-Certificates. This is useful when your server uses a selfmade certificate. You must configure the <code>servercert</code> option in <i>~/.davfs2/davfs2.conf</i> to use it. Certificates must be in PEM format.<br />
 Be sure to verify the certificate. </p>
<dt><i>/etc/davfs2/certs/private</i></p>
<dd>To store client certificates. Certificates must be in PKCS#12 format. You must configure the <code>clientcert</code> option in <i>/etc/davfs2/davfs2.conf</i> or <i>~/.davfs2/davfs2.conf</i> to use it. This directory must be rwx by root only. </p>
<dt><i>~/.davfs2/certs/private</i></p>
<dd>To store client certificates. Certificates must be in PKCS#12 format. You must configure the <code>clientcert</code> option in <i>~/.davfs2/davfs2.conf</i> to use it. This directory must be rwx by the owner only. </p>
<dt><i>/var/run/mount.davfs</i></p>
<dd>PID-files of running mount.davfs processes are stored there. This directory must belong to group <code>davfs2</code> with write permissions for the group and the sticky-bit set (mode 1775). The PID-files are named after the mount point of the file system. </p>
<dt><i>/var/cache/davfs2</i></p>
<dd>System wide directory for cached files. Used when the file system is mounted by root. It must belong do group <code>davfs2</code> and read, write and execute bits for group must be set. There is a subdirectory for every mounted file system. The names of this subdirectories are created from url, mount point and user name. </p>
<dt><i>~/.davfs2/cache</i></p>
<dd>Cache directory in the mounting users home directory. For every mounted WebDAV resource a subdirectory is created. </p>
<p> <code>mount.davfs</code> will try to create missing directories, but it will <code>not</code> touch <i>/etc/davfs2</i>. </p>
</dl>
<h2>Environment</h2>
<dl>
<dt><code>https_proxy http_proxy all_proxy</code></p>
<dd>If no proxy is defined in the configuration file the value is taken from this environment variables. The proxy may be given with or without scheme and with or without port<br />
 http_proxy=[<a rel="nofollow" href="http://]foo.bar[:3218]">http://]foo.bar[:3218]</a><br />
 Only used when the mounting user is root. </p>
<dt><code>no_proxy</code></p>
<dd>A comma separated list of domain names that shall be accessed directly. <code>*</code> matches any domain name. A domain name starting with <code>.</code> (period) matches all subdomains.<br />
 Only used when the mounting user is root.<br />
 Not applied when the proxy is defined in <i>/etc/davfs2</i>. </p>
</dl>
<h2>Examples</h2>
<p><code>Non root user (e.g. filomena):</code> To allow an ordinary user to mount there must be an entry in <i>fstab</i></p>
<dl>
<dd><a rel="nofollow" href="http://webdav.org/dav">http://webdav.org/dav</a> /media/dav davfs noauto,user 0 0</dl>
<p> If a proxy must be used this should be configured in <i>/etc/davfs2/davfs2.conf</i></p>
<dl>
<dd>proxy proxy.mycompany.com:8080</dl>
<p> Credentials are stored in <i>/home/filomena/.davfs2/secrets</i></p>
<dl>
<dd>proxy.mycompany.com filomena &quot;my secret&quot;<br />
 /media/dav webdav-username password</dl>
<p> Now the WebDAV resource may be mounted by user filomena invoking</p>
<dl>
<dd><code>mount /media/dav</code></dl>
<p> and unmounted by user filomena invoking</p>
<dl>
<dd><code>umount /media/dav</code></dl>
<p> <code>Root user only:</code> Mounts the resource <i><a rel="nofollow" href="https://asciigirl.com/webdav">https://asciigirl.com/webdav</a></i> at mount point <i>/mount/site</i>, encrypting all traffic with SSL. Credentials for <i><a rel="nofollow" href="http://webdav.org/dav">http://webdav.org/dav</a></i> will be looked up in <i>/etc/davfs2/secrets</i>, if not found there the user will be asked.</p>
<dl>
<dd><code>mount -t davfs -o uid=otto,gid=users,mode=775 <a rel="nofollow" href="https://asciigirl.com/webdav">https://asciigirl.com/webdav</a> /mount/site</code></dl>
<p> Mounts the resource <i><a rel="nofollow" href="http://linux.org.ar/repos">http://linux.org.ar/repos</a></i> at <i>/dav</i>.</p>
<dl>
<dd><code>mount.davfs -o uid=otto,gid=users,mode=775 <a rel="nofollow" href="http://linux.org.ar/repos/">http://linux.org.ar/repos/</a> /dav</code></dl>
<h2>Bugs</h2>
<p><code>davfs2</code> does not support links. A <code>davfs2</code> file system cannot be moved with <i>mount &#8211;move</i>. </p>
<h2>Authors</h2>
<p>This man page was written by Luciano Bello &lt;luciano [at] linux.org.ar&gt; for Debian, for version 0.2.3 of davfs2. </p>
<p> It has been updated for this version by Werner Baumann &lt;werner.baumann [at] onlinhome.de&gt;. </p>
<p> davfs2 is developed by Sung Kim &lt;hunkim [at] gmail.com&gt;. </p>
<p> Version 1.0.0 (and later) of davfs2 is a complete rewrite by Werner Baumann.</p>
<h2>Davfs2 Home</h2>
<p><a rel="nofollow" href="http://savannah.nongnu.org/projects/davfs2">http://savannah.nongnu.org/projects/davfs2</a></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-umount-davfs/">umount.davfs</a></code>(8), <code><a href="/docs/linux/man/5-davfs2-conf/">davfs2.conf</a></code>(5), <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8), <code><a href="/docs/linux/man/8-umount/">umount</a></code>(8), <code><a href="/docs/linux/man/5-fstab/">fstab</a></code>(5) </p>
