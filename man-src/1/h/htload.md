---
title: "htload(1)"
name: "htload"
section: "1"
letter: "h"
url: "/docs/linux/man/1-htload/"
description: "htload – reads in an ASCII-text version of the document database"
---

<h2 class="name">NAME</h2>
<p> htload &#8211; reads in an ASCII-text version of the document database </p>
<h2>SYNOPSIS</h2>
<p> <code>htload</code> <i>[options]</i></p>
<h2>DESCRIPTION</h2>
<p> Htload reads in an ASCII-text version of the document database in the same form as the -t option of htdig and htdump. Note that this will overwrite data in your databases, so this should be used with great care.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code></p>
<dd> Use alternate work files. Tells htload to append <i>.work</i> to database files, allowing it to operate on a second set of databases.</p>
<dt><code>-c </code><i>configfile</i></p>
<dd> Use the specified <i>configfile</i> instead of the default.</p>
<dt><code>-i</code></p>
<dd> Initial. Do not use any old databases. This is accomplished by first erasing the databases.</p>
<dt><code>-v</code></p>
<dd> Verbose mode. This doesn&#8217;t have much effect.</dl>
<h2>File Formats</h2>
<dl>
<dt><code>Document Database</code></p>
<dd> Each line in the file starts with the document id followed by a list of <i>fieldname</i> : <i>value</i> separated by tabs. The fields always appear in the order listed below:</p>
<dt><code>u</code></p>
<dd> URL</p>
<dt><code>t</code></p>
<dd> Title</p>
<dt><code>a</code></p>
<dd> State (0 = normal, 1 = not found, 2 = not indexed, 3 = obsolete)</p>
<dt><code>m</code></p>
<dd> Last modification time as reported by the server</p>
<dt><code>s</code></p>
<dd> Size in bytes</p>
<dt><code>H</code></p>
<dd> Excerpt</p>
<dt><code>h</code></p>
<dd> Meta description</p>
<dt><code>l</code></p>
<dd> Time of last retrieval</p>
<dt><code>L</code></p>
<dd> Count of the links in the document (outgoing links)</p>
<dt><code>b</code></p>
<dd> Count of the links to the document (incoming links or backlinks)</p>
<dt><code>c</code></p>
<dd> HopCount of this document</p>
<dt><code>g</code></p>
<dd> Signature of the document used for duplicate-detection</p>
<dt><code>e</code></p>
<dd> E-mail address to use for a notification message from htnotify</p>
<dt><code>n</code></p>
<dd> Date to send out a notification e-mail message</p>
<dt><code>S</code></p>
<dd> Subject for a notification e-mail message</p>
<dt><code>d</code></p>
<dd> The text of links pointing to this document. (e.g. &lt;a href=&quot;docURL&quot;&gt;description&lt;/a&gt;)</p>
<dt><code>A</code></p>
<dd> Anchors in the document (i.e. &lt;A NAME=&#8230;)</p>
<dt><code>Word Database</code></p>
<dd> While htdump and htload don&#8217;t deal with the word database directly, it&#8217;s worth mentioning it here because you need to deal with it when copying the ASCII databases from one system to another. The initial word database produced by htdig is already in ASCII format, and a binary version of it is produced by htmerge, for use by htsearch. So, when you copy over the ASCII version of the document database produced by htdump, you need to copy over the wordlist as well, then run htload to make the binary document database on the target system, followed by running htmerge to make the word index.</p>
<dt>Each line in the word list file starts with the word</p>
<dd> followed by a list of <i>fieldname</i> : <i>value</i> separated by tabs. The fields always appear in the order listed below, with the last two being optional:</p>
<dt><code>i</code></p>
<dd> Document ID</p>
<dt><code>l</code></p>
<dd> Location of word in document (1 to 1000)</p>
<dt><code>w</code></p>
<dd> Weight of word based on scoring factors</p>
<dt><code>c</code></p>
<dd> Count of word&#8217;s appearances in document, if more than 1</p>
<dt><code>a</code></p>
<dd> Anchor number if word occurred after a named anchor</dl>
<h2>FILES</h2>
<dl>
<dt><code>/etc/htdig/htdig.conf</code></p>
<dd> The default configuration file.</p>
<dt><code>/var/lib/htdig/db.docs</code></p>
<dd> The default ASCII document database file.</p>
<dt><code>/var/lib/htdig/db.wordlist</code></p>
<dd> The default ASCII word database file.</dl>
<h2>SEE ALSO</h2>
<p> Please refer to the HTML pages (in the htdig-doc package) <code>/usr/share/doc/htdig-doc/html/index.html</code> and the manual pages <i><a href="/docs/linux/man/1-htdig/">htdig</a>(1)</i> , <i><a href="/docs/linux/man/1-htmerge/">htmerge</a>(1)</i> and <i><a href="/docs/linux/man/1-htdump/">htdump</a>(1)</i> for a detailed description of ht://Dig and its commands.</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Stijn de Bekker, based on the HTML documentation of ht://Dig. </p>
<h2>Index</h2>
