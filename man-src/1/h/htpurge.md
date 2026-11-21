---

title: "htpurge(1)"
name: "htpurge"
section: "1"
letter: "h"
url: "/docs/linux/man/1-htpurge/"
description: "htpurge – remove unused odocuments from the database (general maintenance script)"
---

<p> <code>htpurge</code> <i>[-][-a][-c configfile][-u][-v]</i></p>
<p> Htpurge functions to remove specified URLs from the databases as well as bad URLs, unretrieved URLs, obsolete documents, etc. It is recommended that htpurge be run after htdig to clean out any documents of this sort.</p>
<dl>
<dt></dt></dl>
<h2>OPTIONS</h2>
<dd>
</dd><dl>
<dt><code>&#8211;</code></dt>
<dd> Take <i>URL</i> list from standard input (rather than specified with <i>-u</i>). Format of input file is one URL per line. <code>-a</code> Use alternate work files. Tells htpurge to append <i>.work</i> to database files, causing a second copy of the database to be built. This allows the original files to be used by htsearch during the run.</dd>
<dt><code>-c </code><i>configfile</i></dt>
<dd> Use the specified <i>configfile</i> instead of the default.</dd>
<dt><code>-u </code><i>URL</i></dt>
<dd> Add this <i>URL</i> to the list of documents to remove. Must be specified multiple times if more than one <i>URL</i> are to be removed. Should nor be used together with <i>&#8211;</i>.</dd>
<dt><code>-v</code></dt>
<dd> Verbose mode. This increases the verbosity of the program. Using more than 2 is probably only useful for debugging purposes. The default verbose mode (using only one <i>-v</i>) gives a nice progress report while digging.</dd></dl>
<h2>FILES</h2>
<dl>
<dt><code>/etc/htdig/htdig.conf</code></dt>
<dd> The default configuration file.</dd></dl>
<h2>SEE ALSO</h2>
<p> Please refer to the HTML pages (in the htdig-doc package) <code>/usr/share/doc/htdig-doc/html/index.html</code> and the manual pages <i>htdigconfig(8)</i> , <i><a href="/docs/linux/man/1-htdig/">htdig</a>(1)</i> and <i><a href="/docs/linux/man/1-htmerge/">htmerge</a>(1)</i> for a detailed description of ht://Dig and its commands. </p>
<h2>AUTHOR</h2>
<p> This manual page was written by Robert Ribnitz, based on the HTML documentation of ht://Dig. </p>
