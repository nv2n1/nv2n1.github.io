---
title: "auparse_find_field_next(3)"
name: "auparse_find_field_next"
section: "3"
letter: "a"
url: "/docs/linux/man/3-auparse_find_field_next/"
description: "auparse_find_field_next – find next occurrence of field name"
---

<h2>NAME</h2>
<p> auparse_find_field_next &#8211; find next occurrence of field name</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;auparse.h&gt;</code> </p>
<p> const char *auparse_find_field_next(auparse_state_t *au); </p>
<h2>DESCRIPTION</h2>
<p> auparse_find_field_next finds the next occurrence of the previously stored field name. It will scan until it reaches the last record of the current event. </p>
<h2>RETURN VALUE</h2>
<p> Returns NULL field not found. If an error occurs errno will be set. Otherwise, it returns a pointer to the text value associated with the field. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-auparse_first_record/">auparse_first_record</a></code>(3), <code><a href="/docs/linux/man/3-auparse_next_event/">auparse_next_event</a></code>(3), <code><a href="/docs/linux/man/3-auparse_find_field/">auparse_find_field</a></code>(3). </p>
<h2>AUTHOR</h2>
<p> Steve Grubb </p>
<h2>Index</h2>
