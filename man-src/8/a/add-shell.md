---
title: "add-shell(8)"
name: "add-shell"
section: "8"
letter: "a"
url: "/docs/linux/man/8-add-shell/"
description: "add-shell – add shells to the list of valid login shells"
---

<p>add-shell &#8211; add shells to the list of valid login shells</p>
<h2>Synopsis</h2>
<p><code>add-shell</code> <i>shellname</i> [<i>shellname</i>&#8230;]</p>
<h2>Description</h2>
<p><code>add-shell</code> copies <i>/etc/shells</i> to <i>/etc/shells.tmp</i>, adds the given shells to this file if they are not already present, and copies this temporary file back to <i>/etc/shells</i>. </p>
<p> The shells must be provided by their full pathnames.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-shells/">shells</a></code>(5) </p>
