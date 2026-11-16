---
title: "doveadm-search-query(7)"
name: "doveadm-search-query"
section: "7"
letter: "d"
url: "/docs/linux/man/7-doveadm-search-query/"
description: "doveadm-search-query – Overview of search queries for doveadm mailbox commands"
---

<p>doveadm-search-query &#8211; Overview of search queries for doveadm mailbox commands</p>
<h2>Description</h2>
<p>Several <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1) commands use a <i>search_query</i> in order to act only on matching messages. This manual page describes all <i>SEARCH KEYS</i>, which can be used in a <i>search_query</i>. </p>
<p> Each <i>search_query</i> consists at least of one <i>SEARCH KEY</i>. Most of the <i>SEARCH KEYS</i> require an argument. All <i>SEARCH KEYS</i> are case-insensitive. The shortest valid <i>search_query</i> is <code>ALL</code>. For example: </p>
<dl>
<dd>
<pre>doveadm search ALL</pre>
</dd></dl>
<p> Multiple search query expressions will be combined with the <code>AND</code> operator by default. To find all messages that are new and greater than 50 kilobyte, one can use: </p>
<dl>
<dd>
<pre>doveadm search NEW LARGER 50k</pre>
</dd></dl>
<p> <code>OR</code>-ed <i>SEARCH KEYS</i> have to be written in parenthesis, when mixing ANDs and ORs. Shells commonly require escaping for parentheses. To find messages that were saved on the &quot;13th of April 2007&quot; AND have the \Seen and/or \Flagged flag set, one can use for example: </p>
<dl>
<dd>
<pre>doveadm search SAVEDON 2007-04-13 \( SEEN OR FLAGGED \)</pre>
</dd></dl>
<p> It&#8217;s also possible to specify the mailbox, in which should be searched. Use either the keyword <code>mailbox</code> and the name of the mailbox or the keyword <code>mailbox-guid</code> and the mailbox&#8217;s globally unique identifier in the <i>search_query</i>. To find all messages in the mailbox with the GUID &quot;44f68b13ce97044b837f000035ca9452&quot; use: </p>
<dl>
<dd>
<pre>doveadm search mailbox-guid 44f68b13ce97044b837f000035ca9452 ALL</pre>
</dd></dl>
<p> To list all deleted messages in the &quot;Trash&quot; folder use: </p>
<dl>
<dd>
<pre>doveadm search mailbox Trash DELETED</pre>
</dd></dl>
<h2>Search Keys</h2>
<p>The following search keys from the specification of IMAP version 4 revision 1 (see: RFC 3501, section 6.4.4) are supported:</p>
<dl>
<dt><code>ALL</code></dt>
<dd>Matches all messages.</dd>
<dt><code>ANSWERED</code></dt>
<dd>Matches messages with the IMAP flag \Answered set.</dd>
<dt><code>BCC&nbsp;<wbr></code><i>pattern</i></dt>
<dd>Matches messages, which contain <i>pattern</i> in the BCC field of the message&#8217;s IMAP envelope structure.</dd>
<dt><code>BEFORE</code><i>&nbsp;<wbr>date specification</i></dt>
<dd>Matches messages with an internal date before <i>date specification</i>.</dd>
<dt><code>BODY&nbsp;<wbr></code><i>pattern</i></dt>
<dd>Matches messages, which contain <i>pattern</i> in the body part.</dd>
<dt><code>CC&nbsp;<wbr></code><i>pattern</i></dt>
<dd>Matches messages, which contain <i>pattern</i> in the CC field of the message&#8217;s IMAP envelope structure.</dd>
<dt><code>DELETED</code></dt>
<dd>Matches messages with the IMAP flag \Deleted set.</dd>
<dt><code>DRAFT</code></dt>
<dd>Matches messages with the IMAP flag \Draft set.</dd>
<dt><code>FLAGGED</code></dt>
<dd>Matches messages with the IMAP flag \Flagged set.</dd>
<dt><code>FROM&nbsp;<wbr></code><i>pattern</i></dt>
<dd>Matches messages, which contain <i>pattern</i> in the FROM field of the message&#8217;s IMAP envelope structure.</dd>
<dt><code>HEADER</code> <i>field</i> <i>pattern</i></dt>
<dd>Matches messages, which either have the named header <i>field</i>, when empty <i>pattern</i> was given. Or messages, where the given header <i>field</i>&#8216;s value contains the specified <i>pattern</i>.</dd>
<dt><code>KEYWORD&nbsp;<wbr></code><i>keyword</i></dt>
<dd>Matches messages with the given IMAP <i>keyword</i> (e.g. $Forwarded) flag set.</dd>
<dt><code>LARGER&nbsp;<wbr></code><i>size</i></dt>
<dd>Matches messages that are larger than the specified <i>size</i>.</dd>
<dt><code>MAILBOX&nbsp;<wbr></code><i>name</i></dt>
<dd>Matches messages in the mailbox with the specified <i>name</i>.</dd>
<dt><code>MAILBOX-GUID&nbsp;<wbr></code><i>guid</i></dt>
<dd>Matches messages in the mailbox with the specified <i>guid</i>.</dd>
<dt><code>NEW</code></dt>
<dd>Matches messages, which have the IMAP flag \Recent set <code>but not</code> the IMAP flag \Seen.</dd>
<dt><code>NOT&nbsp;<wbr></code><i>search key</i></dt>
<dd>Inverse matching &#8211; matches massages, where the search doesn&#8217;t match the specified <i>search key</i> or its value.</dd>
<dt><code>OLD</code></dt>
<dd>Matches messages, which do not have the IMAP flag \Recent set.</dd>
<dt><code>ON&nbsp;<wbr></code><i>date specification</i></dt>
<dd>Matches messages whose internal date matches the given <i>date specification</i>.</dd>
<dt><i>search key&nbsp;<wbr></i><code>OR&nbsp;<wbr></code><i>search key</i></dt>
<dd>Matches messages where one of the OR-ed search keys matches.<br />
 Note: IMAP4rev1 uses the syntax: <code>OR&nbsp;<wbr></code><i>search key search key</i></dd>
