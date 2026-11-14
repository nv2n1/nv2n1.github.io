---
title: "dblink_get_notify(3)"
name: "dblink_get_notify"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dblink_get_notify/"
description: "dblink_get_notify – retrieve async notifications on a connection"
---

<h2 class="name">NAME</h2>
<p> dblink_get_notify &#8211; retrieve async notifications on a connection </p>
<h2>SYNOPSIS</h2>
<pre>
dblink_get_notify() returns setof (notify_name text, be_pid int, extra text)
dblink_get_notify(text connname) returns setof (notify_name text, be_pid int, extra text)
</pre>
<h2>DESCRIPTION</h2>
<p> <code>dblink_get_notify</code> retrieves notifications on either the unnamed connection, or on a named connection if specified. To receive notifications via dblink, <code>LISTEN</code> must first be issued, using <code>dblink_exec</code>. For details see <code><a href="/docs/linux/man/7-listen/">LISTEN</a></code>(7) and <code><a href="/docs/linux/man/7-notify/">NOTIFY</a></code>(7).</p>
<h2>ARGUMENTS</h2>
<p> <i>connname</i></p>
<dl>
<dt>
<dd> The name of a named connection to get notifications on.</dl>
<h2>RETURN VALUE</h2>
<p> Returns setof (notify_name text, be_pid int, extra text), or an empty set if none.</p>
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd>
<pre><code>
SELECT dblink_exec('LISTEN virtual');
dblink_exec-- -- -- -- -- -- -LISTEN(1 row)
    SELECT *FROM dblink_get_notify();
notify_name | be_pid | extra-- -- -- -- -- -- -+-- -- -- --+-- -- -- -(0 rows)NOTIFY virtual;
NOTIFY
SELECT *FROM dblink_get_notify();
notify_name | be_pid | extra-- -- -- -- -- -- -+-- -- -- --+-- -- -- -virtual | 1229 |
    (1 row)
</code></pre>
</dl>
<h2>Index</h2>
