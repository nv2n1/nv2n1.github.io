---
title: "dblink_disconnect(3)"
name: "dblink_disconnect"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dblink_disconnect/"
description: "dblink_disconnect – closes a persistent connection to a remote database"
---

<h2 class="name">NAME</h2>
<p> dblink_disconnect &#8211; closes a persistent connection to a remote database </p>
<h2>SYNOPSIS</h2>
<pre>
dblink_disconnect() returns text
dblink_disconnect(text connname) returns text
</pre>
<h2>DESCRIPTION</h2>
<p> <code>dblink_disconnect()</code> closes a connection previously opened by <code>dblink_connect()</code>. The form with no arguments closes an unnamed connection.</p>
<h2>ARGUMENTS</h2>
<p> <i>connname</i></p>
<dl>
<dt>
<dd> The name of a named connection to be closed.</dl>
<h2>RETURN VALUE</h2>
<p> Returns status, which is always OK (since any error causes the function to throw an error instead of returning).</p>
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd>
<pre><code>
SELECT dblink_disconnect();
dblink_disconnect-- -- -- -- -- -- -- -- -- -OK(1 row)
    SELECT dblink_disconnect('myconn');
dblink_disconnect-- -- -- -- -- -- -- -- -- -OK(1 row)
</code></pre>
</dl>
<h2>Index</h2>
