---
title: "dblink_connect_u(3)"
name: "dblink_connect_u"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dblink_connect_u/"
description: "dblink_connect_u – opens a persistent connection to a remote database, insecurely"
---

<h2 class="name">NAME</h2>
<p> dblink_connect_u &#8211; opens a persistent connection to a remote database, insecurely </p>
<h2>SYNOPSIS</h2>
<pre>
dblink_connect_u(text connstr) returns text
dblink_connect_u(text connname, text connstr) returns text
</pre>
<h2>DESCRIPTION</h2>
<p> <code>dblink_connect_u()</code> is identical to <code>dblink_connect()</code>, except that it will allow non-superusers to connect using any authentication method. </p>
<p> If the remote server selects an authentication method that does not involve a password, then impersonation and subsequent escalation of privileges can occur, because the session will appear to have originated from the user as which the local PostgreSQL server runs. Also, even if the remote server does demand a password, it is possible for the password to be supplied from the server environment, such as a ~/.pgpass file belonging to the server&#8217;s user. This opens not only a risk of impersonation, but the possibility of exposing a password to an untrustworthy remote server. Therefore, <code>dblink_connect_u()</code> is initially installed with all privileges revoked from PUBLIC, making it un-callable except by superusers. In some situations it may be appropriate to grant EXECUTE permission for <code>dblink_connect_u()</code> to specific users who are considered trustworthy, but this should be done with care. It is also recommended that any ~/.pgpass file belonging to the server&#8217;s user <i>not</i> contain any records specifying a wildcard host name. </p>
<p> For further details see <code>dblink_connect()</code>. </p>
<h2>Index</h2>
