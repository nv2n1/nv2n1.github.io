---
title: "isql-fb(1)"
name: "isql-fb"
section: "1"
letter: "i"
url: "/docs/linux/man/1-isql-fb/"
description: "isql — Firebird Interactive SQL shell"
---

<h2 class="name">NAME</h2>
<p> isql &#8212; Firebird Interactive SQL shell </p>
<h2>SYNOPSIS</h2>
<p> <code>isql</code> [-a] [-cache <i>number</i>] [-database <i>path</i>] [-echo] [-input <i>file</i>] [-merge_stderr] [-noautocommit] [-nowarnings] [-output <i>file</i>] [-password <i>string</i>] [-page <i>number</i>] [-role <i>string</i>] [-s <i>number</i>] [-terminator <i>string</i>] [-user <i>name</i>] [-x] [-z]</p>
<h2>DESCRIPTION</h2>
<p> <code>isql</code> is a program that allows the user to issue arbitrary <font SIZE="-1">SQL</font> commands as well as exctacting the metadata. </p>
<p> <code>isql</code> in <code>Debian</code> is available under the <code>isql-fb</code> name due to filename conflict with an executable from another package.</p>
<h2>OPTIONS</h2>
<p> <code>isql</code> can handle various command line options. Most options can be abbreviated. Below are given the shortest abbreviations as well as the full versions.</p>
<dl>
<dt><code>-a</code></p>
<dd> Extract <font SIZE="-1">DDL</font> (Data definition language) statements necessary to re-create database&#8217;s structure, triggers and other metadata. The <tt>&quot;CREATE DATABASE&quot;</tt> statement is in a comment. Statements are printed to standard output unless -output is used. See also -extract.</p>
<dt><code>-c</code> <i>buffers</i></p>
<dd>
<dt><code>-cache</code> <i>number</i></p>
<dd> Specify default size of the buffers to be used in database pages.</p>
<dt><code>-d</code> <i>path</i></p>
<dd>
<dt><code>-database</code> <i>path</i></p>
<dd> Specifies target database name when extracting the metadata with the -extract option.</p>
<dt><code>-e</code></p>
<dd>
<dt><code>-echo</code></p>
<dd> Prints each statement before executing it.</p>
<dt><code>-x</code></p>
<dd>
<dt><code>-ex</code></p>
<dd>
<dt><code>-extract</code></p>
<dd> Extracts <font SIZE="-1">DDL</font> statements to recreate database metadata. </p>
<p> If no -database option is given, <code>-extract</code> behaves exactly as -a. If -database is given, the <tt>&quot;CREATE DATABASE&quot;</tt> statement is not commented and the database name is replaced with <i>path</i>.</p>
<dt><code>-i</code> <i>file</i></p>
<dd>
<dt><code>-input</code> <i>file</i></p>
<dd> Reads commands from <i>file</i> instead of standard input. Exits with commit after the last command.</p>
<dt><code>-m</code></p>
<dd>
<dt><code>-merge_stderr</code></p>
<dd> Merges standard error to standard output. Useful for redirecting both streams.</p>
<dt><code>-n</code></p>
<dd>
<dt><code>-noautocommit</code></p>
<dd> Normally, all <font SIZE="-1">DDL</font> statements like <tt>&quot;CREATE TABLE&quot;</tt> are automatically committed in a separate transaction. This option disables the automatic commit of <font SIZE="-1">DDL</font> statements.</p>
<dt><code>-nowarnings</code></p>
<dd> Disables displaying of <font SIZE="-1">SQL</font> warnings.</p>
<dt><code>-o</code> <i>file</i></p>
<dd>
<dt><code>-output</code> <i>file</i></p>
<dd> All output is redirected to the given <i>file</i>.</p>
<dt><code>-page</code> <i>number</i></p>
<dd>
<dt><code>-pagelength</code> <i>number</i></p>
<dd> Prints column headers every <i>number</i> output lines. Default is <tt>20</tt>.</p>
<dt><code>-pas</code> <i>string</i></p>
<dd>
<dt><code>-password</code> <i>string</i></p>
<dd> Uses given password as a default when connecting to databases.</p>
<dt><code>-r</code> <i>string</i></p>
<dd>
<dt><code>-role</code> <i>string</i></p>
<dd> Uses given <font SIZE="-1">SQL</font> role as a default when connecting to databases.</p>
<dt><code>-s</code> <i>number</i></p>
<dd>
<dt><code>-sqldialect</code> <i>number</i></p>
<dd> Uses given <font SIZE="-1">SQL</font> dialect as a default when connecting to databases. The default is <tt>1</tt>.</p>
<dt><code>-t</code> <i>string</i></p>
<dd>
<dt><code>-terminator</code> <i>string</i></p>
<dd> Set command line terminator. Default is semicolon <tt>&quot;;&quot;</tt>.</p>
<dt><code>-u</code> <i>string</i></p>
<dd>
<dt><code>-user</code> <i>string</i></p>
<dd> Uses given user name as a default when connecting to databases.</p>
<dt><code>-z</code></p>
<dd> Prints program version string before doing anything else. Prints server version after connecting to a database.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><font SIZE="-1"><code>ISC_USER</code></font></p>
<dd> Default value for the -user option.</p>
<dt><font SIZE="-1"><code>ISC_ROLE</code></font></p>
<dd> Default value for the -role option.</p>
<dt><font SIZE="-1"><code>ISC_PASSWORD</code></font></p>
<dd> Default value for the -password option.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gbak/">gbak</a></code>(1), <code><a href="/docs/linux/man/1-gfix/">gfix</a></code>(1), <code><a href="/docs/linux/man/1-fbstat/">fbstat</a></code>(1). </p>
<p> Additional documentation about Firebird can be found on the Firebird Project website, &lt;<a rel="nofollow" href="http://www.firebirdsql.org">http://www.firebirdsql.org</a>&gt;.</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Damyan Ivanov dmn [at] debian.org for the Debian project. Permission is granted to use this document, with or without modifications, provided that this notice is retained. If we meet some day, and you think this stuff is worth it, you can buy me a beer in return. </p>
<h2>Index</h2>
