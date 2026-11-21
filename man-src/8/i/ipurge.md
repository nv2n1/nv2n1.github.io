---

title: "ipurge(8)"
name: "ipurge"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ipurge/"
description: "ipurge – delete mail from IMAP mailbox or partition based on age or size"
---

<p>&nbsp;<wbr>*</p>

<p>ipurge &#8211; delete mail from IMAP mailbox or partition based on age or size</p>
<h2>Synopsis</h2>
<p><code>ipurge</code> [ <code>-f</code> ] [ <code>-C</code> <i>config-file</i> ] [ <code>-x</code> ] [ <code>-X</code> ] [ <code>-i</code> ] [ <code>-s</code> ] [ <code>-o</code> ] </p>
<p>&nbsp;<wbr>[ <code>-d</code><i> days</i> | <code>-b</code><i> bytes</i> | <code>-k</code><i> Kbytes</i> | <code>-m</code><i> Mbytes</i> ] </p>
<p>&nbsp;<wbr>[ <i>mailbox-pattern</i>&#8230; ]</p>
<h2>Description</h2>
<p><i>Ipurge</i> deletes messages from the mailbox(es) specified by <i>mailbox-pattern</i> that are older or larger than specified by the <code>-d</code>, <code>-b</code>, <code>-k</code> or <code>-m</code> options. If no <i>mailbox-pattern</i> is given, <i>ipurge</i> works on all mailboxes. If the <code>-x</code> option is given, the message age and size MUST match exactly those specified by <code>-d</code>, <code>-b</code>, <code>-k</code> or <code>-m</code>. The are no default values, and at least one of <code>-d</code>, <code>-b</code>, <code>-k</code> or <code>-m</code> MUST be specified. </p>
<p> <i>Ipurge</i> by default only deletes mail below shared folders, which means that mails in mailbox(es) below INBOX.* and user.* stay untouched. Use the option <code>-f</code> to also delete mail in mailbox(es) below these folders. </p>
<p> <i>Ipurge</i> reads its configuration options out of the <i><a href="/docs/linux/man/5-imapd-conf/">imapd.conf</a></i>(5) file unless specified otherwise by <code>-C</code>.</p>
<h2>Options</h2>
<dl>
<dt><code>-f</code></dt>
<dd>Force deletion of mail in <i>all</i> mailboxes.</dd>
<dt><code>-C</code><i> config-file</i></dt>
<dd>Read configuration options from <i>config-file</i>.</dd>
<dt><code>-d</code><i> days</i></dt>
<dd>Age of message in <i>days</i>.</dd>
<dt><code>-b</code><i> bytes</i></dt>
<dd>Size of message in <i>bytes</i>.</dd>
<dt><code>-k</code><i> Kbytes</i></dt>
<dd>Size of message in <i>Kbytes</i> (2^10 bytes).</dd>
<dt><code>-m</code><i> Mbytes</i></dt>
<dd>Size of message in <i>Mbytes</i> (2^20 bytes).</dd>
<dt><code>-x</code></dt>
<dd>Perform an exact match on age or size (instead of older or larger).</dd>
<dt><code>-X</code></dt>
<dd>Use delivery time instead of Date: header for date matches</dd>
<dt><code>-i</code></dt>
<dd>Invert match logic: -x means not equal, date is for newer, size is for smaller</dd>
<dt><code>-s</code></dt>
<dd>Skip over messages that have the \Flagged flag set.</dd>
<dt><code>-o</code></dt>
<dd>Only purge messages that have the \Deleted flag set.</dd></dl>
<h2>Files</h2>
<dl>
<dt><code>/etc/imapd.conf</code></dt>
<dd></dd></dl>
