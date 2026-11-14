---
title: "xrdp-sessvc(8)"
name: "xrdp-sessvc"
section: "8"
letter: "x"
url: "/docs/linux/man/8-xrdp-sessvc/"
description: "xrdp-sessvc – xrdp session supervisor"
---

<p>xrdp-sessvc &#8211; <code>xrdp</code> session supervisor </p>
<h2>Syntax</h2>
<p><code>xrdp-sessvc</code> <i>x_pid wm_pid</i></p>
<h2>Description</h2>
<p><code>xrdp-sessvc</code> is the <code><a href="/docs/linux/man/8-xrdp/">xrdp</a></code>(8) session supervisor, which monitors the running X server and Windows Manager. As soon as one of them quits, the other process is terminated as well.<br />
 This program is only executed internally by <code><a href="/docs/linux/man/8-xrdp-sesman/">xrdp-sesman</a></code>(8). </p>
<h2>Options</h2>
<dl>
<dt><i>x_pid</i></p>
<dd>The process ID of the forked X server to monitor.</p>
<dt><i>wm_pid</i></p>
<dd>The process ID of the forked Window Manager to monitor. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-xrdp-sesrun/">xrdp-sesrun</a></code>(8). for more info on <code>xrdp</code> see <a rel="nofollow" href="http://www.xrdp.org/">http://www.xrdp.org/</a> </p>
