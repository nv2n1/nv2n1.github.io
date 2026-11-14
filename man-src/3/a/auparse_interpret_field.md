---
title: "auparse_interpret_field(3)"
name: "auparse_interpret_field"
section: "3"
letter: "a"
url: "/docs/linux/man/3-auparse_interpret_field/"
description: "auparse_interpret_field – get current field’s value interpreted"
---

<h2>NAME</h2>
<p> auparse_interpret_field &#8211; get current field&#8217;s value interpreted</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;auparse.h&gt;</code> </p>
<p> const char *auparse_interpret_field(auparse_state_t *au); </p>
<h2>DESCRIPTION</h2>
<p> auparse_interpret_field allows access to the interpreted value in the current field of the current record in the current event. The returned string is escaped using the chosen method. The returned value will be destroyed if you call this function again. If you need to interpret another field and keep this value, you will have to copy it for later use. </p>
<p> Examples of things that could be interpreted are: uid, gid, syscall numbers, exit codes, file paths, socket addresses, permissions, modes, and capabilities. There are likely to be more in the future. If a value cannot be interpreted, its original value is returned. </p>
<h2>RETURN VALUE</h2>
<p> Returns NULL if there is an error otherwise a pointer to the interpreted value. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-auparse_get_field_int/">auparse_get_field_int</a></code>(3),<code><a href="/docs/linux/man/3-auparse_get_field_str/">auparse_get_field_str</a></code>(3),<code><a href="/docs/linux/man/3-auparse_set_escape_mode/">auparse_set_escape_mode</a></code>(3). </p>
<h2>AUTHOR</h2>
<p> Steve Grubb </p>
<h2>Index</h2>
