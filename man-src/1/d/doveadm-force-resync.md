---
title: "doveadm-force-resync(1)"
name: "doveadm-force-resync"
section: "1"
letter: "d"
url: "/docs/linux/man/1-doveadm-force-resync/"
description: "doveadm-force-resync – Repair broken mailboxes"
---

<h2>NAME</h2>
<p> doveadm-force-resync &#8211; Repair broken mailboxes</p>
<h2>SYNOPSIS</h2>
<p> <code>doveadm</code> [<code>-Dv</code>] <code>force-resync</code> [<code>-S</code> <i>socket_path</i>] <i>mailbox</i><br />
 <code>doveadm</code> [<code>-Dv</code>] <code>force-resync</code> [<code>-S</code> <i>socket_path</i>] <code>-A</code><i>&nbsp;<wbr>mailbox</i><br />
 <code>doveadm</code> [<code>-Dv</code>] <code>force-resync</code> [<code>-S</code> <i>socket_path</i>] <code>-u</code><i> user mailbox</i></p>
<h2>DESCRIPTION</h2>
<p> Under certain circumstances it may happen, that <code><a href="/docs/linux/man/1-dovecot/">dovecot</a></code>(1) is unable to automatically solve problems with mailboxes. In such situations the <code>force-resync</code> command may be helpful. It tries to fix all problems. For sdbox and mdbox mailboxes the storage files will be also checked.</p>
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
<dt><i>mailbox</i></p>
<dd> The name of the mailbox to fix. With mdbox all of the mailboxes are fixed, so you can use for example INBOX as the name.</dl>
<h2>EXAMPLE</h2>
<p> Fix bob&#8217;s INBOX: </p>
<pre>
<code>doveadm force-resync -u bob INBOX</code>
</pre>
<h2>REPORTING BUGS</h2>
<p> Report bugs, including <i>doveconf -n</i> output, to the Dovecot Mailing List &lt;dovecot [at] dovecot.org&gt;. Information about reporting bugs is available at: <a rel="nofollow" href="http://dovecot.org/bugreport.html">http://dovecot.org/bugreport.html</a></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1) </p>
<h2>Index</h2>
