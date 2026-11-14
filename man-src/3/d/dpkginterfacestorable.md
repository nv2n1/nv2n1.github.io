---
title: "dpkginterfacestorable(3)"
name: "dpkginterfacestorable"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dpkginterfacestorable/"
---

Dpkg::Interface::Storable - common methods related to object serialization 

<h2>Description</h2>Dpkg::Interface::Storable is only meant to be used as parent class for other objects. It provides common methods that are all implemented on top of two basic methods <i>parse()</i> and <i>output()</i>.
<h2>Base Methods</h2>Those methods must be provided by the object that wish to inherit from Dpkg::Interface::Storable so that the methods provided can work.
<dl COMPACT><dt>$obj-&gt;parse($fh, $desc)
<dd>This methods initialize the object with the data stored in the filehandle. <tt>$desc</tt> is optional and is a textual description of the filehandle used in error messages.
<dt>$string = $obj-&gt;output($fh)
<dd>This method returns a string representation of the object in <tt>$string</tt> and it writes the same string to <tt>$fh</tt> (if it's defined).</dl><h2>Provided Methods</h2><dl COMPACT><dt>$obj-&gt;load($filename)
<dd>Initialize the object with the data stored in the file. The file can be compressed, it will be uncompressed on the fly by using a Dpkg::Compression::FileHandle object. If <tt>$filename</tt> is ``-'', then the standard input is read (no compression is allowed in that case).
<dt>$obj-&gt;save($filename)
<dd>Store the object in the file. If the filename ends with a known compression extension, it will be compressed on the fly by using a Dpkg::Compression::FileHandle object. If <tt>$filename</tt> is ``-'', then the standard output is used (data are written uncompressed in that case).
<dt>&quot;$obj&quot;
<dd>Return a string representation of the object.</dl><h2>Changes</h2><h3>Version 1.00</h3>Mark the module as public.
<h2>Author</h2>Raphaël Hertzog &lt;hertzog [at] debian.org&gt;.
