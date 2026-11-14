---
title: "dblink_is_busy(3)"
name: "dblink_is_busy"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dblink_is_busy/"
description: "dblink_is_busy – checks if connection is busy with an async query"
---

<h2 class="name">NAME</h2>
<p> dblink_is_busy &#8211; checks if connection is busy with an async query </p>
<h2>SYNOPSIS</h2>
<pre>
dblink_is_busy(text connname) returns int
</pre>
<h2>DESCRIPTION</h2>
<p> <code>dblink_is_busy</code> tests whether an async query is in progress.</p>
<h2>ARGUMENTS</h2>
<p> <i>connname</i></p>
<dl>
<dt>
<dd> Name of the connection to check.</dl>
<h2>RETURN VALUE</h2>
<p> Returns 1 if connection is busy, 0 if it is not busy. If this function returns 0, it is guaranteed that <code>dblink_get_result</code> will not block.</p>
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd>
<pre>
SELECT dblink_is_busy('dtest1');
</pre>
</dl>
<h2>Index</h2>