<dt><code>RECENT</code></dt>
<dd>Matches messages with the IMAP flag \Recent set.</dd>
<dt><code>SEEN</code></dt>
<dd>Matches messages with the IMAP flag \Seen set.</dd>
<dt><code>SENTBEFORE&nbsp;<wbr></code><i>date specification</i></dt>
<dd>Matches messages with a Date: header before <i>date specification</i>.</dd>
<dt><code>SENTON&nbsp;<wbr></code><i>date specification</i></dt>
<dd>Matches messages with a Date: header matching the given <i>date specification</i>.</dd>
<dt><code>SENTSINCE&nbsp;<wbr></code><i>date specification</i></dt>
<dd>Matches messages with a Date: header matching or after the given <i>date specification</i>.</dd>
<dt><code>SINCE&nbsp;<wbr></code><i>date specification</i></dt>
<dd>Matches messages whose internal date is within or after the given <i>date specification</i>.</dd>
<dt><code>SMALLER&nbsp;<wbr></code><i>size</i></dt>
<dd>Matches messages with a size smaller than the given <i>size</i>.</dd>
<dt><code>SUBJECT&nbsp;<wbr></code><i>pattern</i></dt>
<dd>Matches messages, which contain <i>pattern</i> in the SUBJECT field of the message&#8217;s IMAP envelope structure.</dd>
<dt><code>TEXT&nbsp;<wbr></code><i>pattern</i></dt>
<dd>Matches messages, which contain <i>pattern</i> in the message body.</dd>
<dt><code>TO&nbsp;<wbr></code><i>pattern</i></dt>
<dd>Matches messages, which contain <i>pattern</i> in the TO field of the message&#8217;s IMAP envelope structure.</dd>
<dt><code>UID&nbsp;<wbr></code><i>sequence</i></dt>
<dd>Matches messages with the given UID(s). A <i>sequence</i> may be a single UID. Can be a sequence range, written as <i>from</i>:<i>to</i>, e.g.&nbsp;<wbr><code>100</code>:<code>125</code>. As comma separated list of UIDs, e.g. <code>11,50,4</code>. It&#8217;s also possible to combine multiple sequences, e.g. <code>1,3,5,7,10:20</code>.</dd>
<dt><code>UNANSWERED</code></dt>
<dd>Matches messages, which do not have the IMAP flag \Answered set.</dd>
<dt><code>UNDELETED</code></dt>
<dd>Matches messages, which do not have the IMAP flag \Deleted set.</dd>
<dt><code>UNDRAFT</code></dt>
<dd>Matches messages, which do not have the IMAP flag \Draft set.</dd>
<dt><code>UNFLAGGED</code></dt>
<dd>Matches messages, which do not have the IMAP flag \Flagged set.</dd>
<dt><code>UNKEYWORD&nbsp;<wbr></code><i>keyword</i></dt>
<dd>Matches messages, which do not have the given IMAP <i>keyword</i> flag set</dd>
<dt><code>UNSEEN</code></dt>
<dd>Matches messages, which do not have the IMAP flag \Seen set.</dd></dl>
<h3>Doveadm Search Keys</h3>
<p>Additional search keys, provided by <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1).</p>
<dl>
<dt><code>SAVEDBEFORE&nbsp;<wbr></code><i>date specification</i></dt>
<dd>Matches messages, which were saved before <i>date specification</i>.</dd>
<dt><code>SAVEDON&nbsp;<wbr></code><i>date specification</i></dt>
<dd>Matches messages whose save date matches the given <i>date specification</i>.</dd>
<dt><code>SAVEDSINCE&nbsp;<wbr></code><i>date specification</i></dt>
<dd>Matches messages with a save date matching or after the given <i>date specification</i>.</dd></dl>
<h2>Date Specification</h2>
<p><code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1) supports a few additional <i>date specification</i> formats. They can be used anywhere, where a <i>date specification</i> value is obligatory.</p>
<dl>
<dt><i>day</i><code>&#8211;</code><i>month</i><code>&#8211;</code><i>year</i></dt>
<dd>Default IMAP4rev1 date format.<br />
 <i>day</i>, the day of month: <code>1</code>&#8211;<code>31</code>.<br />
 <i>month</i>, the abbreviated month name: <code>Jan</code>, <code>Feb</code>, <code>Mar</code>, <code>Apr</code>, <code>May</code>, <code>Jun</code>, <code>Jul</code>, <code>Aug</code>, <code>Sep</code>, <code>Oct</code>, <code>Nov</code>&nbsp;<wbr>or <code>Dec</code>.<br />
 <i>year</i>, four digits of year, e.g. <code>2007</code>.<br />
 For example the &quot;13th of April 2007&quot; will be represented as <code>13-Apr-2007</code>.</dd>
