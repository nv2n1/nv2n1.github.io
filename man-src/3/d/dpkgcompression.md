---
title: "dpkgcompression(3)"
name: "dpkgcompression"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dpkgcompression/"
---

Dpkg::Compression - simple database of available compression methods 

<h2>Description</h2>This modules provides a few public funcions and a public regex to interact with the set of supported compression methods.
<h2>Functions</h2><dl COMPACT><dt>my @list = <i>compression_get_list()</i>
<dd>Returns a list of supported compression methods (sorted alphabetically).
<dt>compression_is_supported($comp)
<dd>Returns a boolean indicating whether the give compression method is known and supported.
<dt>compression_get_property($comp, $property)
<dd>Returns the requested property of the compression method. Returns undef if either the property or the compression method doesn't exist. Valid properties currently include ``file_ext'' for the file extension, ``default_level'' for the default compression level, ``comp_prog'' for the name of the compression program and ``decomp_prog'' for the name of the decompression program.
<dt>compression_guess_from_filename($filename)
<dd>Returns the compression method that is likely used on the indicated filename based on its file extension.
<dt>my $regex = <i>compression_get_file_extension_regex()</i>
<dd>Returns a regex that matches a file extension of a file compressed with one of the supported compression methods.
<dt>my $comp = <i>compression_get_default()</i>
<dd>Return the default compression method. It's ``gzip'' unless <tt>&quot;compression_set_default&quot;</tt> has been used to change it.
<dt>compression_set_default($comp)
<dd>Change the default compression method. Errors out if the given compression method is not supported.
<dt>my $level = <i>compression_get_default_level()</i>
<dd>Return the default compression level used when compressing data. It's ``9'' for ``gzip'' and ``bzip2'', ``6'' for ``xz'' and ``lzma'', unless <tt>&quot;compression_set_default_level&quot;</tt> has been used to change it.
<dt>compression_set_default_level($level)
<dd>Change the default compression level. Passing undef as the level will reset it to the compressor specific default, otherwise errors out if the level is not valid (see <tt>&quot;compression_is_valid_level&quot;</tt>).
<dt>compression_is_valid_level($level)
<dd>Returns a boolean indicating whether <tt>$level</tt> is a valid compression level (it must be either a number between 1 and 9 or ``fast'' or ``best'')</dl><h2>Changes</h2><h3>Version 1.02</h3>New function: <i>compression_get_file_extension_regex()</i> 

 Deprecated variables: <tt>$default_compression</tt>, <tt>$default_compression_level</tt> and <tt>$compression_re_file_ext</tt>
<h3>Version 1.01</h3>Default compression level is not global any more, it is per compressor type.
<h3>Version 1.00</h3>Mark the module as public.
<h2>Author</h2>Raphaël Hertzog &lt;hertzog [at] debian.org&gt;.
