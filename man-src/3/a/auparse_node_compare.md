---
title: "auparse_node_compare(3)"
name: "auparse_node_compare"
section: "3"
letter: "a"
url: "/docs/linux/man/3-auparse_node_compare/"
description: "auparse_node_compare – compares node name values"
---

<h2>NAME</h2>
<p> auparse_node_compare &#8211; compares node name values</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;auparse.h&gt;</code> </p>
<p> int auparse_node_compare(au_event_t *e1, au_event_t *e2); </p>
<h2>DESCRIPTION</h2>
<p> auparse_node_compare compares the node name values of 2 events. </p>
<h2>RETURN VALUE</h2>
<p> Returns -1, 0, or 1 respectively depending on whether e2 is less than, equal to, or greater than e1. Since this is a string compare, it probably only matter that they are equal or not equal. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-auparse_get_timestamp/">auparse_get_timestamp</a></code>(3). </p>
<h2>AUTHOR</h2>
<p> Steve Grubb </p>
<h2>Index</h2>
