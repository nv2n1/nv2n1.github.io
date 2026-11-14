---
title: "auparse_get_record_text(3)"
name: "auparse_get_record_text"
section: "3"
letter: "a"
url: "/docs/linux/man/3-auparse_get_record_text/"
description: "auparse_get_record_text – access unparsed record data"
---

<h2>NAME</h2>
<p> auparse_get_record_text &#8211; access unparsed record data</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;auparse.h&gt;</code> </p>
<p> const char *auparse_get_record_text(auparse_state_t *au); </p>
<h2>DESCRIPTION</h2>
<p> auparse_get_record_text returns a pointer to the full unparsed record. </p>
<h2>RETURN VALUE</h2>
<p> Returns NULL if an error occurs; otherwise, a pointer to the record. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-auparse_next_record/">auparse_next_record</a></code>(3). </p>
<h2>AUTHOR</h2>
<p> Steve Grubb </p>
<h2>Index</h2>
