---
title: "nilfs_cleanerd(8)"
name: "nilfs_cleanerd"
section: "8"
letter: "n"
url: "/docs/linux/man/8-nilfs_cleanerd/"
description: "nilfs_cleanerd – NILFS2 garbage collector"
---

<p>nilfs_cleanerd &#8211; NILFS2 garbage collector</p>
<h2>Synopsis</h2>
<p><code>nilfs_cleanerd</code> [<i>options</i>] <i>device</i> [<i>directory</i>]</p>
<h2>Description</h2>
<p><code>nilfs_cleanerd</code> is a system daemon which reclaims disk space of a NILFS2 file system found in <i>device</i>. </p>
<p> The optional <i>directory</i> argument specifies the mount point where the daemon operates. It must be an r/w-mount. </p>
<p> This program can be invoked either automatically by <code><a href="/docs/linux/man/8-mount-nilfs2/">mount.nilfs2</a></code>(8) or manually by an administrator. However, users are recommended to invoke <code>nilfs_cleanerd</code> through <code><a href="/docs/linux/man/8-mount-nilfs2/">mount.nilfs2</a></code>(8) or <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8) and shutdown it through <code><a href="/docs/linux/man/8-umount-nilfs2/">umount.nilfs2</a></code>(8) or <code><a href="/docs/linux/man/8-umount/">umount</a></code>(8) in order to avoid state inconsistencies among administration tools.</p>
<h2>Options</h2>
<dl>
<dt><code>-c</code></p>
<dd>Specify configuration file.</p>
<dt><code>-h</code></p>
<dd>Display help message and exit.</p>
<dt><code>-n</code></p>
<dd>invoke cleanerd without forking process. This option is intended for internal use from <code><a href="/docs/linux/man/8-mount-nilfs2/">mount.nilfs2</a></code>(8).</p>
<dt><code>-p</code></p>
<dd>Override protection period with the specified number of seconds.</dl>
<h2>Signals</h2>
<p><code>nilfs_cleanerd</code> reacts to a set of signals. You may send a signal to <code>nilfs_cleanerd</code> using the <i>PID</i> shown by the mount command (or in <i>/etc/mtab</i>):</p>
<dl>
<dd>
<dl>
<dt><code># mount -t nilfs2</code></p>
<dd>/dev/sdb1 on /nilfs type nilfs2 (rw,gcpid=<i>PID</i>)<br />
 <code># kill &#8211;</code><i>SIGNAL</i> <i>PID</i></dl>
</dl>
<dl>
<dt><code>SIGHUP</code></p>
<dd>This lets <code>nilfs_cleanerd</code> perform a re-initialization. The configuration file (default is <i>/etc/nilfs_cleanerd.conf</i>) will be reread.</p>
<dt><code>SIGTERM</code></p>
<dd>The <code>nilfs_cleanerd</code> will exit cleanly.</p>
<dt><code>SIGUSR1, SIGUSR2</code></p>
<dd>Reserved for future use. These let <code>nilfs_cleanerd</code> die at present.</dl>
<h2>Files</h2>
<dl>
<dt><i>/etc/nilfs_cleanerd.conf</i></p>
<dd>Configuration file for <code>nilfs_cleanerd</code>. See <code><a href="/docs/linux/man/5-nilfs_cleanerd-conf/">nilfs_cleanerd.conf</a></code>(5) for details.</dl>
<h2>Author</h2>
<p>Koji Sato &lt;koji [at] osrg.net&gt;</p>
<h2>Availability</h2>
<p><code>nilfs_cleanerd</code> is part of the nilfs-utils package and available from <a rel="nofollow" href="http://www.nilfs.org.">http://www.nilfs.org.</a></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-nilfs/">nilfs</a></code>(8), <code><a href="/docs/linux/man/8-mount-nilfs2/">mount.nilfs2</a></code>(8), <code><a href="/docs/linux/man/8-umount-nilfs2/">umount.nilfs2</a></code>(8), <code><a href="/docs/linux/man/5-nilfs_cleanerd-conf/">nilfs_cleanerd.conf</a></code>(5). </p>