<dt><i>interval</i></dt>
<dd>Combination of a positive integer <i>number</i> and a <i>time unit</i>.<br />
 Available <i>time units</i> are: <code>weeks</code> (abbr: <code>w</code>), <code>days</code> (abbr: <code>d</code>), <code>hours</code> (abbr: <code>h</code>), <code>mins</code> (abbr: <code>m</code>) and <code>secs</code> (abbr: <code>s</code>).<br />
 To match messages from last week, you may specify for example: <code>since 1w</code>, <code>since 1weeks</code>&nbsp;<wbr>or <code>since 7days</code>.</dd>
<dt><i>Unix timestamp</i></dt>
<dd>A 10 digit Unix timestamp, seconds since the 1st of January 1970, 00:00:00 UTC. For example the &quot;13th of April 2007&quot; will be represented as <code>1176418800</code>.</dd>
<dt><i>YYYY-MM-DD</i></dt>
<dd>Extended ISO-8601 calendar date format. For example the &quot;13th of April 2007&quot; will be represented as <code>2007-04-13</code>.</dd></dl>
<h2>Size</h2>
<p><code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1) provides also an additional <i>size</i> representation format. The following formats can be used anywhere, where a <i>size</i> value is obligatory.</p>
<dl>
<dt><i>octets</i></dt>
<dd>The message size in octets, as specified in the IMAP4rev1 specification.</dd>
<dt><i>size</i></dt>
<dd>The message size in <code>B</code>&nbsp;<wbr>(byte), <code>k</code>&nbsp;<wbr>(kilobyte), <code>M</code>&nbsp;<wbr>(megabyte), <code>G</code>&nbsp;<wbr>(gigabyte)&nbsp;<wbr>or <code>T</code>&nbsp;<wbr>(terabyte).<br />
 To match messages, bigger than 1 megabyte, you may specify for example: <code>larger 1M</code>&nbsp;<wbr>or <code>larger 1024k</code>.</dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1), <code><a href="/docs/linux/man/1-doveadm-search/">doveadm-search</a></code>(1) </p>
