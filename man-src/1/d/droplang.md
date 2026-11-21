---

title: "droplang(1)"
name: "droplang"
section: "1"
letter: "d"
url: "/docs/linux/man/1-droplang/"
description: "droplang – remove a PostgreSQL procedural language"
---

<dl>
<dt> <code>droplang</code> [<i>connection-option</i>&#8230;] <i>langname</i> [<i>dbname</i>]</dt>
<dt> <code>droplang</code> [<i>connection-option</i>&#8230;] <code>&#8211;list</code> | <code>-l</code> [<i>dbname</i>]</dt></dl>
<dd>droplang is a utility for removing an existing procedural language from a PostgreSQL database. </dd>
<p> droplang is just a wrapper around the DROP EXTENSION (<code><a href="/docs/linux/man/7-drop_extension/">DROP_EXTENSION</a></code>(7)) SQL command. </p>
<dl>
<dt>
</dt><dd>
 <font SIZE="+1"> <code>Caution</code> </font> </dd>
<p> droplang is deprecated and may be removed in a future PostgreSQL release. Direct use of the <code>DROP EXTENSION</code> command is recommended instead. </p>
</dl>
<h2>OPTIONS</h2>
<p> droplang accepts the following command line arguments: </p>
<p> <i>langname</i></p>
<dl>
<dt>
</dt><dd> Specifies the name of the procedural language to be removed. (This name is lower-cased.)</dd></dl>
<p> <code>[-d]</code><i>dbname</i>, <code>[&#8211;dbname=]</code><i>dbname</i></p>
<dl>
<dt>
</dt><dd> Specifies from which database the language should be removed. The default is to use the database with the same name as the current system user.</dd></dl>
<p> <code>-e</code>, <code>&#8211;echo</code></p>
<dl>
<dt>
</dt><dd> Display SQL commands as they are executed.</dd></dl>
<p> <code>-l</code>, <code>&#8211;list</code></p>
<dl>
<dt>
</dt><dd> Show a list of already installed languages in the target database.</dd></dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
</dt><dd> Print the droplang version and exit.</dd></dl>
<p> <code>-?</code>, <code>&#8211;help</code></p>
<dl>
<dt>
</dt><dd> Show help about droplang command line arguments, and exit.</dd></dl>
<p> droplang also accepts the following command line arguments for connection parameters: </p>
<p> <code>-h </code><i>host</i>, <code>&#8211;host=</code><i>host</i></p>
<dl>
<dt>
</dt><dd> Specifies the host name of the machine on which the server is running. If host begins with a slash, it is used as the directory for the Unix domain socket.</dd></dl>
<p> <code>-p </code><i>port</i>, <code>&#8211;port=</code><i>port</i></p>
<dl>
<dt>
</dt><dd> Specifies the Internet TCP/IP port or local Unix domain socket file extension on which the server is listening for connections.</dd></dl>
<p> <code>-U </code><i>username</i>, <code>&#8211;username=</code><i>username</i></p>
<dl>
<dt>
</dt><dd> User name to connect as.</dd></dl>
<p> <code>-w</code>, <code>&#8211;no-password</code></p>
<dl>
<dt>
</dt><dd> Never issue a password prompt. If the server requires password authentication and a password is not available by other means such as a .pgpass file, the connection attempt will fail. This option can be useful in batch jobs and scripts where no user is present to enter a password.</dd></dl>
<p> <code>-W</code>, <code>&#8211;password</code></p>
<dl>
<dt>
</dt><dd> Force droplang to prompt for a password before connecting to a database. </dd>
<p> This option is never essential, since droplang will automatically prompt for a password if the server demands password authentication. However, droplang will waste a connection attempt finding out that the server wants a password. In some cases it is worth typing <code>-W</code> to avoid the extra connection attempt.</dl>
<h2>ENVIRONMENT</h2>
<p> <code>PGDATABASE</code>, <code>PGHOST</code>, <code>PGPORT</code>, <code>PGUSER</code></p>
<dl>
<dt>
</dt><dd> Default connection parameters</dd></dl>
<p> This utility, like most other PostgreSQL utilities, also uses the environment variables supported by libpq (see Section 31.14, &#8220;Environment Variables&#8221;, in the documentation).</p>
<h2>DIAGNOSTICS</h2>
<p> Most error messages are self-explanatory. If not, run droplang with the <code>&#8211;echo</code> option and see under the respective SQL command for details. Also, any default connection settings and environment variables used by the libpq front-end library will apply.</p>
<h2>NOTES</h2>
<p> Use <code><a href="/docs/linux/man/1-createlang/">createlang</a></code>(1) to add a language.</p>
<h2>EXAMPLES</h2>
<p> To remove the language pltcl: </p>
<dl>
<dt>
</dt><dd>
<pre>
$ <code>droplang pltcl dbname</code>
</pre>
</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-createlang/">createlang</a></code>(1), DROP EXTENSION (<code><a href="/docs/linux/man/7-drop_extension/">DROP_EXTENSION</a></code>(7)), DROP LANGUAGE (<code><a href="/docs/linux/man/7-drop_language/">DROP_LANGUAGE</a></code>(7)) </p>
