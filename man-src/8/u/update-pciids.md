---
title: "update-pciids(8)"
name: "update-pciids"
section: "8"
letter: "u"
url: "/docs/linux/man/8-update-pciids/"
description: "update-pciids – download new version of the PCI ID list"
---

<p>update-pciids &#8211; download new version of the PCI ID list</p>
<h2>Synopsis</h2>
<p><code>update-pciids</code> [<code>-q</code>] </p>
<h2>Description</h2>
<p><code>update-pciids</code> fetches the current version of the pci.ids file from the primary distribution site and installs it. This utility requires curl, wget or lynx to be installed. If gzip or bzip2 are available, it automatically downloads the compressed version of the list. </p>
<h2>Options</h2>
<dl>
<dt><code>-q</code></p>
<dd>Be quiet and do not report anything except errors. </p>
</dl>
<h2>Files</h2>
<dl>
<dt><code>/usr/share/misc/pci.ids</code></p>
<dd>Here we install the new list. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-lspci/">lspci</a></code>(8), <code><a href="/docs/linux/man/8-setpci/">setpci</a></code>(8) </p>
<h2>Author</h2>
<p>The PCI Utilities are maintained by Martin Mares &lt;mj [at] ucw.cz&gt;.</p>
