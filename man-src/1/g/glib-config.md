---
title: "glib-config(1)"
name: "glib-config"
section: "1"
letter: "g"
url: "/docs/linux/man/1-glib-config/"
description: "glib-config – script to get information about the installed version of GLib"
---

<h2>NAME</h2>
<p> glib-config &#8211; script to get information about the installed version of GLib</p>
<h2>SYNOPSIS</h2>
<p> <code>glib-config [&#8211;prefix</code><i>[=DIR]</i>] [&#8211;exec-prefix<i>[=DIR]</i>] [&#8211;version] [&#8211;libs] [&#8211;cflags] [LIBRARIES]</p>
<h2>DESCRIPTION</h2>
<p> <i>glib-config</i> is a tool that is used to configure to determine the compiler and linker flags that should be used to compile and link programs that use <i>GLib</i>. It is also used internally to the .m4 macros for GNU autoconf that are included with <i>GLib</i>.</p>
<h2>OPTIONS</h2>
<p> <i>glib-config</i> accepts the following options:</p>
<dl>
<dt><code>LIBRARIES</code></p>
<dd> <i>GLib</i> has three libraries &#8216;glib&#8217;, &#8216;gmodule&#8217; and &#8216;gthread&#8217;. If you specify one of them, only the appropriate things for that library will be printed.</p>
<dt><code>&#8211;version</code></p>
<dd> Print the currently installed version of <i>GLib</i> on the standard output.</p>
<dt><code>&#8211;libs</code></p>
<dd> Print the linker flags that are necessary to link a <i>GLib</i> program.</p>
<dt><code>&#8211;cflags</code></p>
<dd> Print the compiler flags that are necessary to compile a <i>GLib</i> program.</p>
<dt><code>&#8211;prefix=PREFIX</code></p>
<dd> If specified, use PREFIX instead of the installation prefix that <i>GLib</i> was built with when computing the output for the &#8211;cflags and &#8211;libs options. This option is also used for the exec prefix if &#8211;exec-prefix was not specified. This option must be specified before any &#8211;libs or &#8211;cflags options.</p>
<dt><code>&#8211;exec-prefix=PREFIX</code></p>
<dd> If specified, use PREFIX instead of the installation exec prefix that <i>GLib</i> was built with when computing the output for the &#8211;cflags and &#8211;libs options. This option must be specified before any &#8211;libs or &#8211;cflags options.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gtk-config/">gtk-config</a></code>(1), <code><a href="/docs/linux/man/1-gimp/">gimp</a></code>(1), <code><a href="/docs/linux/man/1-gimptool/">gimptool</a></code>(1)</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 1998 Owen Taylor </p>
<p> Permission to use, copy, modify, and distribute this software and its documentation for any purpose and without fee is hereby granted, provided that the above copyright notice appear in all copies and that both that copyright notice and this permission notice appear in supporting documentation. </p>
<h2>Index</h2>
