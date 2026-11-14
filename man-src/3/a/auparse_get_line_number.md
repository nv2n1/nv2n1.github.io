---
title: "auparse_get_line_number(3)"
name: "auparse_get_line_number"
section: "3"
letter: "a"
url: "/docs/linux/man/3-auparse_get_line_number/"
description: "auparse_get_line_number – get line number where record was found"
---

<h2>NAME</h2>
<p> auparse_get_line_number &#8211; get line number where record was found</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;auparse.h&gt;</code> </p>
<p> unsigned int auparse_get_line_number(auparse_state_t *au); </p>
<h2>DESCRIPTION</h2>
<p> auparse_get_line_number will return the source input line number for the current record of the current event. Line numbers start at 1. If the source input type is AUSOURCE_FILE_ARRAY the line numbering will reset back to 1 each time a new line in the file array is opened. </p>
<h2>RETURN VALUE</h2>
<p> Returns the line number. Line numbers are 1 based, a zero value indicates the line number information is unavailable. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-auparse_get_filename/">auparse_get_filename</a></code>(3). <code><a href="/docs/linux/man/3-auparse_next_record/">auparse_next_record</a></code>(3). </p>
<h2>AUTHOR</h2>
<p> John Dennis </p>
<h2>Index</h2>
