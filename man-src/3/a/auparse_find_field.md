---
title: "auparse_find_field(3)"
name: "auparse_find_field"
section: "3"
letter: "a"
url: "/docs/linux/man/3-auparse_find_field/"
description: "auparse_find_field – search for field name"
---

<h2>NAME</h2>
<p> auparse_find_field &#8211; search for field name</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;auparse.h&gt;</code> </p>
<p> const char *auparse_find_field(auparse_state_t *au, const char *name); </p>
<h2>DESCRIPTION</h2>
<p> auparse_find_field will scan all records in an event to find the first occurrence of the field name passed to it. Searching begins from the cursor&#8217;s current position. The field name is stored for subsequent searching. </p>
<h2>RETURN VALUE</h2>
<p> Returns NULL field not found. If an error occurs errno will be set. Otherwise, it returns a pointer to the text value associated with the field. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-auparse_first_record/">auparse_first_record</a></code>(3), <code><a href="/docs/linux/man/3-auparse_find_field_next/">auparse_find_field_next</a></code>(3). </p>
<h2>AUTHOR</h2>
<p> Steve Grubb </p>
<h2>Index</h2>
