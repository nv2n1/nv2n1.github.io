---
title: "loadunimap(8)"
name: "loadunimap"
section: "8"
letter: "l"
url: "/docs/linux/man/8-loadunimap/"
description: "loadunimap – load the kernel unicode-to-font mapping table"
---

<p>loadunimap &#8211; load the kernel unicode-to-font mapping table</p>
<h2>Synopsis</h2>
<p><code>loadunimap</code> [ <code>-C</code> <i>console</i> ] [ <code>-o</code> <i>oldmap</i> ] [ <i>map</i> ]</p>
<h2>Description</h2>
<p>The <code>loadunimap</code> command is obsolete &#8211; its function is now built-in into <code><a href="/docs/linux/man/8-setfont/">setfont</a></code>(8). However, for backwards compatibility it is still available as a separate command. </p>
<p> The program <code>loadunimap</code> loads the specified map in the kernel unicode-to-font mapping table. If no map is given <i>def</i> mapping table is assumed. The default extension (that can be omitted) is <i>.uni</i>. </p>
<p> If the <code>-o</code> <i>oldmap</i> option is given, the old map is saved in the file specified. </p>
<p> On Linux 2.6.1 and later one can specify the console device using the <code>-C</code> option. </p>
<p> Usually one does not call <code>loadunimap</code> directly &#8211; its function is also built into <code><a href="/docs/linux/man/8-setfont/">setfont</a></code>(8).</p>
<h2>Files</h2>
<dl>
<dt><i>/usr/share/unimaps</i></p>
<dd>The default directory for unicode mappings.</dl>
<dl>
<dt><i>/usr/share/unimaps/def.uni</i></p>
<dd>The default mapping file.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-mapscrn/">mapscrn</a></code>(8), <code><a href="/docs/linux/man/8-setfont/">setfont</a></code>(8) </p>
