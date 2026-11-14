---
title: "arbitron(8)"
name: "arbitron"
section: "8"
letter: "a"
url: "/docs/linux/man/8-arbitron/"
description: "arbitron – arbitron mailboxes"
---

<p>&nbsp;<wbr>*</p>
<h2>Name</h2>
<p>arbitron &#8211; arbitron mailboxes</p>
<h2>Synopsis</h2>
<p><code>arbitron</code> [ <code>-C</code> <i>config-file</i> ] [ <code>-o</code> ] [ <code>-u</code> ] [ <code>-l</code> ] [ <code>-p</code> <i>months</i> ] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[ <code>-d</code> <i>days</i> | <code>-D</code> <i>mmddyyyy</i>[<code>:</code><i>mmddyyyy</i>] ] <i>mailbox</i>&#8230;</p>
<h2>Description</h2>
<p><i>Arbitron</i> collects and reports readership statistics for mailboxes on the server. It also optionally prunes the mailboxes of \Seen state for dormant users. </p>
<p> <i>Arbitron</i> produces one line of output per mailbox, reporting the mailbox name followed by a space, followed by the number of readers (and if -u is specified, followed by a colon and a comma-separated list of the readers userids), and if -o is not specified, another space and the number of subscribers (and if -u is specified, followed by a colon and a comma-separated list of the subscribers userids). <code>IMPORTANT: This format is subject to change in future versions.</code> </p>
<p> Each &quot;reader&quot; is a distinct authentication identity which has &quot;s&quot; rights to the mailbox and which has SELECTed the mailbox within either the past <i>days</i> days or the specified date range. Users are not counted as reading their own personal mailboxes. Personal mailboxes are not reported unless there is at least one reader other than the mailboxes owner. </p>
<p> <i>Arbitron</i> reads its configuration options out of the <i><a href="/docs/linux/man/5-imapd-conf/">imapd.conf</a></i>(5) file unless specified otherwise by <code>-C</code>.</p>
<h2>Options</h2>
<dl>
<dt><code>-C</code><i> config-file</i></p>
<dd>Read configuration options from <i>config-file</i>.</p>
<dt><code>-o</code></p>
<dd>&quot;old way&quot; &#8212; do not report subscribers.</p>
<dt><code>-u</code></p>
<dd>Report userids in addition to the count(s).</p>
<dt><code>-l</code></p>
<dd>Enable long reporting (comma delimited table consisting of mbox, userid, r/s, start time, end time).</p>
<dt><code>-d </code><i>days</i></p>
<dd>Count as a reader an authentication identity which has SELECTed the mailbox within <i>days</i> days. Default is 30.</p>
<dt><code>-D</code> <i>mmddyyyy</i>[<code>:</code><i>mmddyyyy</i>]</p>
<dd>Count as a reader an authentication identity which has SELECTed the mailbox within the given date range. The start date and optional end date are specified as 2-digit month of the year, 2-digit day of the month, and 4-digit year. If the end date is not specified, then the current system time is used as the end time.</p>
<dt><code>-p </code><i>months</i></p>
<dd>Prune \Seen state for users who have not SELECTed the mailbox within <i>months</i> months. Default is infinity.</dl>
<h2>Files</h2>
<dl>
<dt><code>/etc/imapd.conf</code></p>
<dd></dl>
