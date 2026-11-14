---
title: "auparse_get_field_num(3)"
name: "auparse_get_field_num"
section: "3"
letter: "a"
url: "/docs/linux/man/3-auparse_get_field_num/"
description: "auparse_get_field_num – get current field cursor location"
---

<h2>NAME</h2>
<p> auparse_get_field_num &#8211; get current field cursor location</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;auparse.h&gt;</code> </p>
<p> unsigned int auparse_get_field_num(auparse_state_t *au); </p>
<h2>DESCRIPTION</h2>
<p> auparse_get_field_num will retreive the internal library cursors current field location in the current record. Fields within the same record are numbered starting from 0. This is generally not needed but there are some cases where one may want to know the exact field being looked at. </p>
<h2>RETURN VALUE</h2>
<p> Returns the current field cursor location. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-auparse_goto_field_num/">auparse_goto_field_num</a></code>(3),<code><a href="/docs/linux/man/3-auparse_get_record_num/">auparse_get_record_num</a></code>(3). </p>
<h2>AUTHOR</h2>
<p> Steve Grubb </p>
<h2>Index</h2>
