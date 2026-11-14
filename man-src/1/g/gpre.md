---
title: "gpre(1)"
name: "gpre"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gpre/"
description: "gpre – Firebird source pre-processor"
---

<h2 class="name">NAME</h2>
<p> gpre &#8211; Firebird source pre-processor </p>
<h2>SYNOPSIS</h2>
<dl>
<dt><code>gpre</code> [<i>option</i>&#8230;] <i>input</i> <i>output</i></p>
<dd></dl>
<h2>DESCRIPTION</h2>
<p> <code>gpre</code> is a source pre-processor for easier writing of programs working with the raw Firebird <font SIZE="-1">API.</font> It supports multiple source languages. Using <code>gpre</code>, you can mix special SQL-like language with the normal program source.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-ada</code></p>
<dd> Source is an Ada program.</p>
<dt><code>-handles</code> <i>package name</i></p>
<dd> Ada only. Specifies the handles package.</p>
<dt><code>-c</code></p>
<dd> Source is a C program.</p>
<dt><code>-cxx</code> | <code>-cplusplus</code></p>
<dd> Source is a C<font SIZE="-2">++</font> program.</p>
<dt><code>-database</code> <i>name</i></p>
<dd> Pre-define database connection.</p>
<dt><code>-d_float</code></p>
<dd> Generate <tt>&quot;blr_d_float&quot;</tt> for doubles.</p>
<dt><code>-either_case</code></p>
<dd> Accept upper or lower case <font SIZE="-1">DML</font> in C.</p>
<dt><code>-fetch_password</code></p>
<dd> Fetch password from file.</p>
<dt><code>-charset</code> <i>string</i></p>
<dd> Default character set &amp; format.</p>
<dt><code>-lang_internal</code></p>
<dd> Set some variables to defaults usable for internal Firebird use.</p>
<dt><code>-manual</code></p>
<dd> Do not automatically <font SIZE="-1">ATTACH</font> to a database.</p>
<dt><code>-no_lines</code></p>
<dd> Do not generate C debug lines.</p>
<dt><code>-output</code></p>
<dd> Send output to standard out</p>
<dt><code>-password</code> <i>string</i></p>
<dd> Default password.</p>
<dt><code>-raw</code></p>
<dd> Generate unformatted binary <font SIZE="-1">BLR.</font></p>
<dt><code>-sql_dialect</code> <i>value</i></p>
<dd> <font SIZE="-1">SQL</font> dialect to use.</p>
<dt><code>-sqlda</code> N</p>
<dd> Deprecated feature.</p>
<dt><code>-user</code> <i>name</i></p>
<dd> Default user name.</p>
<dt><code>-verbose</code></p>
<dd> Verbose output to stderr.</p>
<dt><code>-x</code></p>
<dd> External database (used with <code>-database</code>).</p>
<dt><code>-cob</code></p>
<dd> Source is a <font SIZE="-1">COBOL</font> program.</p>
<dt><code>-ansi</code></p>
<dd> Generate <font SIZE="-1">ANSI85</font> compatible <font SIZE="-1">COBOL</font> code.</p>
<dt><code>-rmc</code></p>
<dd> RM/Cobol</p>
<dt><code>-z</code></p>
<dd> Print software version.</p>
<dt><code>-base</code> <i>dir</i></p>
<dd> Base directory for compile-time database.</p>
<dt><code>-dfm</code> <i>format</i></p>
<dd> <font SIZE="-1">COBOL</font> date format</p>
<dt><code>-noqli</code></p>
<dd> Suppress <font SIZE="-1">QLI</font> syntax.</p>
<dt><code>-fortran</code></p>
<dd> Source is a <font SIZE="-1">FORTRAN</font> program.</p>
<dt><code>-pascal</code></p>
<dd> Source is a Pascal program.</p>
<dt><code>-trusted</code></p>
<dd> Use trusted authentication.</dl>
<h2>COPYRIGHT &amp; LICENSE</h2>
<p> Copyright (C) Damyan Ivanov, 2009. </p>
<p> This manpage was written by Damyan Ivanov for the Debian project but may be used by others. Permission is granted to use this document, with or without modifications, provided that this notice is retained. If we meet some day, and you think this stuff is worth it, you can buy me a beer in return. </p>
<h2>Index</h2>
