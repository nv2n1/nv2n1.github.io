---

title: "bfuse(1)"
name: "bfuse"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bfuse/"
description: "bfuse – Create a FUSE filesystem out of BlackBerry databases."
---

<p> <code>bfuse</code> &#8211; Create a FUSE filesystem out of BlackBerry databases. </p>
<p> <code>bfuse</code> mountpoint [options]</p>
<p> <code>bfuse</code> connects to your BlackBerry and turns its databases into a mounted filesystem using the FUSE filesystem library. As such, it has a few basic arguments, and a list of common options supported by FUSE. </p>
<p> The device will remain in Desktop mode for as long as bfuse runs. </p>
<p> For more information on FUSE options, see <a rel="nofollow" href="http://fuse.sourceforge.net/">http://fuse.sourceforge.net/</a> </p>
<h2>BARRY OPTIONS</h2>
<dl>
<dt><code>&#8211;p pin</code></dt>
<dd> Specify the PIN of the device you want to mount. Default is to mount all available devices.</dd>
<dt><code>&#8211;P password</code></dt>
<dd> Simplistic method to specify the device password on the command line. </dd>
</dl>
<h2>FUSE OPTIONS</h2>
<dl>
<dt><code>&#8211;o opt</code></dt>
<dd> FUSE mount options.</dd>
<dt><code>-h</code></dt>
<dd> Display a command help summary.</dd>
<dt><code>-V</code></dt>
<dd> Display version information, including Barry library, FUSE library, and kernel interface.</dd>
<dt><code>-d</code></dt>
<dd> Enable debug output. Implies &#8216;-f&#8217;.</dd>
<dt><code>-f</code></dt>
<dd> Operate in the foreground.</dd>
<dt><code>-s</code></dt>
<dd> Disable multi-threaded operation. </dd>
</dl>
<h2>AUTHOR</h2>
<p> <code>bfuse</code> is part of the Barry project and was written Chris Frey, as was this manual page.</p>
<h2>SEE ALSO</h2>
<p> <a rel="nofollow" href="http://www.netdirect.ca/software/packages/barry">http://www.netdirect.ca/software/packages/barry</a> </p>
