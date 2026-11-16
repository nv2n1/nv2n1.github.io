---
title: "dpkgsourcepackage(3)"
name: "dpkgsourcepackage"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dpkgsourcepackage/"
---

Dpkg::Source::Package - manipulate Debian source packages 

<h2>Description</h2>This module provides an object that can manipulate Debian source packages. While it supports both the extraction and the creation of source packages, the only <font SIZE="-1">API</font> that is officially supported is the one that supports the extraction of the source package.
<h2>Functions</h2><dl COMPACT><dt>my $string = <i>get_default_diff_ignore_regex()</i>
</dt><dd>Returns the default diff ignore regex.
</dd><dt>set_default_diff_ignore_regex($string)
</dt><dd>Set a regex as the new default diff ignore regex.
</dd><dt>my @array = <i>get_default_tar_ignore_pattern()</i>
</dt><dd>Returns the default tar ignore pattern, as an array.
</dd><dt>$p = Dpkg::Source::Package-&gt;new(filename =&gt; $dscfile, options =&gt; {})
</dt><dd>Creates a new object corresponding to the source package described by the file <tt>$dscfile</tt>. 
 The options hash supports the following options:
</dd><dl COMPACT><dd></dd><dl COMPACT><dt>skip_debianization
</dt><dd>If set to 1, do not apply Debian changes on the extracted source package.
</dd><dt>skip_patches
</dt><dd>If set to 1, do not apply Debian-specific patches. This options is specific for source packages using format ``2.0'' and ``3.0 (quilt)''.
</dd><dt>require_valid_signature
</dt><dd>If set to 1, the <i>check_signature()</i> method will be stricter and will error out if the signature can't be verified.
</dd><dt>copy_orig_tarballs
</dt><dd>If set to 1, the extraction will copy the upstream tarballs next the target directory. This is useful if you want to be able to rebuild the source package after its extraction.</dd></dl></dl><dl COMPACT><dd></dd></dl><dt>$p-&gt;<i>get_filename()</i>
</dt><dd>Returns the filename of the <font SIZE="-1">DSC</font> file.
</dd><dt>$p-&gt;<i>get_files()</i>
</dt><dd>Returns the list of files referenced by the source package. The filenames usually do not have any path information.
</dd><dt>$p-&gt;<i>check_checksums()</i>
</dt><dd>Verify the checksums embedded in the <font SIZE="-1">DSC</font> file. It requires the presence of the other files constituting the source package. If any inconsistency is discovered, it immediately errors out.
</dd><dt>$bool = $p-&gt;<i>is_signed()</i>
</dt><dd>Returns 1 if the <font SIZE="-1">DSC</font> files contains an embedded OpenPGP signature. Otherwise returns 0.
</dd><dt>$p-&gt;<i>check_signature()</i>
</dt><dd>Implement the same OpenPGP signature check that dpkg-source does. In case of problems, it prints a warning or errors out. 

 If the object has been created with the ``require_valid_signature'' option, then any problem will result in a fatal error.
</dd><dt>$p-&gt;extract($targetdir)
</dt><dd>Extracts the source package in the target directory <tt>$targetdir</tt>. Beware that if <tt>$targetdir</tt> already exists, it will be erased.</dd></dl><h2>Changes</h2><h3>Version 1.01</h3>New functions: <i>get_default_diff_ignore_regex()</i>, <i>set_default_diff_ignore_regex()</i>, <i>get_default_tar_ignore_pattern()</i> 

 Deprecated variables: <tt>$diff_ignore_default_regexp</tt>, <tt>@tar_ignore_default_pattern</tt>
<h3>Version 1.00</h3>Mark the module as public.
<h2>Author</h2>Raphaël Hertzog, &lt;hertzog [at] debian.org&gt;
