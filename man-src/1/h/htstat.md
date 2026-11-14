---
title: "htstat(1)"
name: "htstat"
section: "1"
letter: "h"
url: "/docs/linux/man/1-htstat/"
description: "htstat – returns statistics on the document and word databases, much like the -s option to htdig or htmerge."
---

<h2 class="name">NAME</h2>
<p> htstat &#8211; returns statistics on the document and word databases, much like the -s option to htdig or htmerge. </p>
<h2>SYNOPSIS</h2>
<p> <code>htstat</code> <i>[-v][-a][-c configfile][-u]</i></p>
<h2>DESCRIPTION</h2>
<p> Htdig retrieves HTML documents using the HTTP protocol and gathers information from these documents which can later be used to search these documents. This program can be referred to as the search robot.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code></p>
<dd> Use alternate work files. Tells htstat to append <i>.work</i> to database files, causing a second copy of the database to be built. This allows the original files to be used by htsearch during the run.</p>
<dt><code>-c </code><i>configfile</i></p>
<dd> Use the specified <i>configfile</i> instead of the default.</p>
<dt><code>-u</code></p>
<dd> Give a list of URLs in the document database.</p>
<dt><code>-v</code></p>
<dd> Verbose mode. This increases the verbosity of the program. Using more than 2 is probably only useful for debugging purposes. The default verbose mode (using only one <i>-v</i>) gives a nice progress report while digging.</dl>
<h2>FILES</h2>
<dl>
<dt><code>/etc/htdig/htdig.conf</code></p>
<dd> The default configuration file.</dl>
<h2>SEE ALSO</h2>
<p> Please refer to the HTML pages (in the htdig-doc package) <code>/usr/share/doc/htdig-doc/html/index.html</code> and the manual pages <i><a href="/docs/linux/man/8-htdigconfig/">htdigconfig</a>(8)</i> , <i><a href="/docs/linux/man/1-htdig/">htdig</a>(1)</i> and <i><a href="/docs/linux/man/1-htmerge/">htmerge</a>(1)</i> for a detailed description of ht://Dig and its commands. </p>
<h2>AUTHOR</h2>
<p> This manual page was written by Robert Ribnitz, based on the HTML documentation of ht://Dig. </p>
<h2>Index</h2>
