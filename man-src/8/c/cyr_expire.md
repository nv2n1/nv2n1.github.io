---
title: "cyr_expire(8)"
name: "cyr_expire"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cyr_expire/"
description: "cyr_expire – expire messages and duplicate delivery database entries"
---

<p>&nbsp;<wbr>*</p>
<h2>Name</h2>
<p>cyr_expire &#8211; expire messages and duplicate delivery database entries</p>
<h2>Synopsis</h2>
<p><code>cyr_expire</code> [ <code>-C</code> <i>config-file</i> ] [ <code>-D</code><i> delete-days</i> ] <code>-E</code><i> expire-duration</i> [ <code>-X</code><i> expunge-days</i> ] [ <code>-p mailbox-prefix</code> ] [ <code>-v</code> ]</p>
<h2>Description</h2>
<p><i>Cyr_expire</i> is used to expire messages and duplicate delivery database entries. <i>Cyr_expire</i> also cleanses mailboxes of partially expunged messages (when using the &quot;delayed&quot; expunge mode). The expiration of messages is controlled by the <code>/vendor/cmu/cyrus-imapd/expire</code> mailbox annotation which specifies the age (in days) of messages in the given mailbox that should be deleted. Any duplicate delivery database entries which correspond to the mailbox are also deleted at the same frequency. </p>
<p> The value of the <code>/vendor/cmu/cyrus-imapd/expire</code> annotation is inherited by all children of the given mailbox, so an entire mailbox tree can be expired by seting a single annotation on the root of that tree. If a mailbox does not have a <code>/vendor/cmu/cyrus-imapd/expire</code> annotation set on it (or does not inherit one), then no messages are expired from the mailbox. </p>
<p> <i>Cyr_expire</i> reads its configuration options out of the <i><a href="/docs/linux/man/5-imapd-conf/">imapd.conf</a></i>(5) file unless specified otherwise by <code>-C</code>.</p>
<h2>Options</h2>
<dl>
<dt><code>-C</code><i> config-file</i></p>
<dd>Read configuration options from <i>config-file</i>.</p>
<dt><code>-D </code><i>delete-duration</i></p>
<dd>Remove previously deleted mailboxes older than <i>delete-duration</i> (when using the &quot;delayed&quot; delete mode). The value can be a floating point number, and may have a suffix to specify the unit of time. If no suffix, the value is number of days. Valid suffixes are <code>d</code> (days), <code>h</code> (hours), <code>m</code> (minutes) and <code>s</code> (seconds).</p>
<dt><code>-E </code><i>expire-duration</i></p>
<dd>Prune the duplicate database of entries older than <i>expire-duration</i>. This value is only used for entries which do not have a corresponding <code>/vendor/cmu/cyrus-imapd/expire</code> mailbox annotation. Format is the same as delete-duration.</p>
<dt><code>-X </code><i>expunge-duration</i></p>
<dd>Expunge previously deleted messages older than <i>expunge-duration</i> (when using the &quot;delayed&quot; expunge mode). Format is the same as delete-duration.</p>
<dt><code> -x</p>
<dd>Do not expunge messages even if using delayed expunge mode (reduces the IO hit considerably, allowing you to run cyr_expire frequently to clean up the duplicate database without overloading your server)</p>
<dt>-p </code><i>mailbox-prefix</i></p>
<dd>Only find mailboxes starting with this prefix. e.g. &quot;user.justgotspammedlots&quot;</p>
<dt><code>-v</code></p>
<dd>Enable verbose output.</p>
<dt><code>-a</code></p>
<dd>Skip the annotation lookup, so all <code>/vendor/cmu/cyrus-imapd/expire</code> annotations are ignored entirely. It behaves as if they were not set, so only <i>expire-days</i> is considered for all mailboxes.</dl>
<h2>Files</h2>
<dl>
<dt><code>/etc/imapd.conf</code></p>
<dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-imapd-conf/">imapd.conf</a>(5)</code>, <code><a href="/docs/linux/man/8-cyrus-master/">cyrus-master</a>(8)</code> </p>
