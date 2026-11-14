---
title: "squatter(8)"
name: "squatter"
section: "8"
letter: "s"
url: "/docs/linux/man/8-squatter/"
description: "squatter – create SQUAT indexes for mailboxes"
---

<p>&nbsp;<wbr>*</p>
<h2>Name</h2>
<p>squatter &#8211; create SQUAT indexes for mailboxes</p>
<h2>Synopsis</h2>
<p><code>squatter</code> [ <code>-C</code> <i>config-file</i> ] [ <code>-r</code> ] [ <code>-s</code> ] [ <code>-i</code> ] [ <code>-a</code> ] [ <code>-v</code> ] <i>mailbox</i>&#8230;</p>
<h2>Description</h2>
<p><i>Squatter</i> creates a new SQUAT index for one or more IMAP mailboxes. The SQUAT index is a unified index of all of the header and body text of each message a given mailbox. This index is used to significantly reduce IMAP SEARCH times on a mailbox. </p>
<p> <i>Squatter</i> creates an index of ALL messages in the mailbox, not just those since the last time that it was run (i.e., it does NOT do incremental updates). Any messages appended to the mailbox after <i>squatter</i> is run, will NOT be included in the index. To include new messages in the index, <i>squatter</i> must be run again. For large and active mailboxes, it is recommended to run <i>squatter</i> periodically as an EVENT in <i><a href="/docs/linux/man/5-cyrus-conf/">cyrus.conf</a></i>(5) </p>
<p> <code>NOTE:</code> Messages and mailboxes that have not been indexed CAN still be SEARCHed, just not as quickly as those with a SQUAT index. </p>
<p> <i>Squatter</i> reads its configuration options out of the <i><a href="/docs/linux/man/5-imapd-conf/">imapd.conf</a></i>(5) file unless specified otherwise by <code>-C</code>.</p>
<h2>Options</h2>
<dl>
<dt><code>-C</code><i> config-file</i></p>
<dd>Read configuration options from <i>config-file</i>.</p>
<dt><code>-r</code></p>
<dd>Recursively create indexes for all sub-mailboxes of the mailboxes or mailbox prefixes given as arguments.</p>
<dt><code>-s</code></p>
<dd>Skip mailboxes whose index file is older than their current squat file (within a small time delta).</p>
<dt><code>-i</code></p>
<dd>Incremental updates where squat indexes already exist.</p>
<dt><code>-a</code></p>
<dd>Only create indexes for mailboxes which have the shared <i>/vendor/cmu/cyrus-imapd/squat</i> annotation set to &quot;true&quot;. </p>
<p> The value of the <code>/vendor/cmu/cyrus-imapd/squat</code> annotation is inherited by all children of the given mailbox, so an entire mailbox tree can be indexed (or not indexed) by setting a single annotation on the root of that tree with a value of &quot;true&quot; (or &quot;false&quot;). If a mailbox does not have a <code>/vendor/cmu/cyrus-imapd/squat</code> annotation set on it (or does not inherit one), then the mailbox is not indexed. In other words, the implicit value of <code>/vendor/cmu/cyrus-imapd/squat</code> is &quot;false&quot;.</p>
<dt><code>-v</code></p>
<dd>Increase the verbosity of progress/status messages.</dl>
<h2>Files</h2>
<dl>
<dt><code>/etc/imapd.conf /etc/cyrus.conf</code></p>
<dd></dl>
