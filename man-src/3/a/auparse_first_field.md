---
title: "auparse_first_field(3)"
name: "auparse_first_field"
section: "3"
letter: "a"
url: "/docs/linux/man/3-auparse_first_field/"
description: "auparse_first_field – reposition field cursor"
---

<h2>NAME</h2>
<p> auparse_first_field &#8211; reposition field cursor</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;auparse.h&gt;</code> </p>
<p> int auparse_first_field(auparse_state_t *au); </p>
<h2>DESCRIPTION</h2>
<p> auparse_first_field repositions the library&#8217;s internal cursor to point to the first field of the current record in the current event. </p>
<h2>RETURN VALUE</h2>
<p> Returns 0 if there is no event data; otherwise, 1 for success. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-auparse_next_field/">auparse_next_field</a></code>(3). </p>
<h2>AUTHOR</h2>
<p> Steve Grubb </p>
<h2>Index</h2>
