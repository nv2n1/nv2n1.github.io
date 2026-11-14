---
title: "sqlite(1)"
name: "sqlite"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sqlite/"
description: "sqlite – A command line interface for SQLite"
---

<h2 class="name">NAME</h2>
<p> sqlite &#8211; A command line interface for SQLite </p>
<h2>SYNOPSIS</h2>
<p> <code>sqlite</code> [<i>options</i>]<i> filename </i>[<i>SQL</i>]</p>
<h3>SUMMARY</h3>
<p> sqlite is a terminal-based front-end to the SQLite library. It enables you to type in queries interactively, issue them to SQLite and see the results. Alternatively, you can specify SQL code on the command-line. In addition it provides a number of meta-commands. </p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>sqlite</code> command. This manual page was written for the Debian GNU/Linux distribution because the original program does not have a manual page.</p>
<h3>GETTING STARTED</h3>
<p> To start the sqlite program, just type &quot;sqlite&quot; followed by the name the file that holds the SQLite database. If the file does not exist, a new one is created automatically. The sqlite program will then prompt you to enter SQL. Type in SQL statements (terminated by a semicolon), press &quot;Enter&quot; and the SQL will be executed. </p>
<p> For example, to create a new SQLite database named &quot;ex1&quot; with a single table named &quot;tbl1&quot;, you might do this: </p>
<pre><code>
$ sqlite ex1
SQLite version 2.0.0
Enter ".help" for instructions
sqlite&gt; create table tbl1(one varchar(10), two smallint);
sqlite &gt; insert into tbl1 values('hello!', 10);
sqlite &gt; insert into tbl1 values('goodbye', 20);
sqlite &gt; select *from tbl1;
hello ! | 10 goodbye | 20 sqlite &gt;
</code></pre>
<h3>SQLITE META-COMMANDS</h3>
<p> Most of the time, sqlite just reads lines of input and passes them on to the SQLite library for execution. But if an input line begins with a dot (&quot;.&quot;), then that line is intercepted and interpreted by the sqlite program itself. These &quot;dot commands&quot; are typically used to change the output format of queries, or to execute certain prepackaged query statements. </p>
<p> For a listing of the available dot commands, you can enter &quot;.help&quot; at any time. For example: </p>
<pre><code>
sqlite &gt;.help
            .dump
    ? TABLE
    ? ... Dump the database in an text format
                  .echo ON |
              OFF Turn command echo on or
          off
                  .exit Exit this program
                  .explain ON |
              OFF Turn output mode suitable for EXPLAIN on or
          off."off" will revert to the output mode that was
                  previously in effect
                      .header(s) ON |
              OFF Turn display of headers on or
          off
              .help Show this message
              .indices TABLE Show names of all indices on TABLE
              .mode MODE Set mode to one of "line(s)",
    "column(s)",
    "insert", "list", or "html"
                                  .mode insert TABLE Generate SQL insert statements for TABLE
                                  .nullvalue STRING Print STRING instead of nothing for NULL data
                                  .output FILENAME Send output to FILENAME
                                  .output stdout Send output to the screen
                                  .prompt MAIN CONTINUE Replace the standard prompts
                              "sqlite &gt; " and
                              "   ...&gt; " with the strings MAIN and CONTINUE CONTINUE is optional..quit Exit this program.read FILENAME Execute SQL in FILENAME.reindex
    ? TABLE
    ? Rebuild indices
          .schema
    ? TABLE
    ? Show the CREATE statements
          .separator STRING Change separator string for "list" mode
          .show Show the current values for the following
    :
        .echo
        .explain
        .mode
        .nullvalue
        .output
        .separator
        .width
        .tables
    ? PATTERN
    ? List names of tables matching a pattern
        .timeout MS Try opening locked tables for MS milliseconds
        .width NUM NUM... Set column widths for "column" mode
              sqlite &gt;
</code></pre>
<h2>OPTIONS</h2>
<p> The program has the following options:</p>
<dl>
<dt><code>-init file</code></p>
<dd> Read in and process &#8216;file&#8217;, which contains &quot;dot commands&quot;. You can use this file to initialize display settings.</p>
<dt><code>-html</code></p>
<dd> Set output mode to HTML.</p>
<dt><code>-list</code></p>
<dd> Set output mode to &#8216;list&#8217;.</p>
<dt><code>-line</code></p>
<dd> Set output mode to &#8216;line&#8217;.</p>
<dt><code>-column</code></p>
<dd> Set output mode to &#8216;column&#8217;.</p>
<dt><code>-separator&nbsp;<wbr></code><i>separator</i></p>
<dd> Specify which output field separator for &#8216;list&#8217; mode to use. Default is &#8216;|&#8217;.</p>
<dt><code>-nullvalue&nbsp;<wbr></code><i>string</i></p>
<dd> When a null is encountered, print &#8216;string&#8217;. Default is no string.</p>
<dt><code>-[no]header</code></p>
<dd> Turn headers on or off. Default is off.</p>
<dt><code>-echo</code></p>
<dd> Print commands before execution. </p>
</dl>
<h2>OUTPUT MODE</h2>
<p> The SQLite program has different output modes, which define the way the output (from queries) is formatted. </p>
<p> In &#8216;list&#8217; mode, which is the default, one record per line is output, each field separated by the separator specified with the <code>-separator</code> option or <code>.separator</code> command. </p>
<p> In &#8216;line&#8217; mode, each column is output on its own line, records are separated by blank lines. </p>
<p> In HTML mode, an XHTML table is generated. </p>
<p> In &#8216;column&#8217; mode, one record per line is output, aligned neatly in colums. </p>
<h2>INIT FILE</h2>
<p> sqlite can be initialized using resource files. These can be combined with command line arguments to set up sqlite exactly the way you want it. Initialization proceeds as follows: </p>
<p> o The defaults of </p>
<pre>
mode            = LIST
separator       = &quot;|&quot;
main prompt     = &quot;sqlite&gt; &quot;
continue prompt = &quot;   ...&gt; &quot;
</pre>
<p> are established. </p>
<p> o If a file .sqliterc can be found in the user&#8217;s home directory, it is read and processed. It should only contain &quot;dot commands&quot;. If the file is not found or cannot be read, processing continues without notification. </p>
<p> o If a file is specified on the command line with the -init option, it is processed in the same manner as .sqliterc </p>
<p> o All other command line options are processed </p>
<p> o The database is opened and you are now ready to begin. </p>
<h2>SEE ALSO</h2>
<p> <a rel="nofollow" href="http://www.hwaci.com/sw/sqlite/">http://www.hwaci.com/sw/sqlite/</a><br />
 The sqlite-doc package</p>
<h2>AUTHOR</h2>
<p> This manual page was originally written by Andreas Rottmann &lt;rotty [at] debian.org&gt;, for the Debian GNU/Linux system (but may be used by others). </p>
<h2>Index</h2>
