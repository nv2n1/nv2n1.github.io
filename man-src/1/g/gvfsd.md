---

title: "gvfsd(1)"
name: "gvfsd"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gvfsd/"
description: "gvfsd – Main daemon for gvfs"
---

<dl>
<dt> <code>gvfsd</code> [OPTION&#8230;]</dt></dl>
<p> <code>gvfsd</code></p>
<dd>is the main daemon for the gvfs virtual filesystem. It provides the <i>org.gtk.vfs.Daemon</i> name on the session bus. gvfsd is autostarted by GIO clients if it is not running. </dd>
<p> The primary task of <code>gvfsd</code> is to act as a mount tracker/manager. It spawns new backends when requested and keeps track of their lifecycle, maintaining a list of active mounts and creates direct connections to them. </p>
<p> Since gvfs backends are running as children of the gvfsd process, it is possible to start gvfsd in a terminal and set environment variables to get debug output from individual backends. </p>
<p> <code>gvfsd</code> also starts the <code><a href="/docs/linux/man/1-gvfsd-fuse/">gvfsd-fuse</a></code>(1), and provides it the mount point where the fuse file system should be mounted.</p>
<h2>OPTIONS</h2>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
</dt><dd> Prints a short help text and exits.</dd></dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
</dt><dd> Shows the version number and exits.</dd></dl>
<p> <code>-r</code>, <code>&#8211;replace</code></p>
<dl>
<dt>
</dt><dd> Replace the currently running gvfsd instance.</dd></dl>
<p> <code>&#8211;no-fuse</code></p>
<dl>
<dt>
</dt><dd> Don&#8217;t start the fuse filesystem.</dd></dl>
<p> <code>-d</code>, <code>&#8211;debug</code></p>
<dl>
<dt>
</dt><dd> Enable debug output.</dd></dl>
<h2>ENVIRONMENT</h2>
<p> <code>GVFS_DISABLE_FUSE</code></p>
<dl>
<dt>
</dt><dd> If this environment variable is set, gvfsd will not start the fuse filesystem.</dd></dl>
<h2>EXIT STATUS</h2>
<p> On success 0 is returned, a non-zero failure code otherwise.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gvfs/">gvfs</a></code>(7), <code><a href="/docs/linux/man/1-gvfsd-fuse/">gvfsd-fuse</a></code>(1) </p>
