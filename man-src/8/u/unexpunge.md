---
title: "unexpunge(8)"
name: "unexpunge"
section: "8"
letter: "u"
url: "/docs/linux/man/8-unexpunge/"
description: "unexpunge – restore expunged (but yet unremoved) messages"
---

<p>&nbsp;<wbr>*</p>
<h2>Name</h2>
<p>unexpunge &#8211; restore expunged (but yet unremoved) messages</p>
<h2>Synopsis</h2>
<p><code>unexpunge</code> [ <code>-C</code> <i>config-file</i> ] <code>-l</code> <i>mailbox</i><br />
 <code>unexpunge</code> [ <code>-C</code> <i>config-file</i> ] <code>-t time-interval</code> [ <code>-d</code> ] [ <code>-v</code> ] <i>mailbox</i><br />
 <code>unexpunge</code> [ <code>-C</code> <i>config-file</i> ] <code>-a</code> [ <code>-d</code> ] [ <code>-v</code> ] <i>mailbox</i><br />
 <code>unexpunge</code> [ <code>-C</code> <i>config-file</i> ] <code>-u</code> [ <code>-d</code> ] [ <code>-v</code> ] <i>mailbox uid</i>&#8230;</p>
<h2>Description</h2>
<p><i>Unexpunge</i> is used to restore expunged messages which have yet to be removed from the Cyrus mailspool. This utility is only useful when the server is configured to use <code>delayed</code> expunge. </p>
<p> <i>Unexpunge</i> reads its configuration options out of the <i><a href="/docs/linux/man/5-imapd-conf/">imapd.conf</a></i>(5) file unless specified otherwise by <code>-C</code>.</p>
<h2>Options</h2>
<dl>
<dt><code>-C</code><i> config-file</i></p>
<dd>Read configuration options from <i>config-file</i>.</p>
<dt><code>-l</code></p>
<dd>List the expunged messages in the specified mailbox which are available for restoration.</p>
<dt><code>-t</code><i> time-interval</i></p>
<dd>Unexpunge messages which were expunged in the last time-interval seconds. (modifiers: m: minutes, h: hours, d: days, w: weeks).</p>
<dt><code>-a</code></p>
<dd>Restore <code>all</code> of the expunged messages in the specified mailbox.</p>
<dt><code>-u</code></p>
<dd>Restore only those messages having the specified UIDs in the specified mailbox.</p>
<dt><code>-d</code></p>
<dd>Unset the <i>\Deleted</i> flag on any restored messages.</p>
<dt><code>-v</code></p>
<dd>Enable verbose output/logging.</dl>
<h2>Files</h2>
<dl>
<dt><code>/etc/imapd.conf</code></p>
<dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-imapd-conf/">imapd.conf</a>(5)</code> </p>
