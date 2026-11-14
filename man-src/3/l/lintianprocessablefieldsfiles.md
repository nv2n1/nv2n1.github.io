---
title: "lintianprocessablefieldsfiles(3)"
name: "lintianprocessablefieldsfiles"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lintianprocessablefieldsfiles/"
description: "Lintian::Processable::Fields::Files – Lintian interface to .buildinfo or changes file data collection"
---

<p>Lintian::Processable::Fields::Files &#8211; Lintian interface to .buildinfo or changes file data collection </p>
<h2>Synopsis</h2>
<pre>
   use Moo;
   with 'Lintian::Processable::Fields::Files';
</pre>
<h2>Description</h2>
<p> Lintian::Processable::Fields::Files provides an interface to data for .buildinfo and changes files. It implements data collection methods specific to .buildinfo and changes files.</p>
<h2>Instance Methods</h2>
<dl COMPACT>
<dt>files</p>
<dd> Returns a reference to a hash containing information about files listed in the .buildinfo file. Each hash may have the following keys:</p>
<dl COMPACT>
<dt>
<dd>
<dl COMPACT>
<dt>name</p>
<dd> Name of the file.</p>
<dt>size</p>
<dd> The size of the file in bytes.</p>
<dt>section</p>
<dd> The archive section to which the file belongs.</p>
<dt>priority</p>
<dd> The priority of the file.</p>
<dt>checksums</p>
<dd> A hash with the keys being checksum algorithms and the values themselves being hashes containing</p>
<dl COMPACT>
<dt>
<dd>
<dl COMPACT>
<dt>sum</p>
<dd> The result of applying the given algorithm to the file.</p>
<dt>filesize</p>
<dd> The size of the file as given in the .buildinfo section relating to the given checksum.</dl>
</dl>
<dl COMPACT>
<dt>
<dd></dl>
</dl>
</dl>
<dl COMPACT>
<dt>
<dd></dl>
<dt>saved_files</p>
<dd></dl>
<h2>Author</h2>
<p> Originally written by Adam D. Barratt &lt;adsb [at] debian.org&gt; for Lintian.</p>
<h2>See Also</h2>
<p> <code><a href="/docs/linux/man/1-lintian/">lintian</a></code>(1), Lintian::Processable</p>
