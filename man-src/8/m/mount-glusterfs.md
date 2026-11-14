---
title: "mount-glusterfs(8)"
name: "mount-glusterfs"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mount-glusterfs/"
description: "mount.glusterfs – script to mount native GlusterFS volume"
---

<p><code>mount.glusterfs &#8211; script to mount native GlusterFS volume</code></p>
<h2>Synopsis</h2>
<p><code>mount -t glusterfs [-o &lt;options&gt;] &lt;volumeserver&gt;:/&lt;volume&gt;</code> <code>&lt;mountpoint&gt;</code></p>
<dl>
<dt><code>mount -t glusterfs [-o &lt;options&gt;] &lt;server1&gt;,&lt;server2&gt;,</code></p>
<dd><code>&lt;server3&gt;,..&lt;serverN&gt;:/&lt;volname&gt; &lt;mount_point&gt;</code></p>
<dt>
<dt><code>mount -t glusterfs [-o &lt;options&gt;] &lt;path/to/volumefile&gt; &lt;mountpoint&gt;</code></p>
<dd>
<dd></dl>
<h2>Description</h2>
<p>This tool is part of <code><a href="/docs/linux/man/8-glusterfs/">glusterfs</a></code>(8) package, which is used to mount using GlusterFS native binary. <code>mount.glusterfs</code> is meant to be used by the <a href="/docs/linux/man/8-mount/">mount</a>(8) command for mounting native GlusterFS client. This subcommand, however, can also be used as a standalone command with limited functionality. </p>
<h2>Options</h2>
<h3>Basic options</h3>
<dl>
<dt><code>log-file=</code>LOG-FILE</p>
<dd>File to use for logging [default:/var/log/glusterfs/glusterfs.log]</p>
<dt><code>log-level=</code>LOG-LEVEL</p>
<dd>Logging severity. Valid options are TRACE, DEBUG, WARNING, ERROR, CRITICAL INFO and NONE [default: INFO]</p>
<dt><code>acl</p>
<dd>Mount the filesystem with POSIX ACL support</p>
<dt>fopen-keep-cache</p>
<dd>Do not purge the cache on file open</p>
<dt>worm</p>
<dd>Mount the filesystem in &#8216;worm&#8217; mode</p>
<dt>aux-gfid-mount</p>
<dd>Enable access to filesystem through gfid directly</p>
<dt>ro</code></p>
<dd>Mount the filesystem read-only</p>
<dt><code>enable-ino32=</code>BOOL</p>
<dd>Use 32-bit inodes when mounting to workaround broken applications that don&#8217;t support 64-bit inodes</p>
<dt><code>mem-accounting</p>
<dd>Enable internal memory accounting</p>
<dt>capability</p>
<dd>Enable file capability setting and retrival </p>
</dl>
<p> </code></p>
<h3>Advanced options</h3>
<dl>
<dt><code>attribute-timeout=</code>SECONDS</p>
<dd>Set attribute timeout to SECONDS for inodes in fuse kernel module [default: 1]</p>
<dt><code>entry-timeout=</code>SECONDS</p>
<dd>Set entry timeout to SECONDS in fuse kernel module [default: 1]</p>
<dt><code>background-qlen=</code>N</p>
<dd>Set fuse module&#8217;s background queue length to N [default: 64]</p>
<dt><code>gid-timeout=</code>SECONDS</p>
<dd>Set auxiliary group list timeout to SECONDS for fuse translator [default: 0]</p>
<dt><code>negative-timeout=</code>SECONDS</p>
<dd>Set negative timeout to SECONDS in fuse kernel module [default: 0]</p>
<dt><code>volume-name=</code>VOLUME-NAME</p>
<dd>Volume name to be used for MOUNT-POINT [default: top most volume in VOLUME-FILE]</p>
<dt><code>direct-io-mode=</code>disable</p>
<dd>Disable direct I/O mode in fuse kernel module</p>
<dt><code>congestion-threshold=</code>N</p>
<dd>Set fuse module&#8217;s congestion threshold to N [default: 48]</p>
<dt>
<dt><code>backup-volfile-servers=</code>SERVERLIST</p>
<dd>
<dd>Provide list of backup volfile servers in the following format [default: None] </p>
<p> <code>$ mount -t glusterfs -obackup-volfile-servers=&lt;server2&gt;:</code> <code> &lt;server3&gt;:&#8230;:&lt;serverN&gt; &lt;server1&gt;:/&lt;volname&gt; &lt;mount_point&gt;</code> </p>
<dt>
<dt><code>backupvolfile-server=</code>SERVER</p>
<dd>
<dd>Provide list of backup volfile servers in the following format [default: None] </p>
<p> <code> $ mount -t glusterfs -obackupvolfile-server=&lt;server2&gt; &lt;server1&gt;:/&lt;volname&gt; &lt;mount_point&gt; </p>
<dt>
<dt>fetch-attempts=</code>N</p>
<dd>
<dd><code>Deprecated</code> option &#8211; placed here for backward compatibility [default: 1]</p>
<dt>
<dt><code>background-qlen=</code>N</p>
<dd>
<dd>Set fuse module&#8217;s background queue length to N [default: 64]</p>
<dt><code>no-root-squash=</code>BOOL</p>
<dd>disable root squashing for the trusted client [default: off]</p>
<dt><code>root-squash=</code>BOOL</p>
<dd>enable root squashing for the trusted client [default: on]</p>
<dt><code>use-readdirp=</code>BOOL</p>
<dd>Use readdirp() mode in fuse kernel module [default: on]</dl>
<h2>Files</h2>
<dl>
<dt><i>/etc/fstab</i></p>
<dd>A typical GlusterFS entry in /etc/fstab looks like below </p>
<p> <code>server1:/mirror /mnt/mirror glusterfs log-file=/var/log/mirror.log,acl 0 0</code> </p>
<dt><i>/proc/mounts</i></p>
<dd>An example entry of a GlusterFS mountpoint in /proc/mounts looks like below </p>
<p> <code>server1:/mirror /mnt/glusterfs fuse.glusterfs rw,allow_other,default_permissions,max_read=131072 0 0</code> </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-glusterfs/">glusterfs</a></code>(8), <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8), <code><a href="/docs/linux/man/8-gluster/">gluster</a></code>(8) </p>
<h2>Copyright</h2>
<p>Copyright(c) 2006-2013 Red Hat, Inc. &lt;<a rel="nofollow" href="http://www.redhat.com">http://www.redhat.com</a>&gt;</p>
