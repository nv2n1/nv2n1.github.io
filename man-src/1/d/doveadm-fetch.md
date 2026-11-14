---
title: "doveadm-fetch(1)"
name: "doveadm-fetch"
section: "1"
letter: "d"
url: "/docs/linux/man/1-doveadm-fetch/"
description: "doveadm-fetch – Fetch partial/full messages or message information"
---

<h2>NAME</h2>
<p> doveadm-fetch &#8211; Fetch partial/full messages or message information</p>
<h2>SYNOPSIS</h2>
<p> <code>doveadm</code> [<code>-Dv</code>] [<code>-f</code> <i>formatter</i>] <code>fetch</code> [<code>-S</code> <i>socket_path</i>] <i>fields search_query</i><br />
 <code>doveadm</code> [<code>-Dv</code>] [<code>-f</code> <i>formatter</i>] <code>fetch</code> [<code>-S</code> <i>socket_path</i>] <code>-A</code><i> fields search_query</i><br />
 <code>doveadm</code> [<code>-Dv</code>] [<code>-f</code> <i>formatter</i>] <code>fetch</code> [<code>-S</code> <i>socket_path</i>] <code>-u</code><i> user fields search_query</i></p>
<h2>DESCRIPTION</h2>
<p> <code>doveadm fetch</code> can be used to fetch messages&#8217; contents and metadata. This can be useful for scripts and for debugging. If you want to fetch messages one at a time, see <code><a href="/docs/linux/man/1-doveadm-search/">doveadm-search</a></code>(1).</p>
<dl>
<dt>Important:</p>
<dd> Please respect your users&#8217; privacy.</dl>
<h2>OPTIONS</h2>
<p> Global <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1) <i>options</i>:</p>
<dl>
<dt><code>-D</code></p>
<dd> Enables verbosity and debug messages.</p>
<dt><code>-f&nbsp;<wbr></code><i>formatter</i></p>
<dd> Specifies the <i>formatter</i> for formatting the output. Supported formatters are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>flow</code></p>
<dd> prints each line with <i>key</i><code>=</code><i>value</i> pairs.</p>
<dt><code>pager</code></p>
<dd> prints each <i>key</i>:&nbsp;<wbr><i>value</i> pair on its own line and separates records with form feed character (<code>^L</code>).</p>
<dt><code>tab</code></p>
<dd> prints a table header followed by tab separated value lines.</p>
<dt><code>table</code></p>
<dd> prints a table header followed by adjusted value lines.</dl>
</dl>
<dt><code>-v</code></p>
<dd> Enables verbosity, including progress counter.</dl>
<p> This command uses by default the output formatter <code>pager</code>. </p>
<p> Command specific <i>options</i>:</p>
<dl>
<dt><code>-A</code></p>
<dd> If the <code>-A</code> option is present, the <i>command</i> will be performed for all users. Using this option in combination with system users from <code>userdb { driver = passwd }</code> is not recommended, because it contains also users with a lower UID than the one configured with the <i>first_valid_uid</i> setting. </p>
<p> When the SQL userdb module is used make sure that the <i>iterate_query</i> setting in <i>/etc/dovecot/dovecot-sql.conf.ext</i> matches your database layout. When using the LDAP userdb module, make sure that the <i>iterate_attrs</i> and <i>iterate_filter</i> settings in <i>/etc/dovecot/dovecot-ldap.conf.ext</i> match your LDAP schema. Otherwise <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1) will be unable to iterate over all users.</p>
<dt><code>-S&nbsp;<wbr></code><i>socket_path</i></p>
<dd> The option&#8217;s argument is either an absolute path to a local UNIX domain socket, or a hostname and port (<i>hostname</i>:<i>port</i>), in order to connect a remote host via a TCP socket. </p>
<p> This allows an administrator to execute <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1) mail commands through the given socket.</p>
<dt><code>-u&nbsp;<wbr></code><i>user/mask</i></p>
<dd> Run the <i>command</i> only for the given <i>user</i>. It&#8217;s also possible to use &#8216;<code>*</code>&#8216; and &#8216;<code>?</code>&#8216; wildcards (e.g. -u *@example.org).<br />
 When neither the <code>-A</code> option nor <code>-u&nbsp;<wbr></code><i>user</i> was specified, the <i>command</i> will be executed with the environment of the currently logged in user.</dl>
