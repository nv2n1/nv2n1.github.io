---
title: "dpkgcontrolfieldscore(3)"
name: "dpkgcontrolfieldscore"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dpkgcontrolfieldscore/"
---

Dpkg::Control::FieldsCore - manage (list of official) control fields 

<h2>Description</h2>The modules contains a list of fieldnames with associated meta-data explaining in which type of control information they are allowed. The types are the CTRL_* constants exported by Dpkg::Control.
<h2>Functions</h2><dl COMPACT><dt>my $f = field_capitalize($field_name)
<dd>Returns the field name properly capitalized. All characters are lowercase, except the first of each word (words are separated by a hyphen in field names).
<dt>field_is_official($fname)
<dd>Returns true if the field is official and known.
<dt>field_is_allowed_in($fname, @types)
<dd>Returns true (1) if the field <tt>$fname</tt> is allowed in all the types listed in the list. Note that you can use type sets instead of individual types (ex: <font SIZE="-1">CTRL_FILE_CHANGES</font> | <font SIZE="-1">CTRL_CHANGELOG</font>). 

 field_allowed_in(A|B, C) returns true only if the field is allowed in C and either A or B. 

 Undef is returned for non-official fields.
<dt>field_transfer_single($from, $to, $field)
<dd>If appropriate, copy the value of the field named <tt>$field</tt> taken from the <tt>$from</tt> Dpkg::Control object to the <tt>$to</tt> Dpkg::Control object. 

 Official fields are copied only if the field is allowed in both types of objects. Custom fields are treated in a specific manner. When the target is not among <font SIZE="-1">CTRL_PKG_SRC, CTRL_PKG_DEB</font> or <font SIZE="-1">CTRL_FILE_CHANGES,</font> then they are alway copied as is (the X- prefix is kept). Otherwise they are not copied except if the target object matches the target destination encoded in the field name. The initial X denoting custom fields can be followed by one or more letters among ``S'' (Source: corresponds to <font SIZE="-1">CTRL_PKG_SRC</font>), ``B'' (Binary: corresponds to <font SIZE="-1">CTRL_PKG_DEB</font>) or ``C'' (Changes: corresponds to <font SIZE="-1">CTRL_FILE_CHANGES</font>). 

 Returns undef if nothing has been copied or the name of the new field added to <tt>$to</tt> otherwise.
<dt>field_transfer_all($from, $to)
<dd>Transfer all appropriate fields from <tt>$from</tt> to <tt>$to</tt>. Calls <i>field_transfer_single()</i> on all fields available in <tt>$from</tt>. 

 Returns the list of fields that have been added to <tt>$to</tt>.
<dt>field_ordered_list($type)
<dd>Returns an ordered list of fields for a given type of control information. This list can be used to output the fields in a predictable order. The list might be empty for types where the order does not matter much.
<dt><i>field_list_src_dep()</i>
<dd>List of fields that contains dependencies-like information in a source Debian package.
<dt><i>field_list_pkg_dep()</i>
<dd>List of fields that contains dependencies-like information in a binary Debian package. The fields that express real dependencies are sorted from the stronger to the weaker.
<dt>field_get_dep_type($field)
<dd>Return the type of the dependency expressed by the given field. Can either be ``normal'' for a real dependency field (Pre-Depends, Depends, ...) or ``union'' for other relation fields sharing the same syntax (Conflicts, Breaks, ...). Returns undef for fields which are not dependencies.
<dt>field_get_sep_type($field)
<dd>Return the type of the field value separator. Can be one of <font SIZE="-1">FIELD_SEP_UNKNOWN, FIELD_SEP_SPACE, FIELD_SEP_COMMA</font> or <font SIZE="-1">FIELD_SEP_LINE.</font>
<dt>field_register($field, $allowed_types, %opts)
<dd>Register a new field as being allowed in control information of specified types. <tt>%opts</tt> is optional
<dt>field_insert_after($type, $ref, @fields)
<dd>Place field after another one ($ref) in output of control information of type <tt>$type</tt>.
<dt>field_insert_before($type, $ref, @fields)
<dd>Place field before another one ($ref) in output of control information of type <tt>$type</tt>.</dl><h2>Changes</h2><h3>Version 1.00</h3>Mark the module as public.
<h2>Author</h2>Raphaël Hertzog &lt;hertzog [at] debian.org&gt;.
