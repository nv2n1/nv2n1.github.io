---
title: "auparse_get_field_name(3)"
name: "auparse_get_field_name"
section: "3"
letter: "a"
url: "/docs/linux/man/3-auparse_get_field_name/"
description: "auparse_get_field_name – get current field’s name"
---

<h2>NAME</h2>
<p> auparse_get_field_name &#8211; get current field&#8217;s name</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;auparse.h&gt;</code> </p>
<p> const char *auparse_get_field_name(auparse_state_t *au); </p>
<h2>DESCRIPTION</h2>
<p> auparse_get_field_name allows access to the current field name of the current record in the current event. </p>
<h2>RETURN VALUE</h2>
<p> Returns NULL if an error occurs; otherwise, a pointer to the field&#8217;s name. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-auparse_get_field_str/">auparse_get_field_str</a></code>(3), <code><a href="/docs/linux/man/3-auparse_interpret_field/">auparse_interpret_field</a></code>(3), <code><a href="/docs/linux/man/3-auparse_next_field/">auparse_next_field</a></code>(3). </p>
<h2>AUTHOR</h2>
<p> Steve Grubb </p>
<h2>Index</h2>
