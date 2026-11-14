---
title: "flatpak-document-info(1)"
name: "flatpak-document-info"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flatpak-document-info/"
description: "flatpak-document-info – Show information about exported files"
---

<h2 class="name">NAME</h2>
<p> flatpak-document-info &#8211; Show information about exported files </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>flatpak document-info</code> [OPTION&#8230;] FILE</dl>
<h2>DESCRIPTION</h2>
<dd>Shows information about an exported file, such as the document id, the fuse path, the original location in the filesystem, and the per-application permissions. </p>
<p> FILE can either be a file in the fuse filesystem at /run/user/$UID/doc/, or a file anywhere else.</p>
<h2>OPTIONS</h2>
<p> The following options are understood: </p>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show help options and exit.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Print debug information during command processing.</dl>
<p> <code>&#8211;ostree-verbose</code></p>
<dl>
<dt>
<dd> Print OSTree debug information during command processing.</dl>
<h2>EXAMPLES</h2>
<p> <code>$ flatpak document-info ~/Sources/gtk/gail-3.0.pc</code> </p>
<dl>
<dt>
<dd>
<pre>
id: dd32c34a
path: /run/user/1000/doc/dd32c34a/gail-3.0.pc
origin: /home/mclasen/Sources/gtk/gail-3.0.pc
permissions:
        org.gnome.gedit read, write
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-flatpak/">flatpak</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-document-export/">flatpak-document-export</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-document-unexport/">flatpak-document-unexport</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-documents/">flatpak-documents</a></code>(1) </p>
<h2>Index</h2>
