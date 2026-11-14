---
title: "auparse_get_field_type(3)"
name: "auparse_get_field_type"
section: "3"
letter: "a"
url: "/docs/linux/man/3-auparse_get_field_type/"
description: "auparse_get_field_type – get current field’s data type"
---

<h2>NAME</h2>
<p> auparse_get_field_type &#8211; get current field&#8217;s data type</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;auparse.h&gt;</code> </p>
<p> int auparse_get_field_type(auparse_state_t *au); </p>
<h2>DESCRIPTION</h2>
<p> auparse_get_field_type returns a value from the auparse_type_t enum that describes the kind of data in the current field of the current record in the current event. </p>
<h2>RETURN VALUE</h2>
<p> Returns AUPARSE_TYPE_UNCLASSIFIED if the field&#8217;s data type has no known description or is an integer. Otherwise it returns another enum. Fields with the type AUPARSE_TYPE_ESCAPED must be interpretted to access their value since those field&#8217;s raw value is encoded. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-auparse_get_field_name/">auparse_get_field_name</a></code>(3). </p>
<h2>AUTHOR</h2>
<p> Steve Grubb </p>
<h2>Index</h2>
