---
title: "ausearch_set_stop(3)"
name: "ausearch_set_stop"
section: "3"
letter: "a"
url: "/docs/linux/man/3-ausearch_set_stop/"
description: "ausearch_set_stop – set the cursor position"
---

<h2>NAME</h2>
<p>&nbsp;<wbr>ausearch_set_stop &#8211; set the cursor position</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;auparse.h&gt;</code> </p>
<p> int ausearch_set_stop(auparse_state_t *au, austop_t where); </p>
<h2>DESCRIPTION</h2>
<p> ausearch_set_stop determines where the internal cursor will stop when a search condition is met. The possible values are: </p>
<dl>
<dt>
<dd>
<dl>
<dt><i>AUSEARCH_STOP_EVENT</i></p>
<dd> This one repositions the cursors to the first field of the first record of the event containing the items searched for.</p>
<dt><i>AUSEARCH_STOP_RECORD</i></p>
<dd> This one repositions the cursors to the first field of the record containing the items searched for.</p>
<dt><i>AUSEARCH_STOP_FIELD</i></p>
<dd> This one simply stops on the current field when the evaluation of the rules becomes true.</dl>
</dl>
<h2>RETURN VALUE</h2>
<p> Returns -1 if an error occurs; otherwise, 0 for success. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ausearch_add_item/">ausearch_add_item</a></code>(3), <code><a href="/docs/linux/man/3-ausearch_add_regex/">ausearch_add_regex</a></code>(3), <code><a href="/docs/linux/man/3-ausearch_clear/">ausearch_clear</a></code>(3), <code><a href="/docs/linux/man/3-ausearch_next_event/">ausearch_next_event</a></code>(3). </p>
<h2>AUTHOR</h2>
<p> Steve Grubb </p>
<h2>Index</h2>
