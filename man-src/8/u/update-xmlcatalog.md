---
title: "update-xmlcatalog(8)"
name: "update-xmlcatalog"
section: "8"
letter: "u"
url: "/docs/linux/man/8-update-xmlcatalog/"
description: "update-xmlcatalog – maintain XML catalog files"
---

<p>update-xmlcatalog &#8211; maintain XML catalog files</p>
<h2>Synopsis</h2>
<p><code>update-xmlcatalog</code> <code>&#8211;add</code> <code>&#8211;root</code> <code>&#8211;package</code>&nbsp;<i>package</i> <code>&#8211;type</code>&nbsp;<i>type</i> <code>&#8211;id</code>&nbsp;<i>id</i> </p>
<p> <code>update-xmlcatalog</code> <code>&#8211;del</code> <code>&#8211;root</code> <code>&#8211;package</code>&nbsp;<i>package</i> <code>&#8211;type</code>&nbsp;<i>type</i> <code>&#8211;id</code>&nbsp;<i>id</i> </p>
<p> <code>update-xmlcatalog</code> <code>&#8211;add</code> <code>&#8211;package</code>&nbsp;<i>package</i> <code>&#8211;local</code>&nbsp;<i>local</i> <code>&#8211;type</code>&nbsp;<i>type</i> <code>&#8211;id</code>&nbsp;<i>id</i> </p>
<p> <code>update-xmlcatalog</code> <code>&#8211;del</code> <code>&#8211;package</code>&nbsp;<i>package</i> <code>&#8211;local</code>&nbsp;<i>local</i> <code>&#8211;type</code>&nbsp;<i>type</i> <code>&#8211;id</code>&nbsp;<i>id</i> </p>
<p> <code>update-xmlcatalog</code> <code>&#8211;add</code> <code>&#8211;local</code>&nbsp;<i>local</i> <code>&#8211;file</code>&nbsp;<i>file</i> <code>&#8211;type</code>&nbsp;<i>type</i> <code>&#8211;id</code>&nbsp;<i>id</i> </p>
<p> <code>update-xmlcatalog</code> <code>&#8211;del</code> <code>&#8211;local</code>&nbsp;<i>local</i> <code>&#8211;file</code>&nbsp;<i>file</i> <code>&#8211;type</code>&nbsp;<i>type</i> <code>&#8211;id</code>&nbsp;<i>id</i> </p>
<p> <code>update-xmlcatalog</code> <code>&#8211;help</code></p>
<h2>Description</h2>
<p><code>update-xmlcatalog</code> add entries to and removes entries from the root <font SIZE="-1">XML</font> catalog file, a package <font SIZE="-1">XML</font> catalog file or a local <font SIZE="-1">XML</font> catalog file.</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;add</code></p>
<dd>Adds the entry to the root <font SIZE="-1">XML</font> catalog file, a package <font SIZE="-1">XML</font> catalog file or a local <font SIZE="-1">XML</font> catalog file. If the <font SIZE="-1">XML</font> catalog file does not exist yet, it is automatically created.</p>
<dt><code>&#8211;del</code></p>
<dd>Deletes the entry from the root <font SIZE="-1">XML</font> catalog file, the package <font SIZE="-1">XML</font> catalog file or the local <font SIZE="-1">XML</font> catalog file. A resulting empty <font SIZE="-1">XML</font> catalog is not automatically deleted from the filesystem.</p>
<dt><code>&#8211;file</code> <i>file</i></p>
<dd>Indicates a local filename.</p>
<dt><code>&#8211;id</code> <i>id</i></p>
<dd>Indicates the <font SIZE="-1">XML</font> catalog file entry identifier.</p>
<dt><code>&#8211;local</code> <i>local</i></p>
<dd>Indicates a local <font SIZE="-1">XML</font> catalog file.</p>
<dt><code>&#8211;package</code> <i>package</i></p>
<dd>Indicates a package <font SIZE="-1">XML</font> catalog file.</p>
<dt><code>&#8211;root</code></p>
<dd>Indicates the root <font SIZE="-1">XML</font> catalog file.</p>
<dt><code>&#8211;type</code> <i>type</i></p>
<dd>Indicates the <font SIZE="-1">XML</font> catalog file entry type (public, system, uri).</p>
<dt><code>&#8211;help</code></p>
<dd>Displays the usage information.</p>
<dt><code>&#8211;verbose</code></p>
<dd>Optional switch to make a verbose output.</p>
<dt><code>&#8211;sort</code></p>
<dd>Optional switch to sort the manipulated catalog content. </p>
<p> Tip: To sort a catalog without adding or removing an item, just add an already existing item to the catalog.</dl>
<h2>Notes</h2>
<p><code>update-xmlcatalog</code> is the de-facto standard tool to be used to maintain <font SIZE="-1">XML</font> catalog files on a Debian system, similar to that <code><a href="/docs/linux/man/8-update-catalog/">update-catalog</a></code>(8) is the standard tool to be used to main <font SIZE="-1">SGML</font> catalog files on a Debian system. A Debian <font SIZE="-1">XML</font> Policy document to this effect is currently under development. </p>
<p> <code>update-xmlcatalog</code> and <code><a href="/docs/linux/man/1-xmlcatalog/">xmlcatalog</a></code>(1) are incompatible. The former has an internal database of all the entries in all the <font SIZE="-1">XML</font> catalog files it maintains and regenerates the indicated <font SIZE="-1">XML</font> catalog file completely from scratch upon an update. The latter updates the indicated <font SIZE="-1">XML</font> catalog file directly. This means that any change made to an <font SIZE="-1">XML</font> catalog file using <code><a href="/docs/linux/man/1-xmlcatalog/">xmlcatalog</a></code>(1) is overwritten the next time that <font SIZE="-1">XML</font> catalog file is updated using <code>update-xmlcatalog</code>.</p>
<h2>See Also</h2>
<p><i>/usr/share/doc/xml-core/README.Debian</i></p>
<h2>Author</h2>
<p><code>Ardo van Rangelrooij</code> &lt;ardo [at] debian.org&gt;</p>
