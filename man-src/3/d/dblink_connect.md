---
title: "dblink_connect(3)"
name: "dblink_connect"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dblink_connect/"
description: "dblink_connect – opens a persistent connection to a remote database"
---

<h2 class="name">NAME</h2>
<p> dblink_connect &#8211; opens a persistent connection to a remote database </p>
<h2>SYNOPSIS</h2>
<pre>
dblink_connect(text connstr) returns text
dblink_connect(text connname, text connstr) returns text
</pre>
<h2>DESCRIPTION</h2>
<p> <code>dblink_connect()</code> establishes a connection to a remote PostgreSQL database. The server and database to be contacted are identified through a standard libpq connection string. Optionally, a name can be assigned to the connection. Multiple named connections can be open at once, but only one unnamed connection is permitted at a time. The connection will persist until closed or until the database session is ended. </p>
<p> The connection string may also be the name of an existing foreign server. It is recommended to use the <code>postgresql_fdw_validator</code> when defining the corresponding foreign-data wrapper. See the example below, as well as the following: CREATE FOREIGN DATA WRAPPER (<code><a href="/docs/linux/man/7-create_foreign_data_wrapper/">CREATE_FOREIGN_DATA_WRAPPER</a></code>(7)), CREATE SERVER (<code><a href="/docs/linux/man/7-create_server/">CREATE_SERVER</a></code>(7)), CREATE USER MAPPING (<code><a href="/docs/linux/man/7-create_user_mapping/">CREATE_USER_MAPPING</a></code>(7))</p>
<h2>ARGUMENTS</h2>
<p> <i>connname</i></p>
<dl>
<dt>
<dd> The name to use for this connection; if omitted, an unnamed connection is opened, replacing any existing unnamed connection.</dl>
<p> <i>connstr</i></p>
<dl>
<dt>
<dd> libpq-style connection info string, for example hostaddr=127.0.0.1 port=5432 dbname=mydb user=postgres password=mypasswd. For details see <code>PQconnectdb</code> in Section 31.1, &#8220;Database Connection Control Functions&#8221;, in the documentation.</dl>
<h2>RETURN VALUE</h2>
<p> Returns status, which is always OK (since any error causes the function to throw an error instead of returning).</p>
<h2>NOTES</h2>
<p> Only superusers may use <code>dblink_connect</code> to create non-password-authenticated connections. If non-superusers need this capability, use <code>dblink_connect_u</code> instead. </p>
<p> It is unwise to choose connection names that contain equal signs, as this opens a risk of confusion with connection info strings in other dblink functions.</p>
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd>
<pre><code>
SELECT dblink_connect('dbname=postgres');
dblink_connect-- -- -- -- -- -- -- --OK(1 row)
    SELECT dblink_connect('myconn', 'dbname=postgres');
 dblink_connect
----------------
 OK
(1 row)
-- FOREIGN DATA WRAPPER functionality
-- Note: local connection must require password authentication for this to work properly
--       Otherwise, you will receive the following error from dblink_connect():
--       ----------------------------------------------------------------------
--       ERROR:  password is required
--       DETAIL:  Non-superuser cannot connect if the server does not request a password.
--       HINT:  Target server's authentication method must be changed.
CREATE USER dblink_regression_test WITH PASSWORD 'secret';
 CREATE FOREIGN DATA WRAPPER postgresql VALIDATOR postgresql_fdw_validator;
 CREATE SERVER fdtest FOREIGN DATA WRAPPER postgresql OPTIONS(hostaddr '127.0.0.1', dbname 'contrib_regression');
 CREATE USER MAPPING FOR dblink_regression_test SERVER fdtest OPTIONS(user 'dblink_regression_test', password 'secret');
 GRANT USAGE ON FOREIGN SERVER fdtest TO dblink_regression_test;
 GRANT SELECT ON TABLE foo TO dblink_regression_test;
 \set ORIGINAL_USER : USER
