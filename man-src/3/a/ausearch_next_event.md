---
title: "ausearch_next_event(3)"
name: "ausearch_next_event"
section: "3"
letter: "a"
url: "/docs/linux/man/3-ausearch_next_event/"
description: "ausearch_next_event – find the next event that meets search criteria"
---

<h2>NAME</h2>
<p> ausearch_next_event &#8211; find the next event that meets search criteria</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;auparse.h&gt;</code> </p>
<p> int ausearch_next_event(auparse_state_t *au); </p>
<h2>DESCRIPTION</h2>
<p> ausearch_next_event will scan the input source and evaluate whether any record in an event contains the data being searched for. Evaluation is done at the record level. </p>
<h2>RETURN VALUE</h2>
<p> Returns -1 if an error occurs, 0 if no matches, and 1 for success. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ausearch_add_item/">ausearch_add_item</a></code>(3), <code><a href="/docs/linux/man/3-ausearch_add_regex/">ausearch_add_regex</a></code>(3), <code><a href="/docs/linux/man/3-ausearch_set_stop/">ausearch_set_stop</a></code>(3). </p>
<h2>AUTHOR</h2>
<p> Steve Grubb </p>
<h2>Index</h2>
