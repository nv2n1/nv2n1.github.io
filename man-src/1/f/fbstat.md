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
<dt>-all</dt>
<dd> Analyze data and index pages.</dd>
<dt>-data</dt>
<dd> Analyze data pages.</dd>
<dt>-system</dt>
<dd> Analyze system tables.</dd>
<dt>-header</dt>
<dd> Display information from the database header, skip analyzing any tables.</dd>
<dt>-index</dt>
<dd> Analyze leaf index pages.</dd>
<dt>-record</dt>
<dd> Analyze average record and version length.</dd>
<dt>-table <i>table</i></dt>
<dd> Analyze data pages used by the given table.</dd>
<dt>-nocreation</dt>
<dd> Suppress creation date.</dd>
<dt>-user <i>name</i></dt>
<dd>
</dd><dt>-password <i>secret</i></dt>
<dd>
</dd><dt>-fetch_password <i>file</i></dt>
<dd> Authentication parameters.</dd>
<dt>-z</dt>
<dd>
</dd><dt>-?</dt>
<dd> Displays version number.</dd></dl>
<h2>AUTHOR &amp; COPYRIGHT</h2>
<p> Copyright (C) 2010, Damyan Ivanov. </p>
<p> This manpage was written by Damyan Ivanov for the Debian project but may be used by others. Permission is granted to use this document, with or without modifications, provided that this notice is retained. If we meet some day, and you think this stuff is worth it, you can buy me a beer in return. </p>
