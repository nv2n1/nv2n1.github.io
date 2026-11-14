---
title: "doveadm-search(1)"
name: "doveadm-search"
section: "1"
letter: "d"
url: "/docs/linux/man/1-doveadm-search/"
description: "doveadm-search – Show a list of mailbox GUIDs and message UIDs matching given search query."
---

<h2>NAME</h2>
<p> doveadm-search &#8211; Show a list of mailbox GUIDs and message UIDs matching given search query.</p>
<h2>SYNOPSIS</h2>
<p> <code>doveadm</code> [<code>-Dv</code>] [<code>-f</code> <i>formatter</i>] <code>search</code> [<code>-S</code> <i>socket_path</i>] <i>search_query</i><br />
 <code>doveadm</code> [<code>-Dv</code>] [<code>-f</code> <i>formatter</i>] <code>search</code> [<code>-S</code> <i>socket_path</i>] <code>-A</code><i>&nbsp;<wbr>search_query</i><br />
 <code>doveadm</code> [<code>-Dv</code>] [<code>-f</code> <i>formatter</i>] <code>search</code> [<code>-S</code> <i>socket_path</i>] <code>-u</code><i> user search_query</i></p>
<h2>DESCRIPTION</h2>
<p> The <code>search</code> command is used to find matching messages. <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1) will print the mailbox&#8217;s guid and the message&#8217;s uid for each match.<br />
 When used with the <code>-A</code> or <code>-u</code><i>&nbsp;<wbr>wildcard</i> options, <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1) will print the fields <code>username</code>, <code>mailbox-guid</code>&nbsp;<wbr>and <code>uid</code> for each matching message. </p>
<p> In the first form, <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1) will executed the <code>search</code> action with the environment of the logged in system user. </p>
<p> In the second form, the command will be performed for all users. </p>
<p> In the third form, only matching mails of the given <i>user</i>(s) will be searched.</p>
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
<p> This command uses by default the output formatter <code>flow</code> (without the <i>key</i>= prefix). </p>
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
<dt><i>search_query</i></p>
<dd> Show messages matching this search query. See <code><a href="/docs/linux/man/7-doveadm-search-query/">doveadm-search-query</a></code>(7) for details.</dl>
<h2>EXAMPLE</h2>
<p> This example demonstrates how to search in user bob&#8217;s dovecot mailboxes all messages, which contains the word &quot;todo&quot; in the Subject: header. </p>
<pre>
<code>doveadm search -u bob mailbox dovecot\* subject todo</code>
3a94c928d66ebe4bda04000015811c6a        8
3a94c928d66ebe4bda04000015811c6a        25
3a94c928d66ebe4bda04000015811c6a        45
</pre>
<p> The search command is mainly useful when used together with <i>doveadm fetch</i> command. For example to save message bodies of all messages from INBOX that have &quot;todo&quot; in subject, use: </p>
<pre><code>
doveadm search - u bob mailbox INBOX subject todo |
    while read guid uid;
do
    &amp;nbsp;
&amp;nbsp;
doveadm fetch - u bob body mailbox - guid $guid uid $uid &gt; msg.$uid
                                                               done
</code></pre>
<h2>REPORTING BUGS</h2>
<p> Report bugs, including <i>doveconf -n</i> output, to the Dovecot Mailing List &lt;dovecot [at] dovecot.org&gt;. Information about reporting bugs is available at: <a rel="nofollow" href="http://dovecot.org/bugreport.html">http://dovecot.org/bugreport.html</a></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1), <code><a href="/docs/linux/man/1-doveadm-fetch/">doveadm-fetch</a></code>(1), <code><a href="/docs/linux/man/7-doveadm-search-query/">doveadm-search-query</a></code>(7) </p>
<h2>Index</h2>
