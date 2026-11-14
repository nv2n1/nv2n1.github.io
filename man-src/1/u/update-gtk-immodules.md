---
title: "update-gtk-immodules(1)"
name: "update-gtk-immodules"
section: "1"
letter: "u"
url: "/docs/linux/man/1-update-gtk-immodules/"
description: "update-gtk-immodules – Update GTK+ immodule cache"
---

<h2 class="name">NAME</h2>
<p> update-gtk-immodules &#8211; Update GTK+ immodule cache </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>update-gtk-immodules</code> [HOST_TRIPLET]</dl>
<h2>DESCRIPTION</h2>
<p> <code>update-gtk-immodules</code></p>
<dd>is a wrapper around gtk-query-immodules-2.0 that tries to help with multilib installations. It is meant to be used in %post scripts of rpm packages that install input method modules for GTK+ 2.x. </p>
<p> It needs to be given a GNU-style host triplet as argument, such as &quot;x86_64-redhat-linux-gnu&quot;. This argument determines where the tool saves the gtk.immodules file that it creates. It must be the same as the host triplet that GTK+ was configured with. </p>
<h2>FILES</h2>
<p> $libdir/gtk-2.0/2.10.0/immodules.cache &#8211; the file created by update-gtk-immodules. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gtk-query-immodules-2-0/">gtk-query-immodules-2.0</a></code>(1) </p>
<h2>Index</h2>
