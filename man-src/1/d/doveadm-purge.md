---
title: "doveadm-purge(1)"
name: "doveadm-purge"
section: "1"
letter: "d"
url: "/docs/linux/man/1-doveadm-purge/"
description: "doveadm-purge – Remove messages with refcount=0 from mdbox files"
---

<h2>NAME</h2>
<p> doveadm-purge &#8211; Remove messages with refcount=0 from mdbox files</p>
<h2>SYNOPSIS</h2>
<p> <code>doveadm</code> [<code>-Dv</code>] <code>purge</code> [<code>-S</code> <i>socket_path</i>]<br />
 <code>doveadm</code> [<code>-Dv</code>] <code>purge</code> [<code>-S</code> <i>socket_path</i>] <code>-A</code><br />
 <code>doveadm</code> [<code>-Dv</code>] <code>purge</code> [<code>-S</code> <i>socket_path</i>] <code>-u</code><i>&nbsp;<wbr>user</i></p>
<h2>DESCRIPTION</h2>
<p> The <code>doveadm purge</code> command is used to remove all messages with refcount=0 from a user&#8217;s mail storage. The refcount of a message is decreased to 0 when the user (or some administration utility) has expunged all instances of a message from all mailboxes. </p>
<p> In the first form, <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1) will perform the <code>purge</code> action for the currently logged in user. </p>
<p> In the second form, the command will be executed for all users </p>
<p> In the last form, only messages of the given <i>user</i>(s) will be purged.</p>
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
<h2>REPORTING BUGS</h2>
<p> Report bugs, including <i>doveconf -n</i> output, to the Dovecot Mailing List &lt;dovecot [at] dovecot.org&gt;. Information about reporting bugs is available at: <a rel="nofollow" href="http://dovecot.org/bugreport.html">http://dovecot.org/bugreport.html</a></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1), <code><a href="/docs/linux/man/1-doveadm-expunge/">doveadm-expunge</a></code>(1) </p>
<p> See <a rel="nofollow" href="http://wiki2.dovecot.org/MailboxFormat/dbox#Multi-dbox">http://wiki2.dovecot.org/MailboxFormat/dbox#Multi-dbox</a> for some details. </p>
<h2>Index</h2>
