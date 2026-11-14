---
title: "auparse_get_filename(3)"
name: "auparse_get_filename"
section: "3"
letter: "a"
url: "/docs/linux/man/3-auparse_get_filename/"
description: "auparse_get_filename – get the filename where record was found"
---

<h2>NAME</h2>
<p> auparse_get_filename &#8211; get the filename where record was found</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;auparse.h&gt;</code> </p>
<p> const char *auparse_get_filename(auparse_state_t *au); </p>
<h2>DESCRIPTION</h2>
<p> auparse_get_filename will return the name of the source file where the record was found if the source type is AUSOURCE_FILE or AUSOURCE_FILE_ARRAY. For other source types the return value will be NULL. </p>
<h2>RETURN VALUE</h2>
<p> Returns pointer to a filename or NULL if unavailable. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-auparse_get_line_number/">auparse_get_line_number</a></code>(3). <code><a href="/docs/linux/man/3-auparse_next_record/">auparse_next_record</a></code>(3). </p>
<h2>AUTHOR</h2>
<p> John Dennis </p>
<h2>Index</h2>
