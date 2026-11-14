---
title: "createlang(1)"
name: "createlang"
section: "1"
letter: "c"
url: "/docs/linux/man/1-createlang/"
description: "createlang – install a PostgreSQL procedural language"
---

<h2 class="name">NAME</h2>
<p> createlang &#8211; install a PostgreSQL procedural language </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>createlang</code> [<i>connection-option</i>&#8230;] <i>langname</i> [<i>dbname</i>]</p>
<dt> <code>createlang</code> [<i>connection-option</i>&#8230;] <code>&#8211;list</code> | <code>-l</code> [<i>dbname</i>]</dl>
<h2>DESCRIPTION</h2>
<dd>createlang is a utility for adding a procedural language to a PostgreSQL database. </p>
<p> createlang is just a wrapper around the CREATE EXTENSION (<code><a href="/docs/linux/man/7-create_extension/">CREATE_EXTENSION</a></code>(7)) SQL command. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Caution</code> </font> </p>
<p> createlang is deprecated and may be removed in a future PostgreSQL release. Direct use of the <code>CREATE EXTENSION</code> command is recommended instead. </p>
</dl>
<h2>OPTIONS</h2>
<p> createlang accepts the following command-line arguments: </p>
<p> <i>langname</i></p>
<dl>
<dt>
<dd> Specifies the name of the procedural language to be installed. (This name is lower-cased.)</dl>
<p> <code>[-d]</code><i>dbname</i>, <code>[&#8211;dbname=]</code><i>dbname</i></p>
<dl>
<dt>
<dd> Specifies the database to which the language should be added. The default is to use the database with the same name as the current system user.</dl>
<p> <code>-e</code>, <code>&#8211;echo</code></p>
<dl>
<dt>
<dd> Display SQL commands as they are executed.</dl>
<p> <code>-l</code>, <code>&#8211;list</code></p>
<dl>
<dt>
<dd> Show a list of already installed languages in the target database.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Print the createlang version and exit.</dl>
<p> <code>-?</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show help about createlang command line arguments, and exit.</dl>
<p> createlang also accepts the following command-line arguments for connection parameters: </p>
<p> <code>-h </code><i>host</i>, <code>&#8211;host=</code><i>host</i></p>
<dl>
<dt>
<dd> Specifies the host name of the machine on which the server is running. If the value begins with a slash, it is used as the directory for the Unix domain socket.</dl>
<p> <code>-p </code><i>port</i>, <code>&#8211;port=</code><i>port</i></p>
<dl>
<dt>
<dd> Specifies the TCP port or local Unix domain socket file extension on which the server is listening for connections.</dl>
<p> <code>-U </code><i>username</i>, <code>&#8211;username=</code><i>username</i></p>
<dl>
<dt>
<dd> User name to connect as.</dl>
<p> <code>-w</code>, <code>&#8211;no-password</code></p>
<dl>
<dt>
<dd> Never issue a password prompt. If the server requires password authentication and a password is not available by other means such as a .pgpass file, the connection attempt will fail. This option can be useful in batch jobs and scripts where no user is present to enter a password.</dl>
<p> <code>-W</code>, <code>&#8211;password</code></p>
<dl>
<dt>
<dd> Force createlang to prompt for a password before connecting to a database. </p>
<p> This option is never essential, since createlang will automatically prompt for a password if the server demands password authentication. However, createlang will waste a connection attempt finding out that the server wants a password. In some cases it is worth typing <code>-W</code> to avoid the extra connection attempt.</dl>
<h2>ENVIRONMENT</h2>
<p> <code>PGDATABASE</code>, <code>PGHOST</code>, <code>PGPORT</code>, <code>PGUSER</code></p>
<dl>
<dt>
<dd> Default connection parameters</dl>
<p> This utility, like most other PostgreSQL utilities, also uses the environment variables supported by libpq (see Section 31.14, &#8220;Environment Variables&#8221;, in the documentation).</p>
<h2>DIAGNOSTICS</h2>
<p> Most error messages are self-explanatory. If not, run createlang with the <code>&#8211;echo</code> option and see the respective SQL command for details. Also, any default connection settings and environment variables used by the libpq front-end library will apply.</p>
<h2>NOTES</h2>
<p> Use <code><a href="/docs/linux/man/1-droplang/">droplang</a></code>(1) to remove a language.</p>
<h2>EXAMPLES</h2>
<p> To install the language pltcl into the database template1: </p>
<dl>
<dt>
<dd>
<pre>
$ <code>createlang pltcl template1</code>
</pre>
</dl>
<p> Note that installing the language into template1 will cause it to be automatically installed into subsequently-created databases as well.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-droplang/">droplang</a></code>(1), CREATE EXTENSION (<code><a href="/docs/linux/man/7-create_extension/">CREATE_EXTENSION</a></code>(7)), CREATE LANGUAGE (<code><a href="/docs/linux/man/7-create_language/">CREATE_LANGUAGE</a></code>(7)) </p>
<h2>Index</h2>
