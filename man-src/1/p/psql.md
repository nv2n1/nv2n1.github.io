---
title: "psql(1)"
name: "psql"
section: "1"
letter: "p"
url: "/docs/linux/man/1-psql/"
description: "psql – PostgreSQL interactive terminal"
---

<h2 class="name">NAME</h2>
<p> psql &#8211; PostgreSQL interactive terminal </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>psql</code> [<i>option</i>&#8230;] [<i>dbname</i>&nbsp;<wbr>[<i>username</i>]]</dl>
<h2>DESCRIPTION</h2>
<dd>psql is a terminal-based front-end to PostgreSQL. It enables you to type in queries interactively, issue them to PostgreSQL, and see the query results. Alternatively, input can be from a file. In addition, it provides a number of meta-commands and various shell-like features to facilitate writing scripts and automating a wide variety of tasks.</p>
<h2>OPTIONS</h2>
<p> <code>-a</code>, <code>&#8211;echo-all</code></p>
<dl>
<dt>
<dd> Print all nonempty input lines to standard output as they are read. (This does not apply to lines read interactively.) This is equivalent to setting the variable <i>ECHO</i> to all.</dl>
<p> <code>-A</code>, <code>&#8211;no-align</code></p>
<dl>
<dt>
<dd> Switches to unaligned output mode. (The default output mode is otherwise aligned.)</dl>
<p> <code>-c </code><i>command</i>, <code>&#8211;command=</code><i>command</i></p>
<dl>
<dt>
<dd> Specifies that psql is to execute one command string, <i>command</i>, and then exit. This is useful in shell scripts. Start-up files (psqlrc and ~/.psqlrc) are ignored with this option. </p>
<p> <i>command</i> must be either a command string that is completely parsable by the server (i.e., it contains no psql-specific features), or a single backslash command. Thus you cannot mix SQL and psql meta-commands with this option. To achieve that, you could pipe the string into psql, for example: echo &#8216;
