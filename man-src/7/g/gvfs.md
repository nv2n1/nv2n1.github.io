---
title: "gvfs(7)"
name: "gvfs"
section: "7"
letter: "g"
url: "/docs/linux/man/7-gvfs/"
description: "gvfs – GIO virtual file system"
---

<p>gvfs &#8211; GIO virtual file system</p>
<h2>Description</h2>
<p>GIO provides a VFS API to GLib applications. It includes a &#8216;local&#8217; implementation using POSIX. gvfs provides implementations that go beyond that and allow to access files and storage using many protocols, such as ftp, http, sftp, dav, nfs, etc. It also provides support for trash folders, for cd burning and for monitoring interesting devices and volumes on the computer. Applications use gvfs indirectly, by means of GIO loading the gvfs module that implements the GIO extension points. The gvfs support for volume monitoring is included in a separate loadable module. The actual gvfs implementation is distributed over a number of processes. None of these are expected to be started from the commandline, except for debugging purposes. Main processes:</p>
<dl>
<dd>&bull; gvfsd &#8211; the main gvfs daemon</dl>
<dl>
<dd>&bull; gvfsd-fuse &#8211; mounts gvfs as a fuse filesystem</dl>
<dl>
<dd>&bull; gvfsd-metadata &#8211; writes gvfs metadata</dl>
<p> Volume monitors:</p>
<dl>
<dd>&bull; gvfs-afc-volume-monitor &#8211; a volume monitor for Apple iPhone/iPod Touch devices</dl>
<dl>
<dd>&bull; gvfs-goa-volume-monitor &#8211; a volume monitor for GNOME Online Accounts</dl>
<dl>
<dd>&bull; gvfs-gphoto2-volume-monitor &#8211; a volume monitor for PTP devices</dl>
<dl>
<dd>&bull; gvfs-mtp-volume-monitor &#8211; a volume monitor for MTP devices</dl>
<dl>
<dd>&bull; gvfs-udisks2-volume-monitor &#8211; a udisks2-based volume monitor</dl>
<p> Mount backends:</p>
<dl>
<dd>&bull; gvfsd-admin &#8211; mounts local filesystem with admin privileges</dl>
<dl>
<dd>&bull; gvfsd-afc &#8211; mounts iPhone/iPod touch volumes</dl>
<dl>
<dd>&bull; gvfsd-afp &#8211; mounts Apple Filing Protocol volumes</dl>
<dl>
<dd>&bull; gvfsd-afp-browse &#8211; browses Apple Filing Protocol volumes</dl>
<dl>
<dd>&bull; gvfsd-archive &#8211; mounts archive files in various formats</dl>
<dl>
<dd>&bull; gvfsd-burn &#8211; provides a location for burning CDs</dl>
<dl>
<dd>&bull; gvfsd-cdda &#8211; mounts audio CDs</dl>
<dl>
<dd>&bull; gvfsd-computer &#8211; provides computer://</dl>
<dl>
<dd>&bull; gvfsd-dav &#8211; mounts DAV filesystems</dl>
<dl>
<dd>&bull; gvfsd-dnssd &#8211; browses dnssd</dl>
<dl>
<dd>&bull; gvfsd-ftp &#8211; mounts over FTP</dl>
<dl>
<dd>&bull; gvfsd-google &#8211; mounts Google Drive shares</dl>
<dl>
<dd>&bull; gvfsd-gphoto2 &#8211; mounts over PTP</dl>
<dl>
<dd>&bull; gvfsd-http &#8211; mounts over HTTP</dl>
<dl>
<dd>&bull; gvfsd-localtest &#8211; a test backend</dl>
<dl>
<dd>&bull; gvfsd-mtp &#8211; mounts over MTP</dl>
<dl>
<dd>&bull; gvfsd-network &#8211; provides network://</dl>
<dl>
<dd>&bull; gvfsd-nfs &#8211; mounts over NFS</dl>
<dl>
<dd>&bull; gvfsd-recent &#8211; provides recent://</dl>
<dl>
<dd>&bull; gvfsd-sftp &#8211; mounts over sftp</dl>
<dl>
<dd>&bull; gvfsd-smb &#8211; mounts Windows Shares Filesystem volumes</dl>
<dl>
<dd>&bull; gvfsd-smb-browse &#8211; browses Windows Shares Filesystem volumes</dl>
<dl>
<dd>&bull; gvfsd-trash &#8211; provides trash://</dl>
<h2>Environment</h2>
<p><code>GIO_USE_VFS</code></p>
<dl>
<dd>If set, specifies the GIO vfs implementation to use. Possible values include &#8216;local&#8217; and &#8216;gvfs&#8217;.</dl>
<p> <code>GIO_USE_VOLUME_MONITOR</code></p>
<dl>
<dd>If set, specifies the GIO volume monitor implementation to use. Possible values include &#8216;unix&#8217;, &#8216;GProxyVolumeMonitorUDisks2&#8217;, as well as other native volume monitors that are described in the key files in <code>$XDG_DATA_DIRS</code>/gvfs/remote-volume-monitors.</dl>
<h2>Files</h2>
<p><code>$XDG_DATA_DIRS</code>/gvfs/mounts</p>
<dl>
<dd>This directory contains key files describing mount daemons.</dl>
<p> <code>$XDG_DATA_DIRS</code>/gvfs/remote-volume-monitors</p>
<dl>
<dd>This directory contains key files describing remote volume monitors.</dl>
<h2>See Also</h2>
<p>m[blue]<code>GIO documentation</code>m[]<font SIZE="-2">[1]</font>, <code><a href="/docs/linux/man/1-gvfsd/">gvfsd</a></code>(1), <code><a href="/docs/linux/man/1-gvfsd-fuse/">gvfsd-fuse</a></code>(1), <code><a href="/docs/linux/man/1-gvfsd-metadata/">gvfsd-metadata</a></code>(1)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>GIO documentation</p>
<dl>
<dd><a rel="nofollow" href="http://developer.gnome.org/gio">http://developer.gnome.org/gio</a></dl>
