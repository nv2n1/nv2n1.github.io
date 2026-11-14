---
title: "auparse_get_type(3)"
name: "auparse_get_type"
section: "3"
letter: "a"
url: "/docs/linux/man/3-auparse_get_type/"
description: "auparse_get_type – get record’s type"
---

<h2>NAME</h2>
<p> auparse_get_type &#8211; get record&#8217;s type</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;auparse.h&gt;</code> </p>
<p> int auparse_get_type(auparse_state_t *au); </p>
<h2>DESCRIPTION</h2>
<p> auparse_get_type will return the integer value for the current record of the current event. </p>
<h2>RETURN VALUE</h2>
<p> auparse_get_type returns 0 if an error occurs; otherwise, the record&#8217;s type. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-auparse_get_type_name/">auparse_get_type_name</a>(3),</code><a href="/docs/linux/man/3-auparse_next_record/">auparse_next_record</a><code>(3).</code> </p>
<h2>AUTHOR</h2>
<p> Steve Grubb </p>
<h2>Index</h2>
