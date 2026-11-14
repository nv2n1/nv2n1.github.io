---
title: "auparse_feed_has_data(3)"
name: "auparse_feed_has_data"
section: "3"
letter: "a"
url: "/docs/linux/man/3-auparse_feed_has_data/"
description: "auparse_feed_has_data – check if there is any data accumulating that might need flushing."
---

<h2>NAME</h2>
<p> auparse_feed_has_data &#8211; check if there is any data accumulating that might need flushing.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;auparse.h&gt;</code> </p>
<p> int auparse_feed_has_data(const auparse_state_t *au); </p>
<h2>DESCRIPTION</h2>
<p> <i>auparse_feed_has_data</i> may be called to determine if there is any records that are accumulating but not yet ready to emit. </p>
<h2>RETURN VALUE</h2>
<p> Returns 1 if any records are accumulating otherwise 0 if empty. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-auparse_feed/">auparse_feed</a></code>(3), <code><a href="/docs/linux/man/3-auparse_feed_age_events/">auparse_feed_age_events</a></code>(3) </p>
<h2>AUTHOR</h2>
<p> Steve Grubb </p>
<h2>Index</h2>
