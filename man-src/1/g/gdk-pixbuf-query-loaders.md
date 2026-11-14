---
title: "gdk-pixbuf-query-loaders(1)"
name: "gdk-pixbuf-query-loaders"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gdk-pixbuf-query-loaders/"
description: "gdk-pixbuf-query-loaders – GdkPixbuf loader registration utility"
---

<h2 class="name">NAME</h2>
<p> gdk-pixbuf-query-loaders &#8211; GdkPixbuf loader registration utility </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>gdk-pixbuf-query-loaders</code> [&#8211;update-cache] [MODULE&#8230;]</dl>
<h2>DESCRIPTION</h2>
<p> <code>gdk-pixbuf-query-loaders</code></p>
<dd>collects information about loadable modules for gdk-pixbuf and writes it to the default cache file location, or to stdout. </p>
<p> If called without arguments, it looks for modules in the gdk-pixbuf loader directory. </p>
<p> If called with arguments, it looks for the specified modules. The arguments may be absolute or relative paths. </p>
<p> Normally, the output of <code>gdk-pixbuf-queryloaders</code> is written to <i>libdir</i>/gdk-pixbuf-2.0/2.10.0/loaders.cache, where gdk-pixbuf looks for it by default. If it is written to some other location, the environment variable <code>GDK_PIXBUF_MODULE_FILE</code> can be set to point gdk-pixbuf at the file.</p>
<h2>OPTIONS</h2>
<p> &#8211;update-cache</p>
<dl>
<dt>
<dd> Write the output to the default cache location instead of stdout</dl>
<h2>ENVIRONMENT</h2>
<p> The environment variable <code>GDK_PIXBUF_MODULEDIR</code> can be used to specify a different loader directory. The default gdk-pixbuf loader directory is <i>libdir</i>/gdk-pixbuf-2.0/<i>version</i>/loaders. </p>
<h2>Index</h2>
