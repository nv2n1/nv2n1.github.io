---
title: "auparse_feed_age_events(3)"
name: "auparse_feed_age_events"
section: "3"
letter: "a"
url: "/docs/linux/man/3-auparse_feed_age_events/"
description: "auparse_feed_age_events – check events for complete based on time."
---

<h2>NAME</h2>
<p> auparse_feed_age_events &#8211; check events for complete based on time.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;auparse.h&gt;</code> </p>
<p> void auparse_feed_age_events(auparse_state_t *au); </p>
<h2>DESCRIPTION</h2>
<p> <i>auparse_feed_age_events</i> should be called to see if any events are complete based on the current clock time. Any newly complete events will be passed to the callback function. </p>
<h2>RETURN VALUE</h2>
<p> None. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-auparse_feed/">auparse_feed</a></code>(3), <code><a href="/docs/linux/man/3-auparse_flush_feed/">auparse_flush_feed</a></code>(3), <code><a href="/docs/linux/man/3-auparse_feed_has_data/">auparse_feed_has_data</a></code>(3) </p>
<h2>AUTHOR</h2>
<p> Steve Grubb </p>
<h2>Index</h2>
