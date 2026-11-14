---
title: "doveadm-altmove(1)"
name: "doveadm-altmove"
section: "1"
letter: "d"
url: "/docs/linux/man/1-doveadm-altmove/"
description: "doveadm-altmove – Move matching mails to the alternative storage (dbox-only)"
---

<h2>NAME</h2>
<p> doveadm-altmove &#8211; Move matching mails to the alternative storage (dbox-only)</p>
<h2>SYNOPSIS</h2>
<p> <code>doveadm</code> [<code>-Dv</code>] <code>altmove</code> [<code>-r</code>] [-S <i>socket_path</i>] <i>search_query</i><br />
 <code>doveadm</code> [<code>-Dv</code>] <code>altmove</code> [<code>-r</code>] [-S <i>socket_path</i>] <code>-A</code><i> search_query</i><br />
 <code>doveadm</code> [<code>-Dv</code>] <code>altmove</code> [<code>-r</code>] [-S <i>socket_path</i>] <code>-u</code><i> user search_query</i></p>
<h2>DESCRIPTION</h2>
<p> This command can be used with sdbox or mdbox storage to move mails to alternative storage path when :ALT=&lt;path&gt; is specified for the mail location. </p>
<p> In the first form, <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1) will executed the <code>altmove</code> action with the environment of the logged in system user. </p>
<p> In the second form, the command will be performed for all users. </p>
<p> In the third form, only matching mails of the given <i>user</i>(s) will be moved to the alternative storage.</p>
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
<dt><code>-r</code></p>
<dd> When the <code>-r</code> option is given this <i>command</i> works the other way round. Mails will be moved from the alternative storage back to the default mail location.</p>
<dt><code>-S&nbsp;<wbr></code><i>socket_path</i></p>
<dd> The option&#8217;s argument is either an absolute path to a local UNIX domain socket, or a hostname and port (<i>hostname</i>:<i>port</i>), in order to connect a remote host via a TCP socket. </p>
<p> This allows an administrator to execute <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1) mail commands through the given socket.</p>
<dt><code>-u&nbsp;<wbr></code><i>user/mask</i></p>
<dd> Run the <i>command</i> only for the given <i>user</i>. It&#8217;s also possible to use &#8216;<code>*</code>&#8216; and &#8216;<code>?</code>&#8216; wildcards (e.g. -u *@example.org).<br />
 When neither the <code>-A</code> option nor <code>-u&nbsp;<wbr></code><i>user</i> was specified, the <i>command</i> will be executed with the environment of the currently logged in user.</dl>
<h2>ARGUMENTS</h2>
<dl>
<dt><i>search_query</i></p>
<dd> Messages matching this search query will be moved to alt storage. See <code><a href="/docs/linux/man/7-doveadm-search-query/">doveadm-search-query</a></code>(7) for details.</dl>
<h2>FILES</h2>
<dl>
<dt><i>/etc/dovecot/conf.d/10-mail.conf</i></p>
<dd> Mailbox locations and namespaces.</p>
<dt><i>/etc/dovecot/conf.d/auth-*.conf.ext</i></p>
<dd> Authentication processes, including userdb settings.</dl>
<h2>EXAMPLE</h2>
<p> This example moves seen mails older than one week to alternative storage under /nfsmount: </p>
<pre>
mail_location = mdbox:~/mdbox:ALT=/nfsmount/%h/mdbox
</pre>
<pre>
<code>doveadm altmove -u johnd [at] example.com seen savedbefore 1w</code>
</pre>
<h2>REPORTING BUGS</h2>
<p> Report bugs, including <i>doveconf -n</i> output, to the Dovecot Mailing List &lt;dovecot [at] dovecot.org&gt;. Information about reporting bugs is available at: <a rel="nofollow" href="http://dovecot.org/bugreport.html">http://dovecot.org/bugreport.html</a></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1), <code><a href="/docs/linux/man/7-doveadm-search-query/">doveadm-search-query</a></code>(7) </p>
<h2>Index</h2>
