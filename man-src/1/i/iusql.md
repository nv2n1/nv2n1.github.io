---
title: "iusql(1)"
name: "iusql"
section: "1"
letter: "i"
url: "/docs/linux/man/1-iusql/"
description: "isql, iusql – unixODBC command-line interactive SQL tool"
---

<h2 class="name">NAME</h2>
<p> isql, iusql &#8211; unixODBC command-line interactive SQL tool</p>
<h2>SYNOPSIS</h2>
<p> <code>isql</code> <i>DSN</i> [<i>USER</i> [<i>PASSWORD</i>]] [<i>options</i>] </p>
<h2>DESCRIPTION</h2>
<p> <code>isql</code> is a command line tool which allows the user to execute SQL in batch or interactively. It has some interesting options such as an option to generate output wrapped in an HTML table. </p>
<p> <code>iusql</code> is the same tool with built-in Unicode support. </p>
<h2>ARGUMENTS</h2>
<dl>
<dt><code>DSN</code></dt>
<dd> The Data Source Name, which should be used to make connection to the database. The data source is looked for in the /etc/odbc.ini and $HOME/.odbc.ini files in that order, with the latter overwriting the former. </dd>
<dt><code>USER</code></dt>
<dd> Specifies the database user/role under which the connection should be made. </dd>
<dt><code>PASSWORD</code></dt>
<dd> Password for the specified <code>USER</code>. </dd>
</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-b</code></dt>
<dd> Run isql in non-interactive batch mode. In this mode, the isql processes its standard input, expecting one SQL command per line. </dd>
<dt><code>-d</code><i>DELIMITER</i></dt>
<dd> Delimits columns with <i>delimiter</i>. </dd>
<dt><code>-x</code><i>HEX</i></dt>
<dd> Delimits columns with <i>HEX</i>, which is a hexadecimal code of the delimiting character in the format 0xNN &#8211; i.e. 0x09 for the TAB character. </dd>
<dt><code>-w</code></dt>
<dd> Format the result as HTML table. </dd>
<dt><code>-c</code></dt>
<dd> Output the names of the columns on the first row. Has any effect only with the <code>-d</code> or <code>-x</code> options. </dd>
<dt><code>-m</code><i>NUM</i></dt>
<dd> Limit the column display width to <i>NUM</i> characters. </dd>
<dt><code>-l</code><i>LOCALE</i></dt>
<dd> Sets locale to <i>LOCALE</i>. </dd>
<dt><code>-q</code></dt>
<dd> Wrap the character fields in double quotes. </dd>
<dt><code>-3</code></dt>
<dd> Use the ODBC 3 calls. </dd>
<dt><code>-n</code></dt>
<dd> Use the newline processing. </dd>
<dt><code>-e</code></dt>
<dd> Use the SQLExecDirect instead of Prepare. </dd>
<dt><code>-k</code></dt>
<dd> Use SQLDriverConnect. </dd>
<dt><code>-v</code></dt>
<dd> Turn on the verbose mode, where the errors are fully described. Useful for debugging. </dd>
<dt><code>&#8211;version</code></dt>
<dd> Prints the program version and exits. </dd>
</dl>
<h2>COMMANDS</h2>
<p> This section briefly describes some isql runtime commands. </p>
<p> <code>help</code></p>
<dl>
<dt>
</dt><dd> List all tables in the database.</dd></dl>
<p> <code>help </code><i>table</i></p>
<dl>
<dt>
</dt><dd> List all columns in the <i>table</i>.</dd></dl>
<p> <code>help help</code></p>
<dl>
<dt>
</dt><dd> List all help options.</dd></dl>
<h2>EXAMPLES</h2>
<pre>
$ isql WebDB MyID MyPWD -w -b &lt; My.sql
</pre>
<p> Connects to the WebDB as user MyID with password MyPWD, then execute the commands in the My.sql file and returns the results wrapped in HTML table. Each line in My.sql must contain exactly 1 SQL command, except for the last line, which must be blank (unless the <code>-n</code> option is specified). </p>
<h2>FILES</h2>
<p> <i>/etc/odbc.ini</i></p>
<dl>
<dt>
</dt><dd> System-wide DSN definitions. See <code><a href="/docs/linux/man/5-odbc-ini/">odbc.ini</a></code>(5) for details.</dd></dl>
<p> <i>$HOME/.odbc.ini</i></p>
<dl>
<dt>
</dt><dd> User-specific DSN definitions. See <code><a href="/docs/linux/man/5-odbc-ini/">odbc.ini</a></code>(5) for details.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-odbcinst/">odbcinst</a></code>(1), <code><a href="/docs/linux/man/5-odbc-ini/">odbc.ini</a></code>(5) </p>
<h2>AUTHORS</h2>
<p> The authors of unixODBC are Peter Harvey &lt;<i>pharvey [at] codebydesign.com</i>&gt; and Nick Gorham &lt;<i>nick [at] easysoft.com</i>&gt;. For the full list of contributors see the AUTHORS file. </p>
<h2>COPYRIGHT</h2>
<p> unixODBC is licensed under the GNU Lesser General Public License. For details about the license, see the COPYING file. </p>
