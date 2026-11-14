---
title: "defncopy(1)"
name: "defncopy"
section: "1"
letter: "d"
url: "/docs/linux/man/1-defncopy/"
description: "defncopy – extract procedures and views from a Microsoft server."
---

<h2 class="name">NAME</h2>
<p> <code>defncopy</code> &#8211; extract procedures and views from a Microsoft server. </p>
<h2>SYNOPSIS</h2>
<p> [-<code>v</code> ] [-<code>U </code><i>username</i> ] [-<code>P </code><i>password</i> ] [-<code>S </code><i>server</i> ] [-<code>D </code><i>database</i> ] [-<code>i </code><i>input_file</i> ] [-<code>o </code><i>output_file</i> ] Bo <i>owner.object_name</i> [<i>owner.object_name &#8230;</i> ] Bc</p>
<h2>DESCRIPTION</h2>
<p> is a utility program distributed with FreeTDS. It replaces a similar program of the same name distributed by Sybase. </p>
<p> reads the text of a stored procedure or view, and writes a script suitable for recreating the procedure or view. For tables, it reads the output of sp_help and constructs a `CREATE&#8217; TABLE statement, complete with `CREATE&#8217; INDEX Ns , too. <i>owner</i> is optional if you or the database owner is the owner of the procedure/view being copied. <i>object_name</i> is the name of the system object you wish to extract.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-U </code><i>username</i></p>
<dd> database server login name.</p>
<dt><code>-P </code><i>password</i></p>
<dd> database server password.</p>
<dt><code>-S </code><i>server</i></p>
<dd> database server to which to connect.</p>
<dt><code>-D </code><i>database</i></p>
<dd> database to use. Optional if the procedure/view being extracted is in your default database.</p>
<dt><code>-i </code><i>input_file</i></p>
<dd> a script to apply to the database. Not currently implemented.</p>
<dt><code>-o </code><i>output_file</i></p>
<dd> a file to hold the script, defaults to standard output.</p>
<dt><code>-v</code></p>
<dd> Show version information and copyright notice.</dl>
<h2>NOTES</h2>
<p> is a filter; it reads from standard input, writes to standard output, and writes errors to standard error. The &#8211;<code>i</code> &#8211;<code>o</code> and &#8211;<code>e</code> options override these defaults. </p>
<p> makes use of the db-lib API provided by FreeTDS. This API is of course also available to application developers.</p>
<h2>EXIT STATUS</h2>
<p> exits 0 on success, and &gt;0 if the server cannot process the query. </p>
<p> will report any errors returned by the server, but will continue processing.</p>
<h2>HISTORY</h2>
<p> first appeared in FreeTDS 0.63.</p>
<h2>AUTHORS</h2>
<p> The utility was written by An James K. Lowden Aq jklowden [at] schemamania.org.</p>
<h2>BUGS</h2>
<p> Works only with Microsoft servers and ancient Sybase servers. Does not create primary keys. Many options are defined by Sybase that this version does not implement. Feel free to correct this situation. In theory, could apply/produce DDL for any system object, but at present only tables, procedures and views are supported, and only for extraction. </p>
<h2>Index</h2>
