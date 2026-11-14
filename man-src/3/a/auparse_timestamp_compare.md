---
title: "auparse_timestamp_compare(3)"
name: "auparse_timestamp_compare"
section: "3"
letter: "a"
url: "/docs/linux/man/3-auparse_timestamp_compare/"
description: "auparse_timestamp_compare – compares timestamp values"
---

<h2>NAME</h2>
<p> auparse_timestamp_compare &#8211; compares timestamp values</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;auparse.h&gt;</code> </p>
<p> int auparse_timestamp_compare(au_event_t *e1, au_event_t *e2); </p>
<h2>DESCRIPTION</h2>
<p> auparse_timestamp_compare compares the values of 2 timestamps. </p>
<h2>RETURN VALUE</h2>
<p> Returns -1, 0, or 1 respectively depending on whether e2 is less than, equal to, or greater than e1. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-auparse_get_timestamp/">auparse_get_timestamp</a></code>(3). </p>
<h2>AUTHOR</h2>
<p> Steve Grubb </p>
<h2>Index</h2>
