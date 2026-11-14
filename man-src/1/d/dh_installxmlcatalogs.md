---
title: "dh_installxmlcatalogs(1)"
name: "dh_installxmlcatalogs"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dh_installxmlcatalogs/"
description: "dh_installxmlcatalogs – install and register XML catalog files"
---

<h2 class="name">NAME</h2>
<p> dh_installxmlcatalogs &#8211; install and register XML catalog files </p>
<h2>SYNOPSIS</h2>
<p> <code>dh_installxmlcatalogs</code> [<i>debhelper options</i>] [<code>-n</code>]</p>
<h2>DESCRIPTION</h2>
<p> <code>dh_installxmlcatalogs</code> is a debhelper program that installs and registers <font SIZE="-1">XML</font> catalog files. It complies with the Debian <font SIZE="-1">XML/SGML</font> policy. </p>
<p> The file <i>debian/package.xmlcatalogs</i> lists the local <font SIZE="-1">XML</font> catalog files to be installed per package as well as the <font SIZE="-1">XML</font> entities in those local <font SIZE="-1">XML</font> catalog files that are to be registered in the <font SIZE="-1">XML</font> catalog system. </p>
<p> The local <font SIZE="-1">XML</font> catalog file entries in that file should be of the form <tt>&quot;local;source;dest&quot;</tt>, where the verbatim <tt>&quot;local&quot;</tt> indicates this is an entry for a local <font SIZE="-1">XML</font> catalog file, <tt>&quot;source&quot;</tt> indicates where the local <font SIZE="-1">XML</font> catalog resides in the source tree, and <tt>&quot;dest&quot;</tt> indicates the destination location for the local <font SIZE="-1">XML</font> catalog under the package build area. <tt>&quot;dest&quot;</tt> should start with <i>/usr/share/xml/</i>. </p>
<p> The entries for the <font SIZE="-1">XML</font> entities to be registered in the package <font SIZE="-1">XML</font> catalog file should be of the form <tt>&quot;package;type;id;catalog&quot;</tt>, where the verbatim <tt>&quot;package&quot;</tt> indicates this is an entry for an <font SIZE="-1">XML</font> entity to be registered in the package <font SIZE="-1">XML</font> catalog file, <tt>&quot;type&quot;</tt> indicates the <font SIZE="-1">XML</font> entity type (public, system, uri), <tt>&quot;id&quot;</tt> indicates the <font SIZE="-1">XML</font> entity id, and <tt>&quot;catalog&quot;</tt> indicates the local <font SIZE="-1">XML</font> catalog file. </p>
<p> The entries for the <font SIZE="-1">XML</font> entities to be registered in the root <font SIZE="-1">XML</font> catalog file should be of the form <tt>&quot;root;type;id&quot;</tt>, where the verbatim <tt>&quot;root&quot;</tt> indicates this is an entry for an <font SIZE="-1">XML</font> entity to be registered in the root <font SIZE="-1">XML</font> catalog file, <tt>&quot;type&quot;</tt> indicates the <font SIZE="-1">XML</font> entity type (public, system, uri), and <tt>&quot;id&quot;</tt> indicates the <font SIZE="-1">XML</font> entity id. </p>
<p> If an entry for is to be registered identically in the root catalog and the package catalog file, you can use the form <tt>&quot;root-and-package;type;id;catalog&quot;</tt>, where the verbatim <tt>&quot;root-and-package&quot;</tt> indicates this is an entry for an <font SIZE="-1">XML</font> entity to be registered in both the root and package <font SIZE="-1">XML</font> catalog files, <tt>&quot;type&quot;</tt> indicates the <font SIZE="-1">XML</font> entity type (public, system, uri), <tt>&quot;id&quot;</tt> indicates the <font SIZE="-1">XML</font> entity id, and <tt>&quot;catalog&quot;</tt> indicates the local <font SIZE="-1">XML</font> catalog file. </p>
<p> <font SIZE="-1">XML</font> entity types are described in <code><a href="/docs/linux/man/8-update-xmlcatalog/">update-xmlcatalog</a></code>(8). Using the <tt>&quot;root&quot;</tt> or <tt>&quot;package&quot;</tt> commands, a type of <tt>&quot;public&quot;</tt> will general <tt>&quot;delegatePublic&quot;</tt> statements in the applicable catalog file. Generally you will want to use the types <tt>&quot;public&quot;</tt> for any formal public identifiers, and <tt>&quot;system&quot;</tt> for any files on the local filesystem or URLs. <tt>&quot;uri&quot;</tt> is only used for non-local files which are not part of the external document subset, e.g., they are not used for entities or DTDs. </p>
<p> <code>dh_installxmlcatalogs</code> automatically adds maintainer script snippets for the registration and unregistration of the listed <font SIZE="-1">XML</font> entities in the <font SIZE="-1">XML</font> catalog system (unless <code>-n</code> is used).<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>A dependency on the<br />
 <code>xml-core</code> package will be added to <tt>&quot;${misc:Depends}&quot;</tt>, so be sure to use that variable in the file <i>debian/control</i>. See <code><a href="/docs/linux/man/1-dh_installdeb/">dh_installdeb</a></code>(1) for an explanation of Debhelper maintainer script snippets.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-n</code>, <code>&#8211;noscripts</code></p>
<dd> Do not modify <i>postinst</i>/<i>postrm</i>/<i>prerm</i> scripts.</dl>
<h2>NOTES</h2>
<p> Note that this command is not idempotent. &#8220;dh_clean -k&#8221; should be called between invocations of this command. Otherwise, it may cause multiple instances of the same text to be added to maintainer scripts.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-debhelper/">debhelper</a></code>(7) </p>
<p> <i>/usr/share/doc/xml-core/</i></p>
<h2>AUTHOR</h2>
<p> <code>Ardo van Rangelrooij</code> &lt;ardo [at] debian.org&gt; </p>
<p> <code>Adam Di Carlo</code> &lt;aph [at] debian.org&gt; </p>
<h2>Index</h2>
