---
title: "dblink_cancel_query(3)"
name: "dblink_cancel_query"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dblink_cancel_query/"
description: "dblink_cancel_query – cancels any active query on the named connection"
---

<h2 class="name">NAME</h2>
<p> dblink_cancel_query &#8211; cancels any active query on the named connection </p>
<h2>SYNOPSIS</h2>
<pre>
dblink_cancel_query(text connname) returns text
</pre>
<h2>DESCRIPTION</h2>
<p> <code>dblink_cancel_query</code> attempts to cancel any query that is in progress on the named connection. Note that this is not certain to succeed (since, for example, the remote query might already have finished). A cancel request simply improves the odds that the query will fail soon. You must still complete the normal query protocol, for example by calling <code>dblink_get_result</code>.</p>
<h2>ARGUMENTS</h2>
<p> <i>connname</i></p>
<dl>
<dt>
<dd> Name of the connection to use.</dl>
<h2>RETURN VALUE</h2>
<p> Returns OK if the cancel request has been sent, or the text of an error message on failure.</p>
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd>
<pre>
SELECT dblink_cancel_query('dtest1');
</pre>
</dl>
<h2>Index</h2>
