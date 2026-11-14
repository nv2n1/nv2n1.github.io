---
title: "doveadm-flags(1)"
name: "doveadm-flags"
section: "1"
letter: "d"
url: "/docs/linux/man/1-doveadm-flags/"
description: "doveadm-flags – add, remove or replace messages’ flags"
---

<h2>NAME</h2>
<p> doveadm-flags &#8211; add, remove or replace messages&#8217; flags</p>
<h2>SYNOPSIS</h2>
<p> <code>doveadm</code> [<code>-Dv</code>] <code>flags</code> [<code>-S</code> <i>socket_path</i>] <i>command flags search_query</i><br />
 <code>doveadm</code> [<code>-Dv</code>] <code>flags</code> [<code>-S</code> <i>socket_path</i>] <i>command flags search_query</i> <code>-A</code><br />
 <code>doveadm</code> [<code>-Dv</code>] <code>flags</code> [<code>-S</code> <i>socket_path</i>] <i>command flags search_query</i> <code>-u </code><i>user</i></p>
<h2>DESCRIPTION</h2>
<p> This command is used to manipulate flags of messages.</p>
<h2>OPTIONS</h2>
<p> Global <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1) <i>options</i>:</p>
<dl>
<dt><code>-D</code></p>
<dd> Enables verbosity and debug messages.</p>
<dt><code>-v</code></p>
<dd> Enables verbosity, including progress counter.</dl>
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
<dt><i>flags</i></p>
<dd> Message flags as described in RFC 3501, section 2.3.2 (Flags Message Attribute): <code>\Answered</code>, <code>\Deleted</code>, <code>\Draft</code>, <code>\Flagged</code>, <code>\Recent</code> and <code>\Seen</code>. And the IMAP keywords <code>$Forwarded</code>, <code>$MDNSent</code>, <code>$SubmitPending</code> and <code>$Submitted</code> or user-defined keywords, e.g. Junk, $NonSpam or $Label1.<br />
 One or multiple flags and/or keywords can be specified.</p>
<dt><i>search_query</i></p>
<dd> Manipulate the flags of messages matching the given search query. See <code><a href="/docs/linux/man/7-doveadm-search-query/">doveadm-search-query</a></code>(7) for details.</dl>
<h2>COMMANDS</h2>
<h3>flags add</h3>
<p> <code>doveadm flags add</code> [<code>-u</code> <i>user</i>|<code>-A</code>] [<code>-S</code> <i>socket_path</i>] <i>flags search_query</i> </p>
<p> This command is used to extend the current set of flags with the given <i>flags</i>.</p>
<h3>flags remove</h3>
<p> <code>doveadm flags remove</code> [<code>-u</code> <i>user</i>|<code>-A</code>] [<code>-S</code> <i>socket_path</i>] <i>flags search_query</i> </p>
<p> In order to remove the given <i>flags</i> from the current set of flags, use this command.</p>
<h3>flags replace</h3>
<p> <code>doveadm flags replace</code> [<code>-u</code> <i>user</i>|<code>-A</code>] [<code>-S</code> <i>socket_path</i>] <i>flags search_query</i> </p>
<p> This command is used to replace ALL current flags with the given <i>flags</i>.</p>
<h2>EXAMPLE</h2>
<p> List and manipulate the message flags of the message with uid 81563 </p>
<pre>
<code>doveadm fetch -u bob 'uid flags' mailbox dovecot uid 81563</code>
uid: 81563
flags: \Answered \Seen NonJunk
<code>doveadm flags -u bob remove NonJunk mailbox dovecot uid 81563</code>
<code>doveadm flags -u bob add '\Flagged $Forwarded' mailbox dovecot uid 81563</code>
</pre>
<h2>REPORTING BUGS</h2>
<p> Report bugs, including <i>doveconf -n</i> output, to the Dovecot Mailing List &lt;dovecot [at] dovecot.org&gt;. Information about reporting bugs is available at: <a rel="nofollow" href="http://dovecot.org/bugreport.html">http://dovecot.org/bugreport.html</a></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1), <code><a href="/docs/linux/man/1-doveadm-fetch/">doveadm-fetch</a></code>(1), <code><a href="/docs/linux/man/7-doveadm-search-query/">doveadm-search-query</a></code>(7) </p>
<h2>Index</h2>
