---
title: "smew(1)"
name: "smew"
section: "1"
letter: "s"
url: "/docs/linux/man/1-smew/"
description: "smew – search related messages from Mew’s database file"
---

<h2>NAME</h2>
<p> smew &#8211; search related messages from Mew&#8217;s database file</p>
<h2>SYNOPSIS</h2>
<p> smew myid [<i>mydb</i> [<i>mydir</i>]]</p>
<h2>DESCRIPTION</h2>
<p> The <code>smew</code> utility searches related messages from a Message-ID database file with SQLite 3 for Mew. </p>
<p> <i>myid</i> is a Message-ID of the message to search. </p>
<p> <i>mydb</i> is a database file name. (default: &quot;~/Mail/id.db&quot;) </p>
<p> <i>mydir</i> is a directory part of the message in the database. Note that messages are contained as a relative path from &quot;~/Mail&quot;. If multiple messages are found by <i>myid</i> , the first found one is preferred. However, the message whose directory is <i>mydir</i> is preferred to the first one. </p>
<p> The options are as follows:</p>
<dl>
<dt><code>-c</code></p>
<dd> Search a parent message only.</p>
<dt><code>-p</code></p>
<dd> Search a child message only. </p>
</dl>
<h2>Index</h2>
