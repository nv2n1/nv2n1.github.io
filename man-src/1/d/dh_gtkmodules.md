---
title: "dh_gtkmodules(1)"
name: "dh_gtkmodules"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dh_gtkmodules/"
description: "dh_gtkmodules – create Gtk module files for Gtk modules"
---

<h2 class="name">NAME</h2>
<p> dh_gtkmodules &#8211; create Gtk module files for Gtk modules </p>
<h2>SYNOPSIS</h2>
<p> <code>dh_gtkmodules</code> [<i>debhelper options</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>dh_gtkmodules</code> is a debhelper program that handles correctly generating a dependency on the versionned Gtk+ module <font SIZE="-1">ABI</font> and indexes for GdkPixbuf loaders and <font SIZE="-1">IM</font> modules that it finds in the Gtk+ module directories. </p>
<p> This command automatically adds a &#8220;&lt;package&gt;.loaders&#8221; file to the current package with the package name or &#8220;&lt;package&gt;.immodules&#8221; if it finds any GdkPixbuf loaders or <font SIZE="-1">IM</font> modules. </p>
<p> If this command finds the versionned standard module directory in the current package, it will generate a dependency on the earliest Gtk version that Gtk currently has compatibility for in ${misc:Depends} (&#8220;binary version&#8221;).</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-k</code></p>
<dd> Do not generate any dependencies in ${misc:Depends}.</dl>
<h2>SEE ALSO</h2>
<p> debhelper </p>
<p> This program relies on Debhelper, but is shipped with the Gtk development files.</p>
<h2>AUTHOR</h2>
<p> Loic Minier &lt;lool [at] dooz.org&gt; </p>
<h2>Index</h2>
