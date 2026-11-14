---
title: "dh_installcatalogs(1)"
name: "dh_installcatalogs"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dh_installcatalogs/"
description: "dh_installcatalogs – install and register SGML Catalogs"
---

<h2 class="name">NAME</h2>
<p> dh_installcatalogs &#8211; install and register SGML Catalogs </p>
<h2>SYNOPSIS</h2>
<p> <code>dh_installcatalogs</code> [<i>debhelper options</i>] [<code>-n</code>]</p>
<h2>DESCRIPTION</h2>
<p> <code>dh_installcatalogs</code> is a debhelper program that installs and registers <font SIZE="-1">SGML</font> catalogs. It complies with the Debian <font SIZE="-1">XML/SGML</font> policy. </p>
<p> Catalogs will be registered in a supercatalog, in <i>/etc/sgml/package.cat</i>. </p>
<p> This command automatically adds maintainer script snippets for registering and unregistering the catalogs and supercatalogs (unless <code>-n</code> is used). These snippets are inserted into the maintainer scripts and the <code>triggers</code> file by <code>dh_installdeb</code>; see <i><a href="/docs/linux/man/1-dh_installdeb/">dh_installdeb</a></i>(1) for an explanation of Debhelper maintainer script snippets. </p>
<p> A dependency on <code>sgml-base</code> will be added to <code>${misc:Depends}</code>, so be sure your package uses that variable in <i>debian/control</i>.</p>
<h2>FILES</h2>
<dl>
<dt>debian/<i>package</i>.sgmlcatalogs</p>
<dd> Lists the catalogs to be installed per package. Each line in that file should be of the form <tt>&quot;</tt>source<tt> </tt>dest<tt>&quot;</tt>, where <i>source</i> indicates where the catalog resides in the source tree, and <i>dest</i> indicates the destination location for the catalog under the package build area. <i>dest</i> should start with <i>/usr/share/sgml/</i>.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-n</code>, <code>&#8211;no-scripts</code></p>
<dd> Do not modify <i>postinst</i>/<i>postrm</i>/<i>prerm</i> scripts nor add an activation trigger.</dl>
<h2>NOTES</h2>
<p> Note that this command is not idempotent. <i><a href="/docs/linux/man/1-dh_prep/">dh_prep</a></i>(1) should be called between invocations of this command. Otherwise, it may cause multiple instances of the same text to be added to maintainer scripts.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/7-debhelper/">debhelper</a></i>(7) </p>
<p> <i>/usr/share/doc/sgml-base-doc/</i></p>
<h2>AUTHOR</h2>
<p> Adam Di Carlo &lt;aph [at] debian.org&gt; </p>
<h2>Index</h2>
