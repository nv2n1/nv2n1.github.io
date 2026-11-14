---
title: "dpkgcontrolhashcore(3)"
name: "dpkgcontrolhashcore"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dpkgcontrolhashcore/"
---

Dpkg::Control::HashCore - parse and manipulate a block of RFC822-like fields 

<h2>Description</h2>The Dpkg::Control::Hash object is a hash-like representation of a set of RFC822-like fields. The fields names are case insensitive and are always capitalized the same when output (see field_capitalize function in Dpkg::Control::Fields). The order in which fields have been set is remembered and is used to be able to dump back the same content. The output order can also be overridden if needed. 

 You can store arbitrary values in the hash, they will always be properly escaped in the output to conform to the syntax of control files. This is relevant mainly for multilines values: while the first line is always output unchanged directly after the field name, supplementary lines are modified. Empty lines and lines containing only dots are prefixed with `` .'' (space + dot) while other lines are prefixed with a single space. 

 During parsing, trailing spaces are stripped on all lines while leading spaces are stripped only on the first line of each field.
<h2>Functions</h2><dl COMPACT><dt>my $c = Dpkg::Control::Hash-&gt;new(%opts)
<dd>Creates a new object with the indicated options. Supported options are:
<dl COMPACT><dd><dl COMPACT><dt>allow_pgp
<dd>Configures the parser to accept OpenPGP signatures around the control information. Value can be 0 (default) or 1.
<dt>allow_duplicate
<dd>Configures the parser to allow duplicate fields in the control information. Value can be 0 (default) or 1.
<dt>drop_empty
<dd>Defines if empty fields are dropped during the output. Value can be 0 (default) or 1.
<dt>name
<dd>The user friendly name of the information stored in the object. It might be used in some error messages or warnings. A default name might be set depending on the type.
<dt>is_pgp_signed
<dd>Set by the parser (starting in dpkg 1.17.0) if it finds an OpenPGP signature around the control information. Value can be 0 (default) or 1, and undef when the option is not supported by the code (in versions older than dpkg 1.17.0).</dl></dl><dl COMPACT><dd></dl><dt>$c-&gt;set_options($option, %opts)
<dd>Changes the value of one or more options.
<dt>my $value = $c-&gt;get_option($option)
<dd>Returns the value of the corresponding option.
<dt>$c-&gt;load($file)
<dd>Parse the content of <tt>$file</tt>. Exits in case of errors. Returns true if some fields have been parsed.
<dt>$c-&gt;parse_error($file, $fmt, ...)
<dd>Prints an error message and dies on syntax parse errors.
<dt>$c-&gt;parse($fh, $description)
<dd>Parse a control file from the given filehandle. Exits in case of errors. <tt>$description</tt> is used to describe the filehandle, ideally it's a filename or a description of where the data comes from. It's used in error messages. Returns true if some fields have been parsed.
<dt>$c-&gt;find_custom_field($name)
<dd>Scan the fields and look for a user specific field whose name matches the following regex: /X[<font SIZE="-1">SBC</font>]*-$name/i. Return the name of the field found or undef if nothing has been found.
<dt>$c-&gt;get_custom_field($name)
<dd>Identify a user field and retrieve its value.
<dt>$c-&gt;save($filename)
<dd>Write the string representation of the control information to a file.
<dt>my $str = $c-&gt;<i>output()</i>
<dd><dt>&quot;$c&quot;
<dd>Get a string representation of the control information. The fields are sorted in the order in which they have been read or set except if the order has been overridden with <i>set_output_order()</i>.
<dt>$c-&gt;output($fh)
<dd>Print the string representation of the control information to a filehandle.
<dt>$c-&gt;set_output_order(@fields)
<dd>Define the order in which fields will be displayed in the <i>output()</i> method.
<dt>$c-&gt;apply_substvars($substvars)
<dd>Update all fields by replacing the variables references with the corresponding value stored in the Dpkg::Substvars object.</dl><h2>Changes</h2><h3>Version 1.01</h3>New method: <tt>$c</tt>-&gt;<i>parse_error()</i>.
<h3>Version 1.00</h3>Mark the module as public.
<h2>Author</h2>Raphaël Hertzog &lt;hertzog [at] debian.org&gt;.
