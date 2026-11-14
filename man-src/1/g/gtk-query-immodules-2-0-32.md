---
title: "gtk-query-immodules-2-0-32(1)"
name: "gtk-query-immodules-2-0-32"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gtk-query-immodules-2-0-32/"
description: "gtk-query-immodules-2.0 – Input method module registration utility"
---

<p>gtk-query-immodules-2.0 &#8211; Input method module registration utility </p>
<h2>Synopsis</h2>
<dl>
<dt> <code>gtk-query-immodules-2.0</code> [&#8211;update-cache] [module&#8230;]</dl>
<h2>Description</h2>
<p><code>gtk-query-immodules-2.0</code></p>
<dd>collects information about loadable input method modules for GTK+ and writes it to the default cache file location, or to stdout. </p>
<p> If called without arguments, it looks for modules in the GTK+ input method module path. </p>
<p> If called with arguments, it looks for the specified modules. The arguments may be absolute or relative paths. </p>
<p> Normally, the output of <code>gtk-query-immodules-2.0</code> is written to <i>libdir</i>/gtk-2.0/2.10.0/immodules.cache, where GTK+ looks for it by default. If it is written to some other location, the environment variable <code>GTK_IM_MODULE_FILE</code> can be set to point GTK+ at the file.</p>
<h2>Options</h2>
<p>&#8211;update-cache</p>
<dl>
<dd>Write the output to the default cache location instead of stdout</dl>
<h2>Environment</h2>
<p>The environment variable <code>GTK_PATH</code> can be used to prepend directories to the input method module path.</p>
<h2>Bugs</h2>
<p>None known yet.</p>
