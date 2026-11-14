---
title: "rmnews(8)"
name: "rmnews"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rmnews/"
description: "rmnews – expunge and remove news articles"
---

<p>&nbsp;<wbr>*</p>
<h2>Name</h2>
<p>rmnews &#8211; expunge and remove news articles</p>
<h2>Synopsis</h2>
<p><code>rmnews</code></p>
<h2>Description</h2>
<p><i>Rmnews</i> reads article data from the standard input. It then expunges and removes the listed articles. <i>Rmnews</i> is designed to be used by InterNetNews to remove canceled, superseded, and expired news articles. </p>
<p> The input is processed as an INN <i>expirerm</i> file listing or an INN cancel stream written as a &#8220;WC&#8221; entry in the <i><a href="/docs/linux/man/5-newsfeeds/">newsfeeds</a></i>(5) file. This data consists of lines of text, each containing a list of relative article pathnames, with a single space between entries. If a listed file is contained in an IMAP news mailbox, it is expunged out of that mailbox. In any case, each listed file is unlinked. </p>
<p> <i>Rmnews</i> reads its configuration options out of the <i><a href="/docs/linux/man/5-imapd-conf/">imapd.conf</a></i>(5) file. The optional <i>newsprefix</i> option specifies a prefix to be prepended to newsgroup names to make the corresponding IMAP mailbox names. The required <i>partition-news</i> option specifies the pathname prefix to the IMAP news mailboxes. The value of <i>partition-news</i> concatenated with the dots-to-slashes-converted value of <i>newsprefix</i> must be the pathname of the news spool directory.</p>
<h2>Files</h2>
<dl>
<dt><code>/etc/imapd.conf</code></p>
<dd></dl>
