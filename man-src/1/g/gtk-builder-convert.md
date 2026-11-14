---
title: "gtk-builder-convert(1)"
name: "gtk-builder-convert"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gtk-builder-convert/"
description: "gtk-builder-convert – Glade file conversion utility"
---

<h2 class="name">NAME</h2>
<p> gtk-builder-convert &#8211; Glade file conversion utility </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>gtk-builder-convert</code> [&#8211;skip-windows] [&#8211;target-version&nbsp;<i>version</i>] [&#8211;root&nbsp;<i>name</i>] {input} {output}</dl>
<h2>DESCRIPTION</h2>
<p> <code>gtk-builder-convert</code></p>
<dd>converts glade files into XML files which can be loaded with GtkBuilder. </p>
<p> It expects the name of a glade file as the first argument, and writes its output the file specified as the second argument.</p>
<h2>OPTIONS</h2>
<p> &#8211;skip-windows, -w</p>
<dl>
<dt>
<dd> Convert everything but GtkWindow subclasses.</dl>
<p> &#8211;target-version, -t</p>
<dl>
<dt>
<dd> Some widgets and properties are different between GTK+ versions 2.0 and 3.0, so this option allows to set the desired GTK+ target version.</dl>
<p> &#8211;root, -r</p>
<dl>
<dt>
<dd> Convert only the widget named <i>name</i> and its children.</dl>
<h2>BUGS</h2>
<p> Toolbars are not handled. </p>
<p> Support for accessibility is not yet implemented. </p>
<p> The script requires a python interpreter to run. </p>
<h2>Index</h2>
