---
title: "doveadm-deduplicate(1)"
name: "doveadm-deduplicate"
section: "1"
letter: "d"
url: "/docs/linux/man/1-doveadm-deduplicate/"
description: "doveadm-deduplicate – expunge duplicate messages"
---

<h2>NAME</h2>
<p> doveadm-deduplicate &#8211; expunge duplicate messages</p>
<h2>SYNOPSIS</h2>
<p> <code>doveadm</code> [<code>-Dv</code>] <code>deduplicate</code> [<code>-u</code> <i>user</i>|<code>-A</code>] [<code>-S</code> <i>socket_path</i>] [<code>-m</code>] <i>search_query</i></p>
<h2>DESCRIPTION</h2>
<p> This command is used to expunge duplicated messages in mailboxes. <code>doveadm deduplicate</code> is mainly useful to revert some (more or less) accidental duplication of messages, e.g. after <code>doveadm copy</code> or <code>doveadm import</code>. <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1) will delete the newest duplicated messages from the mailbox and keep the oldest.<br />
 Deduplication across multiple mailboxes is not supported.</p>
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
<dt><code>-m</code></p>
<dd> if the <code>-m</code> option is given, <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1) will deduplicate by Message-Id header. By default deduplication will be done by message GUIDs.</p>
<dt><code>-u&nbsp;<wbr></code><i>user/mask</i></p>
<dd> Run the <i>command</i> only for the given <i>user</i>. It&#8217;s also possible to use &#8216;<code>*</code>&#8216; and &#8216;<code>?</code>&#8216; wildcards (e.g. -u *@example.org).<br />
 When neither the <code>-A</code> option nor <code>-u&nbsp;<wbr></code><i>user</i> was specified, the <i>command</i> will be executed with the environment of the currently logged in user.</dl>
<h2>ARGUMENTS</h2>
<dl>
<dt><i>search_query</i></p>
<dd> expunge duplicates found from messages matching the given search query. Typically a search query like &#8216;<code>mailbox</code> <i>mailbox_name</i> <code>OR mailbox</code> <i>other_box</i>&#8216; will be sufficient. See <code><a href="/docs/linux/man/7-doveadm-search-query/">doveadm-search-query</a></code>(7) for details.</dl>
<h2>EXAMPLE</h2>
<p> This example shows how to list and expunge duplicate messages from a mailbox. </p>
<pre>
<code>doveadm -f table fetch -u jane 'guid uid' mailbox a_Box | sort</code>
guid                             uid
8aad0f0a30169f4bea620000ca356bad 18751
8aad0f0a30169f4bea620000ca356bad 18756
923e301ab9219b4b4f440000ca356bad 18748
923e301ab9219b4b4f440000ca356bad 18753
...
<code>doveadm deduplicate -u jane mailbox a_Box</code>
<code>doveadm -f table fetch -u jane 'guid uid' mailbox a_Box | sort</code>
guid                             uid
8aad0f0a30169f4bea620000ca356bad 18751
923e301ab9219b4b4f440000ca356bad 18748
a7999e1530739c4bd26d0000ca356bad 18749
...
</pre>
<h2>REPORTING BUGS</h2>
<p> Report bugs, including <i>doveconf -n</i> output, to the Dovecot Mailing List &lt;dovecot [at] dovecot.org&gt;. Information about reporting bugs is available at: <a rel="nofollow" href="http://dovecot.org/bugreport.html">http://dovecot.org/bugreport.html</a></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1), <code><a href="/docs/linux/man/1-doveadm-copy/">doveadm-copy</a></code>(1), <code><a href="/docs/linux/man/1-doveadm-fetch/">doveadm-fetch</a></code>(1), <code><a href="/docs/linux/man/1-doveadm-import/">doveadm-import</a></code>(1), <code><a href="/docs/linux/man/7-doveadm-search-query/">doveadm-search-query</a></code>(7) </p>
<h2>Index</h2>
