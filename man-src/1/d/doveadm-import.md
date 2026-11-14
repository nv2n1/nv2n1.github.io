---
title: "doveadm-import(1)"
name: "doveadm-import"
section: "1"
letter: "d"
url: "/docs/linux/man/1-doveadm-import/"
description: "doveadm-import – Import messages matching given search query"
---

<h2>NAME</h2>
<p> doveadm-import &#8211; Import messages matching given search query</p>
<h2>SYNOPSIS</h2>
<p> <code>doveadm</code> [<code>-Dv</code>] <code>import</code> [<code>-S</code> <i>socket_path</i>] [<code>-s</code>] <i>source_location dest_parent search_query</i><br />
 <code>doveadm</code> [<code>-Dv</code>] <code>import</code> [<code>-S</code> <i>socket_path</i>] [<code>-s</code>] <code>-A</code><i> source_location dest_parent search_query</i><br />
 <code>doveadm</code> [<code>-Dv</code>] <code>import</code> [<code>-S</code> <i>socket_path</i>] [<code>-s</code>] <code>-u</code><i> user source_location dest_parent search_query</i></p>
<h2>DESCRIPTION</h2>
<p> This command can be used to import mails from another mail storage specified by <i>source_location</i> to one or more user&#8217;s mailboxes. All the mailboxes are imported under the given <i>dest_parent</i> mailbox, or to root level if <i>dest_parent</i> is empty (&quot;&quot;). The <i>search_query</i> can be used to restrict which mailboxes or messages are imported. </p>
<p> In the first form, <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1) will executed the <code>import</code> action with the environment of the logged in system user. </p>
<p> In the second form, the mails will be imported for all users. </p>
<p> In the third form, the mails will be imported only for given <i>user</i>(s).</p>
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
<dt><code>-s</code></p>
<dd> When the <code>-s</code> option is present, <i>dest_parent</i> and all new mailboxes under it will be listed in the <i>subscriptions</i> file.</p>
<dt><code>-u&nbsp;<wbr></code><i>user/mask</i></p>
<dd> Run the <i>command</i> only for the given <i>user</i>. It&#8217;s also possible to use &#8216;<code>*</code>&#8216; and &#8216;<code>?</code>&#8216; wildcards (e.g. -u *@example.org).<br />
 When neither the <code>-A</code> option nor <code>-u&nbsp;<wbr></code><i>user</i> was specified, the <i>command</i> will be executed with the environment of the currently logged in user.</dl>
<h2>ARGUMENTS</h2>
<dl>
<dt><i>dest_parent</i></p>
<dd> The name of the destination mailbox, under which the mails should be imported. <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1) will create the <i>dest_parent</i> mailbox if it doesn&#8217;t exist.</p>
<dt><i>search_query</i></p>
<dd> Copy messages matching this search query. See <code><a href="/docs/linux/man/7-doveadm-search-query/">doveadm-search-query</a></code>(7) for details.</p>
<dt><i>source_location</i></p>
<dd> This argument specifies the mailbox format and location of the source location. The syntax is the same as for the <i>mail_location</i> setting. For example: <code>maildir:/backup/20101126/jane.doe/Maildir</code> or <code>mdbox:/srv/mail/john.doe/mdbox:ALT=/nfsmount/john.doe/mdbox</code></dl>
<h2>EXAMPLE</h2>
<p> This example imports all mails from a backup under a <i>backup-20101026</i> mailbox: </p>
<pre>
<code>doveadm import -u jane.doe [at] example.org \</code>
<code>mdbox:/backup/20101026/jane.doe/mdbox backup-20101026 all</code>
</pre>
<p> Another example that imports only messages from foo [at] example.org in the backup mdbox&#8217;s INBOX to jane&#8217;s INBOX: </p>
<pre><code>
doveadm import - u jane.doe[at] example.org mdbox : ~ / mdbox - backup "" mailbox INBOX from foo[at] example.org
</code></pre>
<h2>REPORTING BUGS</h2>
<p> Report bugs, including <i>doveconf -n</i> output, to the Dovecot Mailing List &lt;dovecot [at] dovecot.org&gt;. Information about reporting bugs is available at: <a rel="nofollow" href="http://dovecot.org/bugreport.html">http://dovecot.org/bugreport.html</a></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1), <code><a href="/docs/linux/man/1-doveadm-fetch/">doveadm-fetch</a></code>(1), <code><a href="/docs/linux/man/1-doveadm-search/">doveadm-search</a></code>(1), <code><a href="/docs/linux/man/7-doveadm-search-query/">doveadm-search-query</a></code>(7) </p>
<h2>Index</h2>
