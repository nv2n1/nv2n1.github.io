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
<p><code>update-xmlcatalog</code> add entries to and removes entries from the root XML catalog file, a package XML catalog file or a local XML catalog file.</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;add</code></dt>
<dd>Adds the entry to the root XML catalog file, a package XML catalog file or a local XML catalog file. If the XML catalog file does not exist yet, it is automatically created.</dd>
<dt><code>&#8211;del</code></dt>
<dd>Deletes the entry from the root XML catalog file, the package XML catalog file or the local XML catalog file. A resulting empty XML catalog is not automatically deleted from the filesystem.</dd>
<dt><code>&#8211;file</code> <i>file</i></dt>
<dd>Indicates a local filename.</dd>
<dt><code>&#8211;id</code> <i>id</i></dt>
<dd>Indicates the XML catalog file entry identifier.</dd>
<dt><code>&#8211;local</code> <i>local</i></dt>
<dd>Indicates a local XML catalog file.</dd>
<dt><code>&#8211;package</code> <i>package</i></dt>
<dd>Indicates a package XML catalog file.</dd>
<dt><code>&#8211;root</code></dt>
<dd>Indicates the root XML catalog file.</dd>
<dt><code>&#8211;type</code> <i>type</i></dt>
<dd>Indicates the XML catalog file entry type (public, system, uri).</dd>
<dt><code>&#8211;help</code></dt>
<dd>Displays the usage information.</dd>
<dt><code>&#8211;verbose</code></dt>
<dd>Optional switch to make a verbose output.</dd>
<dt><code>&#8211;sort</code></dt>
<dd>Optional switch to sort the manipulated catalog content. </dd>
<p> Tip: To sort a catalog without adding or removing an item, just add an already existing item to the catalog.</dl>
<h2>Notes</h2>
<p><code>update-xmlcatalog</code> is the de-facto standard tool to be used to maintain XML catalog files on a Debian system, similar to that <code><a href="/docs/linux/man/8-update-catalog/">update-catalog</a></code>(8) is the standard tool to be used to main SGML catalog files on a Debian system. A Debian XML Policy document to this effect is currently under development. </p>
<p> <code>update-xmlcatalog</code> and <code><a href="/docs/linux/man/1-xmlcatalog/">xmlcatalog</a></code>(1) are incompatible. The former has an internal database of all the entries in all the XML catalog files it maintains and regenerates the indicated XML catalog file completely from scratch upon an update. The latter updates the indicated XML catalog file directly. This means that any change made to an XML catalog file using <code><a href="/docs/linux/man/1-xmlcatalog/">xmlcatalog</a></code>(1) is overwritten the next time that XML catalog file is updated using <code>update-xmlcatalog</code>.</p>
<h2>See Also</h2>
<p><i>/usr/share/doc/xml-core/README.Debian</i></p>
<h2>Author</h2>
<p><code>Ardo van Rangelrooij</code> &lt;ardo [at] debian.org&gt;</p>
</p>