---
title: "auparse_next_event(3)"
name: "auparse_next_event"
section: "3"
letter: "a"
url: "/docs/linux/man/3-auparse_next_event/"
description: "auparse_next_event – get the next event"
---

<h2>NAME</h2>
<p> auparse_next_event &#8211; get the next event</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;auparse.h&gt;</code> </p>
<p> int auparse_next_event(auparse_state_t *au); </p>
<h2>DESCRIPTION</h2>
<p> auparse_next_event will position the cursors at the first field of the first record of the next event in a file or buffer. It does not skip events or honor any search criteria that may be stored. </p>
<h2>RETURN VALUE</h2>
<p> Returns -1 if an error occurs, 0 if there&#8217;s no data, 1 for success. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-auparse_next_record/">auparse_next_record</a></code>(3). </p>
<h2>AUTHOR</h2>
<p> Steve Grubb </p>
<h2>Index</h2>
