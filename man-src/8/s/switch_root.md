---
title: "switch_root(8)"
name: "switch_root"
section: "8"
letter: "s"
url: "/docs/linux/man/8-switch_root/"
description: "switch_root – switch to another filesystem as the root of the mount tree"
---

<p>switch_root &#8211; switch to another filesystem as the root of the mount tree</p>
<h2>Synopsis</h2>
<p><code>switch_root</code> [<code>-hV</code>] </p>
<p> <code>switch_root</code> <i>newroot init</i> [<i>arg</i>&#8230;]</p>
<h2>Description</h2>
<p><code>switch_root</code> moves already mounted <i>/proc</i>, <i>/dev</i>, <i>/sys</i> and <i>/run</i> to <i>newroot</i> and makes <i>newroot</i> the new root filesystem and starts <i>init</i> process. </p>
<p> <code>WARNING: switch_root removes recursively all files and directories on the current root filesystem.</code></p>
<h2>Options</h2>
<p><code>-h, &#8211;help</code></p>
<dl>
<dd>Display help text and exit.</dl>
<p> <code>-V, &#8211;version</code></p>
<dl>
<dd>Display version information and exit.</dl>
<h2>Exit Status</h2>
<p><code>switch_root</code> returns 0 on success and 1 on failure.</p>
<h2>Notes</h2>
<p><code>switch_root</code> will fail to function if <i>newroot</i> is not the root of a mount. If you want to switch root into a directory that does not meet this requirement then you can first use a bind-mounting trick to turn any directory into a mount point: </p>
<dl>
<dd>
<pre>mount --bind $DIR $DIR</pre>
</dl>
<h2>Authors</h2>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-chroot/">chroot</a></code>(2), <code><a href="/docs/linux/man/8-init/">init</a></code>(8), <code><a href="/docs/linux/man/8-mkinitrd/">mkinitrd</a></code>(8), <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8)</p>
<h2>Reporting Bugs</h2>
<p>For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>Availability</h2>
<p>The <code>switch_root</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;.</p>
