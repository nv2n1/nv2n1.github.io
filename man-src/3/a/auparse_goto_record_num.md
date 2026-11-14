---
title: "auparse_goto_record_num(3)"
name: "auparse_goto_record_num"
section: "3"
letter: "a"
url: "/docs/linux/man/3-auparse_goto_record_num/"
description: "auparse_goto_record_num – move record cursor to specific record"
---

<h2>NAME</h2>
<p> auparse_goto_record_num &#8211; move record cursor to specific record</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;auparse.h&gt;</code> </p>
<p> int auparse_goto_record_num(auparse_state_t *au, unsigned int num); </p>
<h2>DESCRIPTION</h2>
<p> auparse_goto_record_num will move the internal library cursors to point to a specific physical record number. Records within the same event are numbered starting from 0. This is generally not needed but there are some cases where one may want precise control over the exact record being looked at. </p>
<h2>RETURN VALUE</h2>
<p> Returns 0 on error or 1 for success. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-auparse_get_num_records/">auparse_get_num_records</a></code>(3),<code><a href="/docs/linux/man/3-auparse_next_record/">auparse_next_record</a></code>(3). </p>
<h2>AUTHOR</h2>
<p> Steve Grubb </p>
<h2>Index</h2>
