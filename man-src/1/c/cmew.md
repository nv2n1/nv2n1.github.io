---
title: "cmew(1)"
name: "cmew"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cmew/"
description: "cmew – create Mew’s database file"
---

<h2>NAME</h2>
<p> cmew &#8211; create Mew&#8217;s database file</p>
<h2>SYNOPSIS</h2>
<p> cmew [<i>-f</i>] [<i>db_file</i> [<i>maildir</i> [<i>ignore_regex</i> [<i>target_folder</i>]]]]</p>
<h2>DESCRIPTION</h2>
<p> The <code>cmew</code> utility creates a Message-ID database file with SQLite 3 for Mew. </p>
<p> <i>db_file</i> is a database file name. (default: &quot;~/Mail/id.db&quot;) </p>
<p> <i>maildir</i> is a mail directory name. (default: &quot;~/Mail&quot;) </p>
<p> <i>ignore_regex</i> is a regular expression for the mail directory names to not create the database. (default: &quot;^\./casket$|^\./casket/|/\.&quot;) </p>
<p> <i>target_folder</i> is a target folder. Information about messages contained in this folder only are updated. </p>
<p> The options are as follows:</p>
<dl>
<dt><code>-f</code></p>
<dd> Full update. Unless this option is specified, incremental update is used. </p>
</dl>
<h2>Index</h2>
