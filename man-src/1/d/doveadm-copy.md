---
title: "doveadm-copy(1)"
name: "doveadm-copy"
section: "1"
letter: "d"
url: "/docs/linux/man/1-doveadm-copy/"
description: "doveadm-move – Move messages matching the given search query into another mailbox doveadm-copy – Copy messages matching the given search query into another mailbox"
---

<h2>NAME</h2>
<p> doveadm-move &#8211; Move messages matching the given search query into another mailbox<br />
 doveadm-copy &#8211; Copy messages matching the given search query into another mailbox</p>
<h2>SYNOPSIS</h2>
<p> <code>doveadm</code> [<code>-Dv</code>] <code>move</code> [<code>-S</code> <i>socket_path</i>] <i>destination</i> [<code>user</code> <i>source_user</i>] <i>search_query</i><br />
 <code>doveadm</code> [<code>-Dv</code>] <code>move</code> [<code>-S</code> <i>socket_path</i>] <code>-A</code><i> destination</i> [<code>user</code> <i>source_user</i>] <i>search_query</i><br />
 <code>doveadm</code> [<code>-Dv</code>] <code>move</code> [<code>-S</code> <i>socket_path</i>] <code>-u</code><i> user destination</i> [<code>user</code> <i>source_user</i>] <i>search_query</i> </p>
<p> <code>doveadm</code> [<code>-Dv</code>] <code>copy</code> [<code>-S</code> <i>socket_path</i>] <i>destination</i> [<code>user</code> <i>source_user</i>] <i>search_query</i><br />
 <code>doveadm</code> [<code>-Dv</code>] <code>copy</code> [<code>-S</code> <i>socket_path</i>] <code>-A</code><i> destination</i> [<code>user</code> <i>source_user</i>] <i>search_query</i><br />
 <code>doveadm</code> [<code>-Dv</code>] <code>copy</code> [<code>-S</code> <i>socket_path</i>] <code>-u</code><i> user destination</i> [<code>user</code> <i>source_user</i>] <i>search_query</i></p>
<h2>DESCRIPTION</h2>
<p> <code>doveadm move</code> can be used for moving mails between mailboxes for one or more users. The <i>search_query</i> is used to restrict which messages are moved into the <i>destination</i> mailbox.<br />
 <code>doveadm copy</code> behaves the same as <code>doveadm move</code>, except that copied messages will not be expunged after copying. </p>
<p> In the first form, <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1) will execute the <code>move</code>/<code>copy</code> action with the environment of the logged in system user. </p>
<p> In the second form, <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1) will iterate over all users, found in the configured <i>user_db</i>(s), and move or copy each user&#8217;s messages, matching the given <i>search_query</i>, into the user&#8217;s <i>destination</i> mailbox. </p>
<p> In the third form, matching mails will be moved or copied only for given <i>user</i>(s).</p>
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
<dt><i>destination</i></p>
<dd> The name of the destination mailbox, into which the mails should be moved or copied. The <i>destination</i> mailbox must exist, otherwise this command will fail.</p>
<dt><i>search_query</i></p>
<dd> Move/copy messages matching the given search query. See <code><a href="/docs/linux/man/7-doveadm-search-query/">doveadm-search-query</a></code>(7) for details.</p>
<dt><code>user</code><i>&nbsp;<wbr>source_user</i></p>
<dd> The keyword <code>user</code> followed by a valid user name. When this argument is present, <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1) will apply the <i>search_query</i> to the <i>source_user</i>&#8216;s <i>mail_location</i>.<br />
 <code>Limitation:</code> Currently the users, specified by <code>-u</code><i> user</i> and <code>user</code><i> source_user,</i> must share the same UID and GID.</dl>
<h2>EXAMPLE</h2>
<p> Move jane&#8217;s messages &#8211; received in September 2011 &#8211; from her INBOX into her archive. </p>
<pre>
<code>doveadm move -u jane Archive/2011/09 mailbox INBOX BEFORE \</code>
<code>2011-10-01 SINCE 01-Sep-2011</code>
</pre>
<h2>REPORTING BUGS</h2>
<p> Report bugs, including <i>doveconf -n</i> output, to the Dovecot Mailing List &lt;dovecot [at] dovecot.org&gt;. Information about reporting bugs is available at: <a rel="nofollow" href="http://dovecot.org/bugreport.html">http://dovecot.org/bugreport.html</a></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1), <code><a href="/docs/linux/man/7-doveadm-search-query/">doveadm-search-query</a></code>(7) </p>
<h2>Index</h2>
