---
title: "gda-sql-5-0(1)"
name: "gda-sql-5-0"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gda-sql-5-0/"
description: "gda-sql – an SQL console based on Libgda"
---

<p>gda-sql &#8211; an SQL console based on Libgda</p>
<h2>Synopsis</h2>
<p><code>gda-sql</code> [&#8211;help] [-v] [&#8211;version] [-o] [&#8211;output-file <i>&lt;filename&gt;</i>] [-C] [&#8211;command] [-f] [&#8211;commands-file <i>&lt;filename&gt;</i>] [-i] [&#8211;interactive] [-l] [&#8211;list-dsn] [-L] [&#8211;list-providers] [-s] [&#8211;http-port <i>&lt;port&gt;</i>] [-t] [&#8211;http-token <i>&lt;token phrase&gt;</i>] [&#8211;data-files-list] [&#8211;data-files-purge <i>&lt;criteria&gt;</i>] [connection&#8217;s spec] [connection&#8217;s spec&#8230;] </p>
<h2>Description</h2>
<p>gda-sql is an SQL console based on the <i>Libgda</i> library. </p>
<p> It enables you to type in queries interactively, issue them to be executed by a connection, and see the query results. </p>
<p> Several connections can be opened at the same time, allowing you to switch the active connection to any opened connection. When starting, gda-sql opens a connection for each connection specified on the command line (plus optionally one corresponding to the <code>GDA_SQL_CNC</code> environment variable). The prompt indicates the current connection used when executing commands. See the <code>.c</code> internal command for an explanation about the syntax to specify a connection on the command line. </p>
<p> Alternatively, input can be from a file. In addition, it provides a number of meta-commands and various shell-like features to facilitate writing scripts and automating a wide variety of tasks. </p>
<p> It is also possible to run the tool as a script using the classic &#8216;#!&#8217; string at the start of a script file, with the limitation that behaviour of arguments passed on the line after the &#8216;#!&#8217; command is undefined. Example: </p>
<p> <code>#!/bin/path/to/gda-sql</code> </p>
<p> <code>#!/usr/bin/env gda-sql</code> </p>
<h2>Options</h2>
<p>gda-sql accepts the following options: </p>
<dl>
<dt><code>&#8211;help</code></p>
<dd>Show command-line options.</p>
<dt><code>-o, &#8211;output-file </code><i>&lt;filename&gt;</i></p>
<dd>Specifies a file to which outputs are redirected.</p>
<dt><code>-C, &#8211;command</code></p>
<dd>Run only single command (SQL or internal) and exit.</p>
<dt><code>-f, &#8211;commands-file </code><i>&lt;filename&gt;</i></p>
<dd>Execute commands from <i>&lt;filename&gt;</i>, then exit (except if -i specified).</p>
<dt><code>-i, &#8211;interactive</code></p>
<dd>Keep the console opened after executing a file (used with the -f option).</p>
<dt><code>-l, &#8211;list-dsn</code></p>
<dd>List configured data sources and exit.</p>
<dt><code>-L, &#8211;list-providers</code></p>
<dd>List installed database providers and exit</p>
<dt><code>-s, &#8211;http-port </code><i>&lt;port&gt;</i></p>
<dd>Starts the embedded HTTP server on port <i>&lt;port&gt;</i></p>
<dt><code>-t, &#8211;http-token </code><i>&lt;token phrase&gt;</i></p>
<dd>Requires HTTP clients to authenticate by providing the <i>&lt;token phrase&gt;</i> (empty phrase by default)</p>
<dt><code>&#8211;data-files-list</code></p>
<dd>Lists all the files used to hold information related to each connection (ie. information gathered by the tool about the connection such as meta data, defined statements,&#8230;)</p>
<dt><code>&#8211;data-files-purge </code><i>&lt;criteria&gt;</i></p>
<dd>Removes file used to hold information related to each connection for the criteria passed as argument (note that adding <code>&quot;list-only&quot;</code> to the criteria, either before or after it using a comma, will not actually remove the file): </p>
<p> <code>&quot;non-dsn&quot;</code>: remove all the files which do not correspond to a DSN (data source name). These are the files created when a connection is specified using connection parameters instead of using a DSN </p>
<p> <code>&quot;non-exist-dsn&quot;</code>: same as <code>&quot;non-dsn&quot;</code> except it also removes the files which were for DSN which don&#8217;t exist anymore </p>
<p> <code>&quot;all&quot;</code>: remove all the files, for a complete cleanup </p>
<p> For example: <code>&#8211;data-files-purge all,list-only</code> lists all the files (which would be removed if the command was <code>&#8211;data-files-purge all</code>). </p>
</dl>
<h2>Environment</h2>
<p>gda-sql can be configured through some environment variables: </p>
<dl>
<dt><code>GDA_SQL_CNC</code></p>
<dd>to define a connection to systematically be opened when the program starts.</p>
<dt><code>PAGER</code></p>
<dd>to define a text pager program to use (by default determined by the system).</p>
<dt><code>GDA_NO_PAGER</code></p>
<dd>to specify that no text pager should be used.</p>
<dt><code>GDA_SQL_EDITOR EDITOR VISUAL</code></p>
<dd>to define a text editor to be used (variables are examined in this order).</p>
<dt><code>GDA_SQL_VIEWER_PNG</code></p>
<dd>to define a PNG viewer.</p>
<dt><code>GDA_SQL_VIEWER_PDF</code></p>
<dd>to define a PDF viewer.</p>
<dt><code>GDA_SQL_HISTFILE</code></p>
<dd>to define the history file name to use (by default .gdasql_history), set to NO_HISTORY to disable history logging.</p>
<dt><code>GDA_DATA_MODEL_DUMP_ROW_NUMBERS</code></p>
<dd>if set, the first column of the output will contain row numbers</p>
<dt><code>GDA_DATA_MODEL_DUMP_ATTRIBUTES</code></p>
<dd>if set, also dump the data model&#8217;s columns&#8217; types and value&#8217;s attributes</p>
<dt><code>GDA_DATA_MODEL_DUMP_TITLE</code></p>
<dd>if set, also dump the data model&#8217;s title</p>
<dt><code>GDA_DATA_MODEL_NULL_AS_EMPTY</code></p>
<dd>if set, replace the &#8216;NULL&#8217; string with an empty string for NULL values</p>
<dt><code>GDA_DATA_MODEL_DUMP_TRUNCATE</code></p>
<dd>if set to a numeric value, truncates the output to the width specified by the value. If the value is -1 then the actual terminal size (if it can be determined) is used </p>
<dt>gda-sql can be compiled with support for binary relocatibility.</p>
<dd>This will cause data, plug-ins and configuration files to be searched relative to the location of the gda-sql executable file. </p>
</dl>
<h2>Files</h2>
<p>gda-sql stores data source definitions (DSN) in Libgda defined files ($HOME/.local/share/libgda and /etc/libgda-5.0/config where ${prefix} is typically /usr). </p>
<p> For each connection defined by a DSN, all the information regarding the connection (such as the meta data) is stored in a $HOME/.local/share/libgda/gda-sql-&lt;DSN&gt;.db file. </p>
<h2>SQL commands</h2>
<p>You can run any SQL understood by the database engine of the current connection. Additionally SQL statement can contain variables expressed as <i>##&lt;name&gt;::&lt;type&gt;</i> where <i>&lt;name&gt;</i> is the variable&#8217;s name and <i>&lt;type&gt;</i> is its declared type (which can be &quot;int&quot;, &quot;string&quot;, &quot;boolean&quot;, &quot;time&quot;, &quot;date&quot;, &quot;timestamp&quot; (and other types defined by GLib&#8217;s syntax). </p>
<p> Use the <i>.set</i> internal command to set variable&#8217;s values. </p>
<h2>Internal commands</h2>
<p>In addition to SQL commands, gda-sql supports internal commands which differ from SQL commands because they start with the &quot;.&quot; or &quot;\&quot; character. These commands are: </p>
<dl>
<dt><code>.?</code></p>
<dd>Lists all internal commands</p>
<dt><code>.bind</code></p>
<dd>Bind two or more connections into a single new one (allowing SQL commands to be executed across multiple connections). <code>.bind &lt;CNC_NAME&gt; &lt;CNC_NAME1&gt; &lt;CNC_NAME2&gt; [&lt;CNC_NAME&gt; &#8230;]</code> creates a new connection named <i>&lt;CNC_NAME&gt;</i> which binds the tables of the <i>&lt;CNC_NAME1&gt;</i>, <i>&lt;CNC_NAME2&gt;</i> and any other connection specified.</p>
<dt><code>.c</code></p>
<dd>Opens a connection or sets the current connection. Username and password can pe specified using the <code>&lt;USERNAME&gt;[:&lt;PASSWORD&gt;]@&lt;DSN_NAME&gt;</code> or <code>&lt;USERNAME&gt;[:&lt;PASSWORD&gt;]@&lt;CNC_DEFINITION&gt;</code> syntax, and if a username or a password is required but not specified, it will ba asked interactively. </p>
<p> <code>.c &lt;CNC_NAME&gt; &lt;DSN_NAME&gt;</code> opens a connection internally known as <i>&lt;CNC_NAME&gt;</i>, using the specified DSN. </p>
<p> <code>.c &lt;CNC_NAME&gt; &lt;CNC_DEFINITION&gt; </code> opens a connection internally known as <i>&lt;CNC_NAME&gt;</i>, using a connection specified by <i>&lt;CNC_DEFINITION&gt;</i> which is similar to the <i>&lt;DSN_DEFINITION&gt;</i> parameter of the <code>.lc</code> command. </p>
<p> <code>.c &lt;CNC_NAME&gt;</code> sets the current connection to the connection known as <i>&lt;CNC_NAME&gt;</i>. </p>
<p> <code>.c ~</code> or <code>.c ~&lt;CNC_NAME&gt;</code> set the current connection to the meta data corresponding to the current connection (for the first notation) or to the meta data corresponding to the <i>&lt;CNC_NAME&gt;</i> connection.</p>
<dt><code>.close</code></p>
<dd>Closes a connection. Full syntax is: <code>.close &lt;CNC_NAME&gt;</code>.</p>
<dt><code>.cd</code></p>
<dd>Changes the current working directory. Full syntax is: <code>.cd &lt;DIR_NAME&gt;</code>.</p>
<dt><code>.copyright</code></p>
<dd>Displays copyright information.</p>
<dt><code>.d</code></p>
<dd>Lists all database objects if no argument is provided. <code>.d &lt;OBJ_NAME&gt;</code> gives details about the specified object and <code>.d &lt;SCHEMA&gt;.*</code> lists all objects in specified schema.</p>
<dt><code>.dn</code></p>
<dd>Lists all schemas if no argument is provided. <code>.d &lt;SCHEMA_NAME&gt;</code> lists specified schema.</p>
<dt><code>.dt</code></p>
<dd>Lists all tables if no argument is provided. <code>.d &lt;TABLE_NAME&gt;</code> lists specified table.</p>
<dt><code>.dv</code></p>
<dd>Lists all views if no argument is provided. <code>.d &lt;VIEW_NAME&gt;</code> lists specified view.</p>
<dt><code>.fkdeclare</code></p>
<dd>Declares a new foreign key (no constraint is added to the database). The meta data is modified to take into account a foreign key constraint. The foreign key specification is <code> &lt;fkname&gt; &lt;tableA&gt;(&lt;colA&gt;,&#8230;) &lt;tableB&gt;(&lt;colB&gt;,&#8230;)</code> where <code>&lt;fkname&gt;</code> is the name given to the foreign key constraint and <code>&lt;tableA&gt;</code> references <code>&lt;tableB&gt;</code> using the columns mentionned between the parenthesis. Note that the (<code>&lt;fkname&gt;</code>, <code>&lt;tableA&gt;</code>, <code>&lt;tableB&gt;</code>) triplet uniquely identifies a declared foreign key (declaring a new foreign key with the same triplet will remove any previously declared one). <i>Note:</i> any actual foreign key constraint will always have precedence over any declared foreign key.</p>
<dt><code>.fkundeclare</code></p>
<dd>Un-declares a foreign key (does the opposite of <code>.fkdeclare</code>).</p>
<dt><code>.e</code></p>
<dd>Edits the query buffer with external editor, if no argument is provided. <code>.e &lt;FILE_NAME&gt;</code> edits the specified file name. The external editor can be specified using environment variables.</p>
<dt><code>.echo</code></p>
<dd>Sends output to stdout, full command is: <code>.echo [&lt;TEXT&gt;]</code>.</p>
<dt><code>.export</code></p>
<dd>Exports internal parameter or table&#8217;s value to the FILE file. Internal parameters are named values used when SQL statement containing variables are executed. </p>
<p> <code>.export &lt;NAME&gt; &lt;FILE_NAME&gt;</code> exports the contents of the <i>&lt;NAME&gt;</i> parameter to the specified file. </p>
<p> <code>.export &lt;TABLE&gt; &lt;COLUMN&gt; &lt;ROW_CONDITION&gt; &lt;FILE_NAME&gt;</code> exports the value of the <i>&lt;TABLE&gt;</i> table, column <i>&lt;COLUMN&gt;</i> for the row selected by <i>&lt;ROW_CONDITION&gt;</i> to the specified file. This is most useful to export BLOBs.</p>
<dt><code>.g</code></p>
<dd>Executes the contents of the query buffer, if no parameter is provided. <code>.g &lt;QUERY_BUFFER_NAME&gt;</code> Executes the contents of the specified query buffer. A named query buffer is created using the <code>.qs</code> command.</p>
<dt><code>.graph</code></p>
<dd>Creates a graph of tables showing their relations (based on foreign key constraints). If no argument is provided, the graph lists all tables. <code>.graph &lt;TABLE_NAME&gt; [&lt;TABLE_NAME&gt;&#8230;]</code> creates a graph listing the specified tables. </p>
<p> The generated graph is created as the &quot;gdaph.dot&quot; file. If the <code>GDA_SQL_VIEWER_PNG</code> or <code>GDA_SQL_VIEWER_PDF</code> environment variables are set and if the &quot;dot&quot; program (from GraphViz) is found, then the graph is displayed (if a display is available).</p>
<dt><code>.H</code></p>
<dd>Set output format. Full syntax is: <code>.H [HTML|XML|CSV|DEFAULT]</code>.</p>
<dt><code>.http</code></p>
<dd>Starts/stops the embedded HTTP server. Full syntax is <code>.http [&lt;port&gt; [&lt;authentication_token&gt;]]</code>, where <i>&lt;authentication_token&gt;</i> is an optional token phrase which HTTP clients are required to send to authenticate.</p>
<dt><code>.i</code></p>
<dd>Executes commands from file the specified file: <code>.i &lt;FILE_NAME&gt;</code>.</p>
<dt><code>.l</code></p>
<dd>Lists all data sources if no argument is provided. <code>.l &lt;DSN&gt;</code> lists information about the specified DSN.</p>
<dt><code>.lp</code></p>
<dd>Lists all available database providers if no argument is provided. <code>.lp &lt;provider&gt;</code> lists information about the specified provider.</p>
<dt><code>.lc</code></p>
<dd>Declares a DSN. Full syntax is: <code>.lc &lt;DSN_NAME&gt; &lt;DSN_DEFINITION&gt; [&lt;DESCRIPTION&gt;]</code>. The <i>&lt;DSN_DEFINITION&gt;</i> format is: <i>&lt;provider&gt;://[&lt;username&gt;[:&lt;password&gt;]@]&lt;connection_params&gt;</i> where <i>&lt;connection_params&gt;</i> is a semi-colon (&quot;;&quot;) separated list of &lt;key&gt;=&lt;value&gt; pairs where <i>&lt;key&gt;</i> is defined when using <code>.lp &lt;provider&gt;</code> (if <i>&lt;value&gt;</i> contains non alphanumeric characters, they should be represented as specified by the RFC 1738). </p>
<p> If a DSN with a similar name already exists, it is first removed. </p>
<p> For example: &quot;.lc mydsn PostgreSQL://HOST=moon;DB_NAME=mydb&quot;.</p>
<dt><code>ldap_attributes</code></p>
<dd>This option (see the <code>.option</code> command) defines or list the attributes handled by LDAP commands; it is only useful if the current connection is an LDAP connection. Its values must have the following format: <code>&lt;attribute&gt;[,&lt;attribute&gt;&#8230;]</code>. </p>
<p> For multi valued attributes (such as &quot;objectClass&quot;), it is possible to specify how multiple values are handled by appending <code>::csv</code> (values are listed in a CVS syntax), <code>::*</code> (each row is duplicated with each value of the attribute), <code>::1</code> (only the 1st value of the attribute is shown), <code>::concat</code> (all the values are made into a string, separated by newlines) or <code>::null</code> (a NULL value is used). The default is an error value.</p>
<dt><code>.ldap_descr</code></p>
<dd>Describes an LDAP entry; this command only works if the current connection is an LDAP connection. Full syntax is: <code>.ldap_descr &lt;DN&gt; [&quot;all&quot;|&quot;set&quot;|&quot;unset&quot;]</code>. </p>
<p> If the <code>set</code> option is passed, then all the set attributes are shown, if the <code>all</code> option is passed, then all attributes are shown, and if the <code>unset</code> option is passed, then only attributes which don&#8217;t have a value are shown. The default is to show only the set attributes specified by the <code>ldap_attributes</code> option.</p>
<dt><code>ldap_dn</code></p>
<dd>This option (see the <code>.option</code> command) defines how the DN column is handled for LDAP searched entries; it is useful only if the current connection is an LDAP connection. Its values must be among: <code>dn</code> (use the full DN), <code>rdn</code> (use only the RDN), or <code>none</code> (don&#8217;t use the DN at all).</p>
<dt><code>.ldap_mod</code></p>
<dd>Modifies an LDAP entry&#8217;s attributes; this command only works if the current connection is an LDAP connection. Full syntax is: <code>.ldap_mod &lt;DN&gt; &lt;OPERATION&gt; [&lt;ATTR&gt;[=&lt;VALUE&gt;]] [&lt;ATTR&gt;=&lt;VALUE&gt; &#8230;]</code>. </p>
<p> The <code>.&lt;OPERATION&gt;</code> argument specifies which operation must be performed, among <code>DELETE</code>, <code>REPLACE</code> and <code>ADD</code>.</p>
<dt><code>.ldap_mv</code></p>
<dd>Renames an LDAP entry; this command only works if the current connection is an LDAP connection. Full syntax is: <code>.ldap_mv &lt;DN&gt; &lt;NEW DN&gt;</code>.</p>
<dt><code>.ldap_search</code></p>
<dd>Searches the LDAP directory for entries; this command only works if the current connection is an LDAP connection. Full syntax is: <code>.ldap_search &lt;filter&gt; [&quot;base&quot;|&quot;onelevel&quot;|&quot;subtree&quot; [&lt;base DN&gt;]]</code>. </p>
<p> Filter must be a valid LDAP filter expression (outer most parenthesis are optional though), &quot;base&quot;, &quot;onelevel&quot; or &quot;subtree&quot; can optionally specify the search scope (default is subtree), and <code>.&lt;base DN&gt;</code> can be used to specify a different DN to search from (the default is to use the base DN specified when opening the connection).</p>
<dt><code>.lr</code></p>
<dd>Removes a DSN declaration. Full syntax is: <code>.lc &lt;DSN_NAME&gt;</code>.</p>
<dt><code>.meta</code></p>
<dd>Updates the current connection&#8217;s meta data (use this command after having modified the database&#8217;s schema).</p>
<dt><code>.o</code></p>
<dd>Sends output to a file or |pipe. Full syntax is: <code>.o &lt;FILE_NAME&gt;</code> or <code>.o |&lt;COMMAND&gt;</code>.</p>
<dt><code>.option</code></p>
<dd>Defines options shared among all the connections. Full syntax is: <code>.option [&lt;OPTION NAME&gt; [&lt;VALUE&gt;]]</code>. </p>
<p> If no option name is given, then all the available options and their current values are shown. If an option name is given without any value, its current value is shown, and to define the value of an option, give its name and new value.</p>
<dt><code>.pivot</code></p>
<dd>Performs data summarization on a data set. Full syntax is: <code>.pivot &lt;SELECT&gt; &lt;ROW_FIELDS&gt; [&lt;COLUMN_FIELDS&gt; [&lt;DATA_FIELDS&gt; [&#8230;]]]</code>. </p>
<p> The <i>&lt;SELECT&gt;</i> defines the data set to perform summarization on. </p>
<p> The <i>&lt;ROW_FIELDS&gt;</i> defines the fields from the data set from which each individual value will yield to a row in the analysis (it can be any valid selectable SQL expression on the data set&#8217;s fields); multiple expressions can be provided, separated by commas (forming a valid SQL expression). In this case a row will be created for each combination of values of each of the expression. </p>
<p> The <i>&lt;COLUMN_FIELDS&gt;</i> defines the fields from the data set from which each individual value will yield to a column in the analysis. Its syntax is similar to the <i>&lt;ROW_FIELDS&gt;</i> one. If not specified (or if specified as a single dash (&quot;-&quot;) caracter), then only one column will be created. Note that, if the <i>&lt;DATA_FIELDS&gt;</i> argument is specified each column created from the <i>&lt;COLUMN_FIELDS&gt;</i> will in fact lead to the creation of as many <i>&lt;DATA_FIELDS&gt;</i> arguments provided. </p>
<p> The <i>&lt;DATA_FIELDS&gt;</i> arguments are entirely optional and indicates the way data summarization is done for each pair of (row,column) values (the default is to count occurrences). The syntax for each <i>&lt;DATA_FIELDS&gt;</i> argument is: <code>[aggregate]&lt;SQL_expression&gt;</code>, where the aggregate part is optional and, if present must be among [SUM], [COUNT], [AVG], [MIN] or [MAX], and the SQL expression is a valid selectable SQL expression of the data set&#8217;s fields. </p>
<p> Examples: </p>
<p> <code>.pivot &quot;SELECT * FROM food&quot; person food</code> </p>
<p> <code>.pivot &quot;SELECT * FROM products&quot; category &quot;CASE WHEN price &lt; 15 THEN &#8216;low&#8217; ELSE &#8216;high&#8217; END&quot; [AVG]price </code> </p>
<p> <code>.pivot &quot;SELECT * FROM sales&quot; category,product &#8211; [AVG]quantity</code> </p>
<dt><code>.q</code></p>
<dd>Quits the application.</p>
<dt><code>.qecho</code></p>
<dd>Sends output to the output stream (stdout). Full syntax is: <code>.qecho &lt;TEXT&gt;</code>.</p>
<dt><code>.qa</code></p>
<dd>Lists all saved query buffers in dictionary.</p>
<dt><code>.qd</code></p>
<dd>Deletes a query buffer from the dictionary. Full syntax is: <code>.qd &lt;QUERY_BUFFER_NAME&gt;</code></p>
<dt><code>.ql</code></p>
<dd>Loads query buffer from dictionary into the current query buffer. Full syntax is: <code>.ql &lt;QUERY_BUFFER_NAME&gt;</code>.</p>
<dt><code>.qp</code></p>
<dd>Shows the contents of the current query buffer.</p>
<dt><code>.qr</code></p>
<dd>Resets the query buffer to empty if no argument is provided. <code>.qr &lt;FILE _NAME&gt;</code> loads the specified file into the query buffer.</p>
<dt><code>.qs</code></p>
<dd>Saves query buffer to dictionary, full syntax is <code>.qs &lt;QUERY_BUFFER_NAME&gt;</code>. This creates a new query buffer with the specified name in the dictionary, containing the current query buffer.</p>
<dt><code>.qw</code></p>
<dd>Writes the query buffer to the specified file, full syntax is <code>.qw &lt;FILE_NAME&gt;</code>.</p>
<dt><code>.s</code></p>
<dd>Show commands history. <code>.s &lt;FILE_NAME&gt;</code> saves command history to specified file.</p>
<dt><code>.set</code></p>
<dd>Sets, shows or lists internal parameters. </p>
<p> <code>.set</code> lists all the defined internal parameters. </p>
<p> <code>.set &lt;NAME&gt; &lt;VALUE&gt;</code> (re)defines the internal parameter named <i>&lt;NAME&gt;</i> to the specified value (which can be the <i>_null_</i> literal to set it to NULL). </p>
<p> <code>.set &lt;NAME&gt;</code> shows the contents of the internal parameter named <i>&lt;NAME&gt;</i>.</p>
<dt><code>.setex</code></p>
<dd>Set internal parameter as the contents of the FILE file or from an existing table&#8217;s value. </p>
<p> <code>.setex &lt;NAME&gt; &lt;FILE_NAME&gt;</code> (re)defines the the internal parameter named <i>&lt;NAME&gt;</i> with the contents of the specified file name. </p>
<p> <code>.setex &lt;NAME&gt; &lt;TABLE&gt; &lt;COLUMN&gt; &lt;ROW_CONDITION&gt;</code> (re)defines the the internal parameter named <i>&lt;NAME&gt;</i> with the value of the <i>&lt;TABLE&gt;</i> table, column <i>&lt;COLUMN&gt;</i> for the row selected by <i>&lt;ROW_CONDITION&gt;</i>.This is most useful to export BLOBs.</p>
<dt><code>.unset</code></p>
<dd>Unset (delete) internal parameter. </p>
<p> <code>.unset</code> unsets all the internal parameters. </p>
<p> <code>.unset &lt;NAME&gt;</code> unsets the internal parameter named <i>&lt;NAME&gt;</i>.</dl>
<h2>Suggestions And Bug Reports</h2>
<p>Any bugs found should be reported to the online bug-tracking system available on the web at <a rel="nofollow" href="http://bugzilla.gnome.org/.">http://bugzilla.gnome.org/.</a> Before reporting bugs, please check to see if the bug has already been reported. </p>
<p> When reporting bugs, it is important to include a reliable way to reproduce the bug, version number of gda-sql, OS name and version, and any relevant hardware specs. If a bug is causing a crash, it is very useful if a stack trace can be provided. And of course, patches to rectify the bug are even better. </p>
<h2>Other Info</h2>
<p>Consult the Libgda&#8217;s home page at <a rel="nofollow" href="http://www.gnome-db.org/.">http://www.gnome-db.org/.</a> </p>
<h2>Authors</h2>
<p>Vivien Malerba (for Libgda&#8217;s authors, please consult the AUTORS file within the Libgda&#8217;s sources) </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-psql/">psql</a></code>(1), <code><a href="/docs/linux/man/1-mysql/">mysql</a></code>(1), <code><a href="/docs/linux/man/1-sqlite3/">sqlite3</a></code>(1)</p>
