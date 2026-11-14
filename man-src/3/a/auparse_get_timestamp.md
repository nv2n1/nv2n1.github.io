---
title: "auparse_get_timestamp(3)"
name: "auparse_get_timestamp"
section: "3"
letter: "a"
url: "/docs/linux/man/3-auparse_get_timestamp/"
description: "auparse_get_timestamp – access timestamp of the event"
---

<h2>NAME</h2>
<p> auparse_get_timestamp &#8211; access timestamp of the event</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;auparse.h&gt;</code> </p>
<p> const au_event_t *auparse_get_timestamp(auparse_state_t *au); </p>
<h2>DESCRIPTION</h2>
<p> auparse_get_timestamp provides an accessor function for the event&#8217;s timestamp data structure. The data structure is as follows: </p>
<pre><code>
typedef struct
{
    time_t sec;           // Event seconds
    unsigned int milli;   // millisecond of the timestamp
    unsigned long serial; // Serial number of the event
    const char *host;     // Machine's node name
} au_event_t;
</code></pre>
<h2>RETURN VALUE</h2>
<p> Returns NULL if an error occurs; otherwise, a valid pointer to the data. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-auparse_get_time/">auparse_get_time</a></code>(3), <code><a href="/docs/linux/man/3-auparse_get_milli/">auparse_get_milli</a></code>(3), <code><a href="/docs/linux/man/3-auparse_get_serial/">auparse_get_serial</a></code>(3), <code><a href="/docs/linux/man/3-auparse_get_node/">auparse_get_node</a></code>(3), <code><a href="/docs/linux/man/3-auparse_timestamp_compare/">auparse_timestamp_compare</a></code>(3). </p>
<h2>AUTHOR</h2>
<p> Steve Grubb </p>
<h2>Index</h2>
