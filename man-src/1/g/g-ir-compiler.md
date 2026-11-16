---
title: "g-ir-compiler(1)"
name: "g-ir-compiler"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g-ir-compiler/"
description: "g-ir-compiler – typelib compiler."
---

<h2>NAME</h2>
<p> g-ir-compiler &#8211; typelib compiler.</p>
<h2>SYNOPSIS</h2>
<p> <code>g-ir-compiler</code> [OPTION&#8230;] GIRFILE</p>
<h2>DESCRIPTION</h2>
<p> g-ir-compiler converts one or more GIR files into one or more typelib. The output will be written to standard output unless the &#8211;output is specified.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></dt>
<dd> Show help options</dd>
<dt><code>&#8211;output=FILENAME</code></dt>
<dd> Save the resulting output in FILENAME.</dd>
<dt><code>&#8211;verbose</code></dt>
<dd> Show verbose messages</dd>
<dt><code>&#8211;debug</code></dt>
<dd> Show debug messages</dd>
<dt><code>&#8211;includedir=DIRECTORY</code></dt>
<dd> Adds a directory which will be used to find includes inside the GIR format.</dd>
<dt><code>&#8211;module=MODULE</code></dt>
<dd> FIXME</dd>
<dt><code>&#8211;shared-library=FILENAME</code></dt>
<dd> Specifies the shared library where the symbols in the typelib can be found. The name of the library should not contain the leading lib prefix nor the ending shared library suffix.</dd>
<dt></dt></dl>
<h2>BUGS</h2>
<dd> Report bugs at <a rel="nofollow" href="http://bugzilla.gnome.org/">http://bugzilla.gnome.org/</a> in the gobject-introspection product.</dd>
<h2>HOMEPAGE and CONTACT</h2>
<p> <a rel="nofollow" href="http://live.gnome.org/GObjectIntrospection">http://live.gnome.org/GObjectIntrospection</a></p>
<h2>AUTHORS</h2>
<p> Mattias Clasen </p>
<h2>Index</h2>
