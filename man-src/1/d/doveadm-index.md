---
title: "doveadm-index(1)"
name: "doveadm-index"
section: "1"
letter: "d"
url: "/docs/linux/man/1-doveadm-index/"
description: "doveadm-index – Index mailboxes"
---

<h2>NAME</h2>
<p> doveadm-index &#8211; Index mailboxes</p>
<h2>SYNOPSIS</h2>
<p> <code>doveadm</code> [<code>-Dv</code>] <code>index</code> [<code>-S</code> <i>socket_path</i>] [<code>-q</code>] [<code>-n</code> <i>max_recent</i>] <i>mailbox</i><br />
 <code>doveadm</code> [<code>-Dv</code>] <code>index</code> [<code>-S</code> <i>socket_path</i>] <code>-A</code> [<code>-q</code>] [<code>-n</code> <i>max_recent</i>] <i>mailbox</i><br />
 <code>doveadm</code> [<code>-Dv</code>] <code>index</code> [<code>-S</code> <i>socket_path</i>] <code>-u</code><i>&nbsp;<wbr>user</i> [<code>-q</code>] [<code>-n</code> <i>max_recent</i>] <i>mailbox</i></p>
<h2>DESCRIPTION</h2>
<p> Add unindexed messages in a mailbox into index/cache file. If full text search is enabled, also add unindexed messages to the fts database. </p>
<p> The caching adds only the fields that were previously added to the mailbox&#8217;s caching decisions, so it won&#8217;t do anything useful for mailboxes that user&#8217;s client hasn&#8217;t accessed yet. You can use <code>doveadm dump</code> command to show a specific mailbox&#8217;s current caching decisions. </p>
<p> Messages can also be added automatically to full text search index using: </p>
<pre>
plugin {
  ...
  fts_autoindex = yes
}
</pre>
<p> in <i>/etc/dovecot/conf.d/90-plugin.conf</i>.</p>
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
<dt><code>-n</code><i>&nbsp;<wbr>max_recent</i></p>
<dd> An integer value, which specifies the maximum number of \Recent messages in mailboxes. If the mailbox contains more than <i>max_recent</i> messages with \Recent flag set, the mailbox will not be indexed. This may be useful to avoid unnecessary indexing for large mailboxes that are never opened.</p>
<dt><code>-q</code></p>
<dd> Queues the indexing to be run by indexer process. Without -q the indexing is done directly by the <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1) process. Some backends like fts-lucene can&#8217;t handle multiple processes updating the indexes simultaneously, so -q should usually be used on production.</p>
<dt><code>-S&nbsp;<wbr></code><i>socket_path</i></p>
<dd> The option&#8217;s argument is either an absolute path to a local UNIX domain socket, or a hostname and port (<i>hostname</i>:<i>port</i>), in order to connect a remote host via a TCP socket. </p>
<p> This allows an administrator to execute <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1) mail commands through the given socket.</p>
<dt><code>-u&nbsp;<wbr></code><i>user/mask</i></p>
<dd> Run the <i>command</i> only for the given <i>user</i>. It&#8217;s also possible to use &#8216;<code>*</code>&#8216; and &#8216;<code>?</code>&#8216; wildcards (e.g. -u *@example.org).<br />
 When neither the <code>-A</code> option nor <code>-u&nbsp;<wbr></code><i>user</i> was specified, the <i>command</i> will be executed with the environment of the currently logged in user.</dl>
<h2>ARGUMENTS</h2>
<dl>
<dt><i>mailbox</i></p>
<dd> The name of the mailbox to index.</dl>
<h2>EXAMPLE</h2>
<p> Index bob&#8217;s INBOX: </p>
<pre>
<code>doveadm index -u bob INBOX</code>
</pre>
<h2>REPORTING BUGS</h2>
<p> Report bugs, including <i>doveconf -n</i> output, to the Dovecot Mailing List &lt;dovecot [at] dovecot.org&gt;. Information about reporting bugs is available at: <a rel="nofollow" href="http://dovecot.org/bugreport.html">http://dovecot.org/bugreport.html</a></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1) </p>
<h2>Index</h2>
