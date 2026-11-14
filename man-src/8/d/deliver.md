---
title: "deliver(8)"
name: "deliver"
section: "8"
letter: "d"
url: "/docs/linux/man/8-deliver/"
description: "deliver – deliver mail to an IMAP mailbox"
---

<p>&nbsp;<wbr>*</p>
<h2>Name</h2>
<p>deliver &#8211; deliver mail to an IMAP mailbox</p>
<h2>Synopsis</h2>
<p><code>deliver</code> [ <code>-C</code> <i>config-file</i> ] [ <code>-d</code> ] [ <code>-r</code> <i>address</i> ] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>[ <code>-f</code> <i>address</i> ] [ <code>-m</code> <i>mailbox</i> ] [ <code>-a</code> <i>auth-id</i> ] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>[ <code>-q</code> ] [ <i>userid</i> ]&#8230;<br />
 <code>deliver</code> [ <code>-C</code> <i>config-file</i> ] <code>-l</code></p>
<h2>Description</h2>
<p><i>Deliver</i> reads a message from the standard input and delivers it to one or more IMAP mailboxes. </p>
<p> <i>Deliver</i> reads its configuration options out of the <i><a href="/docs/linux/man/5-imapd-conf/">imapd.conf</a></i>(5) file unless specified otherwise by <code>-C</code>.</p>
<h2>Options</h2>
<dl>
<dt><code>-C</code><i> config-file</i></p>
<dd>Read configuration options from <i>config-file</i>.</p>
<dt><code>-d</code></p>
<dd>Ignored for compatability with <code>/bin/mail.</code></p>
<dt><code>-r</code><i> address</i></p>
<dd>Insert a <code>Return-Path: </code> header containing <i>address</i></p>
<dt><code>-f</code><i> address</i></p>
<dd>Insert a <code>Return-Path: </code> header containing <i>address</i></p>
<dt><code>-m</code><i> mailbox</i></p>
<dd>Deliver to <i>mailbox</i>. If any <i>userid</i>s are specified, attempts to deliver to user.<i>userid</i>.<i>mailbox</i> for each <i>userid</i>. If the ACL on any such mailbox does not grant the sender the &quot;p&quot; right or if <code>-m</code> is not specified, then delivers to the INBOX for the <i>userid</i>, regardless of the ACL on the INBOX.</p>
<dd>If no <i>userid</i>s are specified, attempts to deliver to <i>mailbox</i>. If the ACL on <i>mailbox</i> does not grant the sender the &quot;p&quot; right, the delivery fails.</p>
<dt><code>-a</code><i> auth-id</i></p>
<dd>Specify the authorization id of the sender. Defaults to &quot;anonymous&quot;.</p>
<dt><code>-q</code></p>
<dd>Deliver message even when receiving mailbox is over quota.</p>
<dt><code>-l</code></p>
<dd>Accept messages using the LMTP protocol.</dl>
<h2>Notes</h2>
<p>Depending on the setting of <code>reject8bit</code> in <code><a href="/docs/linux/man/5-imapd-conf/">imapd.conf</a>(5)</code>, deliver either rejects/accepts messages with 8-bit-set characters in the headers. If we accept messages with 8-bit-set characters in the headers, then depending on the setting of <code>munge8bit</code>, these characters are either left un-touched or changed to `X&#8217;. This is because such characters can&#8217;t be interpreted since the character set is not known, although some communities not well-served by US-ASCII assume that those characters can be used to represent characters not present in US-ASCII. </p>
<p> A method for encoding 8-bit-set characters is provided by RFC 2047.</p>
<h2>Files</h2>
<dl>
<dt><code>/etc/imapd.conf</code></p>
<dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-lmtpd/">lmtpd</a>(8)</code> </p>
