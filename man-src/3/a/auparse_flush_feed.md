---
title: "auparse_flush_feed(3)"
name: "auparse_flush_feed"
section: "3"
letter: "a"
url: "/docs/linux/man/3-auparse_flush_feed/"
description: "auparse_flush_feed – flush any unconsumed feed data through parser."
---

<h2>NAME</h2>
<p> auparse_flush_feed &#8211; flush any unconsumed feed data through parser.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;auparse.h&gt;</code> </p>
<p> int auparse_flush_feed(auparse_state_t *au); </p>
<h2>DESCRIPTION</h2>
<p> <i>auparse_flush_feed</i> should be called to signal the end of feed input data and flush any pending parse data through the parsing system. </p>
<h2>RETURN VALUE</h2>
<p> Returns -1 if an error occurs; otherwise, 0 for success. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-auparse_feed/">auparse_feed</a></code>(3), <code><a href="/docs/linux/man/3-auparse_feed_age_events/">auparse_feed_age_events</a></code>(3), <code><a href="/docs/linux/man/3-auparse_feed_has_data/">auparse_feed_has_data</a></code>(3) </p>
<h2>AUTHOR</h2>
<p> John Dennis </p>
<h2>Index</h2>
