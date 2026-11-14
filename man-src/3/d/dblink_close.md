---
title: "dblink_close(3)"
name: "dblink_close"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dblink_close/"
description: "dblink_close – closes a cursor in a remote database"
---

<h2 class="name">NAME</h2>
<p> dblink_close &#8211; closes a cursor in a remote database </p>
<h2>SYNOPSIS</h2>
<pre><code>
dblink_close(text cursorname[, bool fail_on_error]) returns text
    dblink_close(text connname, text cursorname[, bool fail_on_error]) returns text
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>dblink_close</code> closes a cursor previously opened with <code>dblink_open</code>.</p>
<h2>ARGUMENTS</h2>
<p> <i>connname</i></p>
<dl>
<dt>
<dd> Name of the connection to use; omit this parameter to use the unnamed connection.</dl>
<p> <i>cursorname</i></p>
<dl>
<dt>
<dd> The name of the cursor to close.</dl>
<p> <i>fail_on_error</i></p>
<dl>
<dt>
<dd> If true (the default when omitted) then an error thrown on the remote side of the connection causes an error to also be thrown locally. If false, the remote error is locally reported as a NOTICE, and the function&#8217;s return value is set to ERROR.</dl>
<h2>RETURN VALUE</h2>
<p> Returns status, either OK or ERROR.</p>
<h2>NOTES</h2>
<p> If <code>dblink_open</code> started an explicit transaction block, and this is the last remaining open cursor in this connection, <code>dblink_close</code> will issue the matching <code>COMMIT</code>.</p>
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd>
<pre><code>
SELECT dblink_connect('dbname=postgres');
dblink_connect-- -- -- -- -- -- -- --OK(1 row)
    SELECT dblink_open('foo', 'select proname, prosrc from pg_proc');
dblink_open-- -- -- -- -- -- -OK(1 row)
    SELECT dblink_close('foo');
dblink_close-- -- -- -- -- -- --OK(1 row)
</code></pre>
</dl>
<h2>Index</h2>
