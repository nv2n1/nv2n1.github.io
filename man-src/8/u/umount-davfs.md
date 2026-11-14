---
title: "umount-davfs(8)"
name: "umount-davfs"
section: "8"
letter: "u"
url: "/docs/linux/man/8-umount-davfs/"
description: "umount.davfs – Umount-helper to unmount a davfs2 file system"
---

<p>umount.davfs &#8211; Umount-helper to unmount a davfs2 file system </p>
<h2>Synopsis</h2>
<p><code>umount.davfs [-h | &#8211;help] [-V | &#8211;version]</code><br />
 <code>umount </code><i>dir</i> </p>
<h2>SYNOPSIS (root only)</h2>
<p><code>umount.davfs </code><i>dir</i></p>
<h2>Description</h2>
<p><code>umount.davfs</code> is a umount helper program. It is called by the <code><a href="/docs/linux/man/8-umount/">umount</a></code>(8) command. Its purpose is to prevent the umount command from returning unless <code>mount.davfs</code> has synchronized all its cached files with the webdav server. <i>dir</i> is the mountpoint where the WebDAV resource is mounted on. It may be an absolute or relative path. While for local file systems <code><a href="/docs/linux/man/8-umount/">umount</a></code>(8) will only return when all cached data have been written to disk, this is not automatically true for a mounted <code>davfs2</code> file system. With this umount helper the user can rely on the familiar behaviour of <code><a href="/docs/linux/man/8-umount/">umount</a></code>(8). To inform the operating system that the file system uses a network connection, you should always use the <code>_netdev</code> option, when mounting as <code>davfs2</code> file system. Depending on the amount of data and the quality of the connection, unmounting a <code>davfs2</code> file system may take some seconds up to some hours. If the <code>mount.davfs</code> daemon encountered serious errors, <code>umount.davfs</code> may return an error instead of unmounting the file system. In this case try <code>umount -i</code>. The <code>-i</code> option will prevent <code><a href="/docs/linux/man/8-umount/">umount</a></code>(8) from calling <code>umount.davfs</code>. </p>
<h2>Options</h2>
<dl>
<dt><code>-V &#8211;version</code></p>
<dd>Output version. </p>
<dt><code>-h &#8211;help</code></p>
<dd>Print a help message. </p>
<dt><code>-f -l -n -r -v</code></p>
<dd>This options are <code>ignored</code>. They are only recognized for compatibility with <code><a href="/docs/linux/man/8-umount/">umount</a></code>(8). </p>
</dl>
<h2>Files</h2>
<dl>
<dt><i>/var/run/mount.davfs</i></p>
<dd>PID-files of running <code>umount.davfs</code> processes are looked up here. </p>
</dl>
<h2>Bugs</h2>
<p>No known bugs. </p>
<h2>Authors</h2>
<p>This man page was written by Werner Baumann &lt;werner.baumann [at] onlinehome.de&gt;.</p>
<h2>Davfs2 Home</h2>
<p><a rel="nofollow" href="http://savannah.nongnu.org/projects/davfs2">http://savannah.nongnu.org/projects/davfs2</a></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-mount-davfs/">mount.davfs</a></code>(8), <code><a href="/docs/linux/man/8-umount/">umount</a></code>(8), <code><a href="/docs/linux/man/5-davfs2-conf/">davfs2.conf</a></code>(5), <code><a href="/docs/linux/man/5-fstab/">fstab</a></code>(5) </p>
