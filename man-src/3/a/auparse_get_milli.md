---
title: "auparse_get_milli(3)"
name: "auparse_get_milli"
section: "3"
letter: "a"
url: "/docs/linux/man/3-auparse_get_milli/"
description: "auparse_get_milli – get the millisecond value of the event"
---

<h2>NAME</h2>
<p> auparse_get_milli &#8211; get the millisecond value of the event</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;auparse.h&gt;</code> </p>
<p> unsigned int auparse_get_milli(auparse_state_t *au); </p>
<h2>DESCRIPTION</h2>
<p> auparse_get_milli gets the millisecond value of the current event. </p>
<h2>RETURN VALUE</h2>
<p> Returns 0 if an error occurs; otherwise, the value of the millisecond portion of the timestamp. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-auparse_get_timestamp/">auparse_get_timestamp</a></code>(3), <code><a href="/docs/linux/man/3-auparse_get_time/">auparse_get_time</a></code>(3). <code><a href="/docs/linux/man/3-auparse_get_milli/">auparse_get_milli</a></code>(3). <code><a href="/docs/linux/man/3-auparse_get_node/">auparse_get_node</a></code>(3). </p>
<h2>AUTHOR</h2>
<p> Steve Grubb </p>
<h2>Index</h2>
