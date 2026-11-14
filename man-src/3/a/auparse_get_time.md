---
title: "auparse_get_time(3)"
name: "auparse_get_time"
section: "3"
letter: "a"
url: "/docs/linux/man/3-auparse_get_time/"
description: "auparse_get_time – get event’s time"
---

<h2>NAME</h2>
<p> auparse_get_time &#8211; get event&#8217;s time</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;auparse.h&gt;</code> </p>
<p> time_t auparse_get_time(auparse_state_t *au); </p>
<h2>DESCRIPTION</h2>
<p> auparse_get_time will access just the time portion of the timestamp data structure for the current event. </p>
<h2>RETURN VALUE</h2>
<p> Returns 0 if an error occurs; otherwise, the valid time value in time_t format. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-time/">time</a></code>(3), <code><a href="/docs/linux/man/3-auparse_get_timestamp/">auparse_get_timestamp</a></code>(3), <code><a href="/docs/linux/man/3-auparse_get_milli/">auparse_get_milli</a></code>(3). <code><a href="/docs/linux/man/3-auparse_get_serial/">auparse_get_serial</a></code>(3). <code><a href="/docs/linux/man/3-auparse_get_node/">auparse_get_node</a></code>(3). </p>
<h2>AUTHOR</h2>
<p> Steve Grubb </p>
<h2>Index</h2>
