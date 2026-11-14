---
title: "dh_installxfonts(1)"
name: "dh_installxfonts"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dh_installxfonts/"
description: "dh_installxfonts – register X fonts"
---

<h2 class="name">NAME</h2>
<p> dh_installxfonts &#8211; register X fonts </p>
<h2>SYNOPSIS</h2>
<p> <code>dh_installxfonts</code> [<i>debhelper options</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>dh_installxfonts</code> is a debhelper program that is responsible for registering X fonts, so their corresponding <i>fonts.dir</i>, <i>fonts.alias</i>, and <i>fonts.scale</i> be rebuilt properly at install time. </p>
<p> Before calling this program, you should have installed any X fonts provided by your package into the appropriate location in the package build directory, and if you have <i>fonts.alias</i> or <i>fonts.scale</i> files, you should install them into the correct location under <i>etc/X11/fonts</i> in your package build directory. </p>
<p> Your package should depend on <code>xfonts-utils</code> so that the <code>update-fonts-</code><i>*</i> commands are available. (This program adds that dependency to <code>${misc:Depends}</code>.) </p>
<p> This program automatically generates the <i>postinst</i> and <i>postrm</i> commands needed to register X fonts. These commands are inserted into the maintainer scripts by <code>dh_installdeb</code>. See <i><a href="/docs/linux/man/1-dh_installdeb/">dh_installdeb</a></i>(1) for an explanation of how this works.</p>
<h2>NOTES</h2>
<p> See <i><a href="/docs/linux/man/8-update-fonts-alias/">update-fonts-alias</a></i>(8), <i><a href="/docs/linux/man/8-update-fonts-scale/">update-fonts-scale</a></i>(8), and <i><a href="/docs/linux/man/8-update-fonts-dir/">update-fonts-dir</a></i>(8) for more information about X font installation. </p>
<p> See Debian policy, section 11.8.5. for details about doing fonts the Debian way.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/7-debhelper/">debhelper</a></i>(7) </p>
<p> This program is a part of debhelper.</p>
<h2>AUTHOR</h2>
<p> Joey Hess &lt;joeyh [at] debian.org&gt; </p>
<h2>Index</h2>
