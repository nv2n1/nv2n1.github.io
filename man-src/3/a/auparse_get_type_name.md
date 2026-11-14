---
title: "auparse_get_type_name(3)"
name: "auparse_get_type_name"
section: "3"
letter: "a"
url: "/docs/linux/man/3-auparse_get_type_name/"
description: "auparse_get_type_name – get record’s type translation"
---

<h2>NAME</h2>
<p> auparse_get_type_name &#8211; get record&#8217;s type translation</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;auparse.h&gt;</code> </p>
<p> const char *auparse_get_type_name(auparse_state_t *au); </p>
<h2>DESCRIPTION</h2>
<p> The auparse_get_type_name function will return the text representation of the name of the current record type. </p>
<h2>RETURN VALUE</h2>
<p> The auparse_get_type_name function returns NULL on error; otherwise a pointer to a string. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-auparse_get_type/">auparse_get_type</a>(3),</code><a href="/docs/linux/man/3-auparse_next_record/">auparse_next_record</a>(3). </p>
<h2>AUTHOR</h2>
<p> Steve Grubb </p>
<h2>Index</h2>
