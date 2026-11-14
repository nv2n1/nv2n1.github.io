---
title: "doveadm-quota(1)"
name: "doveadm-quota"
section: "1"
letter: "d"
url: "/docs/linux/man/1-doveadm-quota/"
description: "doveadm-quota – Initialize/recalculate or show current quota usage"
---

<h2>NAME</h2>
<p> doveadm-quota &#8211; Initialize/recalculate or show current quota usage</p>
<h2>SYNOPSIS</h2>
<p> <code>doveadm</code> [<code>-Dv</code>] [<code>-f</code> <i>formatter</i>] <code>quota</code> [<code>-S</code> <i>socket_path</i>] <i>command</i><br />
 <code>doveadm</code> [<code>-Dv</code>] [<code>-f</code> <i>formatter</i>] <code>quota</code> [<code>-S</code> <i>socket_path</i>] <i>command&nbsp;<wbr></i><code>-A</code><br />
 <code>doveadm</code> [<code>-Dv</code>] [<code>-f</code> <i>formatter</i>] <code>quota</code> [<code>-S</code> <i>socket_path</i>] <i>command&nbsp;<wbr></i><code>-u</code><i>&nbsp;<wbr>user</i></p>
<h2>DESCRIPTION</h2>
<p> In the first form, <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1) will execute the <i>command</i> for the currently logged in user. </p>
<p> In the second form, the <i>command</i> will be performed for all users. </p>
<p> In the third form, the <i>command</i> will affect only the matching <i>user</i>(s).</p>
<dl>
<dt>Note:</p>
<dd> The <code>quota get</code> and <code>quota recalc</code> commands are only available when the global <i>mail_plugins</i> setting contains the <code>quota</code> plugin.</dl>
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
<h2>COMMANDS</h2>
<h3>quota get</h3>
<p> <code>doveadm</code> [<code>-f</code> <i>formatter</i>] <code>quota get</code> [<code>-A</code>|<code>-u</code> <i>user</i>] </p>
<p> The <code>quota get</code> command is used to display the current quota usage. The storage values are reported in kilobytes. </p>
<p> This command uses by default the output formatter <code>table</code>.</p>
<h3>quota recalc</h3>
<p> <code>doveadm quota recalc</code> [<code>-A</code>|<code>-u</code> <i>user</i>] </p>
<p> The <code>quota recalc</code> command is used to recalculate the current quota usage.</p>
<h2>FILES</h2>
<dl>
<dt><i>/etc/dovecot/dovecot.conf</i></p>
<dd> Dovecot&#8217;s main configuration file, including the <i>dict</i> section.</p>
<dt><i>/etc/dovecot/dovecot-dict-sql.conf.ext</i></p>
<dd> SQL dictionary proxy settings.</p>
<dt><i>/etc/dovecot/conf.d/10-mail.conf</i></p>
<dd> Mailbox locations and namespaces, including global <i>mail_location</i></p>
<dt><i>/etc/dovecot/conf.d/90-quota.conf</i></p>
<dd> Quota configuration.</dl>
<h2>EXAMPLE</h2>
<p> Get the current quota usage of user jane. </p>
<pre>
<code>doveadm quota get -u jane</code>
Quota name                        Type    Value  Limit  %
user                              STORAGE 90099 102400 87
user                              MESSAGE 20548  30000 68
</pre>
<h2>REPORTING BUGS</h2>
<p> Report bugs, including <i>doveconf -n</i> output, to the Dovecot Mailing List &lt;dovecot [at] dovecot.org&gt;. Information about reporting bugs is available at: <a rel="nofollow" href="http://dovecot.org/bugreport.html">http://dovecot.org/bugreport.html</a></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1) </p>
<h2>Index</h2>
