---
title: "auparse_next_field(3)"
name: "auparse_next_field"
section: "3"
letter: "a"
url: "/docs/linux/man/3-auparse_next_field/"
description: "auparse_next_field – move field cursor"
---

<h2>NAME</h2>
<p> auparse_next_field &#8211; move field cursor</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;auparse.h&gt;</code> </p>
<p> int auparse_next_field(auparse_state_t *au); </p>
<h2>DESCRIPTION</h2>
<p> auparse_next_field moves the library&#8217;s internal cursor to point to the next field in the current record of the current event. </p>
<h2>RETURN VALUE</h2>
<p> Returns 0 if no more fields exist and 1 for success. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-auparse_next_record/">auparse_next_record</a></code>(3). </p>
<h2>AUTHOR</h2>
<p> Steve Grubb </p>
<h2>Index</h2>
