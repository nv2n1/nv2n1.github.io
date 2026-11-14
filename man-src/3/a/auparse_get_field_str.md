---
title: "auparse_get_field_str(3)"
name: "auparse_get_field_str"
section: "3"
letter: "a"
url: "/docs/linux/man/3-auparse_get_field_str/"
description: "auparse_get_field_str – get current field’s value"
---

<h2>NAME</h2>
<p> auparse_get_field_str &#8211; get current field&#8217;s value</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;auparse.h&gt;</code> </p>
<p> const char *auparse_get_field_str(auparse_state_t *au); </p>
<h2>DESCRIPTION</h2>
<p> auparse_get_field_str allows access to the value in the current field of the current record in the current event. </p>
<h2>RETURN VALUE</h2>
<p> Returns NULL if an error occurs; otherwise, a pointer to the field&#8217;s value. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-auparse_get_field_name/">auparse_get_field_name</a></code>(3), <code><a href="/docs/linux/man/3-auparse_get_field_int/">auparse_get_field_int</a></code>(3), <code><a href="/docs/linux/man/3-auparse_interpret_field/">auparse_interpret_field</a></code>(3), <code><a href="/docs/linux/man/3-auparse_next_field/">auparse_next_field</a></code>(3). </p>
<h2>AUTHOR</h2>
<p> Steve Grubb </p>
<h2>Index</h2>
