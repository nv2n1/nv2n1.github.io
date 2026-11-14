---
title: "glusterfs(8)"
name: "glusterfs"
section: "8"
letter: "g"
url: "/docs/linux/man/8-glusterfs/"
description: "GlusterFS – clustered file system"
---

<p>GlusterFS &#8211; clustered file system</p>
<h2>Synopsis</h2>
<p><code>glusterfs</code> <i>[options] [mountpoint]</i> </p>
<h2>Description</h2>
<p>GlusterFS is a clustered file system, capable of scaling to several peta-bytes. It aggregates various storage bricks over Infiniband RDMA or TCP/IP and interconnect into one large parallel network file system. Storage bricks can be made of any commodity hardware, such as x86-64 server with SATA-II RAID and Infiniband HBA. GlusterFS is fully POSIX compliant file system. On client side, it has dependency on FUSE package, on server side, it works seemlessly on different operating systems. Currently supported on GNU/Linux and Solaris. </p>
<h2>Options</h2>
<h3>Basic options</h3>
<dl>
<dt><code>-f, &#8211;volfile=VOLUME-FILE</code></p>
<dd>File to use as VOLUME-FILE.</p>
<dt><code>-l, &#8211;log-file=LOGFILE</code></p>
<dd>File to use for logging (the default is &lt;INSTALL-DIR&gt;/var/log/glusterfs/&lt;MOUNT-POINT&gt;.log).</p>
<dt><code>-L, &#8211;log-level=LOGLEVEL</code></p>
<dd>Logging severity. Valid options are TRACE, DEBUG, INFO, WARNING, ERROR and CRITICAL (the default is INFO).</p>
<dt><code>-s, &#8211;volfile-server=SERVER</code></p>
<dd>Server to get the volume from. This option overrides <code>&#8211;volfile </code> option.</p>
<dt><code>&#8211;volfile-max-fetch-attempts=MAX-ATTEMPTS</code></p>
<dd>Maximum number of connect attempts to server. This option should be provided with <code>&#8211;volfile-server</code> option (the default is 1). </p>
</dl>
<h3>Advanced options</h3>
<dl>
<dt><code>&#8211;acl</code></p>
<dd>Mount the filesystem with POSIX ACL support.</p>
<dt><code>&#8211;debug</code></p>
<dd>Run in debug mode. This option sets <code>&#8211;no-daemon</code>, <code>&#8211;log-level</code> to DEBUG, and <code>&#8211;log-file</code> to console.</p>
<dt><code>&#8211;enable-ino32=BOOL</code></p>
<dd>Use 32-bit inodes when mounting to workaround application that doesn&#8217;t support 64-bit inodes.</p>
<dt><code>&#8211;fopen-keep-cache</code></p>
<dd>Do not purge the cache on file open.</p>
<dt><code>&#8211;mac-compat=BOOL</code></p>
<dd>Provide stubs for attributes needed for seamless operation on Macs (the default is off).</p>
<dt><code>-N, &#8211;no-daemon</code></p>
<dd>Run in the foreground.</p>
<dt><code>-p, &#8211;pid-file=PIDFILE</code></p>
<dd>File to use as PID file.</p>
<dt><code>&#8211;read-only</code></p>
<dd>Mount the file system in &#8216;read-only&#8217; mode.</p>
<dt><code>&#8211;selinux</code></p>
<dd>Enable SELinux label (extended attributes) support on inodes.</p>
<dt><code>-S, &#8211;socket-file=SOCKFILE</code></p>
<dd>File to use as unix-socket.</p>
<dt><code>&#8211;volfile-id=KEY</code></p>
<dd>Key of the volume file to be fetched from the server.</p>
<dt><code>&#8211;volfile-server-port=PORT</code></p>
<dd>Port number of volfile server.</p>
<dt><code>&#8211;volfile-server-transport=TRANSPORT</code></p>
<dd>Transport type to get volume file from server (the default is tcp).</p>
<dt><code>&#8211;volume-name=VOLUME-NAME</code></p>
<dd>Volume name to be used for MOUNT-POINT (the default is top most volume in VOLUME-FILE).</p>
<dt><code>&#8211;worm</code></p>
<dd>Mount the filesystem in &#8216;worm&#8217; mode.</p>
<dt><code>&#8211;xlator-option=VOLUME-NAME.OPTION=VALUE</code></p>
<dd>Add/Override a translator option for a volume with the specified value. </p>
</dl>
<h3>Fuse options</h3>
<dl>
<dd><code>&#8211;attribute-timeout=SECONDS</code> Set attribute timeout to SECONDS for inodes in fuse kernel module (the default is 1).</p>
<dt><code>&#8211;background-qlen=N</code></p>
<dd>Set fuse module&#8217;s background queue length to N (the default is 64).</p>
<dt><code>&#8211;congestion-threshold=N</code></p>
<dd>Set fuse module&#8217;s congestion threshold to N (the default is 48).</p>
<dt><code>&#8211;direct-io-mode=BOOL</code></p>
<dd>Enable/Disable the direct-I/O mode in fuse module (the default is enable).</p>
<dt><code>&#8211;dump-fuse=PATHR</code></p>
<dd>Dump fuse traffic to PATH</p>
<dt><code>&#8211;entry-timeout=SECONDS</code></p>
<dd>Set entry timeout to SECONDS in fuse kernel module (the default is 1).</p>
<dt><code>&#8211;gid-timeout=SECONDS</code></p>
<dd>Set auxiliary group list timeout to SECONDS for fuse translator (the default is 0).</p>
<dt><code>&#8211;negative-timeout=SECONDS</code></p>
<dd>Set negative timeout to SECONDS in fuse kernel module (the default is 0).</p>
<dt><code>&#8211;volfile-check</code></p>
<dd>Enable strict volume file checking. </p>
</dl>
<h3>Miscellaneous Options</h3>
<dl>
<dd><code>-?, &#8211;help</code> Display this help.</p>
<dt><code>&#8211;usage</code></p>
<dd>Display a short usage message.</p>
<dt><code>-V, &#8211;version</code></p>
<dd>Print the program version. </p>
</dl>
<h2>Files</h2>
<p>/var/lib/glusterd/vols/*/*.vol</p>
<h2>Examples</h2>
<p>mount a volume named foo on server bar with log level DEBUG on mount point /mnt/foo # glusterfs &#8211;log-level=DEBUG &#8211;volfile-id=foo &#8211;volfile-server=bar /mnt/foo </p>
<h2>See Also</h2>
<pre><code><a href="//www.systutorials.com/docs/linux/man/1-fusermount/">fusermount</a></code>(1), <code><a href="//www.systutorials.com/docs/linux/man/8-mount.glusterfs/">mount.glusterfs</a></code>(8), <code><a href="//www.systutorials.com/docs/linux/man/8-gluster/">gluster</a></code>(8)</pre>
<h2>Copyright</h2>
<pre>Copyright(c) 2006-2011 Red Hat, Inc. &lt;<a rel="nofollow" href="http://www.redhat.com">http://www.redhat.com</a>&gt;</pre>
