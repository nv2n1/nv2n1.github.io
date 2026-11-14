---
title: "ibus-table-createdb(1)"
name: "ibus-table-createdb"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ibus-table-createdb/"
description: "ibus-table-createdb – create ibus-table database from table source"
---

<h2 class="name">NAME</h2>
<p> ibus-table-createdb &#8211; create ibus-table database from table source </p>
<h2>SYNOPSIS</h2>
<p> <code>ibus-table-createdb</code> [ <code>-n </code><i>name</i> | <code>&#8211;name </code><i>name</i> ] [ <code>-s </code><i>source</i> | <code>&#8211;source </code><i>source</i> ] [ <code>-e </code><i>extra</i> | <code>&#8211;extra </code><i>extra</i> ] [ <code>-p </code><i>pinyin</i> | <code>&#8211;pinyin </code><i>pinyin</i> ] [ <code>-o</code> ] [ <code>&#8211;no-create-index</code> ] [ <code>-i</code> ] [ <code>&#8211;create-index-only</code> ] [ <code>-d</code> ] [ <code>&#8211;debug</code> ]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp; </p>
<h2>DESCRIPTION</h2>
<p> <code>ibus-table-createdb</code> creates a database for ibus-table from a source table.</p>
<h2>OPTIONS</h2>
<p> This program follows the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;). A summary of options is included below.</p>
<dl>
<dt><code>-n &#8211;name </code><i>database-file</i></p>
<dd> <i>database-file</i> specifies the file name for the binary database for the IME. The default is &#8221;. If the file name of the database is not specified, the file name of the source file before the first &#8216;.&#8217; will be appended with &#8216;.db&#8217; and that will be used as the file name of the database.</p>
<dt><code>-s &#8211;source </code><i>source-file</i></p>
<dd> <i>source-file</i> specifies the file which contains the source of the IME. The default is &#8221;.</p>
<dt><code>-e &#8211;extra </code><i>extra-words-file</i></p>
<dd> <i>extra-words-file</i> specifies the file name for the extra words for the IME. The default is &#8221;.</p>
<dt><code>-p &#8211;pinyin </code><i>pinyin-file</i></p>
<dd> <i>pinyin-file</i> specifies the source file for the pinyin. The default is &#8216;/usr/share/ibus-table/data/pinyin_table.txt.bz2&#8217;.</p>
<dt><code>-o &#8211;no-create-index </code></p>
<dd> Do not create an index for a database (Only for distribution purposes, a normal user should not use this flag!)</p>
<dt><code>-i &#8211;create-index-only </code></p>
<dd> Only create an index for an existing database. Specifying the file name of the binary database with the -n or &#8211;name option is required when this option is used.</p>
<dt><code>-d &#8211;debug </code></p>
<dd> Print extra debug messages.</dl>
<h2>EXAMPLES</h2>
<dl>
<dt><code>ibus-table-createdb -n ipa-x-sampa.db -s ipa-x-sampa.txt</code></p>
<dd> Create the binary database &#8220;ipa-x-sampa.db&#8221; from the source file &#8220;ipa-x-sampa.txt&#8221;.</p>
<dt><code>ibus-table-createdb -i -n ipa-x-sampa.db</code></p>
<dd> Create an index for the database &#8220;ipa-x-sampa.db&#8221;.</dl>
<h2>AUTHOR</h2>
<p> This manual page was written by Mike FABIAN &lt;mfabian [at] redhat.com&gt;. </p>
<h2>Index</h2>
