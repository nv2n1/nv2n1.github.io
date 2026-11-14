---
title: "sqlite3(1)"
name: "sqlite3"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sqlite3/"
description: "sqlite3 – A command line interface for SQLite version 3"
---

<h2 class="name">NAME</h2>
<p> <code>sqlite3 </code> &#8211; A command line interface for SQLite version 3</p>
<h2>SYNOPSIS</h2>
<p> <code>sqlite3</code> [<i>options</i>] [<i>databasefile</i>] [<i>SQL</i>] </p>
<h2>SUMMARY</h2>
<p> <code>sqlite3</code> is a terminal-based front-end to the SQLite library that can evaluate queries interactively and display the results in multiple formats. <code>sqlite3</code> can also be used within shell scripts and other applications to provide batch processing features. </p>
<h2>DESCRIPTION</h2>
<p> To start a <code>sqlite3</code> interactive session, invoke the <code>sqlite3</code> command and optionally provide the name of a database file. If the database file does not exist, it will be created. If the database file does exist, it will be opened. </p>
<p> For example, to create a new database file named &quot;mydata.db&quot;, create a table named &quot;memos&quot; and insert a couple of records into that table: </p>
<p> $ <code>sqlite3 mydata.db</code><br />
 SQLite version 3.1.3<br />
 Enter &quot;.help&quot; for instructions<br />
 sqlite&gt; <code>create table memos(text, priority INTEGER);</code><br />
 sqlite&gt; <code>insert into memos values(&#8216;deliver project description&#8217;, 10);</code><br />
 sqlite&gt; <code>insert into memos values(&#8216;lunch with Christine&#8217;, 100);</code><br />
 sqlite&gt; <code>select * from memos;</code><br />
 deliver project description|10<br />
 lunch with Christine|100<br />
 sqlite&gt; </p>
<p> If no database name is supplied, the ATTACH sql command can be used to attach to existing or create new database files. ATTACH can also be used to attach to multiple databases within the same interactive session. This is useful for migrating data between databases, possibly changing the schema along the way. </p>
<p> Optionally, a SQL statement or set of SQL statements can be supplied as a single argument. Multiple statements should be separated by semi-colons. </p>
<p> For example: </p>
<p> $ <code>sqlite3 -line mydata.db &#8216;select * from memos where priority &gt; 20;&#8217;</code> </p>
<p>&nbsp;<wbr>text&nbsp;<wbr>=&nbsp;<wbr>lunch with Christine<br />
 priority = 100 </p>
<h3>SQLITE META-COMMANDS</h3>
<p> The interactive interpreter offers a set of meta-commands that can be used to control the output format, examine the currently attached database files, or perform administrative operations upon the attached databases (such as rebuilding indices). Meta-commands are always prefixed with a dot (.). </p>
<p> A list of available meta-commands can be viewed at any time by issuing the &#8216;.help&#8217; command. For example: </p>
<p> sqlite&gt; <code>.help</code> </p>
<pre><code>
.databases List names and files of attached databases
    .dump
    ? TABLE
    ? ... Dump the database in an SQL text format
                  .echo ON |
              OFF Turn command echo on or
          off
                  .exit Exit this program
                  .explain ON |
              OFF Turn output mode suitable for EXPLAIN on or
          off.
                  .header(s) ON |
              OFF Turn display of headers on or
          off
              .help Show this message
              .import FILE TABLE Import data from FILE into TABLE
              .indices TABLE Show names of all indices on TABLE
              .mode MODE
    ? TABLE ? Set output mode where MODE is one of : csv Comma - separated values column Left - aligned columns.(See.width)html HTML&lt;table&gt; code insert SQL insert statements for TABLE line One value per line list Values delimited by.separator string tabs Tab - separated values tcl TCL list elements.nullvalue STRING Print STRING in place of NULL values.output FILENAME Send output to FILENAME.output stdout Send output to the screen.prompt MAIN CONTINUE Replace the standard prompts.quit Exit this program.read FILENAME Execute SQL in FILENAME.schema ? TABLE ? Show the CREATE statements.separator STRING Change separator used by output mode and.import.show Show the current values for various settings.tables ? PATTERN ? List names of tables matching a LIKE pattern.timeout MS Try opening locked tables for MS milliseconds.width NUM NUM... Set column widths for "column" mode sqlite &gt;
</code></pre>
<h2>OPTIONS</h2>
<p> <code>sqlite3</code> has the following options:</p>
<dl>
<dt><code>-init&nbsp;<wbr></code><i>file</i></p>
<dd> Read and execute commands from <i>file</i> , which can contain a mix of SQL statements and meta-commands.</p>
<dt><code>-echo</code></p>
<dd> Print commands before execution.</p>
<dt><code>-[no]header</code></p>
<dd> Turn headers on or off.</p>
<dt><code>-bail</code></p>
<dd> Stop after hitting an error.</p>
<dt><code>-interactive</code></p>
<dd> Force interactive I/O.</p>
<dt><code>-batch</code></p>
<dd> Force batch I/O.</p>
<dt><code>-column</code></p>
<dd> Query results will be displayed in a table like form, using whitespace characters to separate the columns and align the output.</p>
<dt><code>-cmd&nbsp;<wbr></code><i>command</i></p>
<dd> Run <i>command</i> before reading stdin.</p>
<dt><code>-csv</code></p>
<dd> Set output mode to CSV (comma separated values).</p>
<dt><code>-html</code></p>
<dd> Query results will be output as simple HTML tables.</p>
<dt><code>-line</code></p>
<dd> Query results will be displayed with one value per line, rows separated by a blank line. Designed to be easily parsed by scripts or other programs</p>
<dt><code>-list</code></p>
<dd> Query results will be displayed with the separator (|, by default) character between each field value. The default.</p>
<dt><code>-separator&nbsp;<wbr></code><i>separator</i></p>
<dd> Set output field separator. Default is &#8216;|&#8217;.</p>
<dt><code>-nullvalue&nbsp;<wbr></code><i>string</i></p>
<dd> Set string used to represent NULL values. Default is &#8221; (empty string).</p>
<dt><code>-stats</code></p>
<dd> Print memory stats before each finalize.</p>
<dt><code>-version</code></p>
<dd> Show SQLite version.</p>
<dt><code>-vfs&nbsp;<wbr></code><i>name</i></p>
<dd> Use <i>name</i> as the default VFS.</p>
<dt><code>-help</code></p>
<dd> Show help on options and exit. </p>
</dl>
<h2>INIT FILE</h2>
<p> <code>sqlite3</code> reads an initialization file to set the configuration of the interactive environment. Throughout initialization, any previously specified setting can be overridden. The sequence of initialization is as follows: </p>
<p> o The default configuration is established as follows: </p>
<pre>
mode            = LIST
separator       = &quot;|&quot;
main prompt     = &quot;sqlite&gt; &quot;
continue prompt = &quot;   ...&gt; &quot;
</pre>
<p> o If the file <code>~/.sqliterc</code> exists, it is processed first. can be found in the user&#8217;s home directory, it is read and processed. It should generally only contain meta-commands. </p>
<p> o If the -init option is present, the specified file is processed. </p>
<p> o All other command line options are processed. </p>
<h2>SEE ALSO</h2>
<p> <a rel="nofollow" href="http://www.sqlite.org/">http://www.sqlite.org/</a><br />
 The sqlite-doc package</p>
<h2>AUTHOR</h2>
<p> This manual page was originally written by Andreas Rottmann &lt;rotty [at] debian.org&gt;, for the Debian GNU/Linux system (but may be used by others). It was subsequently revised by Bill Bumgarner &lt;bbum [at] mac.com&gt;. </p>
<h2>Index</h2>
