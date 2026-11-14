---
title: "dblink_error_message(3)"
name: "dblink_error_message"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dblink_error_message/"
description: "dblink_error_message – gets last error message on the named connection"
---

<h2 class="name">NAME</h2>
<p> dblink_error_message &#8211; gets last error message on the named connection </p>
<h2>SYNOPSIS</h2>
<pre>
dblink_error_message(text connname) returns text
</pre>
<h2>DESCRIPTION</h2>
<p> <code>dblink_error_message</code> fetches the most recent remote error message for a given connection.</p>
<h2>ARGUMENTS</h2>
<p> <i>connname</i></p>
<dl>
<dt>
<dd> Name of the connection to use.</dl>
<h2>RETURN VALUE</h2>
<p> Returns last error message, or an empty string if there has been no error in this connection.</p>
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd>
<pre>
SELECT dblink_error_message('dtest1');
</pre>
</dl>
<h2>Index</h2>
