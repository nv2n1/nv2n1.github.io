---
title: "htdig(1)"
name: "htdig"
section: "1"
letter: "h"
url: "/docs/linux/man/1-htdig/"
description: "htdig – retrieve HTML documents for ht://Dig search engine"
---

<h2 class="name">NAME</h2>
<p> htdig &#8211; retrieve HTML documents for ht://Dig search engine </p>
<h2>SYNOPSIS</h2>
<p> <code>htdig</code> <i>[options]</i></p>
<h2>DESCRIPTION</h2>
<p> Htdig retrieves HTML documents using the HTTP protocol and gathers information from these documents which can later be used to search these documents. This program can be referred to as the search robot.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;</code></p>
<dd> Get the list of URLs to start indexing from standard input. This will override the default parameter <i>start_url</i> specified in the config file and the file supplied to the <i>-m</i> option.</p>
<dt><code>-a</code></p>
<dd> Use alternate work files. Tells htdig to append <i>.work</i> to database files, causing a second copy of the database to be built. This allows the original files to be used by htsearch during the indexing run.</p>
<dt><code>-c </code><i>configfile</i></p>
<dd> Use the specified <i>configfile</i> instead of the default.</p>
<dt><code>-h </code><i>maxhops</i></p>
<dd> Restrict the dig to documents that are at most <i>maxhops</i> links away from the starting document. This only works if option <i>-i</i> is also given.</p>
<dt><code>-i</code></p>
<dd> Initial. Do not use any old databases. Old databases will be erased before runing the program.</p>
<dt><code>-m </code><i>filename</i></p>
<dd> Minimal run. Only index the URLs given in the file <i>filename</i>, ignoring all others. URLs in the file should be formatted one URL per line. <code>-s</code> Print statistics about the dig after completion.</p>
<dt><code>-t</code></p>
<dd> Create an ASCII version of the document database. This database is easy to parse with other programs so that information can be extracted from it for purposes other than searching. One could gather some interesting statistics from this database. </p>
<table>
<tr VALIGN=top>
<td ALIGN=center><code>Fieldname</code></td>
<td ALIGN=center><code>Value</code>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>u</td>
<td>URL
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>t</td>
<td>Title
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>a</td>
<td>State
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center></td>
<td>(0 normal, 1 not found, 2 not indexed, 3 obsolete)
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>m</td>
<td>Time of last modification reported by the server
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>s</td>
<td>Document Size in bytes
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>H</td>
<td>Excerpt of the document
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>h</td>
<td>Meta Description
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>l</td>
<td>Time of last rerievial
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>L</td>
<td>Count of links in the document or of <i>outgoing links</i>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>b</td>
<td>Number of links to the document, also called
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center></td>
<td><i>incoming</i> links or <i>backlinks</i>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>c</td>
<td>Hop count of this document
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>g</td>
<td>Signature of this document
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center></td>
<td>(used to detect duplicates)
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>e</td>
<td>E-Mail address to use for a notification from <i>htnotify</i>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>n</td>
<td>Date on which such notification is sent
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>S</td>
<td>Subject of the notfication message
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>d</td>
<td>The text of Incoming links pointing to this document
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center></td>
<td>(e.g. &lt;a href=&quot;docURL&quot;&gt;description&lt;/a&gt;)
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>A</td>
<td>Anchors in the document (i.e. &lt;A NAME=&#8230;)
</td>
</tr>
</table>
<dt><code>-u </code><i>username:password</i></p>
<dd> Tells htdig to send the supplied username and password with each HTTP request. The credentials will be encoded using the <i>&#8216;Basic&#8217;</i> authentication method. There <code>HAS</code> to be a colon (:) between the username and password.</p>
<dt><code>-v</code></p>
<dd> Verbose mode. This increases the verbosity of the program. Using more than 2 is probably only useful for debugging purposes. The default verbose mode (using only one -v) gives a nice progress report while digging. Please consult the section below on the exact format of the progress report.</p>
<dt></dl>
<h2>FORMAT OF THE PROGRESS REPORT GIVEN IN VERBOSE MODE</h2>
<dd> A line is shown for each URL, with 3 numbers before the URL and some symbols after the URL. The first number is the number of documents parsed so far, the second is the DocID for this document, and the third is the hop count of the document (number of hops from one of the start_url documents). Signification of the sybols printed after the url:</p>
<dl>
<dt>
<dd> <i>&quot;*&quot;</i> is printed for a link already visited</p>
<dt>
<dd> <i>&quot;+&quot;</i> is printed for a new link just queued</p>
<dt>
<dd> <i>&quot;-&quot;</i> is output for a link rejected for any of a number of reasons. To find out what those reasons are, you need to run htdig with at least 3 <i>-v</i> options, i.e. <i>-vvv</i>.</p>
<dt>If there are no &quot;*&quot;, &quot;+&quot; or &quot;-&quot; symbols after the URL, it doesn&#8217;t mean the document was not parsed or was empty, but only that no links to other documents were found within it. With more verbose output, these symbols will get interspersed in several lines of debugging output.</p>
<dd>
<dt></dl>
<h2>FILES</h2>
<dd>
<dl>
<dt><code>/etc/htdig/htdig.conf</code></p>
<dd> The default configuration file. <code>/var/lib/htdig/db.docdb</code> Stores data about each document (title, url, etc.). <code>/var/lib/htdig/db.words.db, /var/lib/htdig/db.words.db_weakcmpr</code> Record which documents each word occurs in. <code>/var/lib/htdig/db.excerpts</code> Stores start of each document to show context of matches.</dl>
<h2>SEE ALSO</h2>
<p> Please refer to the HTML pages (in the htdig-doc package) <code>/usr/share/doc/htdig-doc/html/index.html</code> and the manual pages <i><a href="/docs/linux/man/8-htdigconfig/">htdigconfig</a>(8)</i> , <i><a href="/docs/linux/man/1-htmerge/">htmerge</a>(1)</i> , <i><a href="/docs/linux/man/1-htnotify/">htnotify</a>(1)</i> , <i><a href="/docs/linux/man/1-htsearch/">htsearch</a>(1)</i> and <i><a href="/docs/linux/man/1-rundig/">rundig</a>(1)</i> for a detailed description of ht://Dig and its commands.</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Christian Schwarz, modified by Stijn de Bekker. It is updated and maintained by Robert Ribnitz and based on the HTML documentation of ht://Dig. </p>
<h2>Index</h2>
