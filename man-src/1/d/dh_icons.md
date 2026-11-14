---
title: "dh_icons(1)"
name: "dh_icons"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dh_icons/"
description: "dh_icons – Update caches of Freedesktop icons"
---

<h2 class="name">NAME</h2>
<p> dh_icons &#8211; Update caches of Freedesktop icons </p>
<h2>SYNOPSIS</h2>
<p> <code>dh_icons</code> [<i>debhelper options</i>] [<code>-n</code>]</p>
<h2>DESCRIPTION</h2>
<p> <code>dh_icons</code> is a debhelper program that updates caches of Freedesktop icons when needed, using the <code>update-icon-caches</code> program provided by <font SIZE="-1">GTK+2.12.</font> Currently this program does not handle installation of the files, though it may do so at a later date, so should be run after icons are installed in the package build directories. </p>
<p> It takes care of adding maintainer script fragments to call <code>update-icon-caches</code> for icon directories. (This is not done for gnome and hicolor icons, as those are handled by triggers.) These commands are inserted into the maintainer scripts by <i><a href="/docs/linux/man/1-dh_installdeb/">dh_installdeb</a></i>(1).</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-n</code>, <code>&#8211;no-scripts</code></p>
<dd> Do not modify maintainer scripts.</dl>
<h2>SEE ALSO</h2>
<p> debhelper </p>
<p> This program is a part of debhelper.</p>
<h2>AUTHOR</h2>
<p> Ross Burton &lt;ross [at] burtonini.com&gt; Jordi Mallach &lt;jordi [at] debian.org&gt; Josselin Mouette &lt;joss [at] debian.org&gt; </p>
<h2>Index</h2>
