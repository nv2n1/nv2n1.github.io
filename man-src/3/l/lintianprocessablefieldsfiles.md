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
<dt>files</dt>
<dd> Returns a reference to a hash containing information about files listed in the .buildinfo file. Each hash may have the following keys:</dd>
<dl COMPACT>
<dl COMPACT>
<dt>name</dt>
<dd> Name of the file.</dd>
<dt>size</dt>
<dd> The size of the file in bytes.</dd>
<dt>section</dt>
<dd> The archive section to which the file belongs.</dd>
<dt>priority</dt>
<dd> The priority of the file.</dd>
<dt>checksums</dt>
<dd> A hash with the keys being checksum algorithms and the values themselves being hashes containing</dd>
<dl COMPACT>
<dl COMPACT>
<dt>sum</dt>
<dd> The result of applying the given algorithm to the file.</dd>
<dt>filesize</dt>
<dd> The size of the file as given in the .buildinfo section relating to the given checksum.</dd></dl>
</dl>
<dl COMPACT>
</dl>
</dl>
</dl>
<dl COMPACT>
</dl>
<dt>saved_files</dt>
<dd></dd></dl>
<h2>Author</h2>
<p> Originally written by Adam D. Barratt &lt;adsb [at] debian.org&gt; for Lintian.</p>
<h2>See Also</h2>
<p> <code><a href="/docs/linux/man/1-lintian/">lintian</a></code>(1), Lintian::Processable</p>
