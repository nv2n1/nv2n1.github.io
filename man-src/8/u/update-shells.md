---
title: "update-shells(8)"
name: "update-shells"
section: "8"
letter: "u"
url: "/docs/linux/man/8-update-shells/"
description: "update-shells – update the list of valid login shells"
---

<p>update-shells &#8211; update the list of valid login shells</p>
<h2>Synopsis</h2>
<p><code>update-shells</code> [<i>options</i>]</p>
<h2>Description</h2>
<p><code>update-shells</code> locates the shells provided by packages from <i>/usr/share/debianutils/shells.d</i> and updates <i>/etc/shells</i> with newly added or removed shells. To track changes made by the administrator, it consults a state file in <i>/var/lib/shells.state .</i></p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;no-act</code></p>
<dd>Do not actually perform the changes to <i>/etc/shells .</i></p>
<dt><code>&#8211;root</code></p>
<dd><i>ROOT</i> </p>
<p> Operate on a chroot at <i>ROOT .</i></p>
<dt><code>&#8211;verbose</code></p>
<dd>Print the shells that are being added or removed.</dl>
<h2>Files</h2>
<p><i>/etc/shells</i> <i>/var/lib/shells.state</i> <i>/usr/share/debianutils/shells.d</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-shells/">shells</a></code>(5) </p>
