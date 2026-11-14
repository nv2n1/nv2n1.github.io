---
title: "dpkgchecksums(3)"
name: "dpkgchecksums"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dpkgchecksums/"
---

Dpkg::Checksums - generate and manipulate file checksums 

<h2>Description</h2>This module provides an object that can generate and manipulate various file checksums as well as some methods to query information about supported checksums.
<h2>Functions</h2><dl COMPACT><dt>@list = <i>checksums_get_list()</i>
<dd>Returns the list of supported checksums algorithms.
<dt>$bool = checksums_is_supported($alg)
<dd>Returns a boolean indicating whether the given checksum algorithm is supported. The checksum algorithm is case-insensitive.
<dt>$value = checksums_get_property($alg, $property)
<dd>Returns the requested property of the checksum algorithm. Returns undef if either the property or the checksum algorithm doesn't exist. Valid properties currently include ``program'' (returns an array reference with a program name and parameters required to compute the checksum of the filename given as last parameter) and ``regex'' for the regular expression describing the common string representation of the checksum (as output by the program that generates it).</dl><h2>Object Methods</h2><dl COMPACT><dt>my $ck = Dpkg::Checksums-&gt;<i>new()</i>
<dd>Create a new Dpkg::Checksums object. This object is able to store the checksums of several files to later export them or verify them.
<dt>$ck-&gt;<i>reset()</i>
<dd>Forget about all checksums stored. The object is again in the same state as if it was newly created.
<dt>$ck-&gt;add_from_file($filename, %opts)
<dd>Add checksums information for the file <tt>$filename</tt>. The file must exists for the call to succeed. If you don't want the given filename to appear when you later export the checksums you might want to set the ``key'' option with the public name that you want to use. Also if you don't want to generate all the checksums, you can pass an array reference of the wanted checksums in the ``checksums'' option. 

 It the object already contains checksums information associated the filename (or key), it will error out if the newly computed information does not match what's stored, and the caller did not request that it be updated with the boolean ``update'' option.
<dt>$ck-&gt;add_from_string($alg, $value, %opts)
<dd>Add checksums of type <tt>$alg</tt> that are stored in the <tt>$value</tt> variable. <tt>$value</tt> can be multi-lines, each line should be a space separated list of checksum, file size and filename. Leading or trailing spaces are not allowed. 

 It the object already contains checksums information associated to the filenames, it will error out if the newly read information does not match what's stored, and the caller did not request that it be updated with the boolean ``update'' option.
<dt>$ck-&gt;add_from_control($control, %opts)
<dd>Read checksums from Checksums-* fields stored in the Dpkg::Control object <tt>$control</tt>. It uses <tt>$self</tt>-&gt;<i>add_from_string()</i> on the field values to do the actual work. 

 If the option ``use_files_for_md5'' evaluates to true, then the ``Files'' field is used in place of the ``Checksums-Md5'' field. By default the option is false.
<dt>@files = $ck-&gt;<i>get_files()</i>
<dd>Return the list of files whose checksums are stored in the object.
<dt>$bool = $ck-&gt;has_file($file)
<dd>Return true if we have checksums for the given file. Returns false otherwise.
<dt>$ck-&gt;remove_file($file)
<dd>Remove all checksums of the given file.
<dt>$checksum = $ck-&gt;get_checksum($file, $alg)
<dd>Return the checksum of type <tt>$alg</tt> for the requested <tt>$file</tt>. This will not compute the checksum but only return the checksum stored in the object, if any. 

 If <tt>$alg</tt> is not defined, it returns a reference to a hash: keys are the checksum algorithms and values are the checksums themselves. The hash returned must not be modified, it's internal to the object.
<dt>$size = $ck-&gt;get_size($file)
<dd>Return the size of the requested file if it's available in the object.
<dt>$ck-&gt;export_to_string($alg, %opts)
<dd>Return a multi-line string containing the checksums of type <tt>$alg</tt>. The string can be stored as-is in a Checksum-* field of a Dpkg::Control object.
<dt>$ck-&gt;export_to_control($control, %opts)
<dd>Export the checksums in the Checksums-* fields of the Dpkg::Control <tt>$control</tt> object.</dl><h2>Changes</h2><h3>Version 1.01</h3>New argument: Accept an options argument in <tt>$ck</tt>-&gt;<i>export_to_string()</i>. 

 New option: Accept new option 'update' in <tt>$ck</tt>-&gt;<i>add_from_file()</i> and <tt>$ck</tt>-&gt;<i>add_from_control()</i>.
<h3>Version 1.00</h3>Mark the module as public.
<h2>Author</h2>Raphaël Hertzog &lt;hertzog [at] debian.org&gt;.
