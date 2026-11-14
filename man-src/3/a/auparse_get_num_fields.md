---
title: "auparse_get_num_fields(3)"
name: "auparse_get_num_fields"
section: "3"
letter: "a"
url: "/docs/linux/man/3-auparse_get_num_fields/"
description: "auparse_get_num_fields – get the number of fields"
---

<h2>NAME</h2>
<p> auparse_get_num_fields &#8211; get the number of fields</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;auparse.h&gt;</code> </p>
<p> unsigned int auparse_get_num_fields(auparse_state_t *au); </p>
<h2>DESCRIPTION</h2>
<p> auparse_get_num_fields gets the number of fields in the current record of the current event. </p>
<h2>RETURN VALUE</h2>
<p> Returns 0 if an error occurs; otherwise, the number of fields. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-auparse_next_record/">auparse_next_record</a></code>(3). </p>
<h2>AUTHOR</h2>
<p> Steve Grubb </p>
<h2>Index</h2>
