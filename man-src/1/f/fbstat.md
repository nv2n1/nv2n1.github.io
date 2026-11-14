---
title: "fbstat(1)"
name: "fbstat"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fbstat/"
description: "fbstat – analyze firebird database"
---

<h2 class="name">NAME</h2>
<p> fbstat &#8211; analyze firebird database </p>
<h2>SYNOPSIS</h2>
<pre><code>
fbstat[command][option...] [server:] database
        fbstat -
    h server : db
                   fbstat -
               all server : db
                                fbstat -
                            data server : db
</code></pre>
<h2>DESCRIPTION</h2>
<p> (<i>Note</i>: Due to file-level conflict, the Debian package has changed the name of <code>gstat</code> to fbstat.) </p>
<p> <code>fbstat</code> Analyzes Firebird databases and produces different kinds of reports. These are useful when analyzing where all this huge disk space has gone or when estimating evaluating index efficiency.</p>
<h2>OPTIONS</h2>
<dl>
<dt>-all</p>
<dd> Analyze data and index pages.</p>
<dt>-data</p>
<dd> Analyze data pages.</p>
<dt>-system</p>
<dd> Analyze system tables.</p>
<dt>-header</p>
<dd> Display information from the database header, skip analyzing any tables.</p>
<dt>-index</p>
<dd> Analyze leaf index pages.</p>
<dt>-record</p>
<dd> Analyze average record and version length.</p>
<dt>-table <i>table</i></p>
<dd> Analyze data pages used by the given table.</p>
<dt>-nocreation</p>
<dd> Suppress creation date.</p>
<dt>-user <i>name</i></p>
<dd>
<dt>-password <i>secret</i></p>
<dd>
<dt>-fetch_password <i>file</i></p>
<dd> Authentication parameters.</p>
<dt>-z</p>
<dd>
<dt>-?</p>
<dd> Displays version number.</dl>
<h2>AUTHOR &amp; COPYRIGHT</h2>
<p> Copyright (C) 2010, Damyan Ivanov. </p>
<p> This manpage was written by Damyan Ivanov for the Debian project but may be used by others. Permission is granted to use this document, with or without modifications, provided that this notice is retained. If we meet some day, and you think this stuff is worth it, you can buy me a beer in return. </p>
<h2>Index</h2>
