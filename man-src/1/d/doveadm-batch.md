---
title: "doveadm-batch(1)"
name: "doveadm-batch"
section: "1"
letter: "d"
url: "/docs/linux/man/1-doveadm-batch/"
description: "doveadm-batch – Execute multiple commands for multiple users"
---

<h2>NAME</h2>
<p> doveadm-batch &#8211; Execute multiple commands for multiple users</p>
<h2>SYNOPSIS</h2>
<p> <code>doveadm</code> [<code>-Dv</code>] <code>batch</code> [<code>-S</code> <i>socket_path</i>] <code>-A</code><i> sep command sep command</i> [&#8230;]<br />
 <code>doveadm</code> [<code>-Dv</code>] <code>batch</code> [<code>-S</code> <i>socket_path</i>] <code>-u</code><i> usermask sep command sep command</i> [&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> The command <code>doveadm batch</code> is used to execute multiple <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1) <i>command</i>s sequentially for multiple users. This is primarily an optimization where Dovecot can do all the mailbox operations for the same user at once, instead of having to go through the users multiple times. </p>
<p> In the first form <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1) will loop over all users, defined in the configured <i>user_db</i>(s), and execute the sequence of <i>command</i>s for each of them. </p>
<p> In the second form the <i>command</i>s will be executed for each user matching the given <i>usermask</i>.</p>
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
<dt><i>command</i></p>
<dd> Any <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1) command, with arguments and options &#8212; except for the <code>-A</code>, <code>-S</code> and <code>-u</code> options.</p>
<dt><i>sep</i></p>
<dd> A single character used as command separator, e.g. &#8216;:&#8217;. Be careful, unquoted characters, like <code>;</code> or <code>&amp;</code>, may be interpreted by your shell and <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1) will never see them.</dl>
<h2>EXAMPLE</h2>
<p> In this example we move seen mails, older than one month, for all example.net users to the alternative storage under /nfsmount: </p>
<pre>
mail_location = mdbox:~/mdbox:ALT=/nfsmount/%h/mdbox
</pre>
<p> The second command will remove messages with refcount=0 from the primary storage. </p>
<pre>
<code>doveadm batch -u \*@example.net : altmove seen savedbefore 30d : purge</code>
</pre>
<h2>REPORTING BUGS</h2>
<p> Report bugs, including <i>doveconf -n</i> output, to the Dovecot Mailing List &lt;dovecot [at] dovecot.org&gt;. Information about reporting bugs is available at: <a rel="nofollow" href="http://dovecot.org/bugreport.html">http://dovecot.org/bugreport.html</a></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1) </p>
<h2>Index</h2>
