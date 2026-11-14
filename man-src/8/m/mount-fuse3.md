---
title: "mount-fuse3(8)"
name: "mount-fuse3"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mount-fuse3/"
description: "fuse – configuration and mount options for FUSE file systems"
---

<p>fuse &#8211; configuration and mount options for FUSE file systems</p>
<h2>Description</h2>
<p>FUSE (Filesystem in Userspace) is a simple interface for userspace programs to export a virtual filesystem to the Linux kernel. FUSE also aims to provide a secure method for non privileged users to create and mount their own filesystem implementations.</p>
<h2>Definitions</h2>
<dl>
<dt><code>FUSE</code></p>
<dd>The in-kernel filesystem that forwards requests to a user-space process.</p>
<dt><code>filesystem</code></p>
<dd>The user-space process that responds to requests received from the kernel.</p>
<dt><code>libfuse</code></p>
<dd>The shared library that most (user-space) filesystems use to communicate with FUSE (the kernel filesystem). libfuse also provides the <code>fusermount3</code> (or <code>fusermount</code> if you have older version of libfuse) helper to allow non-privileged users to mount filesystems.</p>
<dt><code>filesystem owner</code></p>
<dd>The user that starts the filesystem and instructs the kernel to associate it with a particular mountpoint. The latter is typically done by the filesystem itself on start-up. When using libfuse, this is done by calling the <code>fusermount3</code> utility.</p>
<dt><code>client</code></p>
<dd>Any process that interacts with the mountpoint.</dl>
<h2>Configuration</h2>
<p>Some options regarding mount policy can be set in the file <i>/etc/fuse.conf</i>. Currently these options are:</p>
<dl>
<dt><code>mount_max = NNN</code></p>
<dd>Set the maximum number of FUSE mounts allowed to non-root users. The default is 1000.</p>
<dt><code>user_allow_other</code></p>
<dd>Allow non-root users to specify the <code>allow_other</code> or <code>allow_root</code> mount options (see below).</p>
<dt>These limits are enforced by the <code>fusermount3</code> helper, so they can be avoided by filesystems that run as root.</p>
<dd></dl>
<h2>Options</h2>
<p>Most of the generic mount options described in <code>mount</code> are supported (<code>ro</code>, <code>rw</code>, <code>suid</code>, <code>nosuid</code>, <code>dev</code>, <code>nodev</code>, <code>exec</code>, <code>noexec</code>, <code>atime</code>, <code>noatime</code>, <code>sync</code>, <code>async</code>, <code>dirsync</code>). Filesystems are mounted with <code>nodev,nosuid</code> by default, which can only be overridden by a privileged user.</p>
<h3>General mount options:</h3>
<p>These are FUSE specific mount options that can be specified for all filesystems:</p>
<dl>
<dt><code>default_permissions</code></p>
<dd>This option instructs the kernel to perform its own permission check instead of deferring all permission checking to the filesystem. The check by the kernel is done in addition to any permission checks by the filesystem, and both have to succeed for an operation to be allowed. The kernel performs a standard UNIX permission check (based on mode bits and ownership of the directory entry, and uid/gid of the client). </p>
<p> This mount option is activated implicitly if the filesystem enables ACL support during the initial feature negotiation when opening the device fd. In this case, the kernel performs both ACL and standard unix permission checking. </p>
<p> Filesystems that do not implement any permission checking should generally add this option internally.</p>
<dt><code>allow_other</code></p>
<dd>This option overrides the security measure restricting file access to the filesystem owner, so that all users (including root) can access the files.</p>
<dt><code>rootmode=M</code></p>
<dd>Specifies the file mode of the filesystem&#8217;s root (in octal representation).</p>
<dt><code>blkdev</code></p>
<dd>Mount a filesystem backed by a block device. This is a privileged option. The device must be specified with the <code>fsname=NAME</code> option.</p>
<dt><code>blksize=N</code></p>
<dd>Set the block size for the filesystem. This option is only valid for &#8216;fuseblk&#8217; type mounts. The default is 512. </p>
<p> In most cases, this option should not be specified by the filesystem owner but set internally by the filesystem.</p>
<dt><code>max_read=N</code></p>
<dd>With this option the maximum size of read operations can be set. The default is infinite, but typically the kernel enforces its own limit in addition to this one. A value of zero corresponds to no limit. </p>
<p> This option should not be specified by the filesystem owner. The correct (or optimum) value depends on the filesystem implementation and should thus be set by the filesystem internally. </p>
<p> This mount option is deprecated in favor of direct negotiation over the device fd (as done for e.g. the maximum size of write operations). For the time being, libfuse-using filesystems that want to limit the read size must therefore use this mount option <i>and</i> set the same value again in the init() handler.</p>
<dt><code>fd=N</code></p>
<dd>The file descriptor to use for communication between the userspace filesystem and the kernel. The file descriptor must have been obtained by opening the FUSE device (/dev/fuse). </p>
<p> This option should not be specified by the filesystem owner. It is set by libfuse (or, if libfuse is not used, must be set by the filesystem itself).</p>
<dt><code>user_id=N</code></p>
<dd><code>group_id=N</code> Specifies the numeric uid/gid of the mount owner. </p>
<p> This option should not be specified by the filesystem owner. It is set by libfuse (or, if libfuse is not used, must be set by the filesystem itself).</p>
<dt><code>fsname=NAME</code></p>
<dd>Sets the filesystem source (first field in <i>/etc/mtab</i>). The default is the name of the filesystem process.</p>
<dt><code>subtype=TYPE</code></p>
<dd>Sets the filesystem type (third field in <i>/etc/mtab</i>). The default is the name of the filesystem process. If the kernel supports it, <i>/etc/mtab</i> and <i>/proc/mounts</i> will show the filesystem type as <code>fuse.TYPE</code> </p>
<p> If the kernel doesn&#8217;t support subtypes, the source field will be <code>TYPE#NAME</code>, or if <code>fsname</code> option is not specified, just <code>TYPE</code>. </p>
</dl>
<h3>libfuse-specific mount options:</h3>
<p>These following options are not actually passed to the kernel but interpreted by libfuse. They can be specified for all filesystems that use libfuse:</p>
<dl>
<dt><code>allow_root</code></p>
<dd>This option is similar to <code>allow_other</code> but file access is limited to the filesystem owner and root. This option and <code>allow_other</code> are mutually exclusive.</p>
<dt><code>auto_unmount</code></p>
<dd>This option enables automatic release of the mountpoint if filesystem terminates for any reason. Normally the filesystem is responsible for releasing the mountpoint, which means that the mountpoint becomes inaccessible if the filesystem terminates without first unmounting. </p>
<p> At the moment, this option implies that the filesystem will also be mounted with <code>nodev</code> and <code>nosuid</code> (even when mounted by root). This restriction may be lifted in the future. </p>
</dl>
<h3>High-level mount options:</h3>
<p>These following options are not actually passed to the kernel but interpreted by libfuse. They can only be specified for filesystems that use the high-level libfuse API:</p>
<dl>
<dt><code>kernel_cache</code></p>
<dd>This option disables flushing the cache of the file contents on every <code><a href="/docs/linux/man/2-open/">open</a></code>(2). This should only be enabled on filesystems, where the file data is never changed externally (not through the mounted FUSE filesystem). Thus it is not suitable for network filesystems and other &quot;intermediate&quot; filesystems. </p>
<p> <code>NOTE</code>: if this option is not specified (and neither <code>direct_io</code>) data is still cached after the <code><a href="/docs/linux/man/2-open/">open</a></code>(2), so a <code><a href="/docs/linux/man/2-read/">read</a></code>(2) system call will not always initiate a read operation.</p>
<dt><code>auto_cache</code></p>
<dd>This option is an alternative to <code>kernel_cache</code>. Instead of unconditionally keeping cached data, the cached data is invalidated on <code><a href="/docs/linux/man/2-open/">open</a></code>(2) if the modification time or the size of the file has changed since it was last opened.</p>
<dt><code>umask=M</code></p>
<dd>Override the permission bits in <i>st_mode</i> set by the filesystem. The resulting permission bits are the ones missing from the given umask value. The value is given in octal representation.</p>
<dt><code>uid=N</code></p>
<dd>Override the <i>st_uid</i> field set by the filesystem (N is numeric).</p>
<dt><code>gid=N</code></p>
<dd>Override the <i>st_gid</i> field set by the filesystem (N is numeric).</p>
<dt><code>entry_timeout=T</code></p>
<dd>The timeout in seconds for which name lookups will be cached. The default is 1.0 second. For all the timeout options, it is possible to give fractions of a second as well (e.g. <code>entry_timeout=2.8</code>)</p>
<dt><code>negative_timeout=T</code></p>
<dd>The timeout in seconds for which a negative lookup will be cached. This means, that if file did not exist (lookup returned <code>ENOENT</code>), the lookup will only be redone after the timeout, and the file/directory will be assumed to not exist until then. The default is 0.0 second, meaning that caching negative lookups are disabled.</p>
<dt><code>attr_timeout=T</code></p>
<dd>The timeout in seconds for which file/directory attributes are cached. The default is 1.0 second.</p>
<dt><code>ac_attr_timeout=T</code></p>
<dd>The timeout in seconds for which file attributes are cached for the purpose of checking if <code>auto_cache</code> should flush the file data on open. The default is the value of <code>attr_timeout</code></p>
<dt><code>noforget</code></p>
<dd>
<dt><code>remember=T</code></p>
<dd>Normally, libfuse assigns inodes to paths only for as long as the kernel is aware of them. With this option inodes are instead assigned for at least <code>T</code> seconds (or, in the case of <code>noforget</code>, the life-time of the filesystem). This will require more memory, but may be necessary when using applications that make use of inode numbers.</p>
<dt><code>modules=M1[:M2&#8230;]</code></p>
<dd>Add modules to the filesystem stack. Modules are pushed in the order they are specified, with the original filesystem being on the bottom of the stack. </p>
</dl>
<h3><code>mount.fuse3</code> options:</h3>
<p>These options are interpreted by <code>mount.fuse3</code> and are thus only available when mounting a file system via <code>mount.fuse3</code> (such as when mounting via the generic <code><a href="/docs/linux/man/1-mount/">mount</a></code>(1) command or <i>/etc/fstab</i>). Supported options are:</p>
<dl>
<dt><code>setuid=USER</code></p>
<dd>Switch to <code>USER</code> and its primary group before launching the FUSE file system process. mount.fuse3 must be run as root or with <code>CAP_SETUID</code> and <code>CAP_SETGID</code> for this to work.</p>
<dt><code>drop_privileges</code></p>
<dd>Perform setup of the FUSE file descriptor and mounting the file system before launching the FUSE file system process. <code>mount.fuse3</code> requires privilege to do so, i.e. must be run as root or at least with <code>CAP_SYS_ADMIN</code> and <code>CAP_SETPCAP</code>. It will launch the file system process fully unprivileged, i.e. without <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7) and <code><a href="/docs/linux/man/2-prctl/">prctl</a></code>(2) flags set up such that privileges can&#8217;t be reacquired (e.g. via setuid or fscaps binaries). This reduces risk in the event of the FUSE file system process getting compromised by malicious file system data. </p>
</dl>
<h2>Fuse Modules (Stacking)</h2>
<p>Modules are filesystem stacking support to high level API. Filesystem modules can be built into libfuse or loaded from shared object</p>
<h3>iconv</h3>
<p>Perform file name character set conversion. Options are:</p>
<dl>
<dt><code>from_code=CHARSET</code></p>
<dd>Character set to convert from (see <code>iconv -l</code> for a list of possible values). Default is <code>UTF-8</code>.</p>
<dt><code>to_code=CHARSET</code></p>
<dd>Character set to convert to. Default is determined by the current locale.</dl>
<h3>subdir</h3>
<p>Prepend a given directory to each path. Options are:</p>
<dl>
<dt><code>subdir=DIR</code></p>
<dd>Directory to prepend to all paths. This option is <i>mandatory</i>.</p>
<dt><code>rellinks</code></p>
<dd>Transform absolute symlinks into relative</p>
<dt><code>norellinks</code></p>
<dd>Do not transform absolute symlinks into relative. This is the default.</dl>
<h2>Security</h2>
<p>The fusermount3 program is installed set-user-gid to fuse. This is done to allow users from fuse group to mount their own filesystem implementations. There must however be some limitations, in order to prevent Bad User from doing nasty things. Currently those limitations are:</p>
<dl>
<dt>1.</p>
<dd>The user can only mount on a mountpoint, for which it has write permission</p>
<dt>2.</p>
<dd>The mountpoint is not a sticky directory which isn&#8217;t owned by the user (like <i>/tmp</i> usually is)</p>
<dt>3.</p>
<dd>No other user (including root) can access the contents of the mounted filesystem.</dl>
<h2>Note</h2>
<p>FUSE filesystems are unmounted using the <code><a href="/docs/linux/man/1-fusermount3/">fusermount3</a></code>(1) command (<code>fusermount3 -u mountpoint</code>).</p>
<h2>Authors</h2>
<p>FUSE is currently maintained by Nikolaus Rath &lt;Nikolaus [at] rath.org&gt; </p>
<p> The original author of FUSE is Miklos Szeredi &lt;mszeredi [at] inf.bme.hu&gt;. </p>
<p> This man page was originally written by Bastien Roucaries &lt;roucaries.bastien+debian [at] gmail.com&gt; for the Debian GNU/Linux distribution.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-fusermount3/">fusermount3</a></code>(1) <code><a href="/docs/linux/man/1-fusermount/">fusermount</a></code>(1) <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8) <code><a href="/docs/linux/man/4-fuse/">fuse</a></code>(4) </p>
