---
title: "doveadm-mailbox(1)"
name: "doveadm-mailbox"
section: "1"
letter: "d"
url: "/docs/linux/man/1-doveadm-mailbox/"
description: "doveadm-mailbox – Commands related to handling mailboxes"
---

<h2>NAME</h2>
<p> doveadm-mailbox &#8211; Commands related to handling mailboxes</p>
<h2>SYNOPSIS</h2>
<p> <code>doveadm</code> [<code>-Dv</code>] [<code>-f</code> <i>formatter</i>] <i>mailbox_cmd</i> [<i>options</i>] [<i>arguments</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>doveadm mailbox</code> can be used to query and modify mailboxes.</p>
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
<dd> Is the name of a <i>mailbox</i>, as visible to IMAP clients, except in UTF-8 format. The hierarchy separator between a parent and child mailbox is commonly &#8216;<code>/</code>&#8216; or &#8216;<code>.</code>&#8216;, but this depends on your selected mailbox storage format and namespace configuration. The mailbox names may also require a namespace prefix.</dl>
<h2>COMMANDS</h2>
<h3>mailbox create</h3>
<p> <code>doveadm mailbox create</code> [<code>-A</code>|<code>-u</code> <i>user</i>] [<code>-S</code> <i>socket_path</i>] [<code>-g</code> <i>guid</i>] [<code>-s</code>] <i>mailbox&nbsp;<wbr></i>&#8230; </p>
<p> This command is used to create one or more mailboxes. The mailbox format of the created mailboxes depends on the <i>mail_location</i> setting, or the user&#8217;s <i>mail</i> field, returned by the userdb. </p>
<dl>
<dt><code>-g</code><i>&nbsp;<wbr>guid</i></p>
<dd> Create the mailbox with the specified GUID.</p>
<dt><code>-s</code></p>
<dd> When this option was given, the created mailboxes will be also added to the user&#8217;s subscriptions.</dl>
<h3>mailbox delete</h3>
<p> <code>doveadm mailbox delete</code> [<code>-A</code>|<code>-u</code> <i>user</i>] [<code>-S</code> <i>socket_path</i>] [<code>-s</code>] <i>mailbox&nbsp;<wbr></i>&#8230; </p>
<p> This command deletes a mailbox and expunges all the messages it contains. If the mailbox has any children, they won&#8217;t be deleted.<br />
 When the <code>-s</code> option is present, the deleted mailboxes will be also unsubscribed.</p>
<h3>mailbox list</h3>
<p> <code>doveadm mailbox list</code> [<code>-7</code>|<code>-8</code>] [<code>-A</code>|<code>-u</code> <i>user</i>] [<code>-S</code> <i>socket_path</i>] [<code>-s</code>] [<i>mailbox</i> &#8230;] </p>
<p> To get an overview of existing mailboxes use this command. It&#8217;s also possible to use wildcards in the <i>mailbox</i> name.<br />
 When the <code>-s</code> option is present, only subscribed mailboxes will be listed. Listed subscriptions may also contain mailboxes that are already deleted. </p>
<dl>
<dt><code>-7</code></p>
<dd> Lists the mailboxes with mUTF-7 encoding.</p>
<dt><code>-8</code></p>
<dd> Lists the mailboxes with UTF-8 encoding.</dl>
<h3>mailbox mutf7</h3>
<p> <code>doveadm mailbox mutf7</code> [<code>-7</code>|<code>-8</code>] <i>name&nbsp;<wbr></i>&#8230; </p>
<p> The <code>mailbox mutf7</code> command may be used to convert the international mailbox <i>name</i> into a modified version of the UTF-7 encoding and vice versa. See RFC 3501, section 5.1.3 (Mailbox International Naming Convention). </p>
<dl>
<dt><code>-7</code></p>
<dd> Indicates that the <i>name</i>&#8216;s string representation is mUTF-7 encoded and it should be converted to UTF-8.</p>
<dt><code>-8</code></p>
<dd> Indicates that the <i>name</i>&#8216;s is UTF-8 encoded and should be converted to mUTF-7 (default).</p>
<dt><i>name</i></p>
<dd> One or more mailbox names that should be converted.</dl>
<h3>mailbox rename</h3>
<p> <code>doveadm mailbox rename</code> [<code>-A</code>|<code>-u</code> <i>user</i>] [<code>-S</code> <i>socket_path</i>] [<code>-s</code>] <i>old_name</i> <i>new_name</i> </p>
<p> The <code>mailbox rename</code> command is used to rename the mailbox <i>old_name</i> to <i>new_name</i>.<br />
 When the <code>-s</code> option is given, <i>old_name</i> will be unsubscribed and <i>new_name</i> will be subscribed.</p>
<h3>mailbox status</h3>
<p> <code>doveadm</code> [<code>-f</code> <i>formatter</i>] <code>mailbox status</code> [<code>-A</code>|<code>-u</code> <i>user</i>] [<code>-S</code> <i>socket_path</i>] [<code>-t</code>] <i>fields mailbox&nbsp;<wbr></i>&#8230; </p>
<p> Show the <code>status</code> of one or more mailboxes. The <i>mailbox</i> name may also contain wildcards.<br />
 This command uses by default the output <i>formatter</i> <code>flow</code>.</p>
<dl>
<dt><code>-t</code></p>
<dd> Summarize the values of the status <i>fields</i> <code>messages</code>, <code>recent</code>, <code>unseen</code> and/or <code>vsize</code> of multiple mailboxes to a sum (total).</p>
<dt><i>fields</i></p>
<dd> Specify the status <i>fields</i> which should be shown. In order to specify multiple status <i>fields</i>, enclosed them in quotes.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>all</code></p>
<dd> This is a special status field name. It means show all of the following <i>fields</i>. When the <code>-t</code> option is present, it means show only the <code>messages</code>, <code>recent</code>, <code>unseen</code> and <code>vsize</code> <i>fields</i>.</p>
<dt><code>guid</code></p>
<dd> The <i>mailbox</i>&#8216;s globally unique identifier.</p>
<dt><code>highestmodseq</code></p>
<dd> The highest mod-sequence value of all messages in the <i>mailbox</i>.</p>
<dt><code>messages</code></p>
<dd> The number of messages in the <i>mailbox</i>.</p>
<dt><code>recent</code></p>
<dd> The number of messages with the \Recent flag set.</p>
<dt><code>uidnext</code></p>
<dd> The next unique identifier value.</p>
<dt><code>uidvalidity</code></p>
<dd> The unique identifier validity value.</p>
<dt><code>unseen</code></p>
<dd> The message sequence number of the first unseen message in the <i>mailbox</i>.</p>
<dt><code>vsize</code></p>
<dd> The <i>mailbox</i>&#8216;s virtual size, computed with CRLF line terminators.</dl>
</dl>
</dl>
<h3>mailbox subscribe</h3>
<p> <code>doveadm mailbox subscribe</code> [<code>-A</code>|<code>-u</code> <i>user</i>] [<code>-S</code> <i>socket_path</i>] <i>mailbox&nbsp;<wbr></i>&#8230; </p>
<p> This command is used to subscribe one or more mailboxes.</p>
<h3>mailbox unsubscribe</h3>
<p> <code>doveadm mailbox unsubscribe</code> [<code>-A</code>|<code>-u</code> <i>user</i>] [<code>-S</code> <i>socket_path</i>] <i>mailbox&nbsp;<wbr></i>&#8230; </p>
<p> This command is used to unsubscribe one or more mailboxes.</p>
<h2>EXAMPLE</h2>
<p> List subscribed mailboxes, beginning with &#8216;dovecot&#8217;, of user bob. </p>
<pre>
<code>doveadm mailbox list -s -u bob dovecot*</code>
dovecot
dovecot/pigeonhole
dovecot/pigeonhole/2.0
</pre>
<p> Now have a look at the status of user bob&#8217;s dovecot mailboxes. </p>
<pre>
<code>doveadm -f table mailbox status -u bob &quot;messages vsize&quot; dovecot*</code>
mailbox                                    messages vsize
dovecot                                    20501    93968492
dovecot/pigeonhole                         0        0
dovecot/pigeonhole/2.0                     47       323474
</pre>
<p> Converting an internationalized mailbox name from mUTF-7 to UTF-8 and vice versa. </p>
<pre>
<code>doveadm mailbox mutf7 -7 &quot;~peter/mail/&amp;U,BTFw-/&amp;ZeVnLIqe-&quot;</code>
~peter/mail/台北/日本語
<code>doveadm mailbox mutf7 ~peter/mail/台北/日本語</code>
~peter/mail/&amp;U,BTFw-/&amp;ZeVnLIqe-
</pre>
<h2>REPORTING BUGS</h2>
<p> Report bugs, including <i>doveconf -n</i> output, to the Dovecot Mailing List &lt;dovecot [at] dovecot.org&gt;. Information about reporting bugs is available at: <a rel="nofollow" href="http://dovecot.org/bugreport.html">http://dovecot.org/bugreport.html</a></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1) </p>
<h2>Index</h2>
