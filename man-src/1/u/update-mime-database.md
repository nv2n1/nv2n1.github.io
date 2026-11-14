---
title: "update-mime-database(1)"
name: "update-mime-database"
section: "1"
letter: "u"
url: "/docs/linux/man/1-update-mime-database/"
description: "update-mime-database – a program to build the Shared MIME-Info database cache"
---

<h2 class="name">NAME</h2>
<p> update-mime-database &#8211; a program to build the Shared MIME-Info database cache</p>
<h2>SYNOPSIS</h2>
<p> <code>update-mime-database -h</code> | <code>-v</code> | [ <code>-V</code> | <code>-n</code> ] <i>MIME-DIR</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>update-mime-database</code> is a program which is responsible for updating the shared mime-info cache according to the system described in the Shared MIME-Info Database specification from the X Desktop Group. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code></p>
<dd> Print out a command summary.</p>
<dt><code>-v</code></p>
<dd> Print out the version information.</p>
<dt><code>-V</code></p>
<dd> Be verbose.</p>
<dt><code>-n</code></p>
<dd> Only update if <code>MIME-DIR</code>/packages/ or a file in that directory is newer than <code>MIME-DIR</code>/version. This is useful for package pre- and post-installation scripts. </p>
</dl>
<h2>ARGUMENTS</h2>
<dl>
<dt><code>MIME-DIR</code></p>
<dd> This is the directory for which <code>update-mime-database</code> should rebuild the cache. Mandatory if none of the options is provided. </p>
</dl>
<h2>AUTHOR</h2>
<p> Filip Van Raemdonck (mechanix [at] debian.org) wrote this manpage for the Debian GNU/Linux project, but it may be used by others. </p>
<h2>LICENCE</h2>
<p> Copyright (C) 2002 Thomas Leonard.<br />
 You may redistribute copies of <code>update-mime-database</code> under the terms of the GNU General Public License. </p>
<h2>Index</h2>
