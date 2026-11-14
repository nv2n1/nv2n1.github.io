---
title: "auparse_get_node(3)"
name: "auparse_get_node"
section: "3"
letter: "a"
url: "/docs/linux/man/3-auparse_get_node/"
description: "auparse_get_node – get the event’s machine node name"
---

<h2>NAME</h2>
<p> auparse_get_node &#8211; get the event&#8217;s machine node name</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;auparse.h&gt;</code> </p>
<p> const char *auparse_get_node(auparse_state_t *au); </p>
<h2>DESCRIPTION</h2>
<p> auparse_get_node gets the machine&#8217;s node name if it exists in the audit event from the current event&#8217;s timestamp data structure. Not all records have node names since its an admin configurable option. </p>
<h2>RETURN VALUE</h2>
<p> Returns a copy of the node name or NULL if it does not exist or there was an error. The caller must free the string. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-auparse_get_timestamp/">auparse_get_timestamp</a></code>(3), <code><a href="/docs/linux/man/3-auparse_get_time/">auparse_get_time</a></code>(3), <code><a href="/docs/linux/man/3-auparse_get_milli/">auparse_get_milli</a></code>(3). <code><a href="/docs/linux/man/3-auparse_get_serial/">auparse_get_serial</a></code>(3). </p>
<h2>AUTHOR</h2>
<p> Steve Grubb </p>
<h2>Index</h2>