<h2>ARGUMENTS</h2>
<dl>
<dt><i>fields</i></p>
<dd> One or more result field names to display, if the <i>search_query</i> matches any messages. In order to specify multiple fields, enclose them in single or double quotes.<br />
 Supported <i>fields</i> are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>body</code></p>
<dd> The body of a message.</p>
<dt><code>date.received</code></p>
<dd> Date and time of final delivery, when the message was delivered to a user&#8217;s mailbox for the first time.<br />
 The internal date and time of the source message, when the message was copied by the IMAP COPY command.<br />
 The date-time attribute when present, otherwise the current time, when the message was saved by the IMAP APPEND command.</p>
<dt><code>date.saved</code></p>
<dd> Date and time when the message was saved to mailbox.</p>
<dt><code>date.sent</code></p>
<dd> Date and time of the message&#8217;s Date: header.</p>
<dt><code>flags</code></p>
<dd> A message&#8217;s IMAP flags, e.g. \Seen</p>
<dt><code>guid</code></p>
<dd> A message&#8217;s globally unique identifier.</p>
<dt><code>hdr</code></p>
<dd> The header of the message.</p>
<dt><code>imap.body</code></p>
<dd> IMAP BODY output of the message (see RFC 3501).</p>
<dt><code>imap.bodystructure</code></p>
<dd> IMAP BODYSTRUCTURE output of the message (see RFC 3501).</p>
<dt><code>imap.envelope</code></p>
<dd> IMAP ENVELOPE output of the message (see RFC 3501).</p>
<dt><code>mailbox</code></p>
<dd> Name of the mailbox, in which the message is stored. The name is in UTF-8.</p>
<dt><code>mailbox-guid</code></p>
<dd> The globally unique identifier of the mailbox, in which the message is located.</p>
<dt><code>pop3.uidl</code></p>
<dd> A message&#8217;s unique (POP3) identifier within a mailbox.</p>
<dt><code>seq</code></p>
<dd> A message&#8217;s sequence number in a mailbox.</p>
<dt><code>size.physical</code></p>
<dd> A message&#8217;s physical size.</p>
<dt><code>size.virtual</code></p>
<dd> A message&#8217;s virtual size, computed with CRLF line terminators.</p>
<dt><code>text</code></p>
<dd> The entire message (header and body).</p>
<dt><code>text.utf8</code></p>
<dd> The entire message (header and body) &#8212; UTF-8 encoded.</p>
<dt><code>uid</code></p>
<dd> A message&#8217;s unique (IMAP) identifier in a mailbox.</p>
<dt><code>user</code></p>
<dd> A message owner&#8217;s login name.</dl>
</dl>
<dt><i>search_query</i></p>
<dd> Fetch messages matching this search query. See <code><a href="/docs/linux/man/7-doveadm-search-query/">doveadm-search-query</a></code>(7) for details.</dl>
<h2>EXAMPLE</h2>
<p> This example based on the first example from <code><a href="/docs/linux/man/1-doveadm-search/">doveadm-search</a></code>(1). We are fetching the fields <code>mailbox&nbsp;<wbr></code>and&nbsp;<wbr><code>date.sent</code> from user bob&#8217;s mailbox with the guid &quot;3a94c928d66ebe4bda04000015811c6a&quot; for the messages with the UIDs <code>8</code>,&nbsp;<wbr><code>25</code>&nbsp;<wbr>and<code>&nbsp;<wbr>45</code>. </p>
<pre>
<code>doveadm fetch -u bob &quot;mailbox date.sent&quot; \</code>
<code>mailbox-guid 3a94c928d66ebe4bda04000015811c6a uid 8,25,45</code>
mailbox: dovecot/pigeonhole/2.0
date.sent: 2010-01-19 01:17:41 (+0100)
^L
mailbox: dovecot/pigeonhole/2.0
date.sent: 2010-01-28 09:38:49 (+0100)
^L
mailbox: dovecot/pigeonhole/2.0
date.sent: 2010-03-28 18:41:14 (+0200)
^L
</pre>
<h2>REPORTING BUGS</h2>
<p> Report bugs, including <i>doveconf -n</i> output, to the Dovecot Mailing List &lt;dovecot [at] dovecot.org&gt;. Information about reporting bugs is available at: <a rel="nofollow" href="http://dovecot.org/bugreport.html">http://dovecot.org/bugreport.html</a></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1), <code><a href="/docs/linux/man/1-doveadm-search/">doveadm-search</a></code>(1), <code><a href="/docs/linux/man/7-doveadm-search-query/">doveadm-search-query</a></code>(7) </p>
<h2>Index</h2>
