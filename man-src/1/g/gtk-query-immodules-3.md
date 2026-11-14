---
title: "gtk-query-immodules-3(1)"
name: "gtk-query-immodules-3"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gtk-query-immodules-3/"
description: "gtk-query-immodules-3.0 – Input method module registration utility"
---

<h2 class="name">NAME</h2>
<p> gtk-query-immodules-3.0 &#8211; Input method module registration utility </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>gtk-query-immodules-3.0</code> [&#8211;update-cache] [MODULE&#8230;]</dl>
<h2>DESCRIPTION</h2>
<p> <code>gtk-query-immodules-3.0</code></p>
<dd>collects information about loadable input method modules for GTK+ and writes it to the default cache file location, or to stdout. </p>
<p> If called without arguments, it looks for modules in the GTK+ input method module path. </p>
<p> If called with arguments, it looks for the specified modules. The arguments may be absolute or relative paths. </p>
<p> Normally, the output of <code>gtk-query-immodules-3.0</code> is written to <i>libdir</i>/gtk-3.0/3.0.0/immodules.cache, where GTK+ looks for it by default. If it is written to some other location, the <code>GTK_IM_MODULE_FILE</code> environment variable can be set to point GTK+ at the file.</p>
<h2>OPTIONS</h2>
<p> &#8211;update-cache</p>
<dl>
<dt>
<dd> Write the output to the default cache location instead of stdout</dl>
<h2>FILES</h2>
<p> <i>libdir</i>/gtk-3.0/3.0.0/immodules.cache</p>
<dl>
<dt>
<dd> The default im cache file used by GTK+ applications</dl>
<h2>ENVIRONMENT</h2>
<p> <code>GTK_PATH</code></p>
<dl>
<dt>
<dd> Prepends directories to the input method module path</dl>
<p> <code>GTK_IM_MODULE_FILE</code></p>
<dl>
<dt>
<dd> Specifies an alternative im module cache for GTK+ applications</dl>
<h2>Index</h2>
