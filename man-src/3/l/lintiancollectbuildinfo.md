---
title: "lintiancollectbuildinfo(3)"
name: "lintiancollectbuildinfo"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lintiancollectbuildinfo/"
---

Lintian::Collect::Buildinfo - Lintian interface to .buildinfo file data collection 

<h2>Synopsis</h2><pre> my ($name, $type) = ('foobar_1.2_i386.buildinfo', 'changes');
 my $collect = Lintian::Collect-&gt;new($name, $type);
 my $files = $collect-&gt;files;
 foreach my $file (keys %{$files}) {
 my $size = $files-&gt;{$file}{size};
 print &quot;File $file has size $size\n&quot;;
 }</pre><h2>Description</h2>Lintian::Collect::Buildinfo provides an interface to data for .buildinfo files. It implements data collection methods specific to .buildinfo files.
<h2>Class Methods</h2><dl COMPACT><dt>new (PACKAGE)
</dt><dd>Creates a new Lintian::Collect::Buildinfo object. Currently, PACKAGE is ignored. Normally, this method should not be called directly, only via the Lintian::Collect constructor.</dd></dl><h2>Instance Methods</h2>In addition to the instance methods listed below, all instance methods documented in the Lintian::Collect module are also available.
<dl COMPACT><dt>files
</dt><dd>Returns a reference to a hash containing information about files listed in the .buildinfo file. Each hash may have the following keys:
</dd><dl COMPACT><dd></dd><dl COMPACT><dt>name
</dt><dd>Name of the file.
</dd><dt>size
</dt><dd>The size of the file in bytes.
</dd><dt>section
</dt><dd>The archive section to which the file belongs.
</dd><dt>priority
</dt><dd>The priority of the file.
</dd><dt>checksums
</dt><dd>A hash with the keys being checksum algorithms and the values themselves being hashes containing
</dd><dl COMPACT><dd></dd><dl COMPACT><dt>sum
</dt><dd>The result of applying the given algorithm to the file.
</dd><dt>filesize
</dt><dd>The size of the file as given in the .buildinfo section relating to the given checksum.</dd></dl></dl><dl COMPACT><dd></dd></dl></dl>
</dl><dl COMPACT><dd>Needs-Info requirements for using <i>files</i>: ``field ([FIELD[, DEFAULT]])'' in Lintian::Collect</dd></dl></dl><h2>Author</h2>Originally written by Adam D. Barratt &lt;adsb [at] debian.org&gt; for Lintian.
<h2>See Also</h2><i><a HREF="/docs/linux/man/1-lintian/">lintian</a></i>(1), Lintian::Collect
