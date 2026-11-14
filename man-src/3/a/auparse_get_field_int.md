---
title: "auparse_get_field_int(3)"
name: "auparse_get_field_int"
section: "3"
letter: "a"
url: "/docs/linux/man/3-auparse_get_field_int/"
description: "auparse_get_field_int – get current field’s value as an int"
---

<h2>NAME</h2>
<p> auparse_get_field_int &#8211; get current field&#8217;s value as an int</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;auparse.h&gt;</code> </p>
<p> int auparse_get_field_int(auparse_state_t *au); </p>
<h2>DESCRIPTION</h2>
<p> auparse_get_field_int allows access to the value as an int of the current field of the current record in the current event. </p>
<h2>RETURN VALUE</h2>
<p> Returns -1 if there is an error with errno set appropriately or the value if errno is zero. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-auparse_get_field_str/">auparse_get_field_str</a></code>(3). </p>
<h2>AUTHOR</h2>
<p> Steve Grubb </p>
<h2>Index</h2>
