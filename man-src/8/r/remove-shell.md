---
title: "remove-shell(8)"
name: "remove-shell"
section: "8"
letter: "r"
url: "/docs/linux/man/8-remove-shell/"
description: "remove-shell – remove shells from the list of valid login shells"
---

<p>remove-shell &#8211; remove shells from the list of valid login shells</p>
<h2>Synopsis</h2>
<p><code>remove-shell</code> <i>shellname</i> [<i>shellname</i>&#8230;]</p>
<h2>Description</h2>
<p><code>remove-shell</code> operates on the temporary files <i>/etc/shells.tmp</i> and <i>/etc/shells.tmp2</i> to remove the given shells from the list of valid login shells, and copy the result back to <i>/etc/shells</i>.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-shells/">shells</a></code>(5) </p>
