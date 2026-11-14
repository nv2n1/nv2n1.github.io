---
title: "htmerge(1)"
name: "htmerge"
section: "1"
letter: "h"
url: "/docs/linux/man/1-htmerge/"
description: "htmerge – create document index and word database for the ht://Dig search engine"
---

<h2 class="name">NAME</h2>
<p> htmerge &#8211; create document index and word database for the ht://Dig search engine </p>
<h2>SYNOPSIS</h2>
<p> <code>htmerge</code> <i>[options]</i></p>
<h2>DESCRIPTION</h2>
<p> <i>Htmerge</i> is used to create a document index and word database from the files that were created by <i>htdig</i>. These databases are then used by <i>htsearch</i> to perform the actual searched.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code></p>
<dd> Use alternate work files. Tells htdig to append <i>.work</i> to database files, causing a second copy of the database to be built. This allows the original files to be used by htsearch during the indexing run.</p>
<dt><code>-c </code><i>configfile</i></p>
<dd> Use the specified <i>configfile</i> instead of the default.</p>
<dt><code>-d</code></p>
<dd> Prevent the document index from being created.</p>
<dt><code>-s</code></p>
<dd> Print statistics about the document and word databases after htmerge has finished.</p>
<dt><code>-v</code></p>
<dd> Run in verbose mode. This will provide some hints as to the progress of the merge. This can be useful when running htmerge interactively since some parts (especially the word database creation) can take a very long time.</p>
<dt><code>-w</code></p>
<dd> Prevent the word database from being created.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>TMPDIR</code></p>
<dd> In addition to the command line options, the environment variable <i>TMPDIR</i> will be used to designate the directory where intermediate files are stored during the sorting process.</dl>
<h2>FILES</h2>
<dl>
<dt><code>/etc/htdig/htdig.conf</code></p>
<dd> The default configuration file.</dl>
<h2>SEE ALSO</h2>
<p> Please refer to the HTML pages (in the htdig-doc package) <code>/usr/share/doc/htdig-doc/html/index.html</code> and the manual pages <i><a href="/docs/linux/man/1-htdig/">htdig</a>(1)</i> and <i><a href="/docs/linux/man/1-htsearch/">htsearch</a>(1)</i> for a detailed description of ht://Dig and its commands.</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Christian Schwarz, modified by Stijn de Bekker, based on the HTML documentation of ht://Dig. </p>
<h2>Index</h2>
