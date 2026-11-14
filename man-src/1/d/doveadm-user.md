---
title: "doveadm-user(1)"
name: "doveadm-user"
section: "1"
letter: "d"
url: "/docs/linux/man/1-doveadm-user/"
description: "doveadm-user – Perform a user lookup in Dovecot’s userdbs"
---

<h2>NAME</h2>
<p> doveadm-user &#8211; Perform a user lookup in Dovecot&#8217;s userdbs</p>
<h2>SYNOPSIS</h2>
<p> <code>doveadm</code> [<code>-Dv</code>] <code>user</code> [<code>-a</code> <i>userdb_socket_path</i>] [<code>-f</code> <i>field</i>] [<code>-u</code>] [<code>-x</code> <i>auth_info</i>] <i>user&nbsp;<wbr></i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> The <code>user</code> command is used to perform a user lookup &#8211; to show what information Dovecot sees about the <i>user</i>(s), or if it exists at all in the configured <i>userdb</i>(s). </p>
<p> The <i>auth_info</i> may be useful when the userdb is for example a SQL database and you are using %variables, like <code>%s</code> or <code>%l</code>, in the <i>user_query</i> setting. Or when you have configured the userdb in a way like this: </p>
<pre>
userdb {
  driver = passwd-file
  args = /etc/%s.passwd
}
</pre>
<h2>OPTIONS</h2>
<p> Global <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1) <i>options</i>:</p>
<dl>
<dt><code>-D</code></p>
<dd> Enables verbosity and debug messages.</p>
<dt><code>-v</code></p>
<dd> Enables verbosity, including progress counter.</dl>
<p> Command specific <i>options</i>:</p>
<dl>
<dt><code>-a&nbsp;<wbr></code><i>userdb_socket_path</i></p>
<dd> This option is used to specify an absolute path to an alternative UNIX domain socket. </p>
<p> By default <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1) will use the socket <i>/var/run/dovecot/auth-userdb</i>. The socket may be located in another directory, when the default <i>base_dir</i> setting was overridden in <i>/etc/dovecot/dovecot.conf</i>.</p>
<dt><code>-f&nbsp;<wbr></code><i>field</i></p>
<dd> When this option and the name of a userdb field is given, <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1) will show only the value of the specified field.</p>
<dt><code>-u</code></p>
<dd> When this option is given, <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1) will only show values from the <i>userdb</i>. Without -u parameter if any of the <i>uid</i>, <i>gid</i>, <i>home</i> or <i>mail</i> fields are missing, their defaults are taken from configuration file.</p>
<dt><code>-x&nbsp;<wbr></code><i>auth_info</i></p>
<dd> <i>auth_info</i> specifies additional conditions for the <code>user</code> command. The <i>auth_info</i> option string has to be given as <i>name</i><code>=</code><i>value</i> pair. For multiple conditions the <code>-x</code> option could be supplied multiple times.<br />
 Possible names for the <i>auth_info</i> are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>service</code></p>
<dd> The service for which the userdb lookup should be tested. The value may be the name of a service, commonly used with Dovecot. For example: <code>imap</code>, <code>pop3&nbsp;<wbr></code>or <code>smtp</code>.</p>
<dt><code>lip</code></p>
<dd> The local IP address (server) for the test.</p>
<dt><code>rip</code></p>
<dd> The remote IP address (client) for the test.</p>
<dt><code>lport</code></p>
<dd> The local port, e.g. 143</p>
<dt><code>rport</code></p>
<dd> The remote port, e.g. 24567</dl>
</dl>
</dl>
<h2>ARGUMENTS</h2>
<dl>
<dt><i>user</i></p>
<dd> Is a <i>user</i>&#8216;s login name. Depending on the configuration, a login name may be for example <code>jane</code> or <code>john [at] example.com</code>. It&#8217;s also possible to use &#8216;<code>*</code>&#8216; and &#8216;<code>?</code>&#8216; wildcards (e.g. -u *@example.org).</dl>
<h2>EXAMPLE</h2>
<p> Perform a user lookup for the users jane and john [at] example.com. </p>
<pre><code>
doveadm user jane john[at] example.com
        userdb : jane
                     uid : 8001 gid : 8001 home : /
                                                  home / jane mail : sdbox : ~ / sdbox plugins : sieve quota_rule : * : storage = 150M userdb : john[at] example.com
                                                                                                                                                    home : /
                                                                                                                                                           srv / mail / 8 / 70312 / 79832 uid : 79832 gid : 70312 mail : mdbox : ~ / mdbox
</code></pre>
<p> The next example shows a user lookup, using wildcards. </p>
<pre><code>
doveadm user *.? oe[at] example.net
                     jane.doe[at] example.net
                         judy.roe[at] example.net
                             john.doe[at] example.net
</code></pre>
<h2>REPORTING BUGS</h2>
<p> Report bugs, including <i>doveconf -n</i> output, to the Dovecot Mailing List &lt;dovecot [at] dovecot.org&gt;. Information about reporting bugs is available at: <a rel="nofollow" href="http://dovecot.org/bugreport.html">http://dovecot.org/bugreport.html</a></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1) </p>
<h2>Index</h2>
