---
title: "auparse_next_record(3)"
name: "auparse_next_record"
section: "3"
letter: "a"
url: "/docs/linux/man/3-auparse_next_record/"
description: "auparse_next_record – move record cursor"
---

<h2>NAME</h2>
<p> auparse_next_record &#8211; move record cursor</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;auparse.h&gt;</code> </p>
<p> int auparse_next_record(auparse_state_t *au); </p>
<h2>DESCRIPTION</h2>
<p> auparse_next_record will move the internal library cursors to point to the next record of the current event. You should not call this function from a feed interface callback function. Doing so will deadlock the code. In that scenario, you should check the number of records in the current event with auparse_get_num_records and only call this if there are more records. </p>
<h2>RETURN VALUE</h2>
<p> Returns -1 if an error occurs, 0 if no more records in current event, or 1 for success. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-auparse_next_event/">auparse_next_event</a></code>(3),<code><a href="/docs/linux/man/3-auparse_get_num_records/">auparse_get_num_records</a></code>(3). </p>
<h2>AUTHOR</h2>
<p> Steve Grubb </p>
<h2>Index</h2>
