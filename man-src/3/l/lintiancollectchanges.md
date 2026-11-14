---
title: "lintiancollectchanges(3)"
name: "lintiancollectchanges"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lintiancollectchanges/"
---

Lintian::Collect::Changes - Lintian interface to .changes file data collection 

<h2>Synopsis</h2><pre> my ($name, $type) = ('foobar_1.2_i386.changes', 'changes');
 my $collect = Lintian::Collect-&gt;new($name, $type);
 my $files = $collect-&gt;files;
 foreach my $file (keys %{$files}) {
 my $size = $files-&gt;{$file}{size};
 print &quot;File $file has size $size\n&quot;;
 }</pre><h2>Description</h2>Lintian::Collect::Changes provides an interface to data for .changes files. It implements data collection methods specific to .changes files.
<h2>Class Methods</h2><dl COMPACT><dt>new (<font SIZE="-1">PACKAGE</font>)
<dd>Creates a new Lintian::Collect::Changes object. Currently, <font SIZE="-1">PACKAGE</font> is ignored. Normally, this method should not be called directly, only via the Lintian::Collect constructor.</dl><h2>Instance Methods</h2>In addition to the instance methods listed below, all instance methods documented in the Lintian::Collect module are also available.
<dl COMPACT><dt>files
<dd>Returns a reference to a hash containing information about files listed in the .changes file. Each hash may have the following keys:
<dl COMPACT><dd><dl COMPACT><dt>name
<dd>Name of the file.
<dt>size
<dd>The size of the file in bytes.
<dt>section
<dd>The archive section to which the file belongs.
<dt>priority
<dd>The priority of the file.
<dt>checksums
<dd>A hash with the keys being checksum algorithms and the values themselves being hashes containing
<dl COMPACT><dd><dl COMPACT><dt>sum
<dd>The result of applying the given algorithm to the file.
<dt>filesize
<dd>The size of the file as given in the .changes section relating to the given checksum.</dl></dl><dl COMPACT><dd></dl></dl>
</dl><dl COMPACT><dd>Needs-Info requirements for using <i>files</i>: ``field ([FIELD[, <font SIZE="-1">DEFAULT</font>]])'' in Lintian::Collect</dl><dt>repacked
<dd>Returns true if the source package referenced in this changes file has been ``repacked'' and false otherwise. This is determined from the version name containing ``dfsg'' or similar. 

 Needs-Info requirements for using <i>repacked</i>: Same as field</dl><h2>Author</h2>Originally written by Adam D. Barratt &lt;adsb [at] debian.org&gt; for Lintian.
<h2>See Also</h2><i><a HREF="/docs/linux/man/1-lintian/">lintian</a></i>(1), Lintian::Collect
