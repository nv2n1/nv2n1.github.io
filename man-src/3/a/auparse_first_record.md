---
title: "auparse_first_record(3)"
name: "auparse_first_record"
section: "3"
letter: "a"
url: "/docs/linux/man/3-auparse_first_record/"
description: "auparse_first_record – reposition record cursor"
---

<h2>NAME</h2>
<p> auparse_first_record &#8211; reposition record cursor</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;auparse.h&gt;</code> </p>
<p> int auparse_first_record(auparse_state_t *au); </p>
<h2>DESCRIPTION</h2>
<p> auparse_first_record repositions the internal cursors of the parsing library to point to the first field of the first record in the current event. </p>
<h2>RETURN VALUE</h2>
<p> Returns -1 if an error occurs, 0 if there is no event data, or 1 for success. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-auparse_next_event/">auparse_next_event</a></code>(3), <code><a href="/docs/linux/man/3-auparse_next_record/">auparse_next_record</a></code>(3). </p>
<h2>AUTHOR</h2>
<p> Steve Grubb </p>
<h2>Index</h2>
