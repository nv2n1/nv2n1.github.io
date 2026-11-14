---
title: "in(5)"
name: "in"
section: "5"
letter: "i"
url: "/docs/linux/man/5-in/"
description: "in.hosts – newsx incoming host state"
---

<p>in.hosts &#8211; newsx incoming host state </p>
<h2>Description</h2>
<p>The <code>in.hosts</code> directory contains the necessary state information for the incoming news streams fetched by <i><a href="/docs/linux/man/8-newsx/">newsx</a></i>(8). For each incoming news source, there must be a <i>/var/spool/news/inhosts/spoolname</i> file that describes what the latest article is that has been fetched from that particular host. If you want to get all news articles in all the groups defined at your local server, do nothing and let the file be constructed automatically. Other choices, such as using multiple <i><a href="/docs/linux/man/8-cron/">cron</a></i>(8) entries and <i><a href="/docs/linux/man/8-newsx/">newsx</a></i>(8) end tags to control when certain newsgroups are fetched, or using <code>.newsrc</code> article numbers to avoid fetching articles you&#8217;ve already seen, require setting up the <code>in.hosts</code> file for the server by hand. The format of this file is simple: Blank lines and lines starting with a &#8216;#&#8217; are treated as comments. Lines starting with a &#8216;:&#8217; indicate a tag for use with the newsx <code>-e</code> (end tag) option. Otherwise, each line consists of a newsgroup name and the first unread article number, separated by whitespace. No article number is the same as zero, meaning that all available articles on the server will be read. It is important to realize that there is one unique file belonging to each remote newsserver, and that they should not be mixed. If switching from reading news via an NNTP newsreader to fetching with newsx, it is possible to use an existing <code>.newsrc </code> file directly as the initial <code>/var/spool/news/inhosts/</code><i>spoolname</i> file. </p>
<h2>Files</h2>
<dl>
<dt>/var/spool/news/inhosts/<i>spoolname</i></p>
<dd>Incoming host state file. There should be one of these per external news server.</p>
<dt>/var/spool/news/inhosts/<i>spoolname</i>.tmp</p>
<dd>Incoming spool, temporary (while news is being pulled).</p>
<dt>/var/spool/news/inhosts/<i>spoolname</i>.old</p>
<dd>Previous generation of the external host state file.</p>
<dt>/var/spool/news/in.hosts/<i>spoolname</i>.conf</p>
<dd>Standard profile for specific newsspool. See <i><a href="/docs/linux/man/5-newsx-conf/">newsx.conf</a></i>(5) for file format. </p>
</dl>
<h2>Author</h2>
<p>Egil Kvaleberg &lt;egil [at] kvaleberg.no&gt;</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-newsx/">newsx</a></i>(8) </p>
