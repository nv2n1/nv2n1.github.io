---
title: "auparse_get_num_records(3)"
name: "auparse_get_num_records"
section: "3"
letter: "a"
url: "/docs/linux/man/3-auparse_get_num_records/"
description: "auparse_get_num_records – get the number of records"
---

<h2>NAME</h2>
<p> auparse_get_num_records &#8211; get the number of records</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;auparse.h&gt;</code> </p>
<p> unsigned int auparse_get_num_records(auparse_state_t *au); </p>
<h2>DESCRIPTION</h2>
<p> auparse_get_num_records gets the number of records in the current event. </p>
<h2>RETURN VALUE</h2>
<p> Returns 0 if an error occurs; otherwise, the number of records. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-auparse_next_record/">auparse_next_record</a></code>(3). </p>
<h2>AUTHOR</h2>
<p> Steve Grubb </p>
<h2>Index</h2>
