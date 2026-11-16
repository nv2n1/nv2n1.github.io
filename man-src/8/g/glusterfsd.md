---
title: "glusterfsd(8)"
name: "glusterfsd"
section: "8"
letter: "g"
url: "/docs/linux/man/8-glusterfsd/"
description: "GlusterFS – Clustered Filesystem."
---

<p>GlusterFS &#8211; Clustered Filesystem.</p>
<h2>Synopsis</h2>
<p><code>glusterfsd</code> <i>[options] [mountpoint]</i> </p>
<h2>Description</h2>
<p>GlusterFS is a clustered file-system capable of scaling to several peta-bytes. It aggregates various storage bricks over Infiniband RDMA or TCP/IP interconnect into one large parallel network file system. Storage bricks can be made of any commodity hardware such as x86-64 server with SATA-II RAID and Infiniband HBA. GlusterFS is fully POSIX compliant FileSystem. On client side, it has dependency on FUSE package, on server side, it works seemlessly on different OSes. (Currently supported on GNU/Linux, Solaris). </p>
<h2>Options</h2>
<p>Mandatory or optional arguments to long options are also mandatory or optional for any corresponding short options.</p>
<h3>Basic options</h3>
<dl>
<dd><code>-f, &#8211;volfile=VOLUME-FILE</code> File to use as VOLUME-FILE [default:/etc/glusterfs/glusterfs.vol]</dd>
<dt><code>-l, &#8211;log-file=LOGFILE</code></dt>
<dd>File to use for logging [default:/var/log/glusterfs/glusterfs.log]</dd>
<dt><code>-L, &#8211;log-level=LOGLEVEL</code></dt>
<dd>Logging severity. Valid options are TRACE, DEBUG, INFO, WARNING, ERROR and CRITICAL [default: WARNING]</dd>
<dt><code>-s, &#8211;volfile-server=SERVER</code></dt>
<dd>Server to get the volume from. This option overrides <code>&#8211;volfile option </dd>
</dl>
<p> </code></p>
<h3>Advanced options</h3>
<dl>
<dd><code>&#8211;debug</code> Run in debug mode. This option sets <code>&#8211;no-daemon</code>, <code>&#8211;log-level</code> to DEBUG and <code>&#8211;log-file</code> to console</dd>
<dt><code>-N, &#8211;no-daemon</code></dt>
<dd>Run in foreground</dd>
<dt><code>&#8211;read-only</code></dt>
<dd>Makes the filesystem read-only</dd>
<dt><code>-p, &#8211;pid-file=PIDFILE</code></dt>
<dd>File to use as pid file</dd>
<dt><code>-S SOCKFILE</dt>
<dd>Socket file to used for inter-process communication</dd>
<dt>&#8211;brick-name DIRECTORY</dt>
<dd>Directory to be used as export directory for GlusterFS</dd>
<dt>&#8211;brick-port PORT</dt>
<dd>Brick Port to be registered with Gluster portmapper</dd>
<dt>&#8211;volfile-id=KEY</code></dt>
<dd>KEY of the volume file to be fetched from server</dd>
<dt><code>&#8211;volfile-server-port=PORT</code></dt>
<dd>Port number of volfile server</dd>
<dt><code>&#8211;volfile-server-transport=TRANSPORT</code></dt>
<dd>Transport type to get volume file from server [default: tcp]</dd>
<dt><code>&#8211;volume-name=VOLUME-NAME</code></dt>
<dd>Volume name to be used for MOUNT-POINT [default: top most volume in VOLUME-FILE]</dd>
<dt><code>&#8211;xlator-option=VOLUME-NAME.OPTION=VALUE</code></dt>
<dd>Add/override a translator option for a volume with the specified value </dd>
</dl>
<h3>Fuse options</h3>
<dl>
<dd><code>&#8211;attribute-timeout=SECONDS</code> Set attribute timeout to SECONDS for inodes in fuse kernel module [default: 1]</dd>
<dt><code>&#8211;entry-timeout=SECONDS</code></dt>
<dd>Set entry timeout to SECONDS in fuse kernel module [default: 1]</dd>
<dt><code>&#8211;direct-io-mode=BOOL</code></dt>
<dd>Enable/Disable direct-io mode in fuse module [default: enable]</dd>
<dt><code>&#8211;resolve-gids</code></dt>
<dd>Resolve all auxiliary groups in fuse translator (max 32 otherwise) </dd>
</dl>
<h3>Miscellaneous Options</h3>
<dl>
<dd><code>-?, &#8211;help</code> Give this help list</dd>
<dt><code>&#8211;usage</code></dt>
<dd>Give a short usage message</dd>
<dt><code>-V, &#8211;version</code></dt>
<dd>Print program version </dd>
</dl>
<h2>Files</h2>
<p>/etc/glusterfs/*.vol</p>
<h2>Examples</h2>
<p>Start a GlusterFS server on localhost with volume name foo glusterfsd -s localhost &#8211;volfile-id foo.server.media-disk-1 -p /var/lib/glusterd/vols/foo/run/server-media-disk-1.pid -S /tmp/&lt;uniqueid&gt;.socket &#8211;brick-name /media/disk-1 -l /var/log/glusterfs/bricks/media-disk-1.log &#8211;brick-port 24009 &#8211;xlator-option foo-server.listen-port=24009 </p>
<h2>See Also</h2>
<pre><code><a href="//www.systutorials.com/docs/linux/man/1-fusermount/">fusermount</a></code>(1), <code>mount.glusterfs</code>(8), <code><a href="//www.systutorials.com/docs/linux/man/8-gluster/">gluster</a></code>(8)</pre>
<h2>Copyright</h2>
<pre>Copyright(c) 2006-2011 Gluster, Inc. &lt;<a rel="nofollow" href="http://www.gluster.com">http://www.gluster.com</a>&gt;</pre>
