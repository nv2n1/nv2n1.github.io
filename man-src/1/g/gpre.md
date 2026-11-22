---

title: "gpre(1)"
name: "gpre"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gpre/"
description: "gpre – Firebird source pre-processor"
---

<p> gpre &#8211; Firebird source pre-processor </p>
<h2>SYNOPSIS</h2>
<dl>
<dt><code>gpre</code> [<i>option</i>&#8230;] <i>input</i> <i>output</i></dt>
<dd></dd></dl>
<h2>DESCRIPTION</h2>
<p> <code>gpre</code> is a source pre-processor for easier writing of programs working with the raw Firebird API. It supports multiple source languages. Using <code>gpre</code>, you can mix special SQL-like language with the normal program source.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-ada</code></dt>
<dd> Source is an Ada program.</dd>
<dt><code>-handles</code> <i>package name</i></dt>
<dd> Ada only. Specifies the handles package.</dd>
<dt><code>-c</code></dt>
<dd> Source is a C program.</dd>
<dt><code>-cxx</code> | <code>-cplusplus</code></dt>
<dd> Source is a C++ program.</dd>
<dt><code>-database</code> <i>name</i></dt>
<dd> Pre-define database connection.</dd>
<dt><code>-d_float</code></dt>
<dd> Generate <tt>&quot;blr_d_float&quot;</tt> for doubles.</dd>
<dt><code>-either_case</code></dt>
<dd> Accept upper or lower case DML in C.</dd>
<dt><code>-fetch_password</code></dt>
<dd> Fetch password from file.</dd>
<dt><code>-charset</code> <i>string</i></dt>
<dd> Default character set &amp; format.</dd>
<dt><code>-lang_internal</code></dt>
<dd> Set some variables to defaults usable for internal Firebird use.</dd>
<dt><code>-manual</code></dt>
<dd> Do not automatically ATTACH to a database.</dd>
<dt><code>-no_lines</code></dt>
<dd> Do not generate C debug lines.</dd>
<dt><code>-output</code></dt>
<dd> Send output to standard out</dd>
<dt><code>-password</code> <i>string</i></dt>
<dd> Default password.</dd>
<dt><code>-raw</code></dt>
<dd> Generate unformatted binary BLR.</dd>
<dt><code>-sql_dialect</code> <i>value</i></dt>
<dd> SQL dialect to use.</dd>
<dt><code>-sqlda</code> N</dt>
<dd> Deprecated feature.</dd>
<dt><code>-user</code> <i>name</i></dt>
<dd> Default user name.</dd>
<dt><code>-verbose</code></dt>
<dd> Verbose output to stderr.</dd>
<dt><code>-x</code></dt>
<dd> External database (used with <code>-database</code>).</dd>
<dt><code>-cob</code></dt>
<dd> Source is a COBOL program.</dd>
<dt><code>-ansi</code></dt>
<dd> Generate ANSI85 compatible COBOL code.</dd>
<dt><code>-rmc</code></dt>
<dd> RM/Cobol</dd>
<dt><code>-z</code></dt>
<dd> Print software version.</dd>
<dt><code>-base</code> <i>dir</i></dt>
<dd> Base directory for compile-time database.</dd>
<dt><code>-dfm</code> <i>format</i></dt>
<dd> COBOL date format</dd>
<dt><code>-noqli</code></dt>
<dd> Suppress QLI syntax.</dd>
<dt><code>-fortran</code></dt>
<dd> Source is a FORTRAN program.</dd>
<dt><code>-pascal</code></dt>
<dd> Source is a Pascal program.</dd>
<dt><code>-trusted</code></dt>
<dd> Use trusted authentication.</dd></dl>
<h2>COPYRIGHT &amp; LICENSE</h2>
<p> Copyright (C) Damyan Ivanov, 2009. </p>
<p> This manpage was written by Damyan Ivanov for the Debian project but may be used by others. Permission is granted to use this document, with or without modifications, provided that this notice is retained. If we meet some day, and you think this stuff is worth it, you can buy me a beer in return. </p>
